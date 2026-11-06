# Outbound Phone Assessment Research

**Updated:** 2026-11-03. **Status:** Research only; no calls, provider activation, implementation, or measured customer results.

This package evaluates an agent-led outbound phone assessment that could inform a later inbound-answering offer. It covers carrier observations, optional conversational AI, uncertainty, operational controls, costs, and a future implementation plan.

## Read the research

- [Full technical design, provider comparison, state machine and event schema](technical-design.md)
- [Cost model and reproducible 100/1,000-attempt calculations](technical-design.md#12-cost-model)
- [Owned/authorized-number acceptance criteria](technical-design.md#13-acceptance-criteria)
- [Engineering effort and next implementation scope](technical-design.md#14-engineering-effort-and-next-implementation-scope)
- [Open decisions before live implementation](technical-design.md#15-unresolved-requirements-before-live-implementation)
- [Documentation verification and remaining gaps](validation.md)

## Recommendation

Build the eligibility, measurement, queue, evidence, and budget layer. Buy real-time voice handling. Use Twilio as a carrier-measurement baseline, then evaluate Vapi for a separately approved speech-enabled path because its documented ZDR and artifact controls fit metadata-only retention. Retell and Telnyx remain alternatives with different trade-offs.

This is an engineering recommendation, not a selected vendor, purchase, or claim of tested performance.

## Interpretation boundary

A network answer can be a person, IVR, voicemail, or screening service. A no-answer result is not proof of lost revenue or need for AI. Report the protocol, local window, timeout, missing data, and uncertainty.

Overnight processing and reporting can be unattended. Calling still requires an approved recipient-local window, eligibility, caller ID, suppression checks, and budget. After-hours tests are limited to explicitly authorized windows.

Metadata-only measurement does not classify speech. Optional real-time speech processing needs a separate privacy review even when recordings are not retained.

## Relationship to the existing work

- Preserve the shared evidence/profile boundaries in [system responsibilities](../../architecture/system-and-integrations.md).
- Preserve estimated, reported, reconciled, and unknown costs in [spend and measurement](../../architecture/spend-and-measurement.md).
- See [source projects](../../status/source-projects.md) for the separate, unmerged application prototypes.
- The [inbound law-firm intake package](../law-firm-intake/README.md) is related research, not the selected vertical for this assessment.

Public content contains original summaries, official source links, schema proposals, and an explicitly fictional narrative example. It contains no actual lead lists, contact details, call records, private conversation excerpts, or account credentials.
