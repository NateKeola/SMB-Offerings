# Phone Response Assessment: Technical Design

**Research date:** November 3, 2026
**Status:** Architecture proposal, not an implemented or live-tested system
**Initial market assumption:** Standard US domestic destinations; other jurisdictions require separate review

**Recommendation:** Build the measurement, eligibility, scheduling, and evidence layer. Buy the real-time conversation layer. Start with Twilio for carrier-level observations and evaluate Vapi for the optional conversational adapter because its documented ZDR and artifact controls fit metadata-only retention better. Retell is a credible alternative, but its privacy and ring-timing limitations need explicit acceptance.

This research performed no live calls, product implementation, account setup, purchases, provider activation, or deployments. Documentation publication is separate from those activities. See [package overview](README.md) and [verification record](validation.md).

## 1. Product definition

Build an authorized phone-response assessment that answers:

- Did the telephone network connect the call?
- How long elapsed between network-reported ringing and connection?
- When speech processing is approved, did the first answering endpoint appear to be a person, voicemail, an IVR, a screening service, or something uncertain?
- Did an authorized brief conversation complete successfully?
- What operational evidence supports offering an inbound answering pilot?

The output is an evidence-backed observation, not a diagnosis of the business.

“No answer during this test” does not establish that the business lost a customer, has poor service, or needs AI. Closed hours, screening, forwarding, carrier rejection, and a deliberately short test timeout can all affect the result.

**Overnight operation should mean unattended processing and reporting.** Calls run only within the recipient's approved local window. An after-hours assessment can be useful when the business explicitly authorized that test window.

## 2. The practical constraint

