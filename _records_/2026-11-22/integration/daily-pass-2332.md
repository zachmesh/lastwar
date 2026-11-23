---
title: Integrator daily pass - 2026-11-22 23:32 PT
created: 2026-11-23T07:32:21Z
modified: 2026-11-23T07:32:21Z
level: L3
version: 0.1.0
description: Daily pass of the Integrator seat with a correction to the readiness note; counts and SHAs only
status: done
activity: integration
run_id: integration-2026-11-22-daily-pass-2332
verified: git and gh read-only commands run in this session after git fetch --deepen=300 origin main
---

# Integrator daily pass

GitHub actions: one deepening fetch of main, two PR lists, one PR view, one readback of merged PR 858. No push, no PR opened, no merge, no comment.

## Correction to the readiness note

The readiness note says commit 254ab85143 is not on origin/main and that local main is ahead 4912 and behind 1. Both came from a shallow clone and are wrong. After the deepening fetch origin/main reaches 4855 commits: commit 254ab85143 is an ancestor of origin/main, and local main is ahead 72 and behind 3 (ahead 78 at 23:31). Landing baseline: inherited history has 1 commit with a metadata match and never rewritten; a landing branch must add 0 in origin/main..branch.

## Findings

- Open PRs: 838 (records/2026-11-22, head b44dfb28fe) and 425 (work/log-append-delivery-gate, head 4f41cdd6ab), both CONFLICTING, no checks configured. Files with a content match at the heads: 168 and 154; new-commit metadata matches 0 and 0.
- Direct pushes to main: none since 2026-11-01T05:52Z. First-parent chain of origin/main is 674 commits: 176 PR merge commits, 451 GitHub squash merges and 47 single-parent commits with a local committer, all 47 dated before that instant.
- Tip 43c088d8f8 is the merge of PR 858; readback OK (two parents, tree equal to the branch head, head an ancestor).
- Local main holds 72 commits not on origin/main (28 refactor, 23 chore, 14 docs, 6 feat, 1 fix) across _activities_, _records_, _queue_, _conventions_, _seats_, _tools_, _knowledge_ and TEAM.yaml; none pushed. The integrator seat pages and TEAM.yaml 0.6.0 are among them; origin/main still has TEAM.yaml 0.5.0.
- Unmerged remote branches: 26, of which 10 have a last commit older than 7 days (oldest 2026-11-01).
