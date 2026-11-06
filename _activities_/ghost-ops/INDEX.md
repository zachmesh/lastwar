---
title: Ghost Ops
created: 2026-10-26T04:02:00Z
modified: 2026-11-06T07:32:00Z
level: L1
version: 1.1.0
description: Weekly Ghost Ops event missions at the Secret Command Post, one activity folder for ghost ops knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game instructions No.2487 Ghost Ops Guide, read 2026-10-25
  - source: owner direction to register each learned task type as metadata, 2026-10-25
  - source: ghost-ops execution record 2026-11-05 2303 queue run (ticker-2303 unit, failed, Mac device offline, sixty-second consecutive pass, Issue 284)
---

# Ghost ops

## What this activity is

A weekly event run from the third tab of the Secret Command Post.
Missions are published in the post, executed in other warzones, and
rewarded by manual claim. This folder accumulates ghost ops
knowledge. Executions are recorded in
`_records_/<date>/ghost-ops/`, one file per execution. The post
itself belongs to [`secret-missions`](../secret-missions/INDEX.md).

## How to enter

- Open the Secret Command Post (see the entry notes in
  secret-missions) and tap the Ghost Ops tab. On inspection day,
  2026-10-25, the tab carried no badge and the screen read - Next
  event coming soon, 2 days 22 hours 56 minutes - pointing at the
  weekly Thursday running day.

## How it is played

From the in-game guide (No.2487 Ghost Ops Guide), read 2026-10-25.

- Base Level 18 or above to take part. This account is level 30.
- Every Thursday the Secret Command Post of other warzones publishes
  3 Ghost Ops missions; they must be completed in other warzones.
- Missions run in four server time windows - 00:00 to 03:00, 06:00
  to 09:00, 12:00 to 15:00 and 18:00 to 21:00.
- Form a team or go solo. On completion, claim the rewards manually -
  nothing is automatic.
- On an event day, earn rewards by helping allies 3 times per day,
  and plunder 5 Ghost Missions per day is allowed - the guide
  suggests picking UR ones.
- The screen carries an Auto Smart Task Execution option, found
  ticked on inspection.

## Cadence

- Weekly, Thursdays only, inside the four server time windows. Help
  cap 3 per day and plunder cap 5 per day on the event day.

## Scope and availability

- Event system, not yet observed live on this account - everything
  above the What is known section is the guide text, not play
  experience.
- Ghost plundering is PvP by the guide wording. It is not touched
  without the owner explicit instruction, under the recording rules.

## What is known from 2026-10-25

- Inspection only - no event was running. The Ally Team List was
  empty and Rewards for helping allies read 0 of 3.

## Open questions

- What the 3 weekly missions look like in practice, their durations
  and their reward table.
- Whether the account warzone posts missions other warzones
  can run, and what hosting pays.
- Whether Auto Smart Task Execution should stay ticked - it was on
  at first sight and was left as found.

## What the 2026-11-05 2303 unit added - Mac device offline, sixty-second consecutive pass, zero-response form

- Unit ghost-ops-2026-11-05-0000 by ticker-2303, about 23:10 to 23:14 local, status failed. Evidence in `_records_/2026-11-05/ghost-ops/2303-queue-run.md`. On a working screen this unit would have opened the Secret Command Post Ghost Ops tab and read the Thursday missions, help count and claimable rewards. No Ghost Ops tab was opened, no missions run, no help given, no rewards claimed.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses, all node_offline (device offline, no wake-up path): connection.health (attempt 1), computer.session start (attempts 2 and 4), connection.repair (web) (attempt 3), connection.health again (attempt 5). device.list reports the Mac mini offline with last_seen 15:36:52Z, stale about 15 hours 35 minutes at the 23:11 re-check, unchanged since the ticker-1025 pass and identical to the ticker-2152 pass reading. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen 15:36:52Z, and its attempts in the ticker-2041 pass timed out after 25 seconds each, so nothing new would be learned by repeating them.
- Recurrence, not a new failure class: this is the sixty-second recorded consecutive ticker pass with a Mac device-access blocker, twenty-third in the worsened zero-response form after ticker-2152 (sixty-first, twenty-second). Passes between 2152 and 2303 left no record on the branch, so the true consecutive count may be higher; this pass counts recorded passes only. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the sixty-second occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the Thursday missions, the help count or claimable rewards. It must NOT be read as a Ghost Ops state - the 2026-10-25 inspection (no event running, Ally Team List empty, help rewards 0 of 3) stands as the last live read, and this unit neither confirms nor supersedes it. The loss is the unexecuted Ghost Ops Thursday check and the missing closing read for this slot.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset, chain pre-reset-sweep-2026-11-06: the ticker-2152 pass staged the pair only onto the records branch, so the live pool inbox did not hold them; this pass copied the two branch files verbatim into the live pool inbox (unit 001 not_before 2026-11-07T01:30:00Z, unit 002 not_before 2026-11-07T02:30:00Z, both priority 1, expiring at the reset 2026-11-07T03:00:00Z). Tonight's pair (for the 2026-11-05 reset) expired unexecuted on the same Mac device blocker, second consecutive night.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the ghost-ops unit. The pass stopped after this unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 5 (events, passes, secrets, treasures and trucks 2026-11-05-1857, window passed before execution), due 21, produced nothing new, all 21 regulars already queued; the inbox held 71 units at this pass (73 after the zero-sweep pair was restored to the live pool).
