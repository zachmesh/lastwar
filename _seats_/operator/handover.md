---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T09:12:00Z
level: L2
version: 0.5.0
description: The operator's live recipe - launch route, first-tap settling rule, guards, red lines, what to read instead of giant profiles, open claim times
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 20261123T064816Z-7f1c49 and 20261123T065128Z-63e9d0, the launch and the settling observation, 2026-11-23T06:48Z to 06:52Z
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-0659-operator, including the owner decision of 06:47Z on the account dialog
---

# Handover - operator

Updated 2026-11-23 09:12Z from the outgoing operator's handover (`_records_/2026-11-22/growth/0054-operator-handover.md`, detail with commands, coordinates and the inventory map in `0054-operator-handover-detail.md`). Earlier versions are in git history.

## Holder

- Seat `operator`; the outgoing session `session-7f6dd658-ebba-4854-9a29-e2f173975825` (started 07:03Z, respawned at 86 percent context) is replaced by a fresh top-level session recorded in `TEAM.yaml`. Only the operator holds the device token and sends game input. Write scope: queue claimed and done, `_records_/<date>/`, `_tools_/state/`. Reply to the coordinator in four lines.

## Run recipe

- Per run: `queue.py token-acquire`, `claim` for a queue unit, then in one shell `killall -9 UserNotificationCenter NotificationCenter`, check `lsappinfo front` names the game, then `cu_bridge.py start --task ... --model claude-gateway/claude-sonnet-5-5 --max-steps N` (N steps means N-1 executed; the last turn is the report). One action per turn, never zoom, never Escape. The harness cost cap stops near 0.36 of the stated `--max-cost`; a step costs 0.012 to 0.015 USD.
- Interrupts: the account dialog (Confirm once, never twice within 30 minutes); a train boarding banner with 70 seconds or more (board first); local pointer input pauses a run (stop it with `cu_bridge.py control --command stop`, relaunch, tell the coordinator the time and what else ran).

## Hard safeguards for any Use press

The Mystery Supply Box quantity defaults to its FULL count, and the Resources tab selects the 5,000-diamond tile by default. Check in a frame that the number field reads exactly 1 before Use, press Use once per run, split the check and the press into two runs, read the popup. Never open boxes or chests without an assignment. No purchase, diamond spend, speed-up or Finish Now, PvP or march, diplomacy or ally exchange.

## Growth rules

Read first (builders, labs, training), fill only idle slots under the 3x rule above the reserves, collect first before a power read, press Complete the moment a node finishes, never retry the hospital Collect (all-or-nothing), never cancel a running item. Every unit carries a `serves:` line.

## Open

Scout reads S1b and ST1 (Universal Shard counts, store balances); the next 4-hour claim about 12:51Z; the Lv.27 barracks batch about 19:56Z; a lab frees about 11:43Z; builders free 2026-11-24T09:20Z.
