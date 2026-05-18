# Zero-Budget First 50 Lead Sourcing Plan

## Objective

Build the first 50 CiteLocal AI prospects manually without paid tools, paid APIs, scraping at scale, or automated outreach.

Target list:

- One vertical.
- One metro or tightly defined region.
- 50 qualified local businesses.
- 30 personalized first-touch messages in week one.
- 10 free snapshots completed before outreach or shortly after a positive reply.

Recommended default: **HVAC companies in one metro**.

## Prospect data model

Create a simple spreadsheet or CSV with these columns:

- `business_name`
- `category`
- `city`
- `website`
- `phone`
- `owner_or_contact`
- `contact_source`
- `email_or_form_url`
- `linkedin_url`
- `facebook_url`
- `google_business_profile_url`
- `review_count`
- `rating`
- `visible_services`
- `quick_gap_1`
- `quick_gap_2`
- `quick_gap_3`
- `snapshot_status`
- `outreach_channel`
- `outreach_status`
- `follow_up_date`
- `notes`

If using repo files, create `data/prospects.csv` with the same headers.

## Free lead sources

Use only public, manual sources:

1. Google Search / Google Maps results viewed manually.
2. Business websites.
3. Google Business Profiles.
4. LinkedIn public profiles.
5. Facebook business pages.
6. Chamber of commerce member directories.
7. Local trade association directories.
8. Yelp/Angi/HomeAdvisor listings only as discovery references, not paid contact sources.
9. City “best HVAC in [city]” blog posts and local directories.
10. State licensing lookup when useful for owner/entity confirmation.

Do not use paid enrichment tools, paid email databases, or automated scraping.

## Search queries to build the list

Run searches manually and record businesses that match the ICP.

### Core queries

- `HVAC company {{city}}`
- `AC repair {{city}}`
- `furnace repair {{city}}`
- `emergency HVAC {{city}}`
- `heating and cooling {{city}}`
- `HVAC contractor {{city}}`
- `air conditioning repair {{city}}`

### Directory queries

- `site:chamberofcommerce.com HVAC {{city}}`
- `{{city}} chamber HVAC contractor`
- `{{city}} home builders association HVAC members`
- `{{state}} HVAC license lookup {{business name}}`

### Owner/contact queries

- `{{business name}} owner`
- `{{business name}} founder`
- `{{business name}} LinkedIn`
- `site:linkedin.com/in {{business name}} HVAC {{city}}`
- `{{business name}} Facebook`

## Qualification score

Score each prospect 0–10. Prioritize 7+.

- +2: Independent/local business, not a franchise or national chain.
- +2: Has a website with service pages.
- +1: 10–200 reviews or visible local reputation.
- +1: Clear high-value/emergency services.
- +1: Contact email, form, or owner/manager visible.
- +1: Weak FAQ/cost/service-area content.
- +1: Missing or unclear schema/trust proof.
- +1: Site looks maintained enough that updates are possible.

Disqualifiers:

- No usable contact path.
- No website.
- Large agency-managed brand with no owner contact.
- Site is broken or entirely inaccessible.
- Business appears closed or inactive.

## Manual mini-audit checklist for each lead

Spend 3–5 minutes before outreach. Capture concrete personalization.

### Website clarity

- Is the city/service area stated above the fold?
- Are the primary services clear without clicking deeply?
- Is phone number visible on mobile and desktop?
- Are emergency/same-day services clearly stated if offered?

### Answer readiness

- Is there an FAQ page?
- Are there cost/pricing explanation pages?
- Do service pages answer common buyer questions?
- Are headings phrased around customer intent?

### Trust proof

- Are reviews/testimonials visible?
- Is license/insurance/warranty information visible?
- Are team, trucks, before/after photos, or local proof visible?
- Are years in business or family-owned claims stated clearly?

### Technical basics

- Does the home page have a clear title tag?
- Is there a meta description?
- Is schema present? Check by viewing page source and searching for `schema.org`, `LocalBusiness`, `HVACBusiness`, or `application/ld+json`.
- Are sitemap and robots files present? Try `/sitemap.xml` and `/robots.txt`.

## First 50 list-building workflow

### Batch 1: 20 map/search prospects

1. Search core HVAC queries for the selected city.
2. Open Google Maps/local results manually.
3. Record independent businesses from page 1–3 and map pack expansions.
4. Visit each site and record contact paths.
5. Add quick gaps.

### Batch 2: 15 directory prospects

1. Search chamber/trade directories.
2. Add businesses not already captured.
3. Prioritize those with a real website and visible owner/contact.

### Batch 3: 10 competitor/content-gap prospects

1. Search question keywords like `furnace replacement cost {{city}}` and `AC repair cost {{city}}`.
2. Note which local businesses are missing useful answers or have thin pages.
3. Add high-gap prospects.

### Batch 4: 5 warm-ish network/local prospects

1. Ask personal network for local contractor intros.
2. Check neighborhood Facebook/Nextdoor recommendations manually.
3. Add businesses with repeated positive mentions and weak websites.

## Snapshot selection

Do not create full snapshots for all 50 initially. Pick the top 10 with:

- Strong fit.
- Easy-to-explain gap.
- Clear owner/contact path.
- High-value services.

For each of the top 10, prepare:

- One score or simple grade.
- Three specific gaps.
- One concrete fix.
- One sentence explaining business impact.

Example:

> “Your AC repair page mentions service, but it does not answer cost, response time, or service-area questions. Those are exactly the details AI summaries tend to pull into local recommendations.”

## Outreach tracking rules

- Send manually only.
- Personalize every message with one observed gap.
- Do not send attachments on first touch unless requested.
- Log date, channel, message angle, and next follow-up.
- Follow up twice, then stop unless they engage.

Suggested statuses:

- `identified`
- `qualified`
- `snapshot_started`
- `snapshot_ready`
- `sent_first_touch`
- `replied_positive`
- `replied_not_now`
- `booked_call`
- `sold_audit`
- `sold_sprint`
- `closed_lost`

## Daily sourcing target

For the first week:

- Day 1: choose niche/metro and source 20 leads.
- Day 2: source 30 more leads and score all 50.
- Day 3: create 5 snapshots and send 10 messages.
- Day 4: create 5 more snapshots and send 10 messages.
- Day 5: send 10 more messages and follow up with day-3 opens/replies manually.
- Day 6: book calls, deliver requested snapshots, refine scripts.
- Day 7: review metrics and pick the next 50 or narrow the niche.
