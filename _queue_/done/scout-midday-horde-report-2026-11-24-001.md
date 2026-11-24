---
unit: scout-midday-horde-report-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T04:37:41Z
expires_at: 2026-11-24T07:50:00Z
planned_for:
not_before: 2026-11-24T04:45:00Z
window: read only the zombie horde battle report the loss split the rewards and the schedule
est_minutes: 10
serves: PL-07
chain_id: horde-report-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T04:47:56Z
lease_until: 2026-11-24T05:07:56Z
result:
  status: done
  started_at: 2026-11-24T04:47:56Z
  finished_at: 2026-11-24T04:53:02Z
  duration_seconds: 306
  executor: operator
  summary: The Lv.20 Zombie Horde report (2026-11-23 17:47:43): owner victory, owner side -4,953 (squads 2,247, 2,175, 2,145 lost 1,036, 1,772, 2,145), horde -6,300; no wounded or dead split, no rewards section, no schedule; six horde reports Lv.15 to Lv.20 all Victory; Zombie Siege next auto-search 2026-11-26 23:15 server time
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0447-queue-run.md and 0447-queue-run.csv; run 20261124T044756Z-1f23ed
  follow_up: the loss split (wounded against dead) is not on the report: the Hospital's +1,000 wounded is the only split; no rewards are shown on the report
  stats:
    target: read the horde report below the fold: loss split, rewards, schedule
    achieved: report read to its end, answers 'not shown' where absent
    resources_gained: none
    points: 0
    costs: none spent; model 0.455 USD
    verified: yes
    run_id: 20261124T044756Z-1f23ed
    run_steps: 35
    actions_done: 48
    actions_refused: 0
    cost_usd: 0.455
    device_takeovers: 0
    owner_loss: 4953
    horde_loss: 6300
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-07

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the Lv.20 Zombie Horde attack on the base, the Battle Report, Steer A)

serves: PL-07

Record `_records_/2026-11-22/perception-scout/0412-queue-run.md` found the report under the mail Reports list: a Lv.20 Zombie Horde battle report listed 2026-11-23 17:47:43 (about 01:47:43Z): owner victory, owner side -4,953 (squads of 2,247, 2,175 and 2,145 lost 1,036, 1,772 and 2,145 at the summary), horde -6,300. The loss split and rewards sit BELOW THE FOLD: that run did not scroll. 12 steps at most; PRESS NOTHING but the report, its scroll and the dialog answer below.

1. LOSS SPLIT: per squad, wounded, dead, and returned or healed by the game if the panel shows it.
2. REWARDS: items, shards and resources with counts, below the fold; never Claim.
3. SCHEDULE: is the horde attack a recurring base-defence event: server time, how often, whether the base defends by itself (the Zombie Siege page's text, a countdown, the cooldown to 11-26)? Write each [M] with its tag text and the UTC time; none shown: 'not shown'.

NEVER Claim, Heal, Collect, send, start, schedule or cancel. THE TIPS DIALOG 'Enable notifications and never miss important messages again.' (Cancel and Enable Now) may show again: take a frame, identify Cancel BY ITS TEXT, tap Cancel ONCE; never Enable Now; any other unrecognised dialog: stop. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.
Tag text beside every number; none means [G].
Cost cap, stated: 0.50 USD.
