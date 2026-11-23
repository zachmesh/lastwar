---
title: Arms race queue run 2019
created: 2026-11-23T04:21:30Z
modified: 2026-11-23T04:21:30Z
version: 1.0.0
description: Arms race unit arms-race-2026-11-22-1803, operator seat, Base Building phase 18,900 of 30,000 read live, earned chests preview-only, nothing claimed
status: run-partial
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T041949Z-d432f7, 2026-11-23T04:19Z to 04:20Z
  - source: final screenshot of the run saved as _tools_/state/cu_armsrace_2019.png, trajectory under /Users/zhenchen/.computer-use/runs/20261123T041949Z-d432f7
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:19:49Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:19:49Z
---

# Arms race queue run 2019

- Executor: operator seat (top-level session), unit arms-race-2026-11-22-1803,
  assignment A-20261123-0419-operator. Token lease 04:34:49Z, claim lease
  04:39:49Z, attempts 1.
- Status: partial. The phase and score were read live. No chest was claimed,
  because none presented as claimable. The 30,000 top chest is not reached.
- Run: `20261123T041949Z-d432f7`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:19:50Z, ended 04:20:23Z with status `completed`. Active
  32.6 s, model time 23.4 s, so 4.68 s of model time per step. Steps 5, actions
  done 12, refused 0, blocked 0, failed 0. Cost 0.068575 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. There was no local-input takeover.
- Live read on the final screenshot (Events hub, Arms Race tab, shown with an
  icon and no title):
  - Phase: Base Building, Contest Segment Lv.29-30.
  - Timer: 01:39:45 remaining, so the phase ends about 06:00Z.
  - Score: 18,900.
  - Point-chest thresholds: 6,250 / 12,500 / 30,000. The ruby tags read
    2,360 / 4,800 / 11,800.
  - The progress bar is past chests 1 and 2. Chest 3 is locked, with a gap of
    11,100.
  - Cumulative counter chest at the top left: 3/8, not full and not bouncing,
    so it was not tapped.
  - Ranking row: own row at rank 7, #2110 [tag]owner account 18,900. The top row
    is #2112 an ally.
  - Scoring rows: Increase Building Power by 1pt (+1). Use 1-min Construction
    Speed-up (+10) and Buy Packs containing Diamonds (+30) are both red lines
    and were not touched.
- Chest tap: one tap on the 6,250 chest opened a contents preview titled
  "Valued: 2,360": Skill Medal x200, Arms Race Badge x1, Coin, Food and Iron
  Chest (SR) x4 each, 5m Speed-up x8. It was dismissed by tapping empty space.
  No claim popup appeared, and no red dot or bounce was on either earned chest.
  Per the profile, a tap on an earned, unclaimed chest claims it, and a tap on
  a claimed chest shows only its contents. So chests 1 and 2 were most likely
  claimed by an earlier unit. That is an inference from the profile rule,
  not a read.
- Not done: no scoring action. The only in-scope path left is a building
  completion (Building Power). The other two scoring rows are red lines. The
  building queue was not read in this unit.
- Red lines: no speedup, no diamonds, no purchase, no pack, no Go button, no
  PvP, no diplomacy. No confirmation dialog appeared.
- Game left on the Events hub, Arms Race tab.
- Follow-up: before the phase ends at about 06:00Z, a building-completion check
  could decide whether tier 3 can be reached inside the red lines. Otherwise
  the phase closes at 18,900 with tier 3 missed.
