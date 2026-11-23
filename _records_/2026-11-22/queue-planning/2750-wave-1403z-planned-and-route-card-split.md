---
title: Queue Planning The 14:03Z Wave Planned And The Route Card Split 2750 2026-11-23
created: 2026-11-23T06:22:00-08:00
modified: 2026-11-23T06:22:00-08:00
level: L0
version: 1.0.0
description: Planner pass at 14:13Z to 14:22Z - the route card trimmed under the hard limit with its table moved to a CSV, plan run for the 14:03Z wave only, the wave units given the coordinator's shape, and sync run after it
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0622-wave-1403z
trigger: coordinator GO at 14:13Z and the commit gate message at 14:14Z
started_at: 2026-11-23T06:09:00-08:00
finished_at: 2026-11-23T06:22:00-08:00
verified: the inbox diffed before and after plan and sync; the pool simulated at 5 and 8 minutes per slow unit; the route card body counted at 207 words; validate exit 0
grounded_in:
  - source: _tools_/queue.py cmd_plan and live_pool_root
  - source: _records_/2026-11-22/resource-collection/1330-queue-run.md
---

# The 14:03Z wave and the route card split, 2750

## 1. Route card

The card was one body word over the hard limit and blocked the commit. It is now 207 body words (stop reasons, the idle-slot stats, a pointer) at version 1.4.0, and the verified route table is [2700-routes.csv](2700-routes.csv), 11 rows with the operator record each came from. The 29 units that point at the card keep working. My other records are at or under 500 body words (the largest, note 2690, is exactly 500).

## 2. Plan and sync

`plan --hours 3` (the default is 12, and a preview on a scratch copy is refused because the tool bans a pool under /tmp) minted 25 units: the 14:03Z window (arms race, building queues, donations, harvest, radar, research, survivors, training; expiry 18:03Z), the 14:30Z group (duel-score, gifts, help, mail, star-ceremony, train; to 18:30Z), the :57 events, passes, secrets, treasures and trucks (the closing 10:57Z set to 14:57Z and the new set to 18:57Z) and the 15:00Z midday scout. It expired the three stale 10:03Z wave units. `sync` then minted and expired nothing. All carry the roster serves upkeep.

## 3. The shape applied

Donations and harvest are priority 1, so on a tie the earlier-minted donations goes first and harvest second. Radar is held to 14:38Z. Briefs added: donations by policy 2532 with the T1 logging; harvest by the measured panel method (442K coin, 675K food, 623K iron an hour); radar with Quick Execute only, no march, energy floor 40, oil counter and the gift box read for the Bingo lines; mail with the Train arrival notice read only; survivors read-only; both secrets units read-only (the next start is the 02:05Z pair); the three queue reads with the exact idle-slot stats. `trucks-2026-11-23-0257` duplicated the 14:20Z settle unit and was closed.

## 4. Order caveat

The queue ranks by expiry, so the earlier closings go first: the 14:30Z claims (help, gifts, train, duel-score) and the :57 units. Simulated at 5 minutes per slow unit, trucks settle runs at about 15:00Z, harvest 15:05Z, donations 15:10Z and radar 15:15Z; dispatching by name puts donations and harvest first. `star-ceremony-0230` expires unrun in both simulations.
