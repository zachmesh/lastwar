---
title: Queue Run 1850 Event Claims
created: 2026-11-02T18:50:00Z
modified: 2026-11-02T18:50:00Z
level: L0
version: 1.0.0
description: Events unit contested, failed, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 1850 queue run - event claims (failed, contested)

Unit events-2026-11-02-1457, executor ticker-1834, session
about 18:44 to 18:50 America/Los_Angeles. Status failed
(contested): the "active on a different device" dialog
returned for a third time in this pass, after two Confirm
takeovers earlier in the same pass (during the trucks
unit, at norm 501,568, each followed by the app exiting
and being reopened). Per the owner rule of 2026-10-27,
after two takeovers a returning dialog means the owner
is likely playing on his phone, so the pass stopped.
No Events screen was reached and nothing was claimed.
Tracker untouched (failed units do not mark the
tracker).

## Sequence in this pass

- Trucks unit trucks-2026-11-02-1457, partial: dialog
  confirmed twice, base stayed clean after the second
  takeover, trade entry blocked (see
  truck-plunder/1845-queue-run.md).
- Events unit claimed next. On re-activating the game
  window the same dialog was present again, a third
  time in this pass. It was NOT confirmed a third
  time. The pass stopped here and the device token
  was released.
- The game was left with the dialog on screen; the
  owner session on the other device is undisturbed.

## Outcome

- Status: failed (contested).
- Claimed in this unit: none.
- Counters: none read.
- Red lines: no diamonds, no paid button, no purchase.
- Zombie seeding: not enqueued. The Zombie Invasion
  event ended 2026-10-30 and no live return sighting
  occurred in this pass.
