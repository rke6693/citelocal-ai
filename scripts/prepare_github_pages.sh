#!/usr/bin/env bash
set -euo pipefail

# Zero-cost GitHub launch helper for CiteLocal AI.
# Review before running. This creates/pushes a public GitHub repository using the
# currently authenticated `gh` account and enables GitHub Pages via Actions.

REPO_NAME="${REPO_NAME:-citelocal-ai}"
DESCRIPTION="CiteLocal AI — local business AI visibility audit MVP"

cd "$(dirname "$0")/.."

echo "Checking GitHub CLI authentication..."
gh auth status
OWNER="$(gh api user -q .login)"
echo "Authenticated GitHub user: ${OWNER}"

if [ ! -d .git ]; then
  git init
fi

git branch -M main

git add README.md index.html docs site citelocal examples .gitignore .github scripts/prepare_github_pages.sh
if ! git diff --cached --quiet; then
  git commit -m "Launch CiteLocal AI static MVP"
fi

echo "Checking repository availability: ${OWNER}/${REPO_NAME}"
if gh repo view "${OWNER}/${REPO_NAME}" >/dev/null 2>&1; then
  echo "Repository already exists: https://github.com/${OWNER}/${REPO_NAME}"
else
  echo "Creating public repository: ${OWNER}/${REPO_NAME}"
  gh repo create "${OWNER}/${REPO_NAME}" --public --description "$DESCRIPTION"
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "https://github.com/${OWNER}/${REPO_NAME}.git"
fi

git push -u origin main

echo "Ensuring GitHub Pages is configured for branch-source deployment..."
# The endpoint returns non-zero if Pages already exists; in that case patch/update it.
gh api -X POST "repos/${OWNER}/${REPO_NAME}/pages" -f source.branch=main -f source.path=/ >/dev/null 2>&1 || \
  gh api -X PUT "repos/${OWNER}/${REPO_NAME}/pages" -f source.branch=main -f source.path=/ >/dev/null

echo "Done. Check deployment status:"
echo "  gh api repos/${OWNER}/${REPO_NAME}/pages"
echo "Expected URL after deployment: https://${OWNER}.github.io/${REPO_NAME}/"
