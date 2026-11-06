# Outbound Phone Assessment: Verification Record

**Date:** 2026-11-03. **Scope:** Documentation-only research publication. No product implementation or live call testing.

## Repository review

Read the repository's root AGENTS.md, README, decision register, current state, source-project inventory, architecture boundaries, spend contract, and documentation validator before editing. The recursive tree contained no additional applicable AGENTS.md under opportunities, strategy, or status.

The documentation branch started from main commit 725509ee760f3b3348caef41558e7eebcfa161a1. Existing content was preserved with scoped additions to the README, decision register, and current-state report. Source applications, historical test claims, and provider activation settings were not changed.

## Checks performed

- Read back the new technical design and overview plus the three edited handoff files through the connected GitHub reader. Their full text matched the prepared originals.
- Checked H1 headings, terminal newlines, trailing whitespace, and balanced code fences on those five changed Markdown files.
- Checked 136 Markdown links in those five files. Relative targets were resolved against the reviewed repository tree and the new package paths; new-package section anchors were checked against their headings.
- Recorded 37 distinct external HTTPS source links across those five documents. The research used current official source pages; this structural pass is not a new crawl or a guarantee of future URL availability.
- Applied the repository's relevant public-content pattern categories to the changed documents: private document URLs, local absolute paths, email addresses, credential-shaped strings, and internal thread identifiers. No matches were found.
- Manually reviewed public suitability: no private conversation excerpts, real leads, contact lists, actual call records, suppression records, private case examples, or credentials are included. A fictional narrative example is explicitly labeled.
- Recalculated the cost table from the stated unit assumptions. The 1,000-attempt figures use unrounded underlying values rather than rounded 100-attempt display amounts.

The verification record itself and final PR file list are checked by remote readback at publication. No check here establishes market demand, production reliability, or a legal authorization to call.

## Pricing arithmetic check

For 100 attempts with 60 connected calls:

| Configuration | 30-second actual connected calls, before display rounding | 60-second actual connected calls, before display rounding |
|---|---:|---:|
| Twilio carrier | 60 × 0.014 = 0.84 | 60 × 0.014 = 0.84 |
| Twilio with AMD | 60 × (0.014 + 0.0075) = 1.29 | 60 × (0.014 + 0.0075) = 1.29 |
| Retell | 30 × 0.0978 = 2.934 | 60 × 0.0978 = 5.868 |
| Vapi low estimate | 30 × 0.0818 + 0.84 = 3.294 | 60 × 0.0818 + 0.84 = 5.748 |
| Vapi high estimate | 30 × 0.1289 + 0.84 = 4.707 | 60 × 0.1289 + 0.84 = 8.574 |
| Telnyx | 60 × 0.057 + 30 × 0.0064 = 3.612 | 60 × 0.057 + 60 × 0.0064 = 3.804 |

USD estimates only. See [assumptions and primary pricing sources](technical-design.md#12-cost-model). No rate was verified against a paid account or invoice.

## Checks not run

- The required repository-local command `python3 -B scripts/validate_docs.py` was **not run**. This connector-only workflow did not materialize a repository checkout or execute repository code. The in-memory checks above are a narrower substitute, not a claim that the repository validator passed.
- No full-repository executable validation, application test suite, build, deployment, or live telephony integration was run.
- No paid model/voice benchmark, call-quality evaluation, carrier timing comparison, privacy-retention experiment, or invoice reconciliation was executed.
- Current account entitlements, approved recipients, consent evidence, local calling windows, budgets, and exact provider integration remain unresolved.

The draft PR must retain these gaps. Before implementation, use a permitted existing checkout to run the repository validator, inspect the final diff, and resolve the [live implementation requirements](technical-design.md#15-unresolved-requirements-before-live-implementation). No package installation or repository download is needed merely to read this research.

## Research interpretation

Source facts, architecture recommendations, modeled cost, proposed tests, and unknowns are labeled separately. A network answer is not proof of human access; no-answer is not proof of lost revenue or need for AI. Vendor claims and sample latency values are not independent measured performance.

[Return to the package overview](README.md).
