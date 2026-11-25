---
title: Integrator handover
created: 2026-11-23T07:25:00Z
modified: 2026-11-25T12:19:00Z
level: L2
version: 0.4.0
description: The live state a replacement integrator starts from
status: unverified
grounded_in:
  - source: owner decision 2026-11-23 that integration is a dedicated seat, relayed by Steer A
  - source: reflection integrator-role convention, adapted in TEAM.yaml coordination.integration
  - source: the landing notes and catalogs in _records_/2026-11-22/integration
---

# Handover - integrator

Updated 2026-11-25 12:19Z. Earlier versions are in git history.

## Holder

Session `session-bc838015-7852-464e-8cab-cf2fcc70a335`, started 2026-11-23T07:15Z, claude-sonnet-5-5 at high effort since the owner's request of 2026-11-25. Hand-offs come from the coordinator (`session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`) as a branch name. A message to another session fails ("belongs to another parent session"): the final reply is the only channel, and messages cross. Report to the coordinator in English.

## State

- Last merged pull request: 992, merge commit `f00c6228e8bed`, the origin/main tip at 2026-11-25 12:18Z. The only open pull request is 838, stale: never merge it.
- Held: `work/known-dialogs-table` 319d75aee, sent by the scribe and reviewed, never named by the coordinator: land it only when it does.
- Nothing else is waiting. Every branch the coordinator named has merged (908 to 992, branches kept). Many work branches show as unmerged by SHA: they landed as rebuilt `land/` copies or predate this seat. Check the pull request list and the landing notes, not ancestry.
- Findings for others: the lesson page finished-batch-lesson.md carries a pre-registration stamped 2026-11-26T21:10:37Z, in the future (scribe); the unit template's exempt-word list omits "fill idle slot" (coordinator).
- Switches: `require_forecast` is on since 959. `require_state_read` is absent, which is off; flipping it is the coordinator's, never mine.
- Guarded blobs on main: queue.py 7a4b2f11e3d7, cu_bridge.py f595c7303f76, regulars.json 1879aba3489b, observation.py 950ebf74c257. After landing a change to one, give the coordinator the new blob for tool_sync.

## Rule

Scope, then the privacy scan before any push, then the checks. Push the named branch (or a rebuilt `land/` copy proved byte-identical), open the pull request, merge with a merge commit and `--match-head-commit`, read main back: two parents, parent 1 the old main, parent 2 the head, equal trees, both ancestors of origin/main. Fetch origin before every chain: a second chain in one command rebuilt on a stale base and printed a benign tree mismatch on 991. Never squash, force-push, `--admin`, delete a branch, push main, or merge code I wrote. In the live checkout run no checkout, switch, reset, rebase or stash: use worktrees under `/private/tmp/lw-integrator/`. `gh` only for pr list, view, create, merge, comment and checks.

## Checks

`lint_gate.py check --base origin/main` blocks on exit 2; the author's hook replay (`check --staged`); the privacy census, whose control (`--rev 839bad3fda`) must read live. Read every code file and test diff. Records branches: each deleted unit needs a counterpart in `_queue_/done`; an untracked citation is a warning for the coordinator's next snapshot. The cu-bridge tests never run while `_queue_/claimed/` holds a file; a skip is not a pass; poll for a gap; never set CU_TESTS_IGNORE_LIVE_RUN. Landing note: `landing-pr-NNN.md` plus one line in the newest catalog (now catalog-03.md); the coordinator commits them.

## Tools

The durable path is `_tools_/integrator/integrator.py` (status, check, push, open, merge, readback). My chain scripts live only in `/private/tmp/lw-integrator/` and may be gone: rebuild from the wrapper, or ask the toolsmith to check them in.
