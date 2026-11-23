---
title: Integrator readiness check - 2026-11-22
created: 2026-11-23T07:17:55Z
modified: 2026-11-23T07:17:55Z
level: L3
version: 0.1.0
description: Read-only readiness pass of the Integrator seat before its first landing; no push, no PR opened, no merge
status: done
activity: integration
run_id: integration-2026-11-22-readiness
verified: gh and git read-only commands run in this session; counts only
---

# Integrator readiness check

GitHub actions this pass (all read-only, repository zachmesh/lastwar): one version check, one auth status, one PR list, two PR views, two PR checks calls. No push, no PR opened, no merge, no comment.

- gh 2.103.0; logged in as account dtadpole, active; git operations over https.
- Open PRs: #838 (records/2026-11-22, head b44dfb28fe, 52 files, CONFLICTING, no checks reported) and #425 (work/log-append-delivery-gate, head 4f41cdd6ab, 3 files, CONFLICTING since before this pass, no checks reported). Both authored by zachmesh.
- Local clone is shallow. origin/main is a single root commit 43c088d8 (the grafted PR 858 merge); main and origin/main share no merge-base here, so ahead 4912 / behind 1 is a shallow artifact, not a measured divergence.
- Privacy baseline, git grep -P -i -f over the shared denylist (1 entry): files with a content match - origin/main 169, local main 165, push/clean 169, push/clean-2 169, work/privacy-redact 173 (positive control: about 168 expected, so the scan is live). File-name matches 0 on all five. Commit-metadata lines matching: 1 over 4912 commits of local main, commit 254ab85143 (ancestor of push/clean, push/clean-2 and work/privacy-redact; not on origin/main).
- Tooling trap: macOS BSD grep has no -P and exits with an error that reads as an empty result; the name and metadata scans must use git grep -P or python re, never shell grep -P.
- No wrapper under _tools_/integrator yet; the plain gh route is used.

Corrected by [daily-pass-2332.md](daily-pass-2332.md): the shallow-clone figures and the origin/main ancestry statement above are superseded.
