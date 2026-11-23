---
unit: research-age-of-oil-survey-2026-11-23-001
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T12:46:05Z
expires_at: 2026-11-23T14:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: age of oil research tree survey read only press nothing
est_minutes: 10
serves: baseline Age of Oil research tree
chain_id: age-of-oil-survey-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T12:56:32Z
lease_until: 2026-11-23T13:16:32Z
result:
  status: partial
  started_at: 2026-11-23T12:56:32Z
  finished_at: 2026-11-23T12:58:45Z
  duration_seconds: 133
  executor: operator
  summary: Age of Oil survey, run 20261123T125632Z-f6b90b (claude-gateway/claude-sonnet-5-5, 4 steps; claimed 12:56:32Z): no different-device dialog at the no-click first frame; both labs busy (slot 1 Food Output V Lv.0 1d 04:33:08, slot 2 Coin Output V Lv.0 1d 02:02:20 at about 12:56:50Z; Defense Training VIII no longer queued); the flask opens only the Research Queue list when both labs are busy, so no tech hub, tree or node panel and no research speed percent was reachable; nothing pressed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/research-queue/1257-age-of-oil-survey.md and 1257-age-of-oil-survey.csv; run 20261123T125632Z-f6b90b
  follow_up: read the trees when a lab idles (first about 2026-11-24T14:59Z) or locate the Tech Center building and read the hub from its radial menu; the Age of Oil nodes Food Output V and Coin Output V are already running
  stats:
    target: read every node of the Age of Oil path and the research speed percent
    achieved: queue state read; trees not reachable
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.096753 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T125632Z-f6b90b
    run_steps: 4
    actions_done: 3
    actions_refused: 0
    model_s_per_step: 7.0
    cost_usd: 0.096753
    device_takeovers: 0
    rules_used: R1
    rule_failed: none
    rule_gap: No rule gives a route to the tech trees when both labs are busy; the Tech Center building is unlocated.
  stats_missing: []
  stats_warnings: []
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: baseline Age of Oil research tree

## Brief (planner, Age of Oil research tree survey, OD-18 and OD-19 and Steer A's oil analyst, read-only)

serves: baseline Age of Oil research tree

Analyst figures [G] until read: the Base Expansion path is 19 nodes, 4.08M oil, 618M iron, 618M food, 1.83B coin, about 942 lab-days of BASE time, serial. LAB TIME BINDS, not oil; the finish depends on the research speed percent. The Strategist picks the first node from this read (`_records_/retro/owner-decisions-log/od-20261123-19.md`).

1. FIRST read the account's RESEARCH SPEED percent and any research-speed bonus line (the Tech hub, a research panel or the Commander screen): say where it was found; tag text beside the number.
2. Flask icon (the Tech hub). Open the tree that holds 'Unlock Oil Well'. Read the Age of Oil path node by node, one panel at a time: tag text, level n/max, effect, coin, iron, food and OIL cost, the BASE (original) time and the EFFECTIVE time, prerequisite (met or not), power gain if shown. These nodes must be covered: Oil Output I level 1, Coin Output, Iron Output, Food Output V, Fast Builder V, Research Enhancement V, More Oil Wells, the Third Tech Center node, Parts Workshop, Oil Output II and III, Base Expansion.
3. Write the dependency order as a list (which node unlocks which) and mark which nodes can run in parallel on two labs, as the prerequisites decide.
4. Read the oil held (434K at the last read) and whether the Oil Well shows a stock or output figure.
5. Press NOTHING that starts, speeds up or completes (no Research, Speed Up, Complete, Obtain). Close panels with their X, a base menu with an empty-ground tap such as (200,610); never tap WORLD (660,940) with a menu open low. A TIPS dialog about another device: STOP, report, never Confirm.

The Special Forces, Economy tail and Development tail reads were partial: continue only where they touch the Age of Oil path. Up to three runs, 10 steps each, split by tree rows. One row per node with its tag text and frame time; tag text beside every number, none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
