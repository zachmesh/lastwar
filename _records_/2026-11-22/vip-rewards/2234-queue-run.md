---
title: VIP rewards queue run 2234, blocked attempt
created: 2026-11-23T06:40:00Z
modified: 2026-11-23T06:40:00Z
version: 1.0.0
description: VIP unit vip-2026-11-22-1800 attempt 1, operator seat, blocked at the first frame by an account active on a different device dialog and a changed foreground, no result, unit released
status: run-failure
grounded_in:
  - source: cu_bridge start and the run event log for run 20261123T063411Z-49accf, 2026-11-23T06:34Z to 06:37Z
  - source: run screenshots step-0000.png and step-0001.png under /Users/zhenchen/.computer-use/runs/20261123T063411Z-49accf
  - source: lsappinfo front readings before the start at 06:34:11Z and after the run at 06:37:54Z and 06:38:26Z
  - source: queue.py read, token-acquire, claim, release and token-release on the live pool, 2026-11-23T06:34Z to 06:38Z
---

# VIP rewards queue run 2234, blocked attempt

- Unit vip-2026-11-22-1800, operator seat, assignment A-20261123-0633-operator,
  attempt 1 of 3. No VIP screen was reached and nothing was claimed. The unit was
  released back to the inbox. Timeline rows are in the sidecar
  [2234-queue-run-detail.md](2234-queue-run-detail.md).
- Status: failure, blocked by the foreground and by the account state. No game result.
- Run `20261123T063411Z-49accf`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8. It made 2 steps and 1 click that landed, then 1 click that the
  harness blocked. Cost about 0.02 USD. No local-input takeover event.
- Claim gate: the first claim was refused, because the read receipt for the
  queue-ticker record was older than 120 minutes (issue #737). The record was re-read,
  the receipt recorded, and the second claim passed. The token was released between them.
- First frame: the pre-start check had shown the game in front, but the game's first
  frame was a TIPS dialog, "Your account is currently active on a different device!",
  with a red Confirm button. The run tapped the dialog's X once and did not tap
  Confirm. Confirm would take the session over, which is an owner decision.
- Then the foreground changed. The second click was blocked because the front app had
  become Terminal. The next frame was fully black. The harness then waited on a
  consent request to act on Google Chrome, which is not approved, until the run ended.
- State left: at 06:38:26Z Google Chrome was still the front app. No input was sent
  after 06:34:22Z. The unit and the device token were released at 06:38:26Z, and the
  claimed pool was empty.
- Reading: someone was using the Mac or the account on another device. This is a
  precondition failure, not a game state. It says nothing about the VIP freebie or the
  login chest, which are still unread.
- Waiting on this: both UR Secret Missions claims and this unit.
- Red lines held: no Confirm, no purchase, no diamonds, no diplomacy.
- Plan after release: a fresh front-app check showing the game, a read of the TIPS
  dialog state first, and never Confirm unless the coordinator's message says the owner
  approved one Confirm.
