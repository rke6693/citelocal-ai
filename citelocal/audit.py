from __future__ import annotations
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import json, re
from typing import Dict, List, Tuple

@dataclass
class AuditInput:
    name: str
    category: str
    city: str
    url: str

@dataclass
class Finding:
    label: str
    score: int
    max_score: int
    status: str
    evidence: str
    recommendation: str

@dataclass
class AuditResult:
    business: AuditInput
    overall_score: int
    grade: str
    findings: List[Finding]
    extracted: Dict[str, object]
    next_actions: List[str]

class SimpleHTMLExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.meta = {}
        self.links = []
        self.scripts_json_ld = []
        self.headings = []
        self.text_chunks = []
        self._tag_stack = []
        self._capture_title = False
        self._capture_script = False
        self._script_buf = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs); self._tag_stack.append(tag)
        if tag == 'title': self._capture_title = True
        elif tag == 'meta':
            key = (attrs.get('name') or attrs.get('property') or '').lower()
            if key: self.meta[key] = attrs.get('content', '')
        elif tag == 'a' and attrs.get('href'):
            self.links.append((attrs.get('href'), attrs.get('aria-label', '')))
        elif tag == 'script' and attrs.get('type', '').lower() == 'application/ld+json':
            self._capture_script = True; self._script_buf = []
    def handle_endtag(self, tag):
        if tag == 'title': self._capture_title = False
        if tag == 'script' and self._capture_script:
            self.scripts_json_ld.append(''.join(self._script_buf).strip()); self._capture_script = False
        if self._tag_stack: self._tag_stack.pop()
    def handle_data(self, data):
        text = re.sub(r'\s+', ' ', data).strip()
        if not text: return
        if self._capture_title: self.title += text
        elif self._capture_script: self._script_buf.append(data)
        else:
            current = self._tag_stack[-1] if self._tag_stack else ''
            if current in {'h1','h2','h3'}: self.headings.append(text)
            if current not in {'script','style','noscript'}: self.text_chunks.append(text)

def fetch_url(url: str, timeout: int = 12) -> Tuple[str, Dict[str, str]]:
    req = Request(url, headers={'User-Agent': 'CiteLocalAI/0.1 (+zero-budget audit tool)'})
    with urlopen(req, timeout=timeout) as resp:
        raw = resp.read(1_500_000); headers = dict(resp.headers.items())
    encoding = 'utf-8'
    match = re.search(r'charset=([\w-]+)', headers.get('Content-Type',''), re.I)
    if match: encoding = match.group(1)
    return raw.decode(encoding, errors='replace'), headers

def _collect_json_ld_types(value: object) -> List[str]:
    """Return schema.org @type values from common JSON-LD shapes.

    Many production local-business sites wrap entities in @graph or nest them
    under other objects, so only checking the top-level dictionary misses real
    schema and can make launch demos look falsely negative.
    """
    found: List[str] = []
    if isinstance(value, dict):
        t = value.get('@type')
        if isinstance(t, list):
            found.extend(str(item) for item in t if item)
        elif t:
            found.append(str(t))
        for child in value.values():
            if isinstance(child, (dict, list)):
                found.extend(_collect_json_ld_types(child))
    elif isinstance(value, list):
        for item in value:
            found.extend(_collect_json_ld_types(item))
    return found

def extract_page(html: str, base_url: str) -> Dict[str, object]:
    parser = SimpleHTMLExtractor(); parser.feed(html)
    text = re.sub(r'\s+', ' ', ' '.join(parser.text_chunks)).strip()
    json_ld_types = []
    for blob in parser.scripts_json_ld:
        try:
            json_ld_types.extend(_collect_json_ld_types(json.loads(blob)))
        except Exception:
            json_ld_types.append('Unparseable JSON-LD')
    return {'title': parser.title.strip(), 'meta_description': parser.meta.get('description',''), 'headings': parser.headings[:50], 'json_ld_types': json_ld_types, 'links': [urljoin(base_url, h) for h,_ in parser.links[:250]], 'text': text[:100000], 'word_count': len(text.split())}

def count_any(text: str, patterns: List[str]) -> int:
    t = text.lower(); return sum(1 for p in patterns if p.lower() in t)

