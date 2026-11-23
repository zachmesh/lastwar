---
unit: daily-missions-2026-11-22-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-22T14:42:18Z
expires_at: 2026-11-24T02:00:00Z
planned_for: 2026-11-23T02:00:00Z
not_before: 2026-11-23T02:00:00Z
window:
est_minutes: 12
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T06:08:31Z
lease_until: 2026-11-23T06:28:31Z
result:
  status: partial
  started_at: 2026-11-23T06:08:31Z
  finished_at: 2026-11-23T06:09:53Z
  duration_seconds: 82
  executor: operator
  summary: Run 20261123T060831Z-e25a07 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 4 steps): the orange terminal opened MISSION on Main Tasks; one tap switched to Daily Tasks. No green Claim button in view and no red badge on the tab, so nothing was claimed. Rows in view all incomplete Go rows untouched: Donate to Alliance Tech 5 times (0/5), Recruit Heroes (0/1), Kill 5 zombies (0/5), Attack a Commander (0/1); a fifth row cut off, rows below the fold unread (list not dragged). Star 110, chests 40 and 80 open, 120 closed (10 points short); Next Refresh 19:51:19. Back arrow returned to the base. No Go, paid-purchase or PvP row touched. 4 steps, 3 actions done, 0 refused, 3.91 s model time per step, 0.058985 USD. No takeover.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/2208-queue-run.md and sidecar 2208-queue-run-detail.md; run 20261123T060831Z-e25a07 step-0001.png, step-0002.png, final frame _tools_/state/cu_missions_2208.png
  follow_up: Donate to Alliance Tech 5 times (0/5) pays 10 points and would take the star to 120 and open the 120 chest; a later pass should drag the list to read rows below the fold
  stats:
    target: claim the free completed daily mission rows and the reachable activity chests
    achieved: nothing claimable in view (no Claim button, no tab badge); star 110, 40 and 80 chests open, 120 closed; rows below the fold unread
    resources_gained: none
    points: 0
    costs: model 0.058985 USD; no diamonds, money or items spent
    verified: yes
    blocker_category: h
    rows_claimed: 0
    chests_claimed: 0
    star_points: 110
    rows_in_view: 4 all incomplete
    rows_below_fold: unread
    run_id: 20261123T060831Z-e25a07
    run_steps: 4
    actions_done: 3
    actions_refused: 0
    model_s_per_step: 3.91
    cost_usd: 0.058985
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
