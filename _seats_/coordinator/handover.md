---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T11:56:00Z
level: L2
version: 0.11.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, the growth Epic, in-flight landings and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 09:25Z (Mac UTC; quote `date -u`, the gateways' labels have run ahead). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s); daily `schedule-e1887d97` (12:00Z word-budget `watch`); weekly `schedule-fee71877` (Sundays 17:00 PT strategy review). One-shots today: lab frees 11:43Z `schedule-ceb293d6` (research conversion unit by name), Secrets claim 12:50:30Z `schedule-4aef1bc1`; tomorrow 09:21Z `schedule-f3804b22` the three Drill Ground starts (units `building-queues-growth-convert-2026-11-24-001`, `-002`, `-003` in that order; the cu team knows the slot).
- TEAM.yaml 0.7.2: 10 roster rows; operator is now `session-c08193d1-e6c0-489e-aa09-f812877c65ec` (09:07Z). Steer A (`session-eb024f72-e661-4a77-9303-66af95dbcfd1`) and Steer B (`session-e127662e-07ba-4385-b905-3d0e90fd1eeb`) both relay the owner; if two orders collide, tell Steer A.

## Respawn checklist (owner order: Sonnet 5.5 xhigh for every seat)

Respawn an operator past 85 percent context (read its handover file first). Spawn ONLY with `_tools_/spawn_seat.py` (when landed) or, until then, `session-relay spawn` with `--model claude-sonnet-5-5 --effort xhigh`; READ BACK with `inspect`; never leave the host default (opus). Run `_tools_/model_guard.py --apply` in each tick once it lands.

## How a tick runs

`queue.py next`, dispatch in one turn, chain on each verified reply, no-op while the operator plays. Game never stops. Fixed lines: no purchase, diamond spend, Finish Now, PvP or diplomacy; bounded speed-ups and store spending only under decisions 2410 and 2425. Never name the owner's in-game name.

## Growth and the owner's rules

Strategy v2.0 (the Strategist owns it, forecast ledger exists). Coin is not the gate (406M read); slots are; hospital Collect is all-or-nothing. Box sample: up to 22 Mystery Supply Boxes, quantity read as exactly 1 before every Use. Slots: lab about 11:43Z, builders 2026-11-24T09:20Z.

## Landings (Integrator; branch names, never push local main)

Local main equals origin plus my unlanded commits (converged 10:36Z; backup ref `refs/backup/main-before-converge-*`). Deliver: stage explicit paths, commit, `git branch land/records-<UTC> HEAD`, verify in a CLEAN worktree (`check --base origin/main`; the live tree has untracked files that give false findings), whole-tree scan with `/tmp/lw-scan-branch.py` (git archive, wrap-aware), hand the branch name to the Integrator; after each merge: `git fetch && git rebase --autostash origin/main`. The tick runs `_tools_/tool-sync/tool_sync.py` first (the stale-tool guard refuses `next` when queue.py is behind origin's). Never merge origin into this checkout (it was 246 conflicts; no longer needed).

## Open owner decisions

None (register OD-20261123-06 to -16 decided).
