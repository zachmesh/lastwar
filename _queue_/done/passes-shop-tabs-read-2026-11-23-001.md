---
unit: passes-shop-tabs-read-2026-11-23-001
regular: passes
activity: shop-claims
segment: 3
priority: 2
created_at: 2026-11-23T15:01:50Z
expires_at: 2026-11-23T17:00:00Z
planned_for:
not_before: 2026-11-23T15:05:00Z
window: read only shop tab row g tab and any hot sale packs tab
est_minutes: 8
serves: snapshot
chain_id: shop-tabs-read-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T16:29:29Z
lease_until: 2026-11-23T16:49:29Z
result:
  status: done
  started_at: 2026-11-23T16:29:29Z
  finished_at: 2026-11-23T16:30:51Z
  duration_seconds: 82
  executor: operator
  summary: Shop tab row read: Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond, Gold Brick Mall (the G tab, a purchase page), Hot Sale Packs (last tab, Packs sold out); nothing tapped but tabs; no other app opened
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1629-queue-run.md and 1629-queue-run.csv; run 20261123T162933Z-9a1415
  follow_up: scribe: update the shop-claims digest (Hot Sale Packs tab exists as the last tab, sold out at 16:30Z; G tab = Gold Brick Mall purchase page); the free pack is not on offer now
  stats:
    target: read the shop tab row, the G tab and any Hot Sale Packs tab
    achieved: 7 tabs named in order, G tab read (Gold Brick Mall), Hot Sale Packs read (sold out), no claim available
    resources_gained: none
    points: 0
    costs: none spent; model 0.084851 USD
    verified: yes
    run_id: 20261123T162933Z-9a1415
    run_steps: 7
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.084851
    device_takeovers: 0
    rules_used: 2,9
  stats_missing: []
  stats_warnings: []
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (planner, READ-ONLY shop tab read after the passes run 1457)

serves: snapshot

The passes run `_records_/2026-11-22/shop-claims/1457-queue-run.md` found the shop's tab row as Official Event | Weekly Deal | Super Monthly Pass | Weekly Pass | Diamond | a cut-off G tab, with NO Hot Sale Packs tab (the name in `_activities_/shop-claims/rule-digest.md` is stale, or the tab moved). Open the shop by the route in the digest and READ ONLY:

1. Drag the tab bar sideways to bring the G tab and anything beyond it into view; write every tab name in order, with the tag text.
2. Open the G tab and any tab named Hot Sale Packs, Hot Deals or similar. For every card write its name, its timer to the second, its price button text, and whether it says Claim, Claimed or Already claimed today. One frame per tab.
3. Press NOTHING that costs, claims or renews: NEVER tap a price button, Renew, Extension, Take All, Get Now or Buy. A green Claim is read, not tapped: the Daily Pickup unit after 02:05Z claims. Close the shop with its X.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number. No purchase or diamond spend. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
