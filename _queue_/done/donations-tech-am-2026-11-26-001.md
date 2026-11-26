---
unit: donations-tech-am-2026-11-26-001
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-26T12:13:32Z
expires_at: 2026-11-26T20:56:00Z
planned_for:
not_before: 2026-11-26T12:16:00Z
window: alliance tech donations the first unit (steer a 12:12z)
est_minutes: 8
serves: PL-04
chain_id: tech-am-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T12:32:14Z
lease_until: 2026-11-26T12:52:14Z
result:
  status: done
  started_at: 2026-11-26T12:32:14Z
  finished_at: 2026-11-26T12:35:38Z
  duration_seconds: 204
  executor: operator
  summary: Tech donations: entry 12:32:43.5Z count 21 of 30 on Quick Construction Lv.9 of 10 (coin Donate green, 1000, no timer; Tech EXP 6.3M of 8.0M); 16 coin Donate taps 12:32:48.8Z to 12:33:54.6Z took the count to 5 of 30 at 12:34:04.2Z (coin Donate still green, no timer: the floor of 5); the Tech EXP bar read 6.3M of 8.0M after (the open dialog did not refresh); coin 16.0M to 15.9M; the diamond Donate never pressed; no daily reward claimable; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/1232-queue-run.md and 1232-queue-run.csv; run 20261126T123214Z-f7e4d9
  state_change: yes
  follow_up: the count refills one per 20 minutes (5 of 30 left); the Tech EXP bar re-read after a reopen
  stats:
    target: spend the live donation count down to 5 or less with coin
    achieved: 21 to 5 of 30 by 16 taps
    resources_gained: none
    points: 0
    costs: none spent; model 0.23985 USD
    verified: yes
    run_id: 20261126T123214Z-f7e4d9
    run_steps: 17
    actions_done: 25
    actions_refused: 0
    cost_usd: 0.23985
    device_takeovers: 0
    claims: 16
    entry_count: 21
    final_count: 5
    taps: 16
    exp_before: 6.3M
    exp_after: 6.3M
    tram_badge: none
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# donations

Serves: PL-04

## Brief (definition pointer, from the roster)

One of the two donation units a day. Definition `_activities_/alliance-donations/` (its `rule-digest.md` and `refill-clock.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, ALLIANCE TECH DONATIONS, Steer A 12:12Z, the first unit)

serves: PL-04

COIN TAPS ONLY: NEVER the diamond donate button, any button with a gem icon or a price. Donate to the recommended tech while the count reads 1 or more: spend the live count down to 5 OR LESS (a grey Donate with a timer means spent). Write the entry time and the count (1 + floor((entry time - last timer end) / 20 min), the refill clock), every tap's time and the first timer. After the last tap read the Tech EXP bar and the badge (the Quick Construction tech is Lv.9 of 10, the bar 5.5M of 8.0M before) and claim the daily donation reward if claimable. A tap costs 1,000 coin.
At max_steps with the count still live and the panel open: close PARTIAL and say so: the Coordinator runs part two (the alliance-donations/1441 precedent, the 1002 and 1010 runs); never close the panel as spent.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken donation or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
