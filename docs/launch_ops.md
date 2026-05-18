# CiteLocal AI launch ops/account checklist

Last checked/launched: 2026-05-18

## Current zero-cost account/deployment status

- GitHub CLI: authenticated to `github.com` as `rke6693` with `repo` scope.
- Local project path: `/Users/agent1/Operator/citelocal-ai`.
- Local git repo: initialized on `main` and pushed to `origin`.
- Public GitHub repo: `https://github.com/rke6693/citelocal-ai`.
- Static hosting: GitHub Pages branch-source deployment from `main` `/`.
- Public site: `https://rke6693.github.io/citelocal-ai/`.
- Domain: do not register yet; use the free GitHub Pages URL first.
- Intake/contact: landing page uses a zero-cost `request.html` copy/email draft page so prospects do not need to create a GitHub or third-party account.

## What launched at zero cost

1. Public GitHub repository under the authenticated GitHub account.
2. GitHub Pages static site served from the repository root.
3. No-account request page that lets prospects copy a formatted free snapshot request or open an email draft.
4. Manual audit/report delivery from the local Python CLI.
5. Manual outbound sales workflow using the sales docs in this folder.

No paid services, custom domain, new email account, Stripe, Google Workspace, or third-party signup is required for the MVP launch.

## Verification completed

- `python3 -m unittest discover -s tests` passed.
- `python3 -m citelocal.cli audit ...` generated launch-check report successfully.
- `site/index.html` parses as HTML with Python's standard `html.parser`.
- `scripts/prepare_github_pages.sh` passes `bash -n`.
- No placeholder contact email remains in site/docs/README.
- GitHub Pages returned HTTP 200 and the deployed HTML contains `CiteLocal AI`.
- GitHub Pages API reports `status: built`, URL `https://rke6693.github.io/citelocal-ai/`, source `main` `/`.

## Operational commands

Run a sample local audit:

```bash
cd /Users/agent1/Operator/citelocal-ai
python3 -m citelocal.cli audit \
  --name "River City HVAC" \
  --category "HVAC" \
  --city "Cincinnati, OH" \
  --url https://example.com \
  --html-file examples/sample_business.html \
  --out out/demo.html \
  --json-out out/demo.json
```

Check Pages status:

```bash
gh api repos/rke6693/citelocal-ai/pages --jq '{status:.status,url:.html_url,source:.source}'
curl -L https://rke6693.github.io/citelocal-ai/
```

Push future updates:

```bash
cd /Users/agent1/Operator/citelocal-ai
git add -A
git commit -m "Update CiteLocal AI launch assets"
git push
```

## Next free launch tasks

- Use `sales_growth_launch_package.md` as the sales/growth operating index.
- Create `data/prospects.csv` with 50 manually researched prospects in one vertical/metro.
- Generate 10 free snapshot summaries for the highest-fit public prospect sites.
- Send 30 personalized, low-volume outreach messages in week one; do not automate spam.
- Replace the no-account copy/email draft request page with a private inbox/form once the owner approves a contact channel.
