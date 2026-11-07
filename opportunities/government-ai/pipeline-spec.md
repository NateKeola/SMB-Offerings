# Procurement discovery and qualification pipeline

Prepared 2026-11-07. This is an extension proposal for the existing research workflow, not a running scraper, enabled provider or new outreach campaign.

## Sources and scope

Use the existing private research system for real rows. Keep named prospects, contact routes, activity notes, private sheet links and account data out of this public repository.

Start with one service and one route. Suggested test scopes: civilian document-workflow evaluation under a prime; tailored staff training for a local department; or a workforce-provider pool. Federal procurement is buyer/program-based rather than primarily MSA-based. Preserve location for performance requirements and local preferences without confusing headquarters with service territory.

| Source | Use | What it does not prove |
|---|---|---|
| USAspending | Historical prime awards, recipient, funding/awarding office, obligations, descriptions and performance dates | Open work, buyer intent, remaining money or future renewal |
| SAM opportunities and amendments | Notice type, requirement, eligibility, deadline, attachments and response instructions | An Active label alone does not mean responses are still open |
| Agency acquisition forecasts | Anticipated procurements and program context | Funded or released solicitations |
| SBA prime directory / SUBNet / prime supplier pages | Potential teaming routes and relevant contractors | An available work package or permission to register/contact |
| City/county official procurement portals | Local terms, bidding rules, training and workflow requirements | Federal thresholds or federal contract eligibility |
| Public policy/use-case inventories | Possible mission tasks and existing tools | A procurement budget or unfilled need |

[SBA's guide](https://www.sba.gov/counseling/prime-and-subcontracting/) links the prime directory and SUBNet. Use official source tools and permitted interfaces; no bulk download, paid provider or authenticated export is needed for the initial manual batch.

## Reproducible manual pass

1. Define the service, excluded missions, jurisdiction, performance geography, relevant NAICS and review date.
2. Search both the task and common procurement language: AI training, document processing, knowledge management, workflow automation, records search, evaluation. Do not use the word AI alone as qualification.
3. Review a bounded set of awards separately from notices. For annual spending, sum transaction obligations in the selected fiscal window, including deobligations; do not sum ceilings, cumulative award totals and child orders together.
4. Resolve the recipient and buying office. A department is not a single buyer. For primes, verify the relevant program and partner route.
5. Deduplicate notices by notice/solicitation identity and amendments; retain versions and the latest controlling deadline. Distinguish multiple task orders from their parent vehicle.
6. Open the original source and then the complete notice/attachments before qualification. Record what was actually read. Search snippets and third-party summaries are discovery only.
7. Apply the gates below. Preserve expiry, unavailable source, specialist mismatch and no-issue outcomes.
8. Prepare one next verification per retained row. Do not convert a researched route into a qualified opportunity until its requirement, purchasing path and capability fit are established.

## Private record contract

Record: stable ID; organization and buying office; jurisdiction; route (prime, subcontract, local, provider pool); notice/award ID; canonical URL; source date and checked time; notice type; posted/response/expiry dates with original time zone; latest amendment; NAICS/PSC; vehicle; set-aside; current funding/estimated value/ceiling as separate fields; task; buyer role; source evidence; capability requirements; data classification; existing tools; scope/acceptance; performance geography; gap; next verification; stage; owner; activity state and suppression/permission state.

Unknown budget remains null/unknown, never zero or the parent contract ceiling. Contact details are optional until needed; prefer a sourced public business route and do not guess a person's authority.

## Gates and explainable priority

| Gate | Pass condition | Hold example |
|---|---|---|
| Source | Original current notice or official partner route reviewed | Aggregator-only listing or inaccessible attachments |
| Timing | Correct response time remains available | Active notice with expired response date |
| Access | Eligible prime/teaming route and set-aside/vehicle requirements | SAM registration mistaken for a GWAC seat |
| Capability | Relevant deliverable, staff, evidence and location supportable | Generalist agency on a biosequence search product or university-only seminar |
| Task and data | Reproducible workflow, permission and feasible environment | Sensitive-data or mission scope outside demonstrated readiness |
| Commercial | Buyer/program, purchasing route, realistic budget evidence and full cost | Supplier portal or RFI counted as a paid lead |

Prioritize only after these gates: known task fit, access to a buyer/program, short bounded delivery, credible evidence, measurable acceptance and low integration burden. Do not produce a single opaque score or infer intent from agency size.

Stages: discovered → source verified → eligibility reviewed → buyer need verified → proposal preparation → submitted (only with authorization) → awarded → accepted/delivered → paid. RFI response, supplier registration, prime teaming discussion and direct bid are different activity types.

## This pass

Six private research entries were retained: one AI-training provider-pool RFI, one adjacent website-support RFQ and four official contractor partner routes. Two notices belong to the same organization and are separate opportunities, not two distinct buyers. Four held records preserve an expired response, two specialist mismatches and one aggregator-only local listing. There are five distinct organizations in the retained queue, zero qualified buyers, zero submitted responses and zero known revenue.

No suitable open federal RFP was fully qualified in this bounded search. This is a sample shortfall, not evidence that no such work exists. Opportunity attachments were not downloaded or reviewed. The next useful action is reading the best-matched complete source packages and verifying one prime's specific workshare opportunity.

## Later implementation, only if justified

Add a procurement research profile to the existing system rather than starting a parallel CRM. Proposed modules: permitted source adapter; award/notice parser; amendment/version resolver; entity/program linker; eligibility checks; evidence ledger; private queue; review/export. Keep raw imported text untrusted and suggestions pending review.

Evaluate with synthetic fixtures for expired-but-active notices, amended deadlines, inaccessible documents, grants versus contracts, double-counted orders, missing budget, no matching NAICS, missing vehicle access and no-fit outcomes. A source change must invalidate stale review. Preserve user edits and audit history. API keys, rate limits, storage rights, attachment handling and private access controls require their own implementation review; none is enabled here.
