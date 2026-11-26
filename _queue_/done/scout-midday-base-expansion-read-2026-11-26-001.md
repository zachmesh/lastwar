---
unit: scout-midday-base-expansion-read-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-26T05:08:58Z
expires_at: 2026-11-26T05:11:08Z
planned_for:
not_before: 2026-11-26T05:08:00Z
window: base expansion read, the unmet hq 31 prerequisite (read only, steer a 05:08z)
est_minutes: 8
serves: snapshot
chain_id: base-expansion-read-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-26T05:11:09Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Researcher's note base-expansion-what-it-is.md shows records 1308 and 1410 already hold the requirement (the last node of the Age of Oil tree: coin 174.1M, iron 58.0M, food 58.0M, base 55d 12:47:00) and the preview line is unchanged; a read would repeat them (value rule)
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is a one-off requirement read, NOT the midday scout walk: do only the steps below. Definition folder `_activities_/perception-scout/` (its `rule-digest.md` first).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, BASE EXPANSION READ: what the HQ 31 prerequisite is, Steer A 05:08Z)

serves: snapshot

READ ONLY. The HQ Lv.30 to 31 preview shows 'Lv.1 Base Expansion' unmet (record 1308: a research node, red, button 'Research'); the HQ 31 build cannot start without it.
(1) Open the HQ Upgrade PREVIEW: tag 'Headquarters Lv.30' near (565,405), the radial's green up arrow (662,411) (tap points are hints after version 1.0.366: read the tag first). Write the unmet row's text and its button's label.
(2) STEER A APPROVES ONE PLAIN NAVIGATION TAP on that row's button, ONLY IF its label names the requirement or reads Go or Research and no price, diamond, 'Buy' or 'Speed up' shows on the row: tap it ONCE. It must open the requirement's own panel.
(3) Read that panel by TEXT: its name; what it is (a tech node and under which tree, or a building); its level; its cost (every resource and the time, effective and original); its own prerequisites and their green or red state; whether it can start. NOTHING that starts, upgrades, researches, buys or spends is pressed, including that panel's own Research button. Close by its X or the blue back arrow, twice if needed.
(4) Any diamond price, any Buy or Speed up, any other surface: STOP. Never Obtain or Finish Now. No Lottery tab, avatar, bubble or claim.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the requirement's panel read (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap: 0.60 USD.
