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
serves: capacity source: Drill Ground lowest first (builders at 2026-11-24T09:20Z)
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

## Brief (planner, conversion-and-spend for the builders, four grounds)

serves: capacity source: Drill Ground lowest first (builders free at 2026-11-24T09:20Z)

Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md` (conversion, speed-up); `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (red lines, snap; write 1.1G as 1100M). Never touch the owner's running queue; never press Obtain, Finish Now or buy.

FOUR Drill Grounds (F1b record `_records_/2026-11-22/growth/1047-f1b-drill-ground.md`), parade fields of red soldiers; tap a soldier in the middle: Lv.26 about (705,690), Lv.28 about (580,800), Lv.30 about (770,940), Lv.27 about (975,845) off-screen right (pan: drag (540,700) to (290,450); fresh = panned + (250,250), 60 px). The orange-roofed building is a Tavern. Lv.28 to 29 is measured: +200, 119.0M coin, 18d 09:21:34. The Lv.26 and Lv.27 previews come from F1c (pasted here when it lands).

1. Hammer icon: COMPLETE any finished upgrade, note idle builders; if none, read the earliest time left with the UTC time and stop.
2. For each idle builder in turn take the lowest ground not upgrading (Lv.26, 27, 28, 30); read its tag and Upgrade preview.
3. Convert exactly its coin, Coin Chests first (281M read; by quantity if offered, else at most 10 and stop). Guide estimates: Lv.26 about 59.5M, Lv.27 about 83.3M; Lv.30 about 178.5M exceeds the read chests and waits. Read coin before and after, press Upgrade once, read the timer. HAZARD: close menus with an empty-ground tap (200,610); never WORLD (660,940) with a menu open low.
4. Speed-up, bounded: after the preview showed the gain, general speed-up items only, at most 10,000 minutes in total, never Finish Now, diamonds or money, none if the 35,000-minute weekly budget is spent. Log minutes and Total Power before and after.
5. Idle builders left: barracks Lv.24 to 27, then Oil Well levels 1 to 9 (food and iron only).

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.

15 minutes, 10 steps. No hero-lever conversion. No chain successor.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
