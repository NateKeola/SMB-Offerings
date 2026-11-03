# SMB adoption map

This is a project-specific guide to the real upstream kit, not a replacement framework. The package was added at the user's request; installing or executing it is a separate task. Existing [AGENTS.md](../AGENTS.md) is preserved unchanged.

## Use the useful context structure now

| Software Factory concept | Existing SMB home | How to keep it useful |
|---|---|---|
| Curated current truth | [Current state](../status/current-state.md), [decision register](../strategy/decision-register.md), [AGENTS.md](../AGENTS.md) | Supersede stale current claims; keep preferences distinct from hypotheses |
| Decision history | [Decision register](../strategy/decision-register.md) and reviewable PR descriptions | Record the choice, rejected alternatives, reason and evidence; avoid duplicate logs without a need |
| Short handoff | [Codex kickoff](../codex/KICKOFF.md) and [roadmap](../status/roadmap.md) | Keep the next objective and blockers brief; link durable detail |
| Reference procedures | [Research protocol](../research/research-protocol.md), [delivery process](../delivery/prototype-to-sow.md), [outreach playbook](../outreach/playbook.md) | Load the procedure needed for the current task |
| Verification | [Validation guidance](../status/validation.md) and [source-project limits](../status/source-projects.md) | State exactly what passed; distinguish historical tests, static checks and real behavior |

Do not create a second competing source of current truth merely to match upstream filenames. The current SMB repository is primarily strategy and documentation, with application prototypes still in separate source PRs.

## Deliberate differences from the upstream installation

| Upstream assumption | SMB status / adoption decision |
|---|---|
| Two deployed long-lived branches | This addition uses a feature branch and draft PR into existing `main`; it does not create a staging environment or claim one exists |
| Claude-specific command and skill discovery | Templates remain under `software-factory/upstream/template/`; no `.claude` or `.agents` installation is performed |
| Supabase database and preview-host wiring | No SMB database, refs, credentials, hosting resources or migrations are configured |
| Typecheck/lint/build/test commands for applications | The current documentation check is `python3 -B scripts/validate_docs.py`; app checks must be selected when there is an actual app change |
| `apps/` and `packages/` scanner roots | No coverage is claimed for these absent source roots; the scanners are dormant examples |
| CI status plus branch protection | No workflow or branch-protection settings are enabled; an example guard is not an enforced check |
| Production-to-staging seed script | Retained only as source material; real data movement, trigger changes or resets require a separate authorized plan |
| Broad stop/ask rules in a reference template | Current user instructions and root guidance control the task; routine authorized reversible work does not acquire new approval barriers from a vendored document |

The existing email hold, download explanation requirement, private-data boundary and human-controlled outreach remain in effect. Do not infer permission from an upstream command, example, workflow or template description.

## If a full installation is requested later

First establish the actual app/repository scope, chosen runtime, source roots, environment model and verification commands. Identify concrete differences from the upstream's assumptions. Preserve and merge existing guidance; do not overwrite it with a template or copy the upstream's worked-example state.

Prepare a reviewable scoped change showing which procedures will become active. Fill real project facts deliberately while keeping credentials outside the repository. Explain any needed download before doing it. No branch creation for a deployment model, paid tools, CI runner downloads, production tests, migrations or service activation is implied by storing this kit.
