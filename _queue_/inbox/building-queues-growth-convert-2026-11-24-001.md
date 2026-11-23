---
unit: building-queues-growth-convert-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T08:27:06Z
expires_at: 2026-11-24T09:50:00Z
planned_for:
not_before: 2026-11-24T09:22:00Z
window: convert coin, start the lowest Drill Ground and apply bounded speed-ups when the builders free
est_minutes: 15
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: Drill Ground lowest first (builders at 2026-11-24T09:20Z)

## Brief (planner, builders at 09:20Z, funding (a) and steps 1 and 2 of 3, decision 2603)

serves: PL-08

Decision `_records_/2026-11-22/team-operations/2603-first-builder-decision.md` (Strategist veto until 20:00Z today; a veto note here governs). Plan, tap points, previews, hazards: `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`; conversion procedure: `_records_/2026-11-22/queue-planning/2541-conversion-and-speedup-sheet.md`; follow both. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`, `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. The owner plays by hand: start only on IDLE builders, never touch his queue; never press Obtain, Finish Now or buy.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

Run 1, first the finished upgrades: hammer icon; press the button each finished Training Base entry shows, Complete or Collect (verb unverified [G], record its text; never Speed Up or Finish Now); Total Power before and after, since power registers only on Complete; note idle builders, or if none read the earliest time left and stop. Then the conversion: read coin. Inventory, Resources tab: select the Coin Chest UR (87 owned). N = ceil((142.8M + 10M - coin now) / 2.4364M) (from 9.8M that is 59, from 12M 58, from 0.2M 63; if N is 0 or less, skip). Set the field to N with the handle or minus, read the field AND the Total line in a frame, and before Use check the Total line is at least 142.8M + 10M - coin now. If N would exceed 87, STOP and record. Use once. Read coin.

Run 2, the starts: first idle builder, the Lv.26 ground (59.5M coin, 74.8M iron): read its tag and Upgrade preview, press Upgrade once, read the timer. Next idle builder, the Lv.27 ground (83.3M, 102.0M) the same way. Coin should then read about 15M. Speed-ups are unit 003's job.

Tag text: write each building-panel number's tag text beside it (name and level above the building; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]; add a tag_text column.

Two runs, 10 steps each. No hero-lever conversion. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
