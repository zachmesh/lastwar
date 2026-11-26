---
unit: building-queues-helmet-test-2026-11-26-001
regular: building-queues
activity: building-queues
segment: 2
priority: 1
created_at: 2026-11-26T13:47:38Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T13:55:00Z
window: helmet bubble test, check first then one press (steer a 13:46z)
est_minutes: 15
serves: snapshot
chain_id: helmet-test-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T13:55:42Z
lease_until: 2026-11-26T14:15:42Z
result:
  status: done
  started_at: 2026-11-26T13:55:42Z
  finished_at: 2026-11-26T14:39:37Z
  duration_seconds: 2635
  executor: operator
  summary: Helmet bubble test: a white round helmet bubble over the 13-day ground and the Oil Well only (none over the 7-day or 3-day ground); one press on the 13-day ground's helmet (13:58:22.1Z) brought 30 helps: end 2026-12-10T07:24:19Z to 2026-12-08T09:25:35Z (0.50% of the remaining per help); one press on the Oil Well's helmet (14:24:47.8Z) brought 30 helps: end 2026-11-28T19:37:10Z to 2026-11-28T08:50:14Z (about 0.75% per help); Chrome took the front at 14:02:04.5Z (no person at the Mac): stopped, front script once at 14:19:25Z by Steer A's approval, LastWar back; cost 1.22 against 0.80 disclosed; tram badge 1 from 14:35:16Z, not entered; drags 4. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1356-queue-run.md and 1356-queue-run.csv; run 20261126T135810Z-b03786
  state_change: yes
  follow_up: the tram count badge 1 (a returned truck): the trade unit; the Help page has more rows below the fourth (not scrolled)
  stats:
    target: test the helmet bubble as the help request on the 13-day ground, then the Oil Well
    achieved: both builds helped 30 of 30
    resources_gained: none
    points: 0
    costs: none spent; model 1.22042 USD
    verified: yes
    run_id: 20261126T135810Z-b03786
    run_steps: 104
    actions_done: 70
    actions_refused: 0
    cost_usd: 1.22042
    device_takeovers: 0
    claims: 2
    helps_ground: 30
    helps_oil_well: 30
    pct_per_help_ground: 0.50
    pct_per_help_oil_well: 0.75
    tram_badge: count 1
    over_cap: 1.22 of 0.80
    drags_tried: 4
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
---

# building-queues

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off helmet bubble test, NOT the queue walk. Definition `_activities_/building-queues/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, HELMET BUBBLE TEST H118, Steer A 13:46Z: a check first, then ONE press)

serves: snapshot

STEP 1, READ ONLY: take a 6x crop of the bubbles above the Oil Well and the THREE Drill Grounds (pan once from blank ground, about 175 px, if a ground is out of frame; back by WORLD then BASE) and write for each building whether a white round bubble with a green helmet sits above it. If EITHER of the two OLDER grounds (the 11-29 and 12-03 builds; their Help rows read 30/30) carries a helmet, it is a generic builder mark: DO NOT press; write it and STOP.
STEP 2, only if neither older ground has a helmet: find the 13-day ground (the Lv.28 build ending 2026-12-10T07:24:19Z). Its building tag reads 'Drill Ground Lv.27' with a timer of about 13 days: AT MOST TWO building taps to read tags (Steer A to confirm this lift); if it cannot be told apart, DO NOT press and STOP. Read its end time to the second (the tag timer or the queue row) BEFORE. Press the helmet above it ONCE. Read the end time to the second at +1 and +10 minutes (and +30 if nothing fell), with any help count, and compute k = ln(1 - cut/remaining) / ln 0.995; then open the Help page (Alliance, Help) and write whether a row for that build appeared (n of 30). A dialog with a price, a gem, Speed Up or Upgrade: close it by its X. NEVER the green up arrow, NEVER another bubble: the Oil Well's helmet waits for this result.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the press made or the check read (`--state-change yes` if pressed, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
