---
title: Secret missions claim run 4 at 2248
created: 2026-11-23T06:55:00Z
modified: 2026-11-23T06:55:00Z
version: 1.0.0
description: Claim run 4, continuation of secrets-2026-11-22-1857, operator seat, game relaunched after the account was used elsewhere, the 2-hour UR task claimed on the second run
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final results on runs 20261123T064816Z-7f1c49 and 20261123T065128Z-63e9d0, 2026-11-23T06:48Z to 06:52Z
  - source: run screenshots step-0000.png and step-0006.png of the first run and step-0003.png and step-0004.png of the second, final frame saved as _tools_/state/cu_secrets_2251.png
  - source: lsappinfo process and front readings, and the osascript launch of the game, 2026-11-23T06:47Z to 06:50Z
  - source: queue.py token-acquire and token-release around the work, no unit claimed
---

# Secret missions claim run 4 at 2248

- Claim run 4, continuation of secrets-2026-11-22-1857, assignment
  A-20261123-0648-operator. It is not a queue unit. No unit was claimed, the closed
  partial unit file is untouched. Measured rows are in the sidecar
  [2248-queue-run-detail.md](2248-queue-run-detail.md).
- Status: done on the second run. The 2-hour UR task was claimed at 06:51:46Z.
- Launch: the game was not running and Google Chrome, not touched, was in front. The
  game was launched with the helper's `osascript` activate, after checking that no game
  process existed. It reached the front in about seven seconds.
- Run one, `20261123T064816Z-7f1c49`: 7 steps, 6 actions done, 0 refused, 0.087144
  USD. The first frame was the base, with no account-elsewhere dialog and no boarding
  banner, so Confirm was not needed and not tapped. Three taps on the jeep icon,
  spread over about 40 seconds, opened nothing, though the base kept animating. It ended
  not done.
- Run two, `20261123T065128Z-63e9d0`: 5 steps, 10 actions done, 0 refused, 0.068517
  USD. The first jeep tap opened the post. One Claim tap paid the UR task Rescue Missing
  Agent. The popup tiles are in the sidecar. The run dismissed it and returned to the
  base. The cards were not read after the claim, so which are stamped is unverified.
- Why the first taps failed is not established; a settling period after a fresh launch is
  the likely reading.
- Confirm: never tapped, so the two-device guard window never started. The dialog
  did not appear in either run.
- Account state, read on the base, differs from an hour ago: all four builders busy,
  diamonds higher, stamina higher, food and coin lower. That fits play on the other
  device and is not attributed to this seat.
- Still running: the 4-hour UR task Capture the Oil Depot, about 01:59 left at the claim,
  so due at about 08:51Z.
- Closing state: the base screen, no panel open. 
- Not touched: Chrome, every Go button, Plunder, Mega buttons, ally exchange, the
  mid-base trophy bubble.
- Red lines held: no diamonds, no purchase, no speedup, no diplomacy.
- Follow-up: claim the 4-hour UR task at about 08:51Z; then the VIP unit.
