---
title: Arms race queue run 2316
created: 2026-11-23T07:20:00Z
modified: 2026-11-23T07:20:00Z
version: 1.0.0
description: Arms race unit arms-race-2026-11-23-0709, operator seat, Unit Progression phase read live, all three point chests already claimed, top threshold met, nothing to claim or score
status: run-done
grounded_in:
  - source: cu_bridge start, status polls, events and final result on run 20261123T071612Z-d22d83, 2026-11-23T07:16Z to 07:17Z
  - source: frames step-0003 and step-0004 of the run read by the operator, saved as _tools_/state/cu_armsrace_2316.png (untracked)
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T07:16:12Z
  - source: arms-race rule digest, rules 1, 2, 3, 6 and 7
---

# Arms race queue run 2316

- Unit arms-race-2026-11-23-0709, operator seat, assignment A-20261123-0715-operator,
  attempt 1, claimed 07:16:05Z. Rows are in the sidecar
  [2316-queue-run-detail.md](2316-queue-run-detail.md).
- Run `20261123T071612Z-d22d83`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  cap 8 min and 0.5 USD, ended `completed` after 7 steps. Actions done 11, refused 0.
  Model time 5.1 s per step. Cost 0.096741 USD. No takeover.
- Front precondition held. First frame was the base: no account dialog, no boarding
  banner.
- Phase read live: Unit Progression, Contest Segment Lv.29-30, timer 02:43:24, so it ends
  about 10:00Z. Point chests 15,000, 30,000 and 75,000 (ruby values 2,360, 4,800 and
  11,800). The progress bar is full and all three markers are lit.
- Score: the track badge reads 75,000 and the owner account's ranking row, rank 4, reads
  93,900. The row lags the live score (rule 7), so the top threshold is met either way.
- Chests: none bouncing, none with a red dot. One tap on the 75,000 chest opened a
  contents preview "Valued: 11,800" (Skill Medal 1000, Arms Race Badge 3, Coin, Food and
  Iron Chest SR 20 each, 5m Speed-up 40), not a claim popup. So all three were claimed
  earlier, by the profile rule, an inference. Counter chest 9 of 18, not full, not tapped.
- Scoring rows, none tapped: Train a Lv.10 unit +31, Use 1-min Training Speed-up +10
  (a speedup, red line), Buy Packs containing Diamonds +30 (a purchase, red line). With
  the target met, none was needed, so this phase is closed as target met, not as "no safe
  scoring path".
- Outcome: nothing claimable, nothing claimed, 0 points gained this unit. Closing state:
  the base screen.
- Red lines held: no diamonds, no purchase, no speedup, no Go button, no PvP, no
  diplomacy, trophy bubble not tapped. No confirmation dialog appeared.
- Follow-up: the next Arms Race phase starts about 10:03Z. A phase-end check of the
  ranking reward belongs to that unit.
