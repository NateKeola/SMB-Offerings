# Source, scope and verification

Canonical source: [todd-gavin/software-factory](https://github.com/todd-gavin/software-factory), public at review, pinned to [c760cf765e2aa7dd887bf4dbe202490d0f0496ad](https://github.com/todd-gavin/software-factory/tree/c760cf765e2aa7dd887bf4dbe202490d0f0496ad). Reviewed 2026-11-03. The source README attributes the extraction to the miine-platform monorepo on 2026-08-19.

An existing local copy of the user's previously adopted kit was identified. Its **47 file hashes matched the pinned public upstream tree**. The package here copies only the 31 portable files listed in [UPSTREAM.json](UPSTREAM.json), without changing their bytes. Source discovery needed no clone, package installation, dataset export or new download. Private project records and local source paths are not part of this provenance record.

## Included and excluded

Included: upstream README, INSTALL, MANIFEST and PLACEHOLDERS; all six doctrine documents; the complete template tree with seven skills, three commands, context/decision/handoff templates, CI/scanner examples and optional seed-script example.

Excluded: the entire `reference/` worked-example tree, because it carries unrelated project state and environment identifiers; and `check-drift.sh`, which depends on that reference tree and the original project's live harness. The source overview/manifest still describe those upstream components; they are intentionally absent here. The public upstream links preserve their provenance without republishing them in SMB Offerings.

Original files are nested under `upstream/`. The wrapper README, this provenance note, the SMB adoption map and the integration decision are original SMB documentation. The root AGENTS.md is unchanged. No reference examples became current SMB truth, and no install instructions were executed.

## Reuse status

No standalone LICENSE, COPYING or NOTICE file was present in the pinned upstream tree. Its README explicitly invites copying the portable kit into another repository, and the installation/manifest guides explain that use. This package preserves source attribution and records that invitation as the reuse basis. It does **not** label the kit MIT/Apache-licensed or invent broader licensing terms. Any later redistribution under a named license needs an established basis from the rights holder.

## Validation scope

The repository documentation check verifies the included file list and each Git blob hash against the recorded upstream manifest, scans all public payloads for common private/credential patterns, and checks links in the SMB wrapper documentation. Byte-identical templates retain intentional placeholders, original formatting and links to their future installed paths; these are not falsely reported as active SMB paths.

The check rejects extra or changed files inside the vendored tree unless the source manifest is deliberately reviewed and updated. Source skill frontmatter and the presence of six doctrines/seven skill templates/three commands are inspected. No original install, seed, migration, scanner, skill or workflow is executed as validation. Guard coverage, database isolation, paid-provider behavior, deployments and automatic skill discovery are not claimed.
