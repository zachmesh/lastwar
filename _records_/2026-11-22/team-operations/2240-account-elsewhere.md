---
title: Account active on a different device - 2026-11-22 22:40 PT
created: 2026-11-22T22:40:00-08:00
modified: 2026-11-22T22:42:00-08:00
level: L3
version: 0.1.0
description: The vip unit's first frame was the game's account-on-another-device dialog; the operator correctly did not confirm; play is blocked until the owner answers whether the session may be taken over
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2240-account-elsewhere
trigger: operator reply on A-20261123-0633; run 20261123T063411Z-49accf
started_at: 2026-11-22T22:34:11-08:00
finished_at:
duration_seconds:
verified: operator reply and its stop times; bridge and process state read by the coordinator at 06:39:39Z; the cause of the dialog is NOT verified
---

# Account active on a different device

## What happened

- `vip-2026-11-22-1800` was dispatched 06:32:47Z. The operator claimed and started run `20261123T063411Z-49accf` at 06:34:11Z.
- The first frame was the game's dialog "Your account is currently active on a different device!" with a Confirm button. The operator tapped the dialog's X once and did not tap Confirm: Confirm takes the session over from the other device, which is the owner's decision.
- The next click was blocked (front app Terminal), the following frame was black, and the harness waited on a consent request for Google Chrome (not approved) until the run ended at about 06:37:42Z. 2 steps, 1 click, 0 refused, no takeover, about 0.02 USD. Unit released to the inbox (attempts 1 of 3), token released at 06:38:26Z.
- At 06:39:39Z the front app is Google Chrome (the owner's browser, running 8 days); the game is not listed as a running application; two `cu_bridge serve` processes are alive.

## Unverified

Whether the other device is the owner playing, or a lost session. The coordinator cannot tell from files.

## Actions

The Steward is asked whether the owner is playing elsewhere or using Chrome, and whether one Confirm may be tapped. The operator is held with no input. At risk: the 2-hour UR Secret Missions claim (finished about 06:50Z, can be plundered) and the 4-hour claim at about 08:50Z; all other units are long-window. Opened as OD-20261123-05.

## Outcome

Pending the owner's answer.

## Cleanup and the owner's rule (appended 2026-11-23T06:44Z)

- The Steward found the run listed as not finished. It was `awaiting_consent` for the owner's browser in an orphan daemon (3 hours 5 minutes old) that `status` and `control stop` could not reach, because the operator's bridge restart at about 06:37Z had put a new daemon on the socket. At 06:41Z the coordinator ended only the orphan daemon and its child; the new daemon passed `self-test`; nothing was claimed or running. Filed as IMP-20261123-07.
- Owner rule, relayed by the Steward at 06:42Z: "you shall never stop the game." No more play holds for the GitHub login; the login moves to a method that does not touch the desktop. This is a standing rule, recorded in the coordinator handover.
- Still blocked: the account-elsewhere dialog and the single Confirm question (OD-20261123-05); the operator is told to do nothing until the owner answers.
