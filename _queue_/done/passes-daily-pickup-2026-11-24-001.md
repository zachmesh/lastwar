---
unit: passes-daily-pickup-2026-11-24-001
regular: passes
activity: shop-claims
segment: 3
priority: 2
created_at: 2026-11-23T15:01:51Z
expires_at: 2026-11-24T06:00:00Z
planned_for:
not_before: 2026-11-24T02:05:00Z
window: claim the two weekly pass daily pickups after the reset
est_minutes: 6
serves: PL-05
chain_id: daily-pickup-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T05:00:22Z
lease_until: 2026-11-24T05:20:22Z
result:
  status: partial
  started_at: 2026-11-24T05:00:22Z
  finished_at: 2026-11-24T05:02:07Z
  duration_seconds: 105
  executor: operator
  summary: Closed blocked by route: Claim clipped: the S1 Drone Parts Daily Pickup Claim is cut off at the bottom edge of the shop page, a drag up did not move the page and two taps changed nothing; Free Supply Claimed, S2 pickup already claimed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/0500-queue-run.md and 0500-queue-run.csv; run 20261124T050022Z-35c40a
  follow_up: the S1 Drone Parts pickup stays unclaimed until the page can scroll (planner)
  stats:
    target: claim the S1 and S2 Daily Pickups after the reset
    achieved: S2 and Free Supply done earlier; S1 blocked by route
    resources_gained: none
    points: 0
    costs: none spent; model 0.13288 USD
    verified: yes
    run_id: 20261124T050022Z-35c40a
    run_steps: 11
    actions_done: 10
    actions_refused: 0
    cost_usd: 0.13288
    device_takeovers: 0
    blocker_category: f missing precondition (blocked by route: Claim clipped)
    rules_used: 1,2,3,6
  stats_missing: []
  stats_warnings: []
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, the two Daily Pickups after the 02:00Z reset)

serves: PL-05

The weekly cards S2 Drone Components and S1 Drone Parts are OWNED (`_records_/2026-11-22/shop-claims/1457-queue-run.md`: 'Already claimed today' on 2026-11-23, remaining to 2026-11-30 02:00Z), so each has a Daily Pickup that should be claimable after the reset at 02:00Z. Open the shop and the Weekly Pass tab ONLY (record 1629: seven tabs; the G tab is the GOLD BRICK MALL, a purchase page, NEVER tapped; skip Hot Sale Packs until it shows a pack) and read both cards. If a card shows a green Claim, tap it ONCE, read the popup (the items gained) and then the button: Claimed means it landed, a still-green Claim means it did not. Also read Free Supply (it usually auto-claims). Free items and owned pass gifts only: NEVER a price button, Renew, Extension or Take All. NEVER click Go on the check-in banner: it opens the web store. If no Claim shows, write the card states and timers and stop. Digest: `_activities_/shop-claims/rule-digest.md` (its tab name and rule 3 are stale as of 2026-11-23).

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number. No purchase or diamond spend. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
A Claim CLIPPED at the page bottom (the S1 Drone Parts Claim: four taps, no effect, reported by the passes unit on 2026-11-24): drag UP once from mid-page, check the frame, then tap; stop after two failed taps and write 'blocked by route: Claim clipped'.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
