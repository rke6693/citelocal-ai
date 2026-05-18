# CiteLocal AI

Zero-budget startup build: **AI answer visibility audits for local service businesses**.

CiteLocal AI helps plumbers, roofers, dentists, med spas, HVAC companies, landscapers, and other local businesses understand whether their website is easy for AI search engines and answer engines to cite.

## Why this company

Search behavior is shifting from ten blue links to short AI answers. Local businesses still need classic SEO, but they also need pages that answer buyer questions directly, prove trust, expose service-area facts, and contain machine-readable business details. Most single-location operators do not have the budget or sophistication for enterprise SEO tools.

## Product

A free/low-cost audit generator that scores a business website on:

- Local identity clarity: name, address, phone, service area, hours
- Structured data/schema signals
- Buyer-answer content: FAQs, cost pages, service explainers
- Trust signals: reviews, guarantees, credentials, photos, before/after language
- AI citation readiness: direct, quotable answers and entity consistency
- Technical basics: title, meta description, headings, robots.txt, sitemap.xml

The first sellable offer is a manually assisted report:

- **Free:** one-page AI visibility snapshot
- **$149:** full audit + 30-day content plan
- **$49/mo:** monthly re-scan + one FAQ/content update brief
- **$399 setup:** implement schema, FAQ, and location/service pages for early customers

No paid APIs are required for MVP delivery.

## Quick start

Run the bundled sample audit without any paid APIs or network access:

```bash
cd /Users/agent1/Operator/citelocal-ai
python3 -m citelocal.cli audit --name "River City HVAC" --category "HVAC" --city "Cincinnati, OH" --url https://example.com --html-file examples/sample_business.html --out out/demo.html --json-out out/demo.json
```

Open `out/demo.html` in a browser.

To audit a live site instead, omit `--html-file` and pass the real homepage URL. The live-site mode only uses Python standard-library HTTP requests; it does not call paid APIs.

```bash
python3 -m citelocal.cli audit --name "Business Name" --category "Plumber" --city "Austin, TX" --url https://example-business.com --out out/live.html --json-out out/live.json
```

Run the lightweight regression checks:

```bash
python3 -m unittest discover -s tests
```

## Files

- `citelocal/cli.py` — command-line audit/report generator
- `citelocal/audit.py` — scoring and extraction logic
- `citelocal/report.py` — HTML report rendering
- `examples/sample_business.html` — local test fixture
- `site/index.html` — landing page mockup
- `docs/company_brief.md` — positioning, customer, pricing, validation plan
- `docs/outreach.md` — cold outreach scripts
- `docs/implementation_plan.md` — build-out roadmap

## Compliance note

This is a marketing/SEO diagnostic, not a guarantee of rankings, AI citations, leads, or revenue. Reports should avoid claiming direct control over Google, ChatGPT, Perplexity, Bing, or any third-party algorithm.
