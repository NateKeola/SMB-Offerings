# SMB Offerings

A working handoff for building and selling useful, bounded improvements to established small and midsize businesses. Consolidated **2026-11-03** from the project decisions and public research completed through November 2.

**Start with something proven, make it better, and use new capabilities when they help.** Find recurring customer or staff friction, verify it, build a small demonstration, and price the delivery and upkeep honestly. Novelty, an old website, or the absence of a chatbot is not proof of need.

This repository contains strategy, operating preferences, research indexes, offer hypotheses and reusable templates. The working prototypes remain in five separate, unmerged [Dogfood draft PRs](status/source-projects.md). This handoff does not merge, migrate or deploy those applications.

## Start here

1. Read [vision and preferences](strategy/vision-and-preferences.md) and [the decision register](strategy/decision-register.md).
2. Review [current status and limits](status/current-state.md), then [the source projects and exact commits](status/source-projects.md).
3. Use [opportunity qualification](strategy/opportunity-qualification.md) and [research protocol](research/research-protocol.md) to define a bounded batch.
4. Match verified friction to [the service menu](offerings/service-menu.md), [pricing assumptions](offerings/pricing-and-economics.md) and [prototype process](delivery/prototype-to-sow.md).
5. Use the [outreach playbook](outreach/playbook.md) for preparation. **Email sending is on hold.** No outreach execution is authorized by these documents.
6. When opening a Codex project, use [the kickoff prompt](codex/KICKOFF.md). The user will create that project.

## Coverage checklist

Every workstream has substantive content directly in this repository. The linked source PRs retain the original applications and exact history.

