from __future__ import annotations
import argparse, json
from pathlib import Path
from urllib.error import URLError, HTTPError
from .audit import run_audit, audit_local_html, result_to_dict
from .report import render_html

def main(argv=None):
    parser = argparse.ArgumentParser(prog='citelocal', description='AI answer visibility audit for local businesses')
    sub = parser.add_subparsers(dest='cmd', required=True)
    audit = sub.add_parser('audit')
    audit.add_argument('--name', required=True); audit.add_argument('--category', required=True); audit.add_argument('--city', required=True); audit.add_argument('--url', required=True); audit.add_argument('--html-file'); audit.add_argument('--out', required=True); audit.add_argument('--json-out')
    args = parser.parse_args(argv)
    if args.cmd == 'audit':
        try:
            if args.html_file:
                html_path = Path(args.html_file)
                result = audit_local_html(args.name, args.category, args.city, args.url, html_path.read_text(encoding='utf-8', errors='replace'))
            else:
                result = run_audit(args.name, args.category, args.city, args.url)
        except FileNotFoundError as exc:
            parser.error(f'HTML file not found: {exc.filename}')
        except (HTTPError, URLError, TimeoutError, ValueError, OSError) as exc:
            parser.error(f'audit failed: {exc}')
        out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(render_html(result), encoding='utf-8')
        if args.json_out:
            jout = Path(args.json_out); jout.parent.mkdir(parents=True, exist_ok=True); jout.write_text(json.dumps(result_to_dict(result), indent=2), encoding='utf-8')
        print(f'Wrote {out} — score {result.overall_score}, grade {result.grade}')
        return 0
    return 1
if __name__ == '__main__': raise SystemExit(main())
