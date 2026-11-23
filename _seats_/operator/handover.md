---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T07:00:00Z
level: L2
version: 0.4.0
description: The operator's live recipe - launch route, first-tap settling rule, guards, red lines, what to read instead of giant profiles, open claim times
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 20261123T064816Z-7f1c49 and 20261123T065128Z-63e9d0, the launch and the settling observation, 2026-11-23T06:48Z to 06:52Z
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-0659-operator, including the owner decision of 06:47Z on the account dialog
---

# Handover - operator

## Holder

- Seat `operator`, session `session-b718c7de-6aab-4159-b87e-41aa424237e9`. Write scope:
  queue claimed and done, `_records_/<date>/`, `_tools_/state/`.

## Run recipe

- Pre-start, same shell: `killall -9 UserNotificationCenter NotificationCenter`, then
  `lsappinfo front` must name LastWar.
- If the game is not running (check `lsappinfo list`, never start a second copy):
  `osascript -e 'tell application "LastWar" to activate'`. It reaches the front in about
  seven seconds. Never `open_app`, never Chrome.
- First taps after a fresh launch may be inert for a minute: wait, retry once.
- An 8-step cap executes 7. One action per turn, no zoom. Must-execute actions go by step 7. A claim may first ask
  for `queue.py read --record <path> --executor operator`.
- Server time is UTC minus 2 hours. The reset is 02:00Z.

## Guards

- Account-elsewhere dialog: the owner approved Confirm once, as a standing rule. If it
  returns within 30 minutes of a Confirm, stop, report, pause desktop play 30 minutes, then retry.
- A "Boarding closes in" banner with 70 seconds or more at the first frame: board first,
  carriage 2, 3 Trade Contracts.
- Non-UR days: dispatch SR or above trucks only.

## Red lines

No real-money, diamond or premium spend. No PvP, attack, rally, march, Arena or General's
Trial. No diplomacy, no ally-exchange trade. Quick Dispatch frozen. The mid-base trophy
bubble is never tapped. No identifier values in any file or message: write "owner
account", "[tag]", "the owner alliance", "an ally".

## Reading and records

- Never read the giant profiles. Use the digest
  `/tmp/lw-ps-digest.md`, or grep.
- Record bodies 350 words or fewer, rows in a sidecar. Run `stub-index --apply` for new
  records folders.

## Open times (UTC)

- 4-hour UR Capture the Oil Depot due about 08:51Z: jeep, Your Tasks, Claim first.
- Then a treasures re-read.
