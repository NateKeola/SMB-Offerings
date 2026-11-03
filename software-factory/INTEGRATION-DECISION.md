# Integration decision — 2026-11-03

**Request:** Add the user's existing Software Factory to SMB Offerings.

**Decision:** Vendor the exact portable doctrine/template package from public upstream `todd-gavin/software-factory` at commit `c760cf765e2aa7dd887bf4dbe202490d0f0496ad`, with an SMB adoption map, visible README entry and per-file provenance. Use a feature branch and draft PR; leave merging to review.

**Alternatives considered:** Installing the full Supabase/preview-host harness would invent resources and alter the repository's operating behavior without an implementation request. Copying the filled-in worked example would bring unrelated project context into a public repo. Writing a new generic “factory” would substitute an unrelated framework for the one requested. Each was rejected.

**Reasoning:** The original reusable kit is identified and available locally with exact upstream hash matches. It can be made visible without executing it, creating a duplicate current-state system, changing existing agent guidance or enabling workflow downloads.

**Scope:** New files under `software-factory/`; an additive root README entry; and a narrowly scoped validator extension for the pinned source tree. No edits to the separate opportunity-research workstream or the root AGENTS.md.

**Verification:** Static content/hash/link checks and public-content review only. No application, database, deployment or source-workflow execution. See [provenance](PROVENANCE.md) for exclusions and the upstream license-file finding.
