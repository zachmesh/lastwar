---
title: Scribe seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T16:18:04Z
level: L2
version: 0.3.0
description: The live state a replacement starts from
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Handover - scribe

Updated 2026-11-23 16:25Z (harness meter 79 percent, 28 turns).

- Holder: `scribe` seat, session id in `TEAM.yaml`. Respawn at 88 percent harness context or a failed compaction, only with `_tools_/spawn-seat/spawn_seat.py`.
- Schedules: none of this seat's own.

## Open branches and follow-ups

No branch of mine is open: all landed by 16:25Z. The Integrator re-creates commits, so `merge-base --is-ancestor` says no; search the subject on origin instead.

- Follow-up: when the Strategist names the page of its re-ranked plan, swap the pointer on `research.md`, `build.md` and `strategy-plan-p2-errata.md` in `_knowledge_/growth-plan/` (it points at `plan-of-record.md` now).
## Standing orders

- Never run checkout, switch, reset, rebase or stash in the live checkout; use a `/tmp` worktree and read with `git show origin/main:PATH`.
- Fold rule 0.3.0 in `duties.md`. Cards follow the activity-playbook-card convention: 300 words, rules cite records, rewritten in place, numbers line from the coach's CSV.
- The coach names the weekly worst three (first report 11-30; provisional daily-missions, vip-rewards, troop-training): rewrite their INDEX as cards.
- The run-notes move is done (1,095 notes). Class b and c files move only when a fold absorbs them, with `_tools_/run-notes-move/`.
- Steer A, 2026-11-23: never click Go on the check-in banner; nothing that may open another app; consent requests are human-only.
- Replies to the coordinator: four lines, 120 words at most.

## Lessons

- A cited record can stay untracked until the coordinator's snapshot lands: cite it and say so.
- Before each commit run `lint_gate.py record-check` for words, then YAML and link checks.

## Predecessor and limits

The delegated child session `session-23c14ed5-673e-4876-8ff7-fe5379f52de2` held this seat before 2026-11-23T04:01Z; do not use it. `_conventions_/local-conventions/` keeps three article files from the split of its own INDEX (`local-conventions.md`, `contents-section-p1.md`, `contents-section-p2.md`): the linter cannot tell them from instances; leave them.

## Changelog

- 0.2.0, 2026-11-23 - Known limitations and next work added.
- 0.3.0, 2026-11-23 - Rewritten: open branches, standing orders and lessons.
