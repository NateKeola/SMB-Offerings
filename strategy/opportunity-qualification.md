# ICPs, qualification and prioritization

Use this with the [ICP template](../templates/icp.md), [opportunity record](../templates/opportunity-record.md) and [research protocol](../research/research-protocol.md). It summarizes the existing engine's gates and proposes a transparent manual prioritization aid. It is not a new scoring implementation.

## Candidate markets

| Profile / market | Buyer and task to investigate | Evidence needed | Main delivery constraint |
|---|---|---|---|
| Wholesale garments / catalog discovery | Owner, sales operations or ecommerce lead; find a suitable product/variant and prepare a quote | Known-product control, repeated descriptive-search friction, relevant catalog, rep/customer questions | Authorized feeds, variant mapping, freshness and customer-specific pricing |
| Local-service inquiries | Owner or office manager; understand service scope/coverage and the next step for a quote | Known-service control and repeated inquiry, quote-clarity, service-area or navigation friction | Real capacity, approved facts, receipt routing and support |
| Cleaning business | A specific example of the local-service profile | Owner-validated inquiry burden, spare capacity, economics and willingness to pay | Existing form/field-service tools may already suffice |
| HVAC/plumbing | Routing or qualification may matter more than more traffic | Unanswered qualified calls, dispatcher workload, capacity by job type | Urgency, availability and operational reliability; avoid autonomous triage |
| Industrial/MRO distribution | Sales/branch operations or ecommerce/IT; exact specifications and availability | Search/rep lookup evidence, authorized catalog and buyer-defined tasks | ERP/PIM, units, equivalents, permissions and safety-critical specifications |

The table retains hypotheses from the [industry research](https://github.com/NateKeola/Dogfood/blob/5bbe43b32bb8941106c5505c92f438bd4e4e0fe0/research/smb-service-opportunities/industry-analysis.md), not proof of demand or local prevalence. The [2026-11-07 working record](agency-direction-and-icp.md) adds a meeting-level wholesale-first direction and ongoing local-service discovery; it does not validate any profile.

## Gate sequence

| Gate | Required evidence / decision | Hold or reject when |
|---|---|---|
| Scope | ICP, geography, allowed sources, profile, exclusions, batch/query caps and cost basis | Criteria or source rights are missing |
| Identity and access | Business/domain/branch association, current operation, fresh public access | Identity conflict, uncertain operation, login/CAPTCHA, denial or stale access |
| Fit | Industry, geography, maturity, buyer workflow and exclusions; catalog size only when relevant | Wrong market, no capacity evidence, unsupported size or excluded workflow |
| Pain | Successful known-product/service control and matching friction at two distinct timestamps | No control, generic design opinion, unreproduced issue, low confidence or conflicting evidence |
| Contact | Fresh public business route with source and association; the current engine requires a reviewed business phone | Guessed contact, stale/invalid number or unresolved role/domain association |
| Value | Original bounded brief, simulation limits, plausible benefit, effort/price assumptions and test | No usable demonstration plan or unsupported built/ROI claim |
| Preparation ready | All current human reviews, freshness and suppression checks | Pending/held/rejected gate, changed context, suppression or stale evidence |
| Outcome | Record only actions and results that occurred | Missing measurement or invented sales/paid-pilot status |

The engine uses pending/approve/hold/reject decisions, not a universal lead score. Approvals bind to the candidate revision and complete ICP/profile/policy fingerprint. Changed evidence or policy can invalidate readiness. A human-reviewed queue remains preparation, not authorization to call.

## Record the observation honestly

| Editorial label | Meaning | Engine treatment / next step |
|---|---|---|
| Observed | Direct, dated behavior with source and reproduction steps | Manual provenance still needs independent human review |
| Inferred | Plausible explanation or business implication | Keep as hypothesis; obtain a direct observation |
| Unknown | Necessary evidence is missing | Incomplete; never substitute zero or a pass |
| Not assessable | Access or method prevented a valid test | Record blocked/error/unknown as appropriate; no negative business judgment |
| No issue observed | The bounded task worked | Preserve the control/sample; do not invent a pitch or generalize to every task |

Source claims and agent suggestions remain distinct from direct observations. The engine accepts manual, agent, synthetic and legacy-unspecified origins. Agent and unspecified records cannot satisfy gates. Synthetic records can qualify only fictional candidates. Rechecking creates a new dated observation; relabeling a suggestion is not verification.

## Profile-specific task cards

For `catalog-discovery-v1`, identify a real public product and exact name/SKU. Verify the known-product control first. Test a realistic descriptive/application query and attribute query, recording exact input, expected result and observed result. Reproduce meaningful friction at a second time. The default is eight queries including repeats; the engine hard maximum is twelve. An unsuccessful search does not establish its cause or whether semantic technology exists.

For `local-service-inquiry-v1`, confirm a real service on a public page, then test finding the eligibility, coverage and next step needed for an inquiry. Repeat a specific navigation/information mismatch. No SKU or catalog threshold is required. Missing published prices alone does not prove a broken quote process. Do not submit a form, call, book or invent availability during the public-site assessment.

## Proposed prioritization after the gates

Compare qualified candidates on observable dimensions: frequency/severity of the task, buyer access, capacity, usable data, prototype effort, integration risk, measurement feasibility and likely support burden. Give each a short source-backed rationale with low/medium/high confidence and explicit unknowns. Prefer a small reproducible problem that the buyer recognizes and can measure.

This rubric is a manual planning aid, not calibrated probability, market demand or an engine feature. Hard holds and suppressions always take precedence. An evidence-poor candidate does not become ready through a high aggregate score.

## 2026-11-07 — Follow the observed customer journey

Use the [evolving prospecting workflow](../research/prospecting-workflow.md) to preserve the user's actual search, site-inspection and calling pathway as details become available. Its website checks, comparable categories and harness are proposed operating aids, not implemented features.

Record search position and agent presence separately from task pain. The user's three-roofer anecdote is too small and uncontrolled to establish adoption rates or any relationship between visibility and automation. Neither a low rank nor a missing agent qualifies a prospect without the existing identity, fit, pain and value gates. Distinguish agent absence from not observing one on a particular channel, and preserve existing-tool and no-issue outcomes.
