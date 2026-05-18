# CiteLocal AI Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task if expanding into a production app.

**Goal:** Turn the working CLI/report MVP into a sellable zero-budget startup with a static landing page, repeatable audit delivery, and manual sales workflow.

**Architecture:** Keep the core as a local Python audit engine that generates HTML/JSON reports. Add a static landing page first, then a lightweight form/backend only after proof of demand.

**Tech Stack:** Python standard library, static HTML/CSS, optional GitHub Pages/Cloudflare Pages, optional Playwright PDF export.

---

## Task 1: Prove report generation

**Objective:** Ensure the audit engine can generate a report from a local fixture.

**Command:**

```bash
python3 -m citelocal.cli audit --name "River City HVAC" --category HVAC --city "Cincinnati, OH" --url https://rivercity.example --html-file examples/sample_business.html --out out/sample_report.html --json-out out/sample_report.json
```

**Expected:** HTML and JSON files are written; score and grade print to terminal.

## Task 2: Create first prospect batch

**Objective:** Build a spreadsheet/CSV of 25 prospects in one vertical and one metro.

**Files:**
- Create: `data/prospects.csv`

**Columns:** business_name, category, city, website, owner_or_contact, email_or_form, notes, audit_status, outreach_status.

## Task 3: Generate five free snapshots

**Objective:** Produce sample reports for prospects with public websites.

**Files:**
- Create: `out/prospects/*.html`
- Create: `out/prospects/*.json`

**Verification:** Each report has a score, priority fixes, and no obvious broken HTML.

## Task 4: Send manual outreach

**Objective:** Use the cold email script and personalize each message with one concrete issue from the report.

**Files:**
- Existing: `docs/outreach.md`
- Create: `data/outreach_log.csv`

**Safety:** Do not automate spam. Start with small, manual, personalized outreach.

## Task 5: Close first paid audit

**Objective:** Convert one interested prospect into a $149 audit or $399 implementation sprint.

**Deliverables:** Full HTML/PDF report, 30-day content plan, and implementation checklist.

## Task 6: Decide whether to automate

**Objective:** Only after money or strong replies, add a form and queue.

**Decision gate:** At least one paid customer or five strong replies.
