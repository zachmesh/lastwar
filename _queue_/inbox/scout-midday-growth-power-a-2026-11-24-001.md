---
unit: scout-midday-growth-power-a-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:53:17Z
expires_at: 2026-11-24T04:00:00Z
planned_for:
not_before: 2026-11-24T02:00:00Z
window: fixed state power baseline slot A read only
est_minutes: 10
serves: PL-07
chain_id: growth-power-a-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, fixed-state power baseline slot A, strategy v1.4)

serves: PL-07

Read-only unit for the coach, window 02:00Z to 04:00Z. Rules and red lines: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` and stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; never press Power Up, Train, requeue, Claim or Complete.

COLLECT FIRST, because troops count only when collected. Read Total Power on the HUD with its decimals. Collect every finished barracks batch (tap its bubble or tent); read Total Power after each. Do NOT press the Hospital Collect in slot A: it is all-or-nothing (it needs at least 5,306 free slots at once) and slot B makes the one read per day. The green arrow on a barracks is the building Upgrade: never press it. Collecting is the only exception to R1.

Then open Power Details: tap the HUD figure once, expand every chevron, swipe up with a screenshot after each scroll, close with X. Record Total Power and EVERY category and sub-row including tech and troop, the UTC time to the second, and whether troops are marching or wounded.

Run `python3 _tools_/resource_map.py snap total_power=<n> power_hero=<n> power_drone=<n> power_building=<n> power_tech=<n> power_troop=<n> food=<n> iron=<n> coin=<n> --note <this unit id>`, adding a pair for any other category. K or M numbers only: write 1.1G as 1100M. The power_* keys print an unknown-resource warning but are saved.

Slot A, 2026-11-24: the Lv.27 T9 x726 batch finished about 19:56Z on 2026-11-23; collect it and log the exact power change. The Lv.30 T10 x793 batch is due about 11:18Z on 2026-11-24, which slot B collects.

At most 8 steps and 10 minutes. Do not enqueue a chain successor.

Barracks taps (base map `_records_/2026-11-22/growth/1030-base-map.md`, fresh frame): Lv.27 (462,585), Lv.30 (530,637), Lv.24 (628,562), Lv.20 (668,535); the pistol is the middle button under the tag; a portrait bubble may be the Hospital. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
