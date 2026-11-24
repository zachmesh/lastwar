---
unit: scout-midday-siege-report-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T02:31:44Z
expires_at: 2026-11-24T07:50:00Z
planned_for:
not_before: 2026-11-24T02:45:00Z
window: read only the zombie siege report for the 2315 search
est_minutes: 12
serves: PL-07
chain_id: siege-report-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-07

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the Zombie Siege report for the 23:15 server-time search, Steer A)

serves: PL-07

Question: what did the search that ran at 01:15Z send, lose and win? Records `_records_/2026-11-22/perception-scout/0052-queue-run.md` and `_records_/2026-11-22/building-queues/0205-queue-run.md` read the Zombie Siege page (Enemy Power 30.2M, Lv.10 stronghold, cooldown to 11-26 00:00 server time).

Read, one frame per page, 12 steps at most:
1. The mail (Reports or System tab): a Zombie Siege or Stronghold report from about 01:15Z: troops sent, casualties wounded and dead, the REWARDS (items, shards, resources, with counts) and the result text.
2. The Zombie Siege page: any reward or history area, and the cooldown text.
3. Write every figure with its tag text and the UTC time; none found: 'not found' and the pages read.

READ ONLY: press nothing that claims, sends, starts, schedules or cancels (no Cancel Schedule, no new search, no Claim). May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.
Tag text beside every number; none means [G].
Cost cap, stated: 0.50 USD.