- [x] Strategy and preferences: [vision](strategy/vision-and-preferences.md), [decisions and open choices](strategy/decision-register.md), [ICP and evidence gates](strategy/opportunity-qualification.md).
- [x] Opportunity searching: [research protocol](research/research-protocol.md), [official-registry pilot lessons](research/registry-pilot.md), [industry/market analysis](research/industry-market-analysis.md).
- [x] Law-firm inbound intake — **research only**: [opportunity and recommendation](opportunities/law-firm-intake/README.md), [demand and competitors](opportunities/law-firm-intake/market-and-competition.md), [legal/security assessment](opportunities/law-firm-intake/legal-and-security.md), [MVP design](opportunities/law-firm-intake/architecture-and-mvp.md), [economics](opportunities/law-firm-intake/economics.md) and [response-time validation plan](opportunities/law-firm-intake/validation-plan.md). No live pilot, outreach or integration has occurred.
- [x] Outbound AI phone assessment — **research only**: [overview](opportunities/outbound-phone-audit/README.md), [full technical design and provider comparison](opportunities/outbound-phone-audit/technical-design.md), [cost assumptions](opportunities/outbound-phone-audit/technical-design.md#12-cost-model), [acceptance criteria](opportunities/outbound-phone-audit/technical-design.md#13-acceptance-criteria) and [verification limits](opportunities/outbound-phone-audit/validation.md). No live calls, paid providers or product implementation.
- [x] Initial service and automation offers: [full scoped menu](offerings/service-menu.md), [six prototype directions](offerings/prototype-directions.md), [delivery and SOW process](delivery/prototype-to-sow.md).
- [x] Pricing and economics: [explanation and assumptions](offerings/pricing-and-economics.md), [17 market-price observations](research/market-price-observations.csv), [model inputs](offerings/economics-assumptions.json), [24 scenarios](offerings/economic-scenarios.csv), [add-on scenarios](offerings/addon-scenarios.csv), [price floors](offerings/price-floors.csv).
- [x] SEO and AI-search: [playbook and seven launch gates](seo/search-and-ai-visibility.md), [62-entry primary-source register](seo/source-register.md).
- [x] Public research: [source map](research/source-index.md), [26-source market register](research/market-source-register.md), [all 15 exact video/site references](research/video-reference-index.md), [metric provenance](research/reference-snapshots.json), [market-fit reading note](research/market-fit-note.md).
- [x] Outreach: [calling-first playbook, draft messages and proposed cadence](outreach/playbook.md), [private-use blank worksheets](templates/README.md).
- [x] Architecture and spending: [component/integration boundaries](architecture/system-and-integrations.md), [usage, budget and cost rules](architecture/spend-and-measurement.md).
- [x] Handoff and unfinished work: [current state/gaps](status/current-state.md), [roadmap](status/roadmap.md), [exact source commits and test limits](status/source-projects.md), [provenance manifest](status/provenance.json), [validation](status/validation.md), [agent guidance](AGENTS.md), [Codex kickoff](codex/KICKOFF.md).
- [x] Software Factory: [the existing portable kit](software-factory/README.md), [SMB adoption map](software-factory/SMB-ADOPTION.md) and [source/scope/reuse notes](software-factory/PROVENANCE.md). Included as a pinned reference package; no skills, CI, database or deployment workflows activated.

Research summaries and tables are visible here; customer/contact records and private learning-deck files are intentionally excluded. A checked box means the workstream is documented, not that its business hypotheses or software are production-ready.

## What is established

| Area | Available work | Limit |
|---|---|---|
| Idea discovery | 15 public references, exact links, six original directions | Sampled media review; zero built customer demos |
| Business research | Local browser workbench for intake, identity, evidence and offers | Two fictional fixtures; zero real leads in its public data |
| Outreach preparation | Python CLI, shared review gates, catalog and local-service profiles | Disabled external providers; no sending, dialing or live audit service |
| SEO and AI-search | Evidence-led toolkit, 62 primary-source entries, seven launch gates | No completed client audit or ranking/inclusion promise |
| Service economics | 26 sources, 17 price observations, 24 modeled scenarios | Prices, effort, support and conversion assumptions are unvalidated |
| Spend visibility | Local dashboard and usage-event adapter | No live billing; some browser import/persistence/export paths remain unverified |
| Public-registry pilot | Five records reviewed; anonymized [lessons](research/registry-pilot.md) | Zero qualified prototype opportunities; no general market conclusion |

## Repository map

| Directory | Purpose |
|---|---|
| [strategy](strategy/vision-and-preferences.md) | User direction, decisions, ICPs, evidence gates and priorities |
| [research](research/source-index.md) | Source register, video provenance, research methods, registry lessons and article interpretation |
| [opportunities](opportunities/law-firm-intake/README.md) | Bounded research into law-firm intake and [outbound phone assessment](opportunities/outbound-phone-audit/README.md), including risks, architecture, economics and proposed validation |
| [offerings](offerings/service-menu.md) | Scoped menu, prototype directions and economic assumptions |
| [outreach](outreach/playbook.md) | Calling-first preparation, draft messaging, measurement and stop conditions |
| [delivery](delivery/prototype-to-sow.md) | Discovery, demonstration, statement of work and acceptance |
| [seo](seo/search-and-ai-visibility.md) | Search, AI-search, controls, measurement and source toolkit |
| [architecture](architecture/system-and-integrations.md) | Responsibilities, integration boundaries, provider and spend contracts |
| [templates](templates/README.md) | Blank ICP, opportunity, offer and pilot worksheets |
| [status](status/current-state.md) | Implementation inventory, verification limits and roadmap |
| [codex](codex/KICKOFF.md) | Context and safe starting instructions for the next project |

## Read the labels

**User direction** records an expressed preference. **Observed/reported** states what the dated source supports. **Hypothesis** is an offer, price, ICP or design to validate. **Unknown/not assessed** is missing evidence, not a negative result. **Proposed** is a new operating template in this consolidation, not a workflow already executed.

This public repository excludes real leads, contacts, private reports, credentials, client records and unrelated personal work. Public source links and original summaries are preserved; creator assets and proprietary articles are not rehosted. See [AGENTS.md](AGENTS.md) for working rules and [validation](status/validation.md) for the checks applied to this handoff.
