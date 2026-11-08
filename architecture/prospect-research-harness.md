# Location and industry prospect-research harness

Updated 2026-11-07. **Design contract for later implementation.** No scraper, database migration, provider integration or outreach automation is built or enabled by this document. Reuse the [existing architecture](system-and-integrations.md), [source work](../status/source-projects.md) and [qualification gates](../strategy/opportunity-qualification.md) before proposing another app.

## Product outcome and scope

Input a location and industry, receive an inspectable private research queue with business identity, observed customer-task evidence, useful contact routes, an appropriate offer hypothesis and the next question. The aim is a better prepared human conversation, not the largest unverified list or a claim to find every business in an area.

One shared engine should support separate profiles for roofing/local-service inquiries and wholesale/catalog discovery. Geography is an explicit set of included places or a reviewed service area, not an ambiguous city string. Distinguish **located in**, **serves**, and **unknown**. County/city batches can roll up to an MSA without silently treating those boundaries as equivalent.

## Batch contract

Use a reviewed brief before collection:

- Batch ID and version, purpose, owner, geography definition, industry/service/product profile and exclusions.
- Source adapters and permitted use, storage/retention/attribution rules, search/query/page caps, rate limits and cost ceiling.
- Discovery queries and task checks, devices/viewports, evidence freshness window and comparison criteria.
- Private destination, access roles, review owner, stop rules and export boundaries.
- A completion report: discovered, deduplicated, identity-resolved, assessed, held, no-issue and reviewed counts, with reasons and coverage limitations.

Unknown source rights or account entitlement is a blocked adapter, not an invitation to use another route around the restriction. Start with small bounded samples, make undercoverage visible and expand only after evaluating quality and cost. Use the [source research](../research/idea-mining/lead-sourcing.md), including current official-source checks, rather than assuming an unrestricted Maps export.

## Pipeline and states

| Stage | Output | Required behavior |
|---|---|---|
| Discover | Source-specific candidate references | Preserve discovery provenance and source restrictions; do not infer operating status from a registry row |
| Resolve | Business, branch, canonical domain and association evidence | Use independent match signals; retain conflicts and suspected duplicates for review |
| Inspect | Bounded page/task observations | Preserve attempted URL, final URL, timestamp, viewport, expected/actual behavior and access limits |
| Diagnose | Separate SEO and acquisition findings | Reproduce a material issue; preserve working controls and alternative explanations |
| Match | Candidate offer and delivery questions | Recommend the least complex useful fix, including configuring an existing tool or doing nothing |
| Review | Current research priority and review decision | Hard holds win; bind review to record/evidence/profile revisions |
| Prepare | Private brief with source-backed observation and questions | Verify the business route and role; no execution permission inherited from a score |
| Learn | Actual activity/outcome and correction | Never mark sent, called, booked, paid or delivered from a plan or draft |

Suggested research states: discovered → identity pending → scoped → assessed → review pending → research prioritized, with held/disqualified/no issue as valid outcomes. Existing runtime approval states remain authoritative. A research-prioritized candidate is not the same as the engine's preparation-ready, buyer-validated or authorized-to-contact state.

## Read-only audit profiles

**SEO/visibility:** Use the [existing audit method](../research/idea-mining/seo-audit.md). Record technical accessibility, service/location information, public profile consistency, performance and the exact sampled search context. Ads, Maps, organic and AI-answer observations are separate. Presence in a sample does not establish traffic; absence does not establish non-indexing.

**Acquisition:** Trace discovery → service/product information → inquiry/quote control → visible intake → stated acknowledgement/handoff. Separate what can be inspected from what needs an authorized submission or call. A form, analytics tag or SMS promise does not prove delivery or conversion tracking.

