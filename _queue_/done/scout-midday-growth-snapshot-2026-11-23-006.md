---
unit: scout-midday-growth-snapshot-2026-11-23-006
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:03Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot R1 read only never press Upgrade
est_minutes: 7
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 6
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T11:29:14Z
lease_until: 2026-11-23T11:49:14Z
result:
  status: partial
  started_at: 2026-11-23T11:29:14Z
  finished_at: 2026-11-23T11:31:25Z
  duration_seconds: 131
  executor: operator
  summary: R1 read, run 20261123T112935Z-43e7e9 (claude-gateway/claude-sonnet-5-5, 4 steps; claimed 11:29:13Z; token released 11:31Z before the 11:40Z hard stop): research slot 1 Unlock Oil Well Lv.0 00:13:11 left at about 11:29:44Z (frees about 11:42:55Z), slot 2 Defense Training VIII Lv.7 2d 19:49:18; no slot idle; the flask opened the Research Queue panel, which has no route to the TECH hub, so the trees, percents, badges and the Valor Badge balance are unread. Read-only, nothing pressed beyond the flask icon, a row picture and the panel X.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1129-r1-research.md and _records_/2026-11-22/growth/../perception-scout/1129-r1-research.csv; run 20261123T112935Z-43e7e9
  follow_up: read the tech hub trees after the lab frees (about 11:42:55Z) when the flask may open a tree, or locate the Tech Center building; stale hub read 2026-11-11
  stats:
    target: read both research slots and every tech tree with percent and badge
    achieved: both slots read; tech hub trees not reached
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.048347 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T112935Z-43e7e9
    run_steps: 4
    actions_done: 6
    actions_refused: 0
    model_s_per_step: 5.0
    cost_usd: 0.048347
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: No rule gives a route to the TECH hub when the flask opens the queue panel; the panel has no back arrow.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot R1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit R1, order 6. Question: What are the two research slots doing, and how far is each tree?

Route: Flask icon (about 110,262): read the RESEARCH QUEUE panel or the tree that opens; back arrow to the TECH hub; read all tree rows, scroll for the cut-off row.

Read: Slot names, levels, time left; every tree with percent and badge, including Special Forces and Hero.

Budget: at most 7 steps and 7 minutes. Notes: Do not press Complete, Research or Speed Up. Valor Badge balance if the hub shows it. Name each tree as displayed.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
