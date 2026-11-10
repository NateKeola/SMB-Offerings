# Handoff validation

This page concerns the documentation handoff, not a rerun of the source applications' tests. Their historical evidence and limits are in [source-projects.md](source-projects.md).

## Checks for this repository

Run from the repository root:

```sh
python3 -B scripts/validate_docs.py
```

The standard-library check validates local Markdown targets, text formatting, JSON/CSV shapes, the 15-reference/6-direction inventory, 26 market sources, 62 SEO source IDs, 17 price observations, 24 scenarios and pinned source provenance. It scans public payloads for common credential/private-link/email/local-path/internal-ID patterns. It makes no network calls, downloads or writes.

Consolidation result on 2026-11-03: **passed for 40 text files and 307 Markdown links**, with 153 unique external URLs recorded. All **35 unique pinned source file/directory targets** were present in the inspected remote trees. The five reviewed source tree hashes matched the clean existing local source content. External URL recording is not an availability or truth check of those pages.

Editorial review covers the visible coverage checklist; current email/download restrictions; user decisions versus proposed offers; no unsupported customer results; component boundaries; source dates; and the exclusion of private leads, contacts, reports and unrelated personal work. A pattern scan cannot prove that every sentence is accurate or safe; review the content itself.

Remote source PR heads and full trees were inspected through read-only GitHub APIs. Pinned source file/directory links are checked against those trees. Existing local public files supply the source registers and data tables. No source repository clone/fetch, dataset/media/export download or package installation was needed.

The handoff does not claim a fresh check of every external article, video, platform document or price. These are dated research snapshots with original limitations. No production system, real provider, outreach channel, customer integration, billing account or deployment was tested or activated here. No CI workflow was added for this documentation-only repository.

## 2026-11-08 — SEO learning note

Added an original, attributed [carousel note](../seo/learning-notes.md) and navigation/status entries on an isolated branch from main. All ten slides and the caption were inspected; selected public platform/vendor sources were checked and their scope qualified. The historical 62-source register and 15-reference metric snapshot remain intact. Other open PRs and source applications were not modified.

The full `python3 -B scripts/validate_docs.py` check passed, as did `git diff --check`. Manual review confirmed only original prose and public source links, without private business details, creator media, proprietary assets or invented ranking requirements. These checks validate documentation structure and review scope, not a client audit or search-performance result. No package installation, merge, deployment or outreach occurred. Remote publication and exact commit verification are recorded in the draft PR.
