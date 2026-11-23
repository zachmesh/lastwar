---
unit: scout-midday-growth-snapshot-2026-11-23-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:48:54Z
expires_at: 2026-11-23T10:58:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot P1 read only never press Upgrade
est_minutes: 6
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot P1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit P1, order 1. Question: What do Total Power and every category read, and what are the builders doing?

Route: Base HUD power figure (top bar), one tap, Power Details panel; swipe the panel up for lower rows; panel X; hammer icon (about 108,200 in the 1920x1080 frame), BUILDING QUEUE panel; panel X (about 612,237).

Read: Total power; every category and sub-row, chevrons expanded; four builder slots with target and time left; hammer count.

Budget: at most 8 steps and 6 minutes. Notes: Never batch-tap near the HUD power figure; do not press Power Up. Screenshot after each scroll. If the panel does not scroll write single screen. Run daily as well as weekly. Record Total Power with the UTC time of the capture, in a fixed state (no troops marching), as the control for the power baseline.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
