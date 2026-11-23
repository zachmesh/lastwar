---
title: Integrator landings - 2026-11-22
created: 2026-11-23T07:45:08Z
modified: 2026-11-23T07:45:08Z
level: L3
version: 0.1.0
description: One line per landing of the Integrator seat, counts and SHAs only
status: done
activity: integration
run_id: integration-2026-11-22-landings
verified: gh pr view and git read-back after each merge
---

# Landings

- 2026-11-23T07:45:08Z code lane, PR 873, branch land/code-tools-0723 head 16f5d2c766: pushed, merged by merge commit 839bad3fda (parents 43c088d8f8 and 16f5d2c766, tree equal to branch, head an ancestor). 14 paths under _tools_/; tests 124 + 24 + 10 OK; privacy delta 0 added matches; whole-tree baseline 169 and 171 unchanged. Branch kept.
- 2026-11-23T07:52:20Z records lane, PR 874, branch land/records-0723 head 969a2b9262 (stacked on PR 873): pushed, merged by merge commit c3c8b85040 (parents 839bad3fda and the branch head, tree equal to branch, head an ancestor). 1678 paths, every path in a seat scope or the verified redaction; whole-tree privacy on the head and on merged main 0 on all counts (before 169 and 171). Branch kept.
- 2026-11-23T07:56:34Z code lane, PR 875, branch land/log-gate-tool head 516be193d5 (mechanical cherry-pick of the author's single commit 433f716326 onto main; the author's branch was built on the local line with 72 unredacted local-only commits and was not pushed as built): pushed, merged by merge commit cff741e5b6 (parents c3c8b85040 and the branch head, tree equal, head an ancestor). 5 paths under _tools_/; log-append tests 7 OK; privacy 0 on every count. Branch kept.
- 2026-11-23T07:56:34Z PR 425 commented with a pointer to PR 875 and closed (the one permitted close); branch work/log-append-delivery-gate kept; 53 remote branches before and after.
