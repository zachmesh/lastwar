---
title: Troop training queue run 2017
created: 2026-11-23T04:19:00Z
modified: 2026-11-23T04:19:00Z
version: 1.0.0
description: Training unit training-2026-11-22-1803, operator seat, Lv.24 requeue blocked by the live Drill Ground Full toast, 0 troops queued
status: run-partial
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T041712Z-711380, 2026-11-23T04:17Z to 04:18Z
  - source: run trajectory events.jsonl and screenshots step-0005.png and step-0007.png under /Users/zhenchen/.computer-use/runs/20261123T041712Z-711380
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:17:12Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:17:12Z
---

# Troop training queue run 2017

- Executor: operator seat (top-level session), unit training-2026-11-22-1803,
  assignment A-20261123-0416-operator relayed by the Steward. Token lease
  04:32:12Z, claim lease 04:37:12Z, attempts 1.
- Status: partial. One barracks was checked (Lv.24). Its requeue was blocked by
  the live toast "Drill Ground Full: Unable to add more units." 0 troops queued.
- Run: `20261123T041712Z-711380`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:17:13Z, ended 04:18:02Z with status `max_steps` and no
  final message (the step-8 call was recorded but not executed). Active 48.6 s,
  model time 33.3 s, so 4.16 s of model time per step. Steps 8, actions done
  21, refused 0, blocked 0, failed 0, skipped 0. Cost 0.094975 USD, or
  0.0119 USD per step.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Every landed click carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover in
  this run.
- What the run did, from the trajectory: step 1 click (613,174) and step 2 click
  (177,918) left the ALLIANCE hub that the previous donations run had left open,
  and reached the base. Steps 3 and 4 were tent taps at (472,585) and (630,565).
  Step 5 read "Lv.24" and tapped the pistol at (598,616); no panel and no toast
  are visible on step-0005.png. Step 6 re-tapped the tent at (610,565). Step 7
  tapped the pistol at (598,612), and step-0007.png shows the toast "Drill
  Ground Full: Unable to add more units." with no TRAIN UNITS panel.
- Verification on the final screenshot: the toast is read live and the HUD is
  unchanged against step-0005: food 732.3M, iron 1.1G, gold 35.3M, diamonds
  8,336, power 150,080,120. No batch was started, and nothing was spent.
- Blocker: the Drill Ground Full requeue block (Issue #678) is live again. The
  2026-11-22 0134 and 0958 units requeued Lv.27 and Lv.30 without it. Lv.24 has
  been idle since the 1005 arms-race cross-read collected its 143 Lv.8 batch.
  Category `e` (repeated blocker).
- Not checked: Lv.27 (T9 x726 queued at 0134, expected busy), Lv.30 (T10 x793
  queued at 0958, expected busy) and the fourth barracks Lv.20 were not opened.
  Their state is carried, not read.
- Red lines: no speedup, no diamonds, no purchase, no upgrade arrow, no Finish
  Now, no PvP, no diplomacy. Quick Dispatch was not tapped.
- Note on the prior unit: the donations unit donations-2026-11-22-1803 was
  closed partial by another session holding the operator scope, at 04:15:33Z
  (record alliance-donations/2013-queue-run.md). This session also tried one
  bridge `resume` on that run at 04:14:46Z, before the Screen Sharing cause was
  known. The server refused it (`resume_needs_control`), so no input followed.
  The other record does not mention this attempt, so it is disclosed here.
- Follow-up: requeue needs a cleared Drill Ground. The Drill Ground screen has
  still not been read live. The next training unit should open the Drill Ground
  first, or the owner should decide how a full Drill Ground is cleared
  (Issue #678).
