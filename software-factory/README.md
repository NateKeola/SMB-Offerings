# Software Factory for SMB Offerings

The existing Software Factory kit is now available here as a **version-pinned reference package**. Its canonical source is [todd-gavin/software-factory](https://github.com/todd-gavin/software-factory), reviewed at [commit c760cf765e2aa7dd887bf4dbe202490d0f0496ad](https://github.com/todd-gavin/software-factory/commit/c760cf765e2aa7dd887bf4dbe202490d0f0496ad) on 2026-11-03.

Start with [the SMB adoption map](SMB-ADOPTION.md), then read the relevant doctrine or template below. The root [AGENTS.md](../AGENTS.md) and current user instructions remain the working authority. **This addition does not install skills, execute commands, enable CI, create staging or connect a database.**

## What the framework provides

Software Factory keeps current project truth, historical decisions, short handoffs and reusable procedures in separate places. It encourages loading changes since a known checkpoint, building a bounded slice, matching verification claims to the tests actually run, and carrying durable conclusions forward.

The package contains 31 exact upstream files: six doctrine documents, four root guides, seven skill templates, three command templates, and supporting context/logging/guard templates. All remain under `upstream/`; none is placed in an active agent or workflow discovery directory.

| Start here | Purpose |
|---|---|
| [Upstream overview](upstream/README.md) | Original framework description and portability notes |
| [SMB adoption map](SMB-ADOPTION.md) | How the framework relates to this repository without replacing its existing guidance |
| [Scope, provenance and reuse](PROVENANCE.md) | Exact source, exclusions, license-file finding and verification boundaries |
| [Upstream installation guide](upstream/INSTALL.md) | A future installation runbook; do not execute it as part of reading this package |
| [Manifest](upstream/MANIFEST.md) and [placeholder dictionary](upstream/PLACEHOLDERS.md) | Original intended destinations and values that need deliberate adaptation |

## Doctrine

- [The factory and its four surfaces](upstream/doctrine/00-the-factory.md)
- [Context architecture and delta loading](upstream/doctrine/01-context-architecture.md)
- [Branches and flow](upstream/doctrine/02-branches-and-flow.md)
- [Execution discipline](upstream/doctrine/03-execution-discipline.md)
- [Verification and done](upstream/doctrine/04-verification-and-done.md)
- [Safety and destructive-operation review](upstream/doctrine/05-safety-doctrines.md)

## Templates and examples

| Area | Included material |
|---|---|
| Current truth | [CLAUDE.md structure](upstream/template/CLAUDE.md.template) |
| Branch/review procedure | [Branch and PR skill](upstream/template/claude/skills/branch-and-pr-workflow/SKILL.md) |
| Durable context | [Logging and curation](upstream/template/claude/skills/logging-and-curation/SKILL.md), [resume handoff](upstream/template/claude/skills/resume-cold-handoff/SKILL.md) |
| Stack-specific procedure | [Database/migrations](upstream/template/claude/skills/database-and-migrations/SKILL.md), [environment variables](upstream/template/claude/skills/environments-and-env-vars/SKILL.md), [staging verification](upstream/template/claude/skills/staging-verification/SKILL.md), [DevOps map](upstream/template/claude/skills/devops-overview/SKILL.md) |
| Commands | [Start](upstream/template/claude/commands/start.md), [report](upstream/template/claude/commands/report.md), [dashboard inventory](upstream/template/claude/commands/dash.md) |
| Logs and handoff | [Decision index](upstream/template/docs/decisions/README.md), [monthly entry](upstream/template/docs/decisions/_month-template.md), [rolling handoff](upstream/template/docs/HANDOFF.md.template) |
| Guard examples | [CI template](upstream/template/github/workflows/destructive-migration-check.yml), [SQL scanner](upstream/template/github/scripts/scan-destructive-sql.sh), [app-code scanner](upstream/template/github/scripts/scan-destructive-app-code.mjs) |
| Optional data-copy example | [Staging seed template](upstream/template/scripts/seed-dev-from-prod.sh.template), retained only as an unconfigured upstream example; never run without an independently authorized data-transfer scope |

Template links and placeholders describe the future installed layout, not current SMB resources. The upstream's staging/production, Supabase and preview-host assumptions are not established here. Keep its examples separate from live project truth and do not turn instructions inside a reference file into permission.