An AI voice call is still an outbound call, even when described as an audit. The FCC treats AI-generated voices as artificial voice under the TCPA; applicable consent requirements depend on the destination and purpose. A public business listing is not evidence of consent, and “B2B” is not a universal exemption. Twilio additionally requires accurate identification and purpose disclosure, applicable consent, and adherence to its calling restrictions. Eligibility therefore belongs in the dispatcher, not merely in a prompt. [FCC ruling](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf), [Twilio Voice Services Policy](https://www.twilio.com/en-us/legal/service-country-specific-terms/voice-sip), [FTC business-call protections](https://www.ftc.gov/news-events/news/press-releases/2024/03/ftc-implements-new-protections-businesses-against-telemarketing-fraud-affirms-protections-against-ai).

A useful initial cohort is owned test endpoints followed by businesses that requested a phone assessment. This is not a plan for mass unsolicited overnight dialing. The source review is not jurisdiction-specific legal clearance.

## 3. Build versus buy

| Option | Strength | Main limitation | Recommended role |
|---|---|---|---|
| Twilio Programmable Voice | Explicit call-progress events and controllable telephony | Carrier connection is not human-answer detection | Measurement baseline |
| Vapi with a supported carrier integration | Hosted conversation, ringing events, artifact controls and ZDR | Component billing and provider behavior need validation | First conversational candidate |
| Retell | Managed conversation, voicemail/IVR handling, analysis and SIP integration | Transient content storage; basic lifecycle events lack a ringing event | Alternative after privacy review |
| Telnyx Voice API plus hosted AI | Carrier and voice-agent capabilities in one ecosystem | Destination rates, minute rounding and account-specific capacity | Challenger for cost and operational simplicity |
| Custom media pipeline | Maximum control | Audio transport, interruptions, endpointing, failure recovery and observability become engineering responsibilities | Defer until requirements justify it |

### Recommended implementation shape

1. Preserve the existing industry-independent intake, evidence, profile, and spend-control core.
2. Add a provider-neutral call-assessment domain.
3. Build a Twilio metadata adapter first, with live execution disabled.
4. Add a Vapi adapter for separately approved speech-enabled testing.
5. Retain provider interfaces so Retell or Telnyx can be evaluated without rewriting the application.

The existing components remain separate prototypes, not an integrated production service. Their established boundaries and pinned provenance are documented in [system responsibilities](../../architecture/system-and-integrations.md) and [source projects](../../status/source-projects.md).

For Vapi, importing a Twilio number is a documented integration. Vapi emits ringing and in-progress status updates. Nevertheless, prove the relationship between those events and carrier timestamps before publishing a ring-time metric. Do not configure two systems to control the same call independently. [Vapi Twilio integration](https://docs.vapi.ai/phone-numbers/import-twilio), [Vapi server events](https://docs.vapi.ai/server-url/events).

Retell supports both SIP trunking and a register-call/SIP-URI integration. The latter leaves carrier control with the application, including transfer and hangup logic, and requires connecting the registered call within five minutes. It can support a carrier-controlled measurement design, but is more integration work than a managed outbound call. [Retell custom telephony](https://docs.retellai.com/deploy/custom-telephony).

A middle ground between a hosted agent and raw audio is Twilio ConversationRelay, which handles speech recognition and synthesis while the application supplies conversational logic. A raw bidirectional Media Streams implementation requires a long-lived WebSocket service; Twilio allows one bidirectional stream per call and does not support outbound DTMF through that stream. [ConversationRelay](https://www.twilio.com/docs/voice/conversationrelay), [Media Streams](https://www.twilio.com/docs/voice/media-streams).

## 4. Separate metadata measurement from speech processing

### Mode A: Metadata-only assessment

Store call-progress events, timing, network outcomes, configured timeout, and cost.

- Recording, transcription, audio streaming, and AMD are off.
- An approved fixed identification message can be used on an answered authorized test.
- Answering-party classification remains unknown.
- Avoid silent nuisance calls to unsuspecting recipients.

This is the smallest useful engineering baseline.

### Mode B: Approved speech-enabled assessment

Add real-time voice processing only after reviewing the cohort, purpose, provider chain, disclosure, retention, and applicable consent.

- Use an identified automated assistant.
- Keep interaction short and bounded.
- Do not retain audio, transcripts, detailed speech logs, or content-bearing webhook payloads in the application.
- Store only approved operational outcomes and structured observations.
- Disable voice cloning, unsolicited messages, payment tools, arbitrary transfers, and unrelated external actions.

“No retained recording” and “no speech processing” are different properties.

### Vendor privacy details

Vapi documents organization-wide ZDR that removes retained call content after a call ends while preserving operational metadata. Separately disable recording, detailed logging, transcript artifacts, and PCAP in the current artifactPlan; documented defaults enable several of these. Leave structured-output storage overrides off and do not configure a storage bucket for content. Review the selected model, transcription, and voice providers separately. [Vapi ZDR](https://docs.vapi.ai/security-and-privacy/zero-data-retention), [Vapi artifact controls](https://docs.vapi.ai/assistants/call-recording).

Retell's “Basic Attributes Only” is not strict zero transient artifact storage. Its documentation says content can still arrive in webhooks, with raw recordings, transcripts, and logs deleted approximately ten minutes after post-call processing. Do not describe this option as “audio is never stored.” Its default retention setting is also indefinite unless changed. [Retell storage settings](https://docs.retellai.com/accounts/privacy-disable), [Retell retention](https://docs.retellai.com/accounts/data-retention).

For either platform, verify webhook authenticity in memory, then persist an allowlisted metadata projection. Disable request-body logging in the application, proxy, error tracker, queue, and observability tools.

## 5. What the system can measure honestly

Twilio distinguishes initiation, ringing, answer, and terminal outcomes. A completed call may have reached a person, IVR, or voicemail. Its no-answer state can also include rejection. Event timestamps and sequence numbers are available, but callbacks can arrive out of order. [Twilio Call resource](https://www.twilio.com/docs/voice/api/call-resource).

Use explicit metric definitions:

- **Queue delay:** submission to actual dialing.
- **Network setup time:** dialing to first reported ringing.
- **Network ring-to-answer:** first reported ringing to network answer.
- **Time to first human interaction:** a separate speech-derived observation, if approved and reliably identified.
- **Connected duration:** answer to disconnect.
- **Agent response latency:** end of recipient speech to start of assistant speech.

Do not report API submission-to-answer as “ring time.” Do not derive an exact number of physical rings from elapsed seconds.

For unconnected calls, record the timeout and outcome. These are censored observations, not zero-second answers. Missing timestamps remain missing.

### Classification design

Maintain separate fields:

- network_outcome
- initial_endpoint_class
- eventual_endpoint_class
- conversation_outcome
- classification_source
- classification_version
- confidence_band
- uncertainty_reason

Suggested endpoint classes: human, voicemail, ivr, screening, fax_or_other, unknown.

Preserve the provider's original label alongside the normalized label. A model's self-reported confidence is not a calibrated probability.

AMD is inherently uncertain. Twilio's detector uses speech and silence patterns and explicitly documents false classifications. Its synchronous mode can delay interaction; its FAQ reports roughly four seconds on average with default settings. Prefer a conversational design that does not leave a person waiting in unexplained silence. [Twilio AMD](https://www.twilio.com/docs/voice/answering-machine-detection), [AMD timing and trade-offs](https://www.twilio.com/docs/voice/answering-machine-detection-faq-best-practices).

Retell handles voicemail and IVR separately and currently limits detection to the first three minutes after connection. Vapi offers configurable voicemail detection. Neither feature should be treated as proof that a human did or did not answer. Telnyx's richer AMD labels and screening events likewise remain observations, not business facts. [Retell detection](https://docs.retellai.com/build/handle-voicemail), [Vapi detection](https://docs.vapi.ai/calls/voicemail-detection), [Telnyx AMD](https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection).

## 6. Control-plane architecture

Use the application's existing backend stack where possible:

- Relational database for consent evidence, attempts, suppression, and budgets.
- Durable queue with leases and bounded retries.
- Transactional outbox for dispatch.
- Provider adapter for create, cancel, retrieve, and normalize.
- Authenticated webhook ingress.
- Append-only metadata event store.
- Reconciliation worker.
- Read-only review dashboard and report generator.

Hosted speech keeps media outside this control plane. A future custom audio service should be deployed separately from short-lived webhook handlers.

### Attempt state machine

draft → eligibility_checked → approved → scheduled → leased → dispatching → provider_accepted → dialing → ringing → connected → ended → reconciled

Alternative outcomes include blocked, suppressed, expired, canceled, busy, no_answer, provider_failed, and dispatch_outcome_unknown.

Classification and analysis are separate projections that can arrive after termination. A late analysis event must not reopen an ended call.

### Dispatch safeguards

Before each provider request, atomically verify:

1. Authorized recipient and permitted purpose.
2. Valid consent or other reviewed eligibility evidence.
3. Current suppression status.
4. Approved local calling window.
5. Remaining attempt allowance.
6. Available concurrency.
7. Reserved worst-case spending allowance.
8. Approved caller ID and agent version.
9. Required privacy settings.
10. Global and cohort kill switches.

Schedule approval is not permanent eligibility. Recheck at dispatch. Evidence fingerprints must bind the reviewed recipient, purpose, policy, script, provider configuration, and approval version; imported or agent-generated flags must not approve themselves.

## 7. Webhooks, retries, and duplicate prevention

Treat delivery as at least once and potentially out of order.

- Authenticate the original request using the provider's documented mechanism.
- Persist the sanitized event durably before acknowledging.
- Keep webhook handling fast; perform analysis asynchronously.
- Deduplicate events using stable provider identifiers or documented compound keys.
- Build projections from event occurrence time and sequence where available, not arrival order.
- Reconcile stuck or incomplete attempts against provider records.
- Keep call initiation idempotency separate from webhook deduplication.

Retell retries webhooks up to three times when it does not receive a success response within ten seconds. Its lifecycle events can be deduplicated by event type plus call ID; unsuccessful connections may have no call_started event. [Retell webhooks](https://docs.retellai.com/features/webhook-overview).

Telnyx explicitly warns about duplicate and out-of-order delivery. Its command deduplication window is limited, so application-level protection must last longer than a provider retry window. [Telnyx webhook handling](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks).

Use provider-specific authentication, not one assumed scheme. Retell requires the raw body for signature verification. Vapi's current server authentication uses configured credentials and documents cases where credentials are not attached to dynamically supplied server URLs. [Retell signatures](https://docs.retellai.com/features/secure-webhook), [Vapi server authentication](https://docs.vapi.ai/server-url/server-authentication), [Twilio webhook security](https://www.twilio.com/docs/usage/webhooks/webhooks-security).

### Critical uncertain-outcome rule

If call creation times out, the provider may already have created the call. Mark dispatch_outcome_unknown, reconcile, and do not blindly dial again.

A webhook retry is not permission for another telephone attempt. Busy, no-answer, suppression, rejection, and carrier blocking must not automatically trigger repeated dialing. Any additional recipient attempt requires the approved assessment protocol and another eligibility check.

Do not rotate providers or caller IDs to get around blocks.

## 8. Scheduling, capacity, and spending

Store an IANA timezone and its provenance for each destination. Use verified business-location information or explicit recipient confirmation, not area code alone. Account for daylight-saving changes, local holidays, and exceptions.

If timezone or eligibility is uncertain, fail closed. Cancel or reschedule work that would start after its authorized window. Avoid placing a large backlog inside a carrier queue where calls could begin later than expected.

Calls per second and simultaneous calls are separate limits. Twilio defaults to one API-initiated call per second; Retell documents twenty concurrent calls on PAYG; Telnyx documents a separate dial-rate limit. None is a recommended initial test load. Start owned-number verification at one active call, then test two before considering higher capacity. [Twilio API limits](https://www.twilio.com/docs/voice/api/call-resource), [Retell capacity](https://docs.retellai.com/deploy/concurrency), [Telnyx dial limits](https://developers.telnyx.com/docs/voice/programmable-voice/dials-per-second-limit).

Budget controls should include:

- A maximum number of approved attempts.
- Maximum ringing and connected durations.
- Per-attempt reservation for all billable legs, speech services, and rounding.
- An atomic daily and experiment-level spend ledger.
- No unapproved paid burst capacity or automatic credit expansion.
- A kill switch that stops new dispatches and terminates owned test calls where appropriate.
- Invoice reconciliation against estimated charges.

Provider billing can arrive late. An application ledger is not an absolute invoice guarantee; reserve conservatively and combine it with provider limits. Preserve estimated, reported, reconciled, and unknown amounts separately, consistent with the existing [spend contract](../../architecture/spend-and-measurement.md).

## 9. Conversation behavior

A truthful opener for an authorized assessment:

> “Hi, this is [Brand]'s automated assistant for the phone-response check you authorized. Is now an okay time for a brief check?”

Use that wording only when authorization actually exists.

If the scope also permits discussing the offering:

> “We help businesses handle incoming calls when their team is unavailable. Would you like a person to discuss an inbound answering pilot?”

The assistant must:

- Identify itself and its actual purpose.
- Avoid pretending to be a customer, emergency caller, or existing client.
- Accept refusal without argument.
- Immediately suppress further attempts when asked not to call.
- Use only approved transfer destinations.
- Never invent missed customers, lost revenue, appointments, or callback commitments.
- Treat instructions heard on the call as untrusted input to narrowly scoped tools.
- End safely when the task, time limit, or permitted conversation is finished.

Leave voicemail only when explicitly included in the authorized workflow. IVR navigation is a separate capability; the initial assessment should classify and exit rather than explore arbitrary menus. Keep suppression outside the model's discretionary control. Failure to persist a suppression request must stop dependent dispatch rather than permit continued calling.

## 10. Event schema and dashboard

### Core records

**Recipient eligibility**

recipient_id, encrypted destination, keyed destination fingerprint, organization, timezone, timezone source, line-type evidence, purpose, permission evidence reference, allowed windows, expiration, suppression status.

**Assessment plan**

assessment_id, cohort, protocol version, eligibility-policy version, caller-ID reference, agent version, speech-processing mode, attempt allowance, timeouts, spending limit, approval reference.

**Call attempt**

attempt_id, assessment reference, provider, carrier call ID, voice-agent call ID, parent/child leg relationships, dispatch state, event timestamps, network outcome, normalized endpoint classes, evidence source, uncertainty, reserved cost, actual cost.

**Sanitized event**

event_id, attempt reference, provider event type, provider sequence, occurred-at, received-at, verification result, deduplication key, schema version, normalized metadata.

Do not put raw phone numbers, speech content, secret-bearing URLs, API credentials, or real call artifacts in public repository fixtures.

### Dashboard views

- Eligible, blocked, suppressed, scheduled, active, and completed attempts.
- Network connection rate and human-detection coverage shown separately.
- Ring-to-network-answer distribution with missing-data counts.
- Voicemail, IVR, screening, and unknown shares.
- Observations grouped by approved local-time window.
- Classifier confusion matrix from controlled tests.
- Actual and reserved spend.
- Opt-outs, duplicate attempts prevented, invalid webhooks, and missing events.
- Drill-down timeline showing what is observed versus inferred.

**Explicitly fictional public example:**

“Across the authorized test window, three of five attempts connected to an automated endpoint and two were not connected before the configured timeout. This small sample does not establish missed customer demand.”

This example is not an executed test or a real business result.

## 11. Latency engineering

Proposed acceptance targets, not vendor guarantees:

- Median conversational response latency below one second.
- P95 below 1.8 seconds in the controlled test environment.
- No unexplained initial silence longer than two seconds after a completed greeting.
- Prompt interruption response without continuing stale speech.
- Bounded tool timeouts with a short truthful fallback.

Measure first-response latency separately from later turns. Measure what the recipient hears, not only internal API timing.

Hosted latency metrics have limits. Retell's documented e2e metric excludes turns where the agent only runs a tool and does not include the final network trip to the user's frontend. Its sample values are examples, not performance promises. [Retell latency definitions](https://docs.retellai.com/reliability/check-actual-latency).

Keep prompts short, preload static context, avoid network retrieval for the opening line, and minimize mid-call tools. Do not add an LLM to carrier outcomes that can be handled deterministically.

## 12. Cost model

### Workload assumptions

All estimates are USD and exclude taxes, rental, application hosting, engineering, number verification, optional analytics, transfers, and promotions.

- 100 attempts: 60 connected, 40 genuinely unconnected.
- Connected calls last exactly 30 seconds or exactly 60 seconds.
- Voicemail and IVR count as connected.
- 1,000 attempts use the same proportions.
- No automatic redials.
- These compare workloads, not identical model quality.

| Configuration | 100 attempts, 30s connected | 1,000 attempts, 30s connected | 100 attempts, 60s connected | 1,000 attempts, 60s connected |
|---|---:|---:|---:|---:|
| Twilio carrier only | $0.84 | $8.40 | $0.84 | $8.40 |
| Twilio plus AMD, no conversational agent | $1.29 | $12.90 | $1.29 | $12.90 |
| Retell economical managed configuration | $2.93 | $29.34 | $5.87 | $58.68 |
| Vapi plus imported Twilio number | $3.29–$4.71 | $32.94–$47.07 | $5.75–$8.57 | $57.48–$85.74 |
| Telnyx hosted AI, illustrative tokens | $3.61 | $36.12 | $3.80 | $38.04 |

### Basis and caveats

**Twilio:** Standard US local outbound is $0.014/minute, rounded per call; AMD adds $0.0075 per answered call when enabled. A local number is $1.15/month. Carrier-only measurement does not identify humans or machines. [Twilio pricing](https://www.twilio.com/en-us/voice/pricing/us), [billing rounding](https://help.twilio.com/articles/223132307-How-do-you-rou), [AMD billing trigger](https://www.twilio.com/en-us/blog/answering-machine-detection-generally-available).

**Retell:** Example uses $0.055 infrastructure, $0.015 platform voice, $0.0128 GPT-4.1-mini, and $0.015 managed telephony per minute: $0.0978 total, billed per second. Number rental is $2/month. Optional batch dialing adds $0.005 per dial. Prompt length and dynamic openings can introduce billing exceptions. [Retell pricing](https://www.retellai.com/pricing), [billing exceptions](https://docs.retellai.com/accounts/billing-exceptions).

**Vapi:** Current calculator component estimates yield $0.0818–$0.1289 per actual minute before telephony. Add Twilio's separately rounded carrier charge. This is a planning range, not a quote: model tokens, synthesis, transcription, detection, analysis, and minimums depend on configuration. Hosting proration should be reconfirmed against current billing terms before purchase. [Vapi pricing](https://vapi.ai/pricing), [component billing](https://docs.vapi.ai/assistants/model-intelligence/understanding-cost).

The Vapi range comprises hosting at $0.05, transcription at $0.0095–$0.0099, estimated model usage at $0.0077–$0.0452, and estimated synthesis at $0.0146–$0.0238 per minute. Those modeled components are not fixed tariff rates for every call. The table assumes no charge for the 40% of calls that never connect; confirm failed-attempt and detection billing for the selected path before using it as a budget.

**Telnyx:** Example uses $0.05 per rounded voice-engine minute, $0.002 Voice API, outbound SIP starting at $0.005/minute, and an illustrative $0.0064 LLM cost per actual minute. Carrier destinations and token usage can change the total. [Voice AI pricing](https://telnyx.com/pricing/voice-ai-agents), [Voice API pricing](https://telnyx.com/pricing/voice-api), [billing increments](https://support.telnyx.com/en/articles/1130659-billing-increments).

The table assumes a simple supported carrier path. A carrier-controlled SIP bridge can add another billable leg. Recalculate after choosing the exact integration.

Short calls are not automatically cheaper: minute rounding dominates, and Telnyx documents possible surcharges when calls of six seconds or less exceed its short-call threshold. Tests exactly at sixty seconds also risk crossing into another billing increment. [Telnyx short-call policy](https://support-v2.telnyx.com/en/articles/1130707-what-are-short-duration-calls).

### Reproducible arithmetic

Let N be attempted calls, A = 0.60 × N connected calls, and M = A × connected_seconds / 60 actual connected minutes. In these specific 30s and 60s scenarios, each connected Twilio/Telnyx call consumes one rounded carrier minute.

- Twilio carrier: A × 0.014.
- Twilio with AMD: A × (0.014 + 0.0075).
- Retell: M × (0.055 + 0.015 + 0.0128 + 0.015).
- Vapi low estimate: M × 0.0818 + A × 0.014.
- Vapi high estimate: M × 0.1289 + A × 0.014.
- Telnyx: A × (0.05 + 0.002 + 0.005) + M × 0.0064.

Calculate the 1,000-attempt rows from unrounded amounts, not from ten times the displayed two-decimal 100-attempt rows. All values are estimates, not invoices or authorized spend.

## 13. Acceptance criteria

### Offline and simulated tests

Before any paid calls:

- All ineligible, suppressed, expired, and out-of-window records are blocked.
- Duplicate jobs cannot produce duplicate provider submissions.
- A timed-out create request enters reconciliation rather than immediate retry.
- Duplicate and shuffled webhooks produce the same final projection.
- A terminal event arriving before a start event does not corrupt state.
- Suppression invalidates already queued attempts.
- Budget reservations prevent concurrent workers from overcommitting.
- Forged webhook requests are rejected.
- Audio, transcripts, credentials, and raw request bodies do not enter durable logs.
- Daylight-saving transitions and ambiguous timezones fail safely.
- Provider outages, missing callbacks, and canceled queued calls reconcile.

### Owned or explicitly authorized live tests

Use a controlled matrix covering:

- Short and long human greetings.
- Speech over background noise and interruptions.
- Short and long voicemail greetings, with and without a beep.
- IVRs, hold music, forwarding, and call screening.
- Busy, rejected, disconnected, and unanswered destinations.
- Opt-out, wrong destination, agent failure, and carrier failure.

A reasonable first engineering milestone is 100 controlled attempts plus simulated fault tests, not 100 unsolicited businesses.

Required outcomes:

- Zero unauthorized or duplicate calls.
- Every attempt reaches a reconciled terminal state or a visible unresolved exception.
- Every opt-out blocks subsequent queued dispatches.
- Timing metrics agree with independently observed test behavior within documented precision.
- Human/voicemail/IVR precision, recall, and unknown coverage are reported separately.
- A provisional 95% precision target applies only to classified controlled examples; report sample size and uncertainty rather than claiming production accuracy.
- Latency targets are measured on actual test endpoints.
- Charges reconcile to the chosen billing model.
- Provider and application retention settings are verified after the call.

A small successful test does not validate broad production accuracy or market demand.

## 14. Engineering effort and next implementation scope

Planning estimates for an experienced engineer, assuming an existing backend and dashboard:

- **Offline schema, state machine, policy gates, mocks:** 2–4 days.
- **Carrier metadata integration and owned-number verification:** another 3–5 days.
- **Hosted conversation integration and failure-path testing:** another 3–7 days.
- **Small pilot hardening, monitoring, retention verification, and operations:** total approximately 2–4 weeks.
- **Custom audio stack:** several additional weeks, with substantially more ongoing operational work.

Provider onboarding, approved credentials, eligibility review, and test access can dominate elapsed time. These estimates are not delivery commitments.

The first Codex implementation should deliver schemas, mock provider adapters, dry-run planning, synthetic fixtures, policy tests, cost estimation, and a review dashboard. Keep live providers disabled until the acceptance gates and launch requirements are satisfied. This research does not create a new Codex project or authorize product implementation.

## 15. Unresolved requirements before live implementation

1. Which countries and destination line types are in scope?
2. What evidence makes each recipient eligible for the assessment and any sales discussion?
3. Is the goal initial endpoint availability, eventual human access, or an inbound answering pilot?
4. What local windows and attempt limits have recipients approved?
5. Does “no audio retention” prohibit even temporary vendor artifacts?
6. Which speech subprocessors and regions are acceptable?
7. Which caller ID and callback handling will be used?
8. What exact spend cap, connected-duration cap, and initial concurrency are approved?
9. Which carrier integration will provide validated timing and billable-leg visibility?
10. What evidence would justify an inbound pilot beyond the assessment itself?

The commercially useful result is a transparent assessment followed, where appropriate, by an authorized inbound pilot measuring real handling outcomes. The assessment should support that conversation, not manufacture the problem it proposes to solve.

## 16. Evidence and implementation boundary

Vendor facts above are dated public documentation observations. The architecture, latency targets, test protocol, effort ranges, and commercial recommendation are original proposals. Pricing arithmetic uses explicit assumptions; it is not paid-usage evidence.

No target business has been assessed by this package. No classifier, local-time scheduler, consent gate, spend cap, provider adapter, or dashboard described here has been built or tested as part of this work. Current account entitlements, vendor terms, and pricing must be rechecked before use. Comparative vendor testing may also be restricted by provider terms; review the proposed test purpose before execution.

For the documentation checks actually completed and the repo-local validator not executed in this connector-only workflow, see [verification record](validation.md).
