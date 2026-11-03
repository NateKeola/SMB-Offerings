# API usage, budgets and outcome costs

The API Spend Dashboard is separate from the outreach engine and from the service-margin model. It is a local prototype with no live billing connection. See [source inventory](../status/source-projects.md) and [verification limits](https://github.com/NateKeola/Dogfood/blob/2e3b285ee80c121571e06cf223934aa26f581579/projects/api-spend-dashboard/VERIFICATION.md).

## Preserve cost provenance

| Class | Meaning |
|---|---|
| Provider reported / invoice | Imported assertion from a provider or invoice; reconciliation still needed |
| Manual actual | A user-recorded cost or local-execution fact with provenance |
| Estimated | Units multiplied by an explicit rate/assumption; not a bill |
| Unknown | Missing amount/currency; never silently treated as zero |

The outreach prototype made zero real provider calls. Its zero-cost local preparation events describe those operations only. They do not establish zero subscription costs, free assistant usage, completed audits or qualified leads.

## Engine v1 usage contract

The local JSONL contract contains `version`, `event_id`, `provider`, `operation`, `units`, `unit`, `timestamp`, `run_id`, `batch_id`, nullable `amount`/`currency`, `cost_basis` (`actual`, `estimated`, `unknown`) and `provenance`. IDs are opaque. Do not place prospect names, contact data, prompts, request payloads, account identifiers or credentials in ledger fields.

The dashboard maps estimated to estimate; actual provider-response/invoice records to provider-reported; other actual provenance to manual; and unknown to unknown. It supplies an outreach-engine project label but does not invent status/attempt values or stage counts absent from the source. The adapter still accepts the same v1 contract after the engine's profile update. [Engine contract](https://github.com/NateKeola/Dogfood/blob/c33eb2122fafe787ed65619bf4dcde2bc6fa7b7c/projects/outreach-engine/docs/USAGE.md) · [Dashboard mapping](https://github.com/NateKeola/Dogfood/blob/2e3b285ee80c121571e06cf223934aa26f581579/projects/api-spend-dashboard/USAGE_CONTRACT.md).

Stable event IDs prevent identical reimport duplication. They do not detect two semantically overlapping charges under different IDs. Do not count a whole model call in both input and output components, or a manual invoice plus the same provider charge. Estimate-to-actual reconciliation needs explicit linkage before summing.

## Plan costs without false precision

Keep provider credits, requests, tokens and browser minutes in their own units. Keep currencies separate. Include subscriptions, included-credit allocation, retries, failed operations, overages and human review time. The existing dashboard has 100/1,000-candidate scenarios; neither is a completed real batch.

A historical engine example modeled 100 inputs as thirty Exa discovery searches and two hundred content pages, for $0.41 variable cost under its selected rates; the linear 1,000-input example was $4.10. This excludes subscription minimums, duplication, retries, content extras, taxes and labor and does not guarantee any number of unique companies. Apollo credits had no established dollar conversion. These are dated estimates, not a current quote or approved spending ceiling.

Budget warnings are visibility tools, not provider-enforced hard caps. A later paid adapter needs explicit scope and budget authorization, account limits, pre-dispatch reservation, request/cost logging, uncertainty reconciliation and stop behavior. No authorization comes from entering a budget into a prototype.

## Relate cost to meaningful outcomes

Track discovered, audited, qualified, prototyped and call-ready counts with clear definitions, dates and scope. Preparation status is separate from actual calls and paid outcomes. Use deduplicated counts, not retries; preserve unknown denominators. Allocate costs and outcomes explicitly when a batch spans months. Do not invent a funnel where stage definitions differ.

Report cost per assessed opportunity, qualified conversation and paying customer only when the corresponding denominator exists. API cost per input alone obscures human labor and failed acquisition. The [pilot scorecard](../templates/pilot-scorecard.md) provides a blank private worksheet.
