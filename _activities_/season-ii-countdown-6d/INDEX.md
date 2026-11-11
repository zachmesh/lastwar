---
title: Season II Countdown
created: 2026-11-09T18:43:00Z
modified: 2026-11-09T19:32:17Z
level: L1
version: 1.0.0
description: Season II HUD countdown - opens the Transfer Surge cross-warzone transfer window; rejected as a queue task, no reward, no cost, no recurring action; the transfer decision is the owner's (Issue #514)
status: unverified
grounded_in:
  - source: ticker-1038 scout discovery unit 011 execution record 2026-11-09 1044 queue run (done, Transfer Surge confirmed live in all 3 tabs, candidate rejected as a task, duplicate of unit 004 exploration; record commit d630be83 on records/2026-11-09)
---


# Season II countdown

## What this activity is

The Season II globe icon on the base right edge, with a countdown
beneath it ("6d 07:13:29" at read). Tapping it opens the TRANSFER
SURGE page: a cross-warzone transfer window, not a task, a claim or a
reward track. REJECTED as a queue task - no reward, no cost, no
scoring and no recurring action for this account: nothing to claim,
nothing to do on a schedule. What remains is an owner decision, not a
task: whether to apply to transfer to another warzone or stay in
#2110, before the application phase ends. That decision is filed as
GitHub Issue #514 (owner-decision). Executions are recorded in
`_records_/<date>/season-ii-countdown-6d/`, one file per execution.

## How it is done

There is no recurring action. Read-only description of the Transfer
Surge page, for the record:

- Home tab: progress bar, "Application Day 1/4", "11.09--11.13",
  countdown "3d 07:12:52" (read about 10:48 PT). Twelve destination
  warzones, all "Semi-open": #2085 to #2096. Three buttons: "Ideal
  Environment", "Easy Alliance Changes", "Talk and Connect" (not
  tapped - their destinations were not explored).
- Details tab: "Transfer Warzone Group (32)": #2085 to #2116
  including our #2110. Per-warzone cards carry a president power, four
  fill counts, a language, a message and an Apply button. Read live:
  #2085 "Come join my warzone!", 43/60, 39/40, 5/5, 1/1, English,
  "Requirements met"; #2086 "Disneyland of the last war", 19/60,
  36/40, 4/5, 1/1, Arabic, "Requirements met". No Apply button was
  tapped - applying to transfer is an owner decision.
- #2110 Settings tab (our warzone): President [CTR1]HawksMav, fill
  30/60, 29/40, 2/5, 1/1. Incoming applications to #2110: #2097
  ColonelP816, [Crck] Cracken, Power 110,856,819, "No message from
  this person", 2026-11-9 00:08:44; #2103 Airi Lufthansa, [RnR2] Unity
  Sector II, Power 81,142,911, "No message from this person",
  2026-11-9 03:00:59; a third applicant partly visible below. Each
  carries Reject and Accept (x1) buttons. Neither was tapped -
  accepting or rejecting applicants is the president's call, not this
  agent's. A "Transfer Settings" button sits at the bottom (not tapped
  - it could change warzone settings).
- Bottom bar on every tab: "Your Status: Follower", "0/50" with a plus
  button (not tapped, meaning unexplored).

## What is known from 2026-11-09 1044

- Entry: base screen right edge column top to bottom: Events (red dot
  1), VS with timer 07:13:28, then the Season II globe icon with
  "6d 07:13:29" beneath it, then Alliance, Mail, Inventory. The Season
  II countdown and the VS timer share the same clock (07:13:28 vs
  07:13:29, one second apart at screenshot time).
- Base screen read live about 10:46 PT: food 544.5M, iron 871.8M, coin
  46.2M, diamonds 6,077, 13.22K, power 149,217,331, stamina 112. Task
  "Upgrade Builder's Hut to Lv.26 [0/1]". Building queue 1/4, research
  1/2. At exit about 10:54 PT the VS timer read 07:10:43 and the base
  figures were unchanged (coin 46.21M, power 149,217,331, stamina 114).
- Mechanism learned: the Season II HUD countdown is the Transfer Surge
  event timer. The 6d figure is the whole event window; the
  application phase runs 11.09-11.13 (3d 07:12:52 left at read).
- Deadline discrepancy (flagged in the Issue #514 comment for the
  retro to confirm): the issue states the application phase ends
  2026-11-12 18:00 UTC, but the live Home countdown read 3d 07:12:52
  at 2026-11-09 about 18:48 UTC, which implies an end around
  2026-11-13 02:00 UTC - eight hours later, i.e. the game's 11/12
  18:00 is plausibly local (PST) rather than UTC. The owner deadline
  in #514 may be 8 hours early.

## Open questions

- The fourth tab (label starts "Ti", cut off at the right edge) was
  not opened.
- The "0/50" bottom-right figure and the plus button beside it are
  unexplored.
- The three Home buttons (Ideal Environment, Easy Alliance Changes,
  Talk and Connect) were not opened.
- None of these blocks the verdict - none of them is a claim or a
  reward.

## What the 2026-11-09 1044 scout-discovery unit added - Transfer Surge confirmed, candidate rejected, deadline discrepancy flagged

- Unit scout-scout-discovery-2026-11-09-011 by ticker-1038, about
  10:44 to 10:54 local, status done (status unverified on the record:
  the verdict is a reading, not a measured claim). Evidence in
  `_records_/2026-11-09/season-ii-countdown-6d/1044-queue-run.md`
  (commit d630be83 on records/2026-11-09). Exploration only -
  read-only learning, nothing claimed, nothing applied, nothing
  accepted, nothing bought. Session cc-262, windowed 642x951 (window
  489932, titled "Last War").
- This unit is a duplicate exploration of the same candidate: unit 004
  (ticker-0804, record 0812-queue-run.md) had already closed it and
  filed Issue #514, and the pool staged it again after that. The
  duplicate is recorded here and in the #514 comment instead of filing
  a duplicate issue; the stale-pool re-production is tracked in Issue
  #466.
- Result stats: target explain-season-ii-countdown-mechanism, achieved
  1, costs about 11 minutes, resources_gained none, no items spent,
  verified yes (same-unit live reads), blocker_category none.
