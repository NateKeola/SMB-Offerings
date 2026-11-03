# Pricing evidence and economics

Historical research snapshot: **2026-11-02**. All operating costs, prices to test, acquisition, support and churn assumptions below are hypotheses. Recheck published offers and the actual payment/provider account before selling. No customer willingness to pay or realized profit has been measured.

Visible in this repository: [market-price table](../research/market-price-observations.csv), [source register](../research/market-source-register.md), [model assumptions](economics-assumptions.json), [24 scenarios](economic-scenarios.csv), [incremental add-on sensitivity](addon-scenarios.csv) and [price floors](price-floors.csv). These preserve the original model inputs/outputs; the source model remains linked below.

## What was researched

The source project retained 26 primary-source URLs, 17 price observations and 24 economic scenarios. See the [source register](https://github.com/NateKeola/Dogfood/blob/5bbe43b32bb8941106c5505c92f438bd4e4e0fe0/research/smb-service-opportunities/sources.md), [dated price table](https://github.com/NateKeola/Dogfood/blob/5bbe43b32bb8941106c5505c92f438bd4e4e0fe0/research/smb-service-opportunities/data/market-prices-2026-11-02.csv), [assumptions](https://github.com/NateKeola/Dogfood/blob/5bbe43b32bb8941106c5505c92f438bd4e4e0fe0/research/smb-service-opportunities/economics/assumptions.json) and [scenario outputs](https://github.com/NateKeola/Dogfood/blob/5bbe43b32bb8941106c5505c92f438bd4e4e0fe0/research/smb-service-opportunities/economics/scenarios.csv).

| Dated vendor observation | Interpretation and limitations |
|---|---|
| Oak Harbor: $175/month, five-page website, twelve-month minimum | A particular bundled offer; hosting/edits/support terms matter. Cancellation ownership differs from a lump-sum purchase. USD was inferred from context. |
| Oak Harbor: $3,800 lump-sum website plus $25/month hosting | A different ownership/payment model; edits and extra pages can cost more. |
| Web Engine: $97/month website or support offers, $297 ecommerce | Page counts, edit caps, ownership and checkout terms were not fully established. |
| WebFX: local SEO from $575/month; SMB SEO from $2,900/month | Specific vendor starting offers, not market averages; final location/content scope and terms need a quote. |
| AI-search agencies: $590/month starter; another $499 audit and $2,500/month starter | Currency/geography and efficacy were unresolved for these dollar-symbol offers; no adoption of promotional outcome promises. |
| BrightLocal: $41/$54/$65 monthly tiers for one location; annual pricing differs | Software costs, not a managed-service labor price. Citation work and renewals are separate. |
| Screaming Frog: £199/year; free crawler up to 500 URLs | Historical operator-license observation; no FX conversion or hosted API inference. |

Published offers establish what a vendor advertised, not transactions, customer satisfaction or fair-market value. The historical Ahrefs provider survey is not a current median; its methodology and timing have limits. Keep software pricing, agency pricing and our own hypotheses separate.

## Model assumptions

Base case: $60/hour direct labor; 15 support minutes/account/month; $3 infrastructure; $10 shared overhead (a $200 pool across twenty accounts); $200 acquisition cost; $399 setup for six labor hours plus $30 other cost; 3% monthly churn. Payment example: 2.9% + $0.30 plus a **hypothetical 1% billing allowance**. The billing fee was not verified and must be replaced.

The model's fifteen-minute base is not the care menu's twenty-minute cap. Recalculate using expected actual work and stress scenarios before quoting. A five-account pilot allocates $40 overhead per account; scale does not eliminate work.

Setup nets $387.129 after the modeled card fee against $390 delivery cost. With acquisition, unrecovered cost is $202.871. A credited diagnostic must fit within the same setup total and hours; it is not additional setup revenue. Replacing 3% churn in a stable book implies a $6.08613 monthly per-account allowance. It is not a second charge against the same customer or an extra acquisition deduction in lifetime calculations.

```text
recurring contribution = price × (1 − variable fee rate)
                         − fixed fee − labor − infrastructure − allocated overhead
economic contribution = recurring contribution − churn × unrecovered acquisition/setup
break-even price = (fixed fee + labor + infrastructure + overhead
                    + churn × unrecovered acquisition/setup) / (1 − variable fee rate)
```

This contribution excludes tax, financing, refunds, bad debt and extraordinary incidents. It is not net profit. Setup revenue is not ARR.

## Standalone versus incremental

| Monthly price | Base economic contribution | Support-stress case | Five-account pilot |
|---:|---:|---:|---:|
| $10 | −$24.78 | −$64.78 | −$71.78 |
| $30 | −$5.56 | −$45.56 | −$52.56 |
| $40 | $4.05 | −$35.95 | −$42.95 |
| $79 | $41.53 | $1.53 | −$5.47 |
| $99 | $60.75 | $20.75 | $13.75 |
| $149 | $108.80 | $68.80 | $61.80 |

The $40 standalone idea leaves about $4 only under the base assumptions. It is not observed profit. At eight-percent churn that modeled contribution becomes −$6.09. The model's chosen 40% contribution target gives floors of $61.29 base, $132.60 support stress and $145.07 low utilization; those are arithmetic, not willingness to pay.

Incremental additions on a shared account/invoice can have different economics: $10 with two extra minutes and $0.50 infrastructure gives $7.11 modeled contribution; $30 with ten minutes and $1 gives $17.83; $40 with twenty minutes and $2 gives $16.44. These exclude new base overhead, CAC and the fixed transaction fee. Each becomes negative if it consumes a full labor hour. Do not present add-on margins as standalone margins.

## What to validate before scaling

Track all research, failed selling, demos, onboarding, support and incident time. One thousand prospects at five research minutes each means 83.3 hours before calls or follow-up. At hypothetical 1% versus 3% paid conversion, that research labor alone is $500 versus $166.67 per customer at the model's labor rate; neither conversion is observed.

One thousand active accounts at fifteen support minutes require 250 hours/month. Replacing 3% monthly churn with six-hour setups adds 180 hours, before sales and incidents. Standardization, capacity and exception management are necessary; this is not a passive-income projection.

The next price decision should use actual delivery minutes, permitted tool costs, customer capacity/value, cancellations and support tails. If there is no recurring benefit, offer a one-time job. Preserve scope caps and re-quote unfamiliar integrations before selling.
