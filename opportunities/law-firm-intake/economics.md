# Economics and pricing hypotheses

All amounts USD. Model date 2026-11-03. **No actual customer, revenue, operating bill or willingness-to-pay observation exists.** This is a sensitivity model, not a quote or revenue forecast. Public competitor prices are separately labeled in [market research](market-and-competition.md).

## What the service would sell

Charge for bounded discovery/configuration, one approved intake workflow, training, integration QA and defined ongoing support. Prefer the firm's existing paid platform and make provider costs transparent. A new software subscription must show value beyond configuring the tools the firm already owns. Security, legal review and human escalation are delivery costs; reducing data scope can reduce those costs without eliminating them.

Potential commercial forms to test:

| Form | Potential value | Cost and contract discipline |
|---|---|---|
| Existing-platform implementation | Fix a specific response/handoff failure and train staff | Fixed scoped project; customer pays platform directly; verify vendor terms and partner/resale permissions |
| Managed callback workflow | Maintain scripts, queues, integrations, reporting and reliability | Setup plus monthly care; explicit minutes/calls/email/support caps and human coverage |
| Custom multichannel software | Only a demonstrated need not met by native products | Separate discovery, threat model and development estimate; do not absorb custom portal/security work into a cheap receptionist fee |

No percentage of legal fees or cross-firm lead resale is proposed. Outcome-based competitor pricing is an observation, not approval of our compensation model.

## Cost assumptions

[Inputs](economics-assumptions.json) and [calculated scenarios](economics-scenarios.csv) contain the full model. All prices below except the identified public examples are **analyst assumptions to replace with quotes/time logs**.

- Voice: **$0.20 per minute**, a planning allowance for a configurable AI voice stack including carrier cost. The [Retell public example](https://www.retellai.com/pricing) totals $0.125/min for selected components before add-ons; that example is not the price of our proposed implementation. Do not add a second carrier charge if already included. Taxes, toll-free/international routing, transfer legs and unusual features may add costs.
- Email: **$0.03 per processed thread**, hypothetical model/processing allowance; retries, message/token length and attachment processing are not benchmarked. Includes no per-message paid provider quote. Mailbox/automation hosting belongs in the platform allowance.
- Number: **$2/month** assumed. Platform/hosting/integration allowance **$75–$150/month per firm**. No separate custom-portal development is included.
- Human fallback: **$8 per escalation**, assumed; proposed shares **10%, 10%, 25%**. Availability and terms are not contracted. A firm's own staff time still has a cost.
- Support/QA: **$75/hour** loaded labor, **2/3/6 hours per month**. Security/insurance/compliance-operations allocation: **$100/$150/$200 per firm per month**, unvalidated. A small customer base may not cover minimum organization-wide costs at these allocations.

## Monthly sensitivity

| Hypothetical case | Calls / average minutes | Email threads | All modeled cost | Illustrative price | Contribution / margin | Price needed for 50% modeled margin |
|---|---|---|---|---|---|---|
| Low volume | 80 / 3.5 | 100 | $450 | $599 | $149 / 24.9% | $900 |
| Base | 200 / 4 | 300 | $806 | $1,199 | $393 / 32.8% | $1,612 |
| Heavy support | 400 / 6 | 600 | $2,100 | $2,499 | $399 / 16.0% | $4,200 |

Formula: `monthly cost = calls × average minutes × voice rate + email threads × email rate + number + platform + calls × escalation share × escalation unit cost + support hours × loaded hourly rate + security allocation`. Contribution is price minus modeled cost; margin is contribution divided by price. This is not company net profit. Sales/acquisition, general administration, financing, taxes, refunds, bad debt, extraordinary incidents and product development can reduce it further.

At the base price, moving escalation from 10% to 25% adds **$240/month** and cuts contribution to **$153**. Three more support hours add **$225**. Both together make contribution **negative $72**. Low raw model cost does not guarantee a healthy service margin.

## Setup and customer break-even

Hypothetical implementation labor at $75/hour: 12/24/40 hours, plus $300/$600/$1,200 allocation for external legal/security review, gives **$1,200/$2,400/$4,200** modeled setup cost. Illustrative setup prices $2,000/$4,000/$7,000 yield 40% modeled contribution before acquisition and general overhead. These allowances may be insufficient; specialist review and custom development require separate quotes. Do not treat them as a promise that counsel will approve the design.

Customer incremental value should use **collected contribution per additional suitable matter after delivery costs**, not the face value of a case or gross legal fees. Example only: $1,199/month plus $4,000 setup amortized over 12 months is $1,532.33/month. At hypothetical $1,000 contribution per additional matter, break-even requires about **1.53 incremental matters/month**, practically two; at $500, about 3.06, practically four. Add staff/vendor costs borne directly by the firm. A paid consultation might never turn into a retained matter; contingency receipts may take a long time.

Do not multiply the Clio nonresponse rate by a firm's inquiries and call the result recoverable revenue. Measure eligible incremental outcomes, no-shows, capacity, collection timing and displaced work. The attractive path may be a modest configuration project rather than a custom recurring product.
