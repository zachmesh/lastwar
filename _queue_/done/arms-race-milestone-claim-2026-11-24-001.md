---
unit: arms-race-milestone-claim-2026-11-24-001
regular: arms-race
activity: arms-race
segment: 2
priority: 2
created_at: 2026-11-24T15:25:17Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T15:33:00Z
window: read the arms race milestones and claim the free ones held for steer a
est_minutes: 5
serves: upkeep
chain_id: milestone-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T15:48:18Z
lease_until: 2026-11-24T16:08:18Z
result:
  status: done
  started_at: 2026-11-24T15:48:18Z
  finished_at: 2026-11-24T15:51:40Z
  duration_seconds: 202
  executor: operator
  summary: Arms Race ladder read (Drone Boost, 02:09:18 left, 4,000 points, rank 12): the 1,500 chest is reached but, like the 10,000 and 30,000 chests, carries a ruby price tag with no plain Claim: nothing free to claim, nothing pressed; tram badge 1 at 15:48:25Z, 15:50:18Z and 15:50:57Z; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/event-claims/1548-queue-run.md and 1548-queue-run.csv; run 20261124T155014Z-2b2127
  follow_up: the chests are offered for rubies; whether the 1,500 chest pays by mail at the phase end is unread; the tram badge 1 awaits cycle B
  stats:
    target: claim each claimable free milestone
    achieved: no free milestone claim exists
    resources_gained: none
    points: 0
    costs: none spent; model 0.174777 USD
    verified: yes
    run_id: 20261124T155014Z-2b2127
    run_steps: 13
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.174777
    device_takeovers: 0
    claims: 0
    arms_race_points: 4000
    tram_badge: 1
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# arms-race

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `arms-race`: Arms Race - read the phase and score; meet the live target; claim all earned rewards, not only the three point chests; return to the Events screen for a final sweep and claim any bouncing chest or reward red dot. Its definition is the activity folder `_activities_/arms-race/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE ARMS RACE MILESTONES: read, then claim the free ones, WAITING FOR STEER A)

serves: upkeep

Steer A approved this unit 15:32Z (points from free actions only; no resource or speed-up spent to score).
Record `_records_/2026-11-22/event-claims/1512-queue-run.md`: the Arms Race shows 4,000 points, the tab dot RED and the 1,500 milestone passed; claimability unread. The digest: claim all earned chests in one visit, leave no red dot; never spend diamonds or money, burn speed-ups, swap stages or start research or building. 5 steps:
(1) Open the Arms Race (verify the title by a frame); read the phase, its timer and the milestone ladder: write which milestones are claimable (the red dot), each reward by NAME AND QUANTITY and any price line.
(2) For each claimable milestone whose Claim reads a plain CLAIM with NO diamond, gem, price, Buy, Purchase, Unlock or Upgrade line: tap it ONCE; read what it paid and the points after; re-check the dot.
(3) Anything that costs, or a milestone needing points the unit would have to buy: press nothing and record it.
(4) A price line, diamond spend, real-money line or app store sheet: STOP. Any other element: touch nothing, take the frame, stop, tell the Coordinator.
Verify each HUD icon by its label or glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
