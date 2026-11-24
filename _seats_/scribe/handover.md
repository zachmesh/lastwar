---
title: Scribe seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T01:12:21Z
level: L2
version: 0.4.0
description: The live state a replacement starts from
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Handover - scribe

Updated 2026-11-23 17:15Z (meter 48 percent).

- Holder: `scribe` seat, session id in `TEAM.yaml`. Respawn at 88 percent harness context or a failed compaction, with `_tools_/spawn-seat/spawn_seat.py`.
- Schedules: none of this seat's own.

## Open branches and follow-ups

No branch of mine is open (all landed by 17:12Z); the Integrator re-creates commits, so search the subject on origin, not `merge-base`.

- When the Toolsmith reports the CU-721 restart done (the bridge moves to a worktree under `~/dtadpole/computer-use-wt/`; 300 s returns with CU-720): update the dated note in `5-computer-use.md`, ask the operator to update its hazards line, and update the bridge tool page with the project path. Small branches, no history edits.
- When the Strategist names its re-ranked page, swap the pointer on `research.md`, `build.md` and `strategy-plan-p2-errata.md` in `_knowledge_/growth-plan/`.

## Standing orders

- Never run checkout, switch, reset, rebase or stash in the live checkout; use a `/tmp` worktree and read with `git show origin/main:PATH`.
- Fold rule 0.3.0 in `duties.md`; cards follow the activity-playbook-card convention.
- The coach names the weekly worst three (first report 11-30; provisional daily-missions, vip-rewards, troop-training): rewrite their INDEX as cards.
- The run-notes move is done; class b and c files move only when a fold absorbs them (`_tools_/run-notes-move/`).
- Steer A, 2026-11-23: never click Go on the check-in banner; nothing that may open another app; consent requests are human-only.
- Replies: four lines, 120 words at most.

## Lessons

- A cited record can stay untracked until the coordinator's snapshot lands: cite it and say so.
- Before each commit check words (`record-check`), YAML and links.

## Predecessor and limits

Predecessor `session-23c14ed5-673e-4876-8ff7-fe5379f52de2` is retired; do not use it. `_conventions_/local-conventions/` keeps three split article files (`local-conventions.md`, `contents-section-p1.md`, `contents-section-p2.md`): leave them.

## Changelog

- 0.2.0, 2026-11-23 - Known limitations and next work added.
- 0.3.0, 2026-11-23 - Rewritten: open branches, standing orders and lessons.
- 0.4.0, 2026-11-23 - The CU-721 follow-up added; no open branch.
