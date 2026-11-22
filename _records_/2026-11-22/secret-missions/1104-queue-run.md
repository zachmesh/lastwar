---
title: Secret missions queue run 1104
created: 2026-11-22T19:04:00Z
modified: 2026-11-22T19:04:00Z
level: L0
version: 1.0.0
description: Secrets unit secrets-2026-11-22-0657, ticker-1050, 2 finished UR tasks claimed with one tap but both plundered before the claim, assists already 5/5, no pending tasks to deploy, Reward Recovery 2026-11-19 CLAIMED
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 11:00-11:04 PT
  - source: unit secrets-2026-11-22-0657 in _queue_/claimed
  - source: tools/duel.py --json, duel day 7 Off day - settlement, no scoring actions
---

# Secret missions queue run 1104 (ticker-1050)

Unit secrets-2026-11-22-0657, regular secrets, segment 3.
Executor ticker-1050. Computer session cc-139. Session
window about 11:00 to 11:04 PT. Game in window mode
(642x951, window 127196), background input working. No
"active on a different device" dialog.

## Outcome

Done - 2 finished UR tasks claimed with one Claim tap
(the claim-all behaviour); both had been plundered
before the claim, so their listed rewards went to the
plunderers and no received-rewards figure was displayed
to read. Ally assists already 5/5 for this reset day.
No pending tasks to Mega Deploy. Reward Recovery
2026-11-19 record reads CLAIMED; the 2026-11-18 record
would not expand (presumed settled, as with the
2026-10-16 record). No diamonds or items spent, no
Mega Refresh used, Plunder Others untouched.

Note: this unit's slot was 06:57 PT and its expires_at
10:57 PT; it was picked at 10:59 PT and finished after
expiry, a late finish.

## Post state at entry - read live about 11:01

- SECRET COMMAND POST verified (opened first tap from
  the base left column slot (48,648)).
- Assist Allies 5/5, Plunder Others 0/5. Your Tasks
  badge 3.
- Rows: UR Rescue Test Subject (Claim), UR Capture the
  Oil Depot (Claim), UR Disrupt electric grid (orange
  plunder stamp), SSR Provide Tech Support to Refugees
  (gold PERFECT stamp).
- Duel posture (tools/duel.py): day 7, Off day -
  settlement, no scoring actions, radar posture stack.
  The Mega Refresh-for-UR rule does not apply.

## Claim - about 11:02

- One tap on the Rescue Test Subject Claim button
  opened the CONGRATULATIONS popup over the interaction
  list. The Your Tasks badge cleared and no Claim
  button remains on any visible row.
- Plunder rows in the popup: [GLYD]바니윤 Bunny,
  11-21 22:48, and one further plunderer (name cut off
  at the top of the list) - each "Plundered your task
  rewards" with ? x15, green box x144, triangle 240,
  Hero EXP 1.2M. The two finished UR tasks sat finished
  since about 22:47 on 2026-11-21 (dispatched about
  18:47 that day) and were plundered overnight.
- Help rows: [AP3x]D Texas Boy, 11-22 03:47, and
  [AP3x]Lisas49ers 리사, 11-21 22:48 - "helped you
  claim task rewards". Like All tapped (thumbs-up icons
  on the two help rows show liked); the popup was then
  dismissed by tapping the dimmed area.
- Post-claim read: all three UR rows now carry the
  orange plunder stamp; the SSR row keeps the gold
  PERFECT stamp. Lesson repeated from ticker-2234:
  finished tasks left unclaimed for hours get
  plundered - the claim unit should run soon after the
  shortest tasks finish.

## Dispatch check - about 11:03

- A scroll of the Your Tasks list produced no change:
  the 4 resolved rows are the whole list, no pending
  (Go) task exists, so no Mega Deploy this unit. New
  tasks spawn over time; the next secrets unit
  dispatches them.

## Reward Recovery - about 11:03

- 2026-11-19 18:00 record: "OVER THE PAST 1 DAYS,
  YOU HAD 8 UNSTARTED SECRET TASKS. WE'VE SINCE
  COMPLETED THEM FOR YOU AND RECOVERED SOME OF THE
  REWARDS." Rewards shown include map fragments
  5/2/2/3/1, envelope x1, fragment x1, Mystery Supply
  Box 287, puzzle x2, 6.0K x5 (more below the fold).
  Status CLAIMED - nothing unclaimed.
- 2026-11-18 18:00 record: collapsed; a tap on its
  header did not expand it (same as the 2026-10-16
  record) - presumed settled, not verified.
- "ONLY THE LAST 7 RECOVERY RECORDS ARE RETAINED."

## Result stats

- target: claim every finished secret task, use ally assists to the 5/day cap, dispatch pending tasks, check Reward Recovery
- achieved: 2 finished tasks claimed (both plundered before claim); assists already 5/5; no pending tasks to dispatch; Recovery 2026-11-19 CLAIMED
- resources_gained: none read - no received-rewards figure was displayed for the plundered claims
- points: 0
- costs: about 12 minutes device time, no spend, no stamina, no items
- verified: yes (post state, claim popup, Recovery panel all read live in this unit)
- tasks_claimed: 2
- tasks_plundered: 2
- assists_used: 5
- assists_cap: 5
- pending_tasks: 0
- late_finish: true (slot 06:57 PT, expires_at 10:57 PT, finished about 11:04 PT)
