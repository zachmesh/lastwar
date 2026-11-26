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
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
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