def score_audit(inp: AuditInput, page: Dict[str, object], robots_status='unknown', sitemap_status='unknown') -> AuditResult:
    text = str(page.get('text','')); title = str(page.get('title','')); meta = str(page.get('meta_description','')); headings = ' '.join(page.get('headings', [])); links = page.get('links', []); json_ld_types = [str(x) for x in page.get('json_ld_types', [])]
    all_text = ' '.join([title, meta, headings, text])
    findings: List[Finding] = []
    local_hits = count_any(all_text, [inp.name, inp.city, inp.category])
    findings.append(Finding('Local entity clarity', min(20, local_hits*7), 20, 'strong' if local_hits>=3 else 'weak', f'Found {local_hits}/3 core identity signals across title/meta/headings/body.', 'Put the exact business name, city/service area, and primary category in the homepage H1, title tag, footer, and About/Contact copy.'))
    nap_hits = count_any(all_text, ['phone','call','address','hours','service area','directions']); phone_like = bool(re.search(r'(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}', all_text))
    findings.append(Finding('NAP/contact accessibility', min(15, nap_hits*3 + (6 if phone_like else 0)), 15, 'strong' if nap_hits>=3 and phone_like else 'medium' if nap_hits>=2 else 'weak', f'Contact terms: {nap_hits}; phone pattern detected: {phone_like}.', 'Expose phone, address/service area, hours, and contact CTA in plain text; avoid hiding core details only inside images.'))
    schema_types = ', '.join(json_ld_types) if json_ld_types else 'none detected'; local_schema = any(t.lower() in {'localbusiness','organization','hvacbusiness','plumber','dentist','roofingcontractor'} for t in json_ld_types)
    findings.append(Finding('Structured data/schema', 15 if local_schema else 6 if json_ld_types else 0, 15, 'strong' if local_schema else 'medium' if json_ld_types else 'weak', f'JSON-LD types detected: {schema_types}.', 'Add LocalBusiness/Organization JSON-LD with name, phone, URL, address/service area, opening hours, sameAs links, and service catalog.'))
    faq_hits = count_any(all_text, ['faq','frequently asked','how much','cost','price','near me','emergency','same day','quote']); question_marks = all_text.count('?')
    findings.append(Finding('Buyer-answer content', min(20, faq_hits*3 + min(5, question_marks)), 20, 'strong' if faq_hits>=5 or question_marks>=5 else 'medium' if faq_hits>=3 else 'weak', f'Buyer intent terms: {faq_hits}; question marks: {question_marks}.', 'Create concise FAQ, cost, comparison, emergency/same-day, and service-area answer sections that AI systems can quote directly.'))
    trust_hits = count_any(all_text, ['review','rated','testimonial','licensed','insured','guarantee','warranty','years','family owned','before','after'])
    findings.append(Finding('Trust and proof density', min(15, trust_hits*2), 15, 'strong' if trust_hits>=6 else 'medium' if trust_hits>=3 else 'weak', f'Trust terms detected: {trust_hits}.', 'Add first-party review excerpts, license/insurance language, warranty details, years in business, photos, and proof-backed claims.'))
    service_link_hits = sum(1 for l in links if any(x in l.lower() for x in ['service','repair','installation','pricing','cost','areas','locations','faq']))
    findings.append(Finding('Service/content architecture', min(10, service_link_hits*2), 10, 'strong' if service_link_hits>=5 else 'medium' if service_link_hits>=2 else 'weak', f'Service/FAQ/location-like internal links detected: {service_link_hits}.', 'Build separate pages for the top services, common problems, pricing ranges, and service areas; link them from homepage navigation.'))
    tech_score = (3 if title else 0)+(3 if meta else 0)+(2 if int(page.get('word_count',0))>=300 else 0)+(1 if robots_status=='ok' else 0)+(1 if sitemap_status=='ok' else 0)
    findings.append(Finding('Technical crawl basics', tech_score, 10, 'strong' if tech_score>=8 else 'medium' if tech_score>=5 else 'weak', f'Title: {bool(title)}; meta: {bool(meta)}; words: {page.get("word_count")}; robots: {robots_status}; sitemap: {sitemap_status}.', 'Ensure each important page has a unique title/meta description, 300+ useful words, crawlable HTML, robots.txt, and sitemap.xml.'))
    total = sum(f.score for f in findings); grade = 'A' if total>=85 else 'B' if total>=70 else 'C' if total>=55 else 'D' if total>=40 else 'F'
    next_actions = [f.recommendation for f in sorted(findings, key=lambda x: (x.score/max(1,x.max_score)))[:4]]
    return AuditResult(inp, total, grade, findings, {k:v for k,v in page.items() if k!='text'}, next_actions)

def probe_side_files(url: str) -> Tuple[str, str]:
    def probe(path):
        try:
            target = urljoin(url.rstrip('/')+'/', path); req = Request(target, headers={'User-Agent':'CiteLocalAI/0.1'})
            with urlopen(req, timeout=5) as resp: return 'ok' if 200 <= resp.status < 400 else f'http {resp.status}'
        except Exception: return 'missing/error'
    return probe('robots.txt'), probe('sitemap.xml')

def run_audit(name: str, category: str, city: str, url: str) -> AuditResult:
    parsed = urlparse(url)
    if parsed.scheme not in {'http', 'https'} or not parsed.netloc:
        raise ValueError('URL must include http:// or https:// and a host')
    html, _ = fetch_url(url); page = extract_page(html, url); robots, sitemap = probe_side_files(url); return score_audit(AuditInput(name, category, city, url), page, robots, sitemap)

def audit_local_html(name: str, category: str, city: str, url: str, html: str) -> AuditResult:
    return score_audit(AuditInput(name, category, city, url), extract_page(html, url), 'not checked', 'not checked')

def result_to_dict(result: AuditResult) -> Dict[str, object]: return asdict(result)
