---
unit: scout-midday-builders-read-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-26T04:45:41Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T04:45:00Z
window: builders read, price the hospital and hq upgrade previews for the free builder (read only)
est_minutes: 6
serves: PL-08
chain_id: builders-read-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T04:53:44Z
lease_until: 2026-11-26T05:13:44Z
result:
  status: done
  started_at: 2026-11-26T04:53:44Z
  finished_at: 2026-11-26T05:02:22Z
  duration_seconds: 518
  executor: operator
  summary: Builders read (read only): Oil Well Lv.25 ends ~13:09:56Z, one builder idle, labs Defense Training VIII ~11-29T12:38Z and Oil Output I ~11-27T23:20Z; Hospital Lv.25 to 26 preview: power +23,200, food 255.0M and coin 68.8M needed (red), effective 10d 19:49:37; HQ Lv.30 to 31 preview: power 388,300 to 452,000, Lv.1 Base Expansion unmet, oil 1.2M, iron 1.3G, food 1.3G, coin 433.5M all red, effective 52d 14:17:16; nothing upgraded; a Barracks tag opened by a wrong tent tap (closed, nothing pressed); cost 0.67 USD over the cap 0.35; drags 2. state_change: no. state_read: Hospital Lv.25 to 26 preview: food 171.3M of 255.0M and coin 4.4M of 68.8M red, power 120,900 to 144,100; HQ Lv.30 to 31 preview read; builder row 3 idle | step 7 | 04:56:10Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0453-queue-run.md and 0453-queue-run.csv; run 20261126T045344Z-eb2ffb
  state_read: Hospital Lv.25 to 26 preview: food 171.3M of 255.0M and coin 4.4M of 68.8M red, power 120,900 to 144,100; HQ Lv.30 to 31 preview read; builder row 3 idle | step 7 | 04:56:10Z
  state_change: no
  follow_up: the idle builder has no affordable candidate: coin 4.4M is short of the Hospital's 68.8M and the HQ's 433.5M
  stats:
    target: price the candidates for the free builder
    achieved: both previews read
    resources_gained: none
    points: 0
    costs: none spent; model 0.67027 USD
    verified: yes
    run_id: 20261126T045344Z-eb2ffb
    run_steps: 53
    actions_done: 27
    actions_refused: 0
    cost_usd: 0.67027
    device_takeovers: 0
    claims: 0
    hospital_power_gain: 23200
    hq_power_gain: 63700
    slots_idle: 1
    tram_badge: not read
    drags_tried: 2
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is a one-off builders read, NOT the midday scout walk: do only the steps below. Definition folder `_activities_/perception-scout/` (its `rule-digest.md` first).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, BUILDERS READ: price the candidates for the free builder, PL-08)

serves: PL-08

Coordinator 04:47Z. READ ONLY: no Upgrade is pressed, no chest is used, no speed-up, no claim. HUD 04:41Z: coin 2.7M; one builder idle.
(1) The hammer panel: write every row (building, level, time left), the idle row and both labs' timers to the second.
(2) HOSPITAL Lv.26 (the Main Tasks row; tag Lv.25 to 26): tent E about (678,510) in a fresh frame (a portrait bubble may be the Hospital: read its tag). The tag's green up arrow opens the Upgrade PREVIEW: write the level step, EVERY cost row (coin, iron, food, oil, any other) with its red or green state, the effective and original time, the power gain and the capacity a Hospital level adds if shown. Close it by its X or the blue back arrow: NEVER the panel's own Upgrade button.
(3) HQ: tag 'Headquarters Lv.30' near (565,405), the radial's green up arrow (662,411): the Lv.30 to 31 preview, the same rows, the unmet prerequisite and the oil gate. The cost list scrolls by ONE drag from the left of a row: check after it.
(4) BUILDER'S HUT Lv.26: only if a Hut tag is ALREADY one tap from a building in the frames taken (it is unlocated: NO search): read the tag, then its panel text. STATE FIRST: what the phone already started is read, not repeated: a verified nothing-to-do (`state_read:` line).
Hazards: (400,640) after a camera shift selects a Barracks, (200,610) is a Gold Mine Lv.28; never Obtain; the Finish Now diamond figure is only READ. Tap points are hints: verify the label first; a screen that differs: STOP. No Lottery tab, avatar, bubble or claim.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for both previews read (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap: 0.35 USD.