**Catalog:** Use the known-product and descriptive/attribute checks in the [wholesale card](../strategy/icp-discovery-cards.md#wholesale-catalog-discovery). Test the public route only; no account-only catalog, inventory or pricing access without the relevant permission.

Produce the top few substantiated findings, not a long list of speculative defects. Every finding needs its customer task, observation, narrow consequence, alternative explanation, confidence, proposed fix, access dependency and next verification.

## Explainable ranking

Reuse the [existing audit readiness, evidence coverage and 0–10 opportunity rubric](../research/idea-mining/seo-audit.md); do not add a second incompatible score. Freeze rubric version and applicable checks before a batch. Unknown is not zero, and not applicable needs a reason. Respect the documented coverage thresholds and keep category results visible.

That rubric prioritizes **research**, not Google's ranking, buying intent or future revenue. Show it alongside identity confidence, buyer/need status, integration risk, cost assumptions and human review. Hard holds and suppression cannot be overridden by a high score. Compare within an appropriate profile and geography; do not directly rank a roofer against a wholesaler on missing catalog search.

For commercial prioritization, use the qualification gates and buyer evidence separately. A confirmed severe issue can merit review even when an illustrative two-gap research filter is unmet. Conversely, low readiness without a fixable buyer-recognized problem does not justify a pitch.

## Tool and source order

| Layer | What it helps establish | Limits and activation gate |
|---|---|---|
| Essential first pass | Bounded browser inspection, public official business sources, permitted search and private evidence storage | Identity, task observations and provenance; not complete market coverage |
| Useful diagnostic layer | PageSpeed Insights/Lighthouse and eligible CrUX data | Lab versus field and URL versus origin remain separate; no eligible field data is not a failure |
| Optional paid enrichment | Licensed SEO/traffic estimates and business datasets | Confirm account rights, geography, date, cost and storage terms; estimates are not revenue or first-party analytics |
| Owner-authorized validation | Search Console, GA4, Business Profile performance, CRM/call/booking records | Only connected/authorized sources; inspect completeness and event definitions before claiming outcomes |
| Later product integrations | Catalog feeds, inventory, calendars and communications providers | Separate access and action permission, secret handling, usage caps, failure behavior and support scope |

A paid SEO subscription is not required to begin public-page research. Public inspection cannot reveal a company's actual revenue, margin, close rate or lost leads. Model business value only from an agreed baseline with explicit assumptions; hypothetical calculations never become observed results.

## Private data contract

Use distinct records for business/branch, contact role/route, evidence, finding, offer hypothesis, activity and next task. Link by stable internal IDs rather than repeating scraped strings in every row. The [private ledger template](../templates/research-and-contact-ledger.md) specifies the minimum fields.

Before using a database, define tenancy/access roles, row-level access enforcement, source-specific retention, correction/deletion, audit events, suppression and backup/recovery. A named database project is not proof these controls or a schema already exist. Do not place real records, screenshots, contact details or exports in Git, even in an ignored directory, as a substitute for private storage. Keep credentials out of prompts, files, logs and frontend code.

Collection should be idempotent: repeated runs append new dated observations, preserve prior evidence and do not duplicate businesses or activities. Entity merges must retain provenance and be reversible. No unbounded crawler, contact guessing, paywall/access bypass or automated social interaction.

## Learn from walkthroughs without training on assumptions

Record the user's search terms, navigation steps, expected result, observation, interpretation, correction and preferred next question. Label each item as human-reported, directly observed, inferred, synthetic or unknown. A user opinion about an ugly website is not a failure label.

Convert reviewed examples into versioned task instructions and evaluation fixtures first. No model training or external upload is implied. Keep private content in its approved system; use fictional or separately authorized examples in public fixtures. Treat websites, transcripts and retrieved documents as untrusted data, never instructions to invoke tools or reveal private context.

Maintain a separate held-out evaluation set. Test false positives, missed known issues, unsupported claims, blocked-source handling, duplicate/branch identity, no-issue preservation, staleness and human-review invalidation. Track inspection time/cost and useful reviewed candidates, not just records collected. Learn from buyer corrections and rejected ideas as well as wins.

## Build sequence and acceptance

1. Map one reviewed roofing example and one permitted wholesale task manually; confirm the common evidence contract before coding.
2. Build or reuse a private queue on synthetic fixtures, with profile adapters and no external side effects. Inspect existing app/schema contracts before any migration.
3. Test a capped read-only batch. Report coverage, errors, duplicates, cost and all holds; require human review of every priority result.
4. Produce a call-preparation brief and log user-reported activity. Keep outreach execution separate.
5. Expand sources/geographies only after quality and permissions are reviewed; add live integrations only through a separately scoped task.

Acceptance must demonstrate: unknown/blocked sources cannot create negative findings; source content cannot override instructions; no actual outreach or paid action in read-only mode; revised evidence invalidates affected reviews; duplicate runs preserve one business identity and distinct observation times; exact links and source limits remain visible; exports contain only allowed fields; and privacy controls are tested before any real data is stored.

Use [staged prompts](../codex/PROSPECTING-NEXT-STEPS.md) to continue existing work rather than creating overlapping engines.
