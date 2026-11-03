# Validation and response-time benchmarking

Proposed 2026-11-03; **nothing has been executed**. This plan preserves the upside of response-time measurement while limiting needless disruption to firms and prospective clients. Commercial evidence and legal/security readiness are separate gates; passing either does not establish the other.

## Commercial questions before building

For a later authorized discovery batch, compare about 8–12 firms in the proposed segment. This sample size is a planning choice, not statistical validation. Do not contact them under this assignment. Draft questions:

1. What happens to an inquiry received while staff are busy or outside business hours? Who owns the callback and who can see overdue work?
2. How many unique new inquiries arrived last month by channel? How many were spam, wrong practice, conflicts, existing clients or duplicates? Which counts are reliable?
3. What does “responded” mean here: automatic receipt, human reply, conversation, consultation or signed engagement?
4. Is there capacity for more consultations and matters? What is the actual constraint: answering, screening, scheduling, follow-through or legal availability?
5. What already exists in the CRM/receptionist service, and why is it insufficient? Would configuring the native feature solve the problem?
6. Which information may intake collect before conflict review, and what must wait for a lawyer? Who approves scripts, vendors, retention and disclosures?
7. What implementation fee and recurring obligations would make sense? Would the buyer pay for a scoped pilot at a specified price, with a clear stop option?

Record buyer statements separately from analyst inference. A positive conversation, interest in AI or hypothetical budget is weaker evidence than a signed, paid scope. Do not invent conversion percentages from this small sample.

## Benchmarking methods that preserve useful signal

The user wants to understand response times using realistic, practice-specific scenarios. Recommended methods are **firm-authorized synthetic tests**, **authorized retrospective inquiry-log audits**, and **clearly disclosed non-client questions**. Do not pose as a genuine person with a fabricated legal dispute to prospect to an unsuspecting firm. That can occupy staff, create misleading conflict/intake records and produce a poor measure of real customer fit. This is an operational recommendation, not a legal finding that every mystery-shop test is unlawful.

| Method | Evidence obtained | Control and limitation |
|---|---|---|
| Authorized retrospective audit | Actual receipt, callback and outcome timestamps across channels | Firm supplies permitted deidentified/aggregated extracts in an approved private system; counsel/privacy owner approves access. Missing logs and selection bias remain explicit. No raw mailbox access in this research. |
| Firm-authorized synthetic mystery shop | End-to-end routing, response latency, errors and staff workflow | Firm owner approves channels, windows, caps, test identities, content and cleanup. Staff awareness/timing can be blinded only within that agreement. Use controlled contact routes, no real adverse parties or court deadlines, no false emergency and no consultation capacity reservation without permission. Label/reconcile test records privately. |
| Clearly disclosed non-client inquiry | Whether the business routes a commercial/research question | Say what the inquiry is. Do not interpret its response time as equivalent to a legal client's urgent request. Requires separate outreach authorization. |
| Offline fictional replay | Script boundaries, extraction and failure handling | No real mail/phone endpoints. Useful for mechanics, not market demand or actual reception quality. |

Do not reproduce third-party secret-shop studies as an outbound campaign merely because their published research used fictional scenarios. No emails, calls, forms, bookings or messages were sent here, and the repository's current email hold remains in force.

## Proposed baseline and pilot design

After explicit authorization and firm/counsel/vendor readiness, collect a **2–4 week baseline** and a **4–6 week pilot** for one firm, one practice scope and one defined coverage window. These are planning ranges. Match weekday/time windows and note staffing changes, campaigns and holidays. Prefer a permitted staggered rollout; do not intentionally withhold normal care or misroute urgent calls for an experiment.

Use one inquiry ID across channels with human-resolved duplicates. Define eligibility before looking at results. Report total arrivals, spam/irrelevant items, eligible unique inquiries and unresolved classifications separately. Keep nonresponses as censored/unresolved outcomes, not missing rows. Show median and p90 times alongside the number and percentage never reached within the fixed observation window; a responders-only median hides failures. Separate business-hours and clock-hours measurements.

| Measure | Definition |
|---|---|
| Acknowledgement latency | Receipt to confirmed automatic receipt; does not prove a person responded |
| Human-response latency | Receipt to first verified personal outreach; report failed attempts separately |
| Contact-completion rate | Eligible unique inquiries with successful two-way human contact / eligible unique inquiries |
| Callback adherence | Promised callbacks completed in the approved window / callbacks promised |
| Record quality | Reviewed records with correct contact, consent, channel, party spellings and routing; field-level errors and omissions |
| Workflow reliability | Delivery/CRM/calendar failures, duplicates, unowned records and reconciliation time |
| Consultation and engagement | Scheduled, attended, accepted and hired are separate events; human recorded |
| Economics | Provider bill, human-fallback cost, staff minutes, support hours, setup effort and actually collected contribution |
| Experience and accessibility | Caller abandonment, human requests, consent declines, accessibility failures and complaints |

No uplift target is established by the studies. Agree a baseline-specific minimum improvement and price before launch. With low volume, report counts and uncertainty; do not claim causality from a simple before/after change. Safety failures are not averaged away by faster response.

## Synthetic acceptance pack to prepare before any live pilot

Create original fictional fixtures for: ordinary new callback; repeated email plus call; wrong practice; existing client; represented party; shared phone/email; unclear party spelling; unexpected sensitive narrative; urgent deadline; immediate danger; declined recording/AI processing; relay/accessibility needs; unsupported language; malicious attachment; prompt-injection request; spam/autoresponder loop; invalid destination; CRM outage; duplicate webhook; revoked credentials; calendar conflict; staff unavailable; spending threshold; deletion/legal hold; attempted cross-firm access.

For every case specify input, approved output/action, forbidden action, accountable reviewer and expected private audit evidence. Critical synthetic cases must all pass before seeking live-pilot approval. This research has designed the cases, not executed or passed them.

## Go, change direction or stop

**Proceed to a bounded pilot only if** a buyer verifies an important failure, has capacity, assigns an owner, agrees a measurable outcome and price, and the required counsel/security/vendor controls are satisfied. A nonresponse percentage alone is not enough.

**Change direction to implementation-only** if native products meet the functional need and the buyer mainly needs setup, training and follow-through. **Stop or pause** if there is no meaningful pain, no staffed handoff, no willingness to pay a sustainable price, inadequate vendor/data controls, unsupported languages/urgency, or repeated material errors. A single serious privacy/consent/cross-firm incident triggers suspension and investigation, not silent tuning in production.

Legal/security obligations should guide scope and cost, not automatically disqualify the business. The [risk-to-solution table](decision-log.md#risks-solutions-and-value-preserved) makes the tradeoffs visible.
