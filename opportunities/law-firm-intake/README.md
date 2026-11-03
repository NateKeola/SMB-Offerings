# Law-firm inbound intake opportunity

Research date: **2026-11-03**. Status: **research and proposed validation; no product or pilot launched**. Scope: California-first legal review, US market evidence, inbound voice and email, and a firm-facing review queue.

**Recommendation: pursue a bounded managed-intake service experiment; defer building a general-purpose legal intake platform.** Unanswered inquiries are a documented problem. The full proposed feature set also has direct competitors. The defensible question is whether a particular kind of small firm will pay for better configuration, cross-channel handoff and accountable human follow-through.

## The idea, preserved

Help a firm acknowledge a new inquiry, gather the minimum information needed for a callback, identify the intended service and relevant parties, and route the request with useful context. Voice and email should share one intake record. A lawyer or trained staff member should see what is known, what is missing, what needs review, and who owns the next action. Later, after firm approval and conflict screening, the system could request specific supplementary information or documents through a controlled channel.

The motivation is friction experienced when trying to obtain timely legal help. That is a useful hypothesis source, not a verified market sample. This public record contains no personal matter, law-firm identities, private correspondence or contact records.

## What the evidence supports

- **A material responsiveness problem exists in studied samples.** Clio's 2024 secret shop of 500 US firms found 40% answered the initial call, 52% answered or called back, and 33% responded to email. Hennessey Digital's separate 2025 study found 26% of 1,333 firms failed to make personal contact within seven days after a website-form inquiry. Different channels, samples and methods prevent pooling these rates. Both publishers sell legal-industry services. [Evidence and limits](market-and-competition.md).
- **The combined voice/email idea already exists.** Clio's current Grow AI documentation describes inbound phone, email and web chat, information collection, a lead inbox, assessment and scheduling. This verifies advertised availability, not quality or fit for a particular firm. [Competitor comparison](market-and-competition.md).
- **No legal advice does not mean no confidentiality.** California's prospective-client rule can protect information even without an engagement. Gathering case narratives can also create conflicts. Whether a particular conversation is privileged is a different, fact-dependent question. [Legal analysis](legal-and-security.md).
- **A smaller product can reduce exposure, but security remains necessary.** Callback-only collection, no document uploads initially, limited processing and an existing firm system reduce complexity. They do not establish a confidentiality exemption. [MVP and architecture](architecture-and-mvp.md).
- **Commercial viability is unproven.** There are no buyer interviews, paid pilots, measured recoverable cases or actual operating costs in this research. [Economics](economics.md) separates public prices from hypothetical costs.

## Proposed first customer and offer

Test California firms with roughly **2–10 attorneys**, an existing intake/CRM system, a responsible office manager, spare consultation capacity and enough inquiries to observe repeat failures. Start with scheduled, comparatively low-urgency services such as routine estate-planning or small-business consultations; both still require confidentiality and conflict controls. Firm size and practice type are hypotheses, not a market selection already made by the user.

Proposed offer: **“Make every eligible inquiry visible, assign a callback owner, and close the loop.”** Begin by improving the firm's existing system, using provider-native voice intake where suitable and a dedicated intake mailbox. Sell implementation, QA and ongoing workflow care only where these create demonstrable value beyond self-service configuration.

Do not lead with autonomous legal qualification, promised conversions, “never miss a case,” or a low-security portal. An instant acknowledgement does not equal a substantive response or a completed callback. A firm that will not staff the handoff is not a good pilot customer.

## Everything needed for the next decision

| Document | Contents |
|---|---|
| [Market and competition](market-and-competition.md) | Two empirical datasets, sample limits, alternative explanations, competitor channels/prices and ICP hypotheses |
| [Legal and security](legal-and-security.md) | California rules and statutes, broader US distinctions, risk matrix and counsel questions |
| [MVP and architecture](architecture-and-mvp.md) | Callback-first tiers, minimum data, voice/email workflow, portal controls and human escalation |
| [Economics](economics.md) | Model assumptions, explicit support/security costs, margins and customer break-even |
| [Model inputs](economics-assumptions.json) / [scenarios](economics-scenarios.csv) | Reproducible hypothetical arithmetic; no actual financial results |
| [Validation plan](validation-plan.md) | Buyer questions, synthetic acceptance cases, proposed pilot scorecard and stop conditions |
| [Decision log and current state](decision-log.md) | User direction, recommendations, unresolved decisions and completed work |
| [Source register](sources.md) | Primary URLs, dates, evidence type and retrieval limits |
| [Validation evidence](validation.md) | Documentation checks, arithmetic verification and test limits |
| [Codex kickoff](CODEX-KICKOFF.md) | Research/prototype planning handoff with current restrictions |
| [Repository integration notes](integration-notes.md) | Suggested root-index/status additions for the concurrent repository update |

The next decision is whether to validate an implementation service with a narrowly selected customer segment. It is not approval to launch an agent, send messages, connect a mailbox, purchase services or handle real prospective-client data.
