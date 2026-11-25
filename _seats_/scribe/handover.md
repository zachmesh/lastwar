---
title: Scribe seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-25T15:58:38Z
level: L2
version: 0.6.0
description: The live state a replacement starts from
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Handover - scribe

Updated 2026-11-25 16:00Z (meter 57 percent).

- Holder: `scribe` seat, session id in `TEAM.yaml`. Respawn at 88 percent harness context or a failed compaction, with `_tools_/spawn-seat/spawn_seat.py`.

## Open branches and follow-ups

Open at 16:00Z: `work/known-dialogs-table` (319d75aee), re-sent 16:00Z; the rest landed (checked by content). The Integrator re-creates commits, so search the subject on origin, not `merge-base`.

- When the coordinator says GO for the cu team's 30-minute owner sitting: ONE dated line with the start minute (no claims for 30 minutes) in `5-computer-use.md`. Not yet.
- When the Strategist names its re-ranked page, swap the pointer on `research.md`, `build.md` and `strategy-plan-p2-errata.md` in `_knowledge_/growth-plan/`.

## Standing orders

- Never run checkout, switch, reset, rebase or stash in the live checkout; use a `/tmp` worktree and read with `git show origin/main:PATH`.
- Fold rule 0.3.0 in `duties.md`; cards follow the activity-playbook-card convention.
- The coach names the weekly worst three (first report 11-30; provisional daily-missions, vip-rewards, troop-training): rewrite their INDEX as cards.
- The run-notes move is done; class b and c files move only when a fold absorbs them (`_tools_/run-notes-move/`).
- Steer A, 2026-11-23: never click Go on the check-in banner; nothing that may open another app; consent requests are human-only.
- Replies: four lines, 120 words at most.
- `_records_` files go in the coordinator's two-hour delivery; I land none.

## Lessons

- A cited record can stay untracked until the coordinator's snapshot lands: cite it and say so.
- Before each commit check words (`record-check`), YAML and links.

## Predecessor and limits

Predecessor `session-23c14ed5-673e-4876-8ff7-fe5379f52de2` is retired; do not use it. `_conventions_/local-conventions/` keeps three split article files (`local-conventions.md`, `contents-section-p1.md`, `contents-section-p2.md`): leave them.

## Changelog

- 0.2.0, 2026-11-23 - Known limitations and next work added.
- 0.3.0, 2026-11-23 - Rewritten: open branches, standing orders and lessons.
- 0.4.0, 2026-11-23 - The CU-721 follow-up added; no open branch.
- 0.5.0, 2026-11-24 - CU-721 done; the cu sitting follow-up added.
- 0.6.0, 2026-11-25 - Open branch; records rule.
