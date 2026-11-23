---
unit: building-queues-2026-11-23-0720
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T07:20:16Z
expires_at: 2026-11-23T10:03:00Z
planned_for:
not_before: 2026-11-23T07:30:00Z
window: builders reread and start idle builder per OD-20261109-02, no diamonds, no Finish Now, no speedup
est_minutes: 10
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T07:35:46Z
lease_until: 2026-11-23T07:55:46Z
result:
  status: done
  started_at: 2026-11-23T07:35:46Z
  finished_at: 2026-11-23T07:37:18Z
  duration_seconds: 92
  executor: operator
  summary: Run 20261123T073552Z-31ee06 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 5 steps): back to the base from the Secret Command Post, hammer 4/4 opened the Building Queue. At 07:36:04Z all four builders busy on Lv.25 Training Base upgrades, time left 1d 01:44:09, 01:44:12, 01:44:15, 01:44:19 (finish 2026-11-24T09:20:13Z, 09:20:16Z, 09:20:19Z, 09:20:23Z); earliest finish 2026-11-24T09:20:13Z. Every slot shows only a Speed Up button, not tapped. No idle builder, so the Builders Hut decision was not reached and nothing was started. Stocks food 638.0M, iron 1.0G, coin 9.6M, diamonds 11,136, unchanged. Banner quest Build: Oil Well (0/1). No account dialog or boarding banner. 5 steps, 7 actions done, 0 refused, 5.6 s model time per step, 0.068898 USD. No takeover. Game on the base, panel closed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2335-queue-run.md and sidecar 2335-queue-run-detail.md; run 20261123T073552Z-31ee06 step 2; panel frame _tools_/state/cu_buildq_2335.png
  follow_up: next builder check at 2026-11-24T09:20Z (earliest finish 09:20:13Z); Builders Hut start only if a builder is freed
  stats:
    target: re-read the builders; start the Builders Hut or top no-diamond upgrade on an idle builder
    achieved: builders re-read: 4 of 4 busy, no idle builder, nothing to start; earliest finish 2026-11-24T09:20:13Z
    resources_gained: none (read-only)
    points: 0
    costs: model 0.068898 USD; nothing spent, nothing started
    verified: yes
    builders_busy: 4
    builders_idle: 0
    upgrades_started: 0
    earliest_finish: 2026-11-24T09:20:13Z
    run_id: 20261123T073552Z-31ee06
    run_steps: 5
    actions_done: 7
    actions_refused: 0
    model_s_per_step: 5.6
    cost_usd: 0.068898
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, coordinator release after the digest amendment, OD-20261109-02)

Re-read the builders first: open the build queue from the hammer icon and record each running upgrade, its level and its time left (building-queues rule digest rule 1). The builders read 4 of 4 busy at 06:51Z, so expect no idle builder; if none is idle, start nothing, record every timer to the second beside the UTC time, name the earliest finish, and stop. That finish time is what the planner needs to schedule the next build unit.

If a builder is idle: the owner decided to start the Builders Hut Lv.25 to Lv.26 upgrade (iron 170M, food 56.9M on the 2026-11-09 read, no diamonds). The standing rule (digest rule 3): when the stocks of food, iron and coin are each at least 3 times the cost, an idle builder starts the highest-power upgrade that needs no diamonds and no speed-up, in the priority HQ, then Builders Hut, then military. Read each candidate's cost and prerequisites on its panel before pressing anything, in that order; start the first one whose three stocks pass the 3 times test and whose button shows no diamond cost; press Upgrade once; re-read the queue and record the new timer and the stock change.

Never press Finish Now, never use a speed-up, never spend diamonds (rule 4), and never use the green up arrow to close a panel (rule 5). If the only available start shows a diamond cost or fails the 3 times test, start nothing and record the numbers.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no identifier values in any record. Any such surface stops the unit as needs-owner.
