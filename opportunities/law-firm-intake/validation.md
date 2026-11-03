# Research-package validation

Checked 2026-11-03. Scope: documentation and hypothetical economic calculations only.

- The repository's dependency-free `python3 -B scripts/validate_docs.py` checks local Markdown targets/anchors, required historical source counts, JSON/CSV shapes, whitespace and public-content patterns. It was run against an isolated copy of the existing repository plus this opportunity directory.
- The three cost scenarios were independently recalculated from JSON inputs and compared with the CSV; setup contribution and the combined escalation/support stress case were checked. An initial low-volume narrative arithmetic error was corrected before publication. Final modeled monthly costs are **$450, $806 and $2,100**.
- Manual review covers source-to-claim fit, current versus proposed/future law, expired pricing promotions, incomplete vendor evidence, hypothetical versus observed metrics, and public suitability. No personal legal narrative, actual contact record, private URL, credential or source document is included.
- Existing repository files are preserved. The publication scope contains only original files under `opportunities/law-firm-intake/`; root index/status suggestions are in [integration notes](integration-notes.md).

The documentation checker records external URLs but does not fetch them. Research source reads are separately described in the [source register](sources.md). No application, telephony, email, portal, security, integration or synthetic acceptance tests were run, because none of those systems was built or activated in this task. Proposed pilot criteria are not passed checks.

No counsel has approved the design, no vendor has been selected, no customer has paid, and no real-world response or business impact has been measured. GitHub draft status and exact commit are reported in the delivery handoff after remote verification.

## Discoverability follow-up

On 2026-11-03, the publication scope expanded to additive research links and status/next-step explanations in the root README, current-state document and roadmap. Their existing text was preserved. The opportunity's integration/decision notes record this completion, superseding the initial scope description above. The documentation validator was rerun after these additions; no new research, download or application test was needed.

The follow-up validator passes for **53 text files and 467 Markdown links**. A line-level comparison confirmed that all original text in the three shared documents remains, with additions only. An isolated three-way README check against the inspected Software Factory PR #1 head `a8862a4369a803652a287ed91bd6138c465ba4c8` completed without conflicts and retained both research/factory index entries. This was a temporary-file compatibility check, not a branch merge or validation of the combined applications.
