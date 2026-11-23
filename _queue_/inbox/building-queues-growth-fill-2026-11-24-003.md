---
unit: building-queues-growth-fill-2026-11-24-003
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T07:55:31Z
expires_at: 2026-11-24T09:55:00Z
planned_for:
not_before: 2026-11-24T09:40:00Z
window: growth read then fill idle slots window 11-24T09:40Z
est_minutes: 10
serves: fill idle slot
chain_id: growth-fill-2026-11-24
chain_seq: 3
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth read-then-fill, decision record 2350)

serves: fill idle slot

Read-then-fill under `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Read the builders (hammer icon), then the labs (flask icon), then the training queues. Fill ONLY idle slots. Each start costs at most one third of EACH needed stock AND leaves the RESERVES: food 100M, iron 150M, coin 10M, diamonds untouched, and the duel-day reservation (not quantified in the decision record; the coordinator names it per day). Never cancel, replace or reorder a running item. Never use a speed-up, Finish Now, purchase or diamond spend.

BUILDER PRIORITY when a builder is idle (strategy v1.4): the Drill Ground, lowest first; then barracks Lv.24 to 27, and Lv.30 only for tier unlocks; then OIL WELL levels 1 to 9 (food and iron only, no coin; the well appears after 'Unlock Oil Well'); collect the oil twice a day (12-hour storage cap). Age of Oil and HQ 31 stay OFF. LABS: one lab on Special Forces VIII or IX; the other on Drill Ground Expansion, then Extra Barracks (only if fewer than four barracks), then Coin Output V (raises coin income), then Garage 1 and the Alliance Duel tree. The labs today are Unlock Oil Well and Defense Training VIII, not Special Forces: never cancel a running one. TRAIN: keep every queue full at its top tier from surplus stock, Drill Ground capacity permitting.

PRESS COMPLETE the moment a research or a build finishes: a finished research neither banks its power nor frees the lab until Complete is pressed (the lab 'Unlock Oil Well' frees about 11:43Z on 2026-11-23, which the 11:35Z to 12:20Z fill series covers). Collect every finished troop batch (tap the barracks bubble) before requeueing; power registers only on collection.

Every unit that reads the HUD runs `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>`. The tool reads only plain numbers with a K or M suffix: write 1.1G as 1100M and 732.3M as 732.3M, because a G suffix crashes it with a ValueError. An idle slot at the read is a MISS: record it with the slot and the time. Run one growth unit at a time; do not stack two. Do not enqueue a chain successor; the planner owns this chain.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.
