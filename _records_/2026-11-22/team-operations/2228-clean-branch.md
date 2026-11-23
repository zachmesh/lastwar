---
title: Clean push branch and a wider denylist - 2026-11-22 22:28 PT
created: 2026-11-22T22:28:00-08:00
modified: 2026-11-22T22:31:00-08:00
level: L3
version: 0.1.0
description: The Steward's independent check and the operator's redactions showed the first scan missed alliance and ally names; a wider local denylist, a redaction, and a clean fast-forward branch for the Steward to push
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2228-clean-branch
trigger: Steward independent check 06:25Z; operator redaction of its own records
started_at: 2026-11-22T22:24:00-08:00
finished_at: 2026-11-22T22:31:00-08:00
duration_seconds: 420
verified: scans run by the coordinator with all 17 patterns over the staged diffs and the committed snapshot; counts only, no value printed or recorded
---

# Clean push branch and a wider denylist

## Why the first scan was not enough

My scan covered the owner account name and the alliance tag. The operator redacted allies' names and alliance names from its own records as well. I derived 15 more patterns from its redactions into the local `.git/privacy-denylist.txt` (17 patterns, regular expressions, case-insensitive; never committed). With all 17, my delivery commit `2481d606` was not clean: 12 files (9 records, 3 queue units) still added matching lines. The Steward, who had checked it with two patterns, held the push.

## What was done

- Removal-only redaction committed on main as `2086a07b` (staged diff: 0 added, 25 removed matching lines; JSON still valid).
- `push/clean` at `16297e70`: one commit whose parent is the published head `5173ed7d`, so it fast-forwards the work branch. It is the current tree except the `alliance-donations` and `resource-collection` splits, which stay as already published because they are the only places that still add matching text. Scan: 0 added lines, 0 file names, 0 images; 138 files; gate ok. The Steward rescans and pushes only that branch, not local main.
- Screenshots in `_tools_/state` (37) are gitignored by `.gitignore` line 9; none is tracked or staged.
- Local `expect-min` annotations (owner name 150, tag 300; actual 173 and 338 at HEAD) so a regex-versus-string error fails loudly; the toolsmith's check reads them.

## Still open

OD-20261123-04 (redact the current tree, history, public meanwhile, allies' names). After the answer: redact the split directories, merge `push/clean` into main, push the splits.
