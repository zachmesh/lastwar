---
unit: donations-tech-pm-2026-11-26-001
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-26T12:13:33Z
expires_at: 2026-11-26T23:50:00Z
planned_for:
not_before: 2026-11-26T21:04:00Z
window: alliance tech donations the second unit (steer a 12:12z)
est_minutes: 8
serves: PL-04
chain_id: tech-pm-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# donations

Serves: PL-04

## Brief (definition pointer, from the roster)

One of the two donation units a day. Definition `_activities_/alliance-donations/` (its `rule-digest.md` and `refill-clock.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, ALLIANCE TECH DONATIONS, Steer A 12:12Z, the second unit)

serves: PL-04

COIN TAPS ONLY: NEVER the diamond donate button, any button with a gem icon or a price. Donate to the recommended tech while the count reads 1 or more: spend the live count down to 5 OR LESS (a grey Donate with a timer means spent). Write the entry time and the count (1 + floor((entry time - last timer end) / 20 min), the refill clock), every tap's time and the first timer. After the last tap CLOSE AND REOPEN THE PANEL (the open dialog does not refresh its bar), then read the Tech EXP bar and the badge (the Quick Construction tech is Lv.9 of 10, the bar 6.3M of 8.0M at 12:32Z on 11-26) and claim the daily donation reward if claimable. A tap costs 1,000 coin.
At max_steps with the count still live and the panel open: close PARTIAL and say so: the Coordinator runs part two (the alliance-donations/1441 precedent, the 1002 and 1010 runs); never close the panel as spent.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken donation or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
