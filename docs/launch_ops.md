# CiteLocal AI launch ops/account checklist

Last checked: 2026-05-18

## Current zero-cost account/deployment status

- GitHub CLI: authenticated to `github.com` as `rke6693` with `repo` scope.
- Local project path: `/Users/agent1/Operator/citelocal-ai`.
- Git repository: not initialized locally at inspection time.
- Remote GitHub repository: `rke6693/citelocal-ai` was not found at inspection time, so the name appears available for creation under the authenticated account.
- Static hosting: ready for GitHub Pages using the included Actions workflow at `.github/workflows/pages.yml`.
- Domain: do not register yet; use the free GitHub Pages URL first.
- Email/contact: landing page uses a zero-cost GitHub Issue intake form for free snapshot requests until a private inbox/form is connected.

## What can be launched now at zero cost

1. Public GitHub repository under the authenticated account.
2. GitHub Pages static site served from `site/` via GitHub Actions.
3. Manual audit/report delivery from the local Python CLI.
4. Manual outbound sales workflow using the existing outreach docs.

No paid services, custom domain, new email account, Stripe, Google Workspace, or third-party signup is required for the MVP launch.

## Pre-publish checks completed

- `python3 -m citelocal.cli audit ...` generated `out/sample_report.html` and `out/sample_report.json` successfully.
- `site/index.html` parses as HTML with Python's standard `html.parser`.
- Static landing page has no build step and can be uploaded directly as a GitHub Pages artifact.

## Recommended parent/owner verification before external publishing

1. Decide whether `rke6693/citelocal-ai` should be public.
2. Confirm the public GitHub Issue intake form is acceptable for the first free-snapshot requests; replace with a private inbox/form later if needed.
3. Review pricing/claims on the landing page for accuracy and compliance.
4. Confirm that publishing sample files in `out/` is acceptable; otherwise do not add `out/` to the first public commit.

## Exact zero-cost launch commands

From `/Users/agent1/Operator/citelocal-ai`:

```bash
chmod +x scripts/prepare_github_pages.sh
REPO_NAME=citelocal-ai scripts/prepare_github_pages.sh
```

Then check the deployment:

```bash
gh run list --repo rke6693/citelocal-ai --workflow pages.yml --limit 5
gh run watch --repo rke6693/citelocal-ai
```

Expected public URL after the Pages deployment finishes:

```text
https://rke6693.github.io/citelocal-ai/
```

## Manual fallback commands

If the helper script is not used:

```bash
cd /Users/agent1/Operator/citelocal-ai
git init
git branch -M main
git add README.md docs site citelocal examples .gitignore .github/workflows/pages.yml
git commit -m "Launch CiteLocal AI static MVP"
gh repo create rke6693/citelocal-ai --public --description "CiteLocal AI — local business AI visibility audit MVP" --source=. --remote=origin --push
gh api -X POST repos/rke6693/citelocal-ai/pages -f build_type=workflow || gh api -X PUT repos/rke6693/citelocal-ai/pages -f build_type=workflow
gh workflow run "Deploy static site to GitHub Pages" --repo rke6693/citelocal-ai
```

## Next free launch tasks

- Use `sales_growth_launch_package.md` as the sales/growth operating index.
- Create `data/prospects.csv` with 50 manually researched prospects in one vertical/metro.
- Generate 10 free snapshot summaries for the highest-fit public prospect sites.
- Send 30 personalized, low-volume outreach messages in week one; do not automate spam.
- After first positive replies, consider a free form backend only if it does not require a new account with email/2FA.
