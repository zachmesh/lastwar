---
unit: scout-midday-growth-snapshot-2026-11-23-004
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:48:59Z
expires_at: 2026-11-23T08:42:00Z
planned_for:
not_before: 2026-11-23T08:00:00Z
window: growth snapshot T1 read only never press Upgrade
est_minutes: 10
chain_id: growth-snapshot-2026-11-23
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T08:06:04Z
lease_until: 2026-11-23T08:26:04Z
result:
  status: done
  started_at: 2026-11-23T08:06:04Z
  finished_at: 2026-11-23T08:07:54Z
  duration_seconds: 110
  executor: operator
  summary: Run 20261123T080610Z-7faa88 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 6 steps), read-only. Barracks Lv.30 busy: Lv.10 x793, Training in progress 1d 03:12:00 at 08:06:31Z (ends about 2026-11-24T11:18:31Z); Power 1647, Morale 750.0, Squad Load 2200, HP 4779.05, Attack 38.87, Defense 7.96. Barracks Lv.27 busy: Lv.9 x726, 11:49:49 at 08:06:45Z (ends about 19:56:34Z); Power 1352, Morale 625.0, Load 2000, HP 4167.45, Attack 33.87, Defense 6.96, Lv.10 locked. Tier counts Lv.7 1,116, Lv.8 2,141, Lv.9 1,878, Lv.10 35.1K, Lv.6 cut off. Only Speed Up shown, not tapped; no slider, cost or Train on a busy barracks. HUD before and after identical: food 638.0M, iron 1.0G, coin 9.6M, diamonds 11,136, Total Power 150,211,809; snapshot taken. No account dialog or boarding banner. 6 steps, 12 actions done, 0 refused, 4.9 s model time per step, 0.078709 USD. No takeover. Game on the base.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0006-queue-run.md and sidecar 0006-queue-run-detail.md; run 20261123T080610Z-7faa88; frame _tools_/state/cu_growth_snap_0006.png
  follow_up: Lv.27 batch ends about 19:56Z, Lv.30 batch about 2026-11-24T11:18Z; batch cost and slider cap unread until a barracks is idle with Drill Ground room
  stats:
    target: read Lv.30 and Lv.27 barracks: tier counts, six unit stats, batch, busy or idle (T1, order 4)
    achieved: both read: busy, six stats and tier counts recorded; batch cost and slider cap not shown on a busy barracks
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.078709 USD; nothing spent, nothing pressed
    verified: yes
    surfaces_walked: 2
    items_observed: 22
    barracks_read: 2
    barracks_busy: 2
    run_id: 20261123T080610Z-7faa88
    run_steps: 6
    actions_done: 12
    actions_refused: 0
    model_s_per_step: 4.9
    cost_usd: 0.078709
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot T1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit T1, order 4. Question: What do the Lv.30 and Lv.27 barracks hold: tier counts, unit stats, batch cap, busy or idle?

Route: Re-ground the tents fresh in this view; tap body, read label, pistol button opens TRAIN UNITS; read; panel X; second barracks the same way.

Read: Tier counts, slider cap, Power, Morale, Load, HP, Attack, Defense, Training in progress line and time, batch cost.

Budget: at most 8 steps and 10 minutes. Notes: Never press Train or Finish Now. Run right after the regular training unit so no finished batch is waiting; a Training complete toast ends the unit, log count and power change. Tent taps often miss, S6 applies. Run right after the regular training work so no finished batch is waiting; a Training complete toast ends the unit, log count and power change.

Stop rules from `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`: S1 never press Upgrade, Finish Now, Speed Up, Construct, Research, Train, Hire, Complete, Claim, Quick Dispatch, Promote or Equip. S2 read a diamond or price figure, never tap it. S3 stop at any march, attack, rally, Arena or PvP surface. S4 close any Confirm dialog with Cancel or X. S5 close a preview only by X or left-edge swipe-back, never a low tap (one once hit Upgrade, +14,800 power). S6 two failed taps on one target end the unit as partial. S7 no owner name or ID; skip profile and ranking screens.

If this unit reads the HUD, run `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>`. The tool reads only plain numbers with a K or M suffix: write 1.1G as 1100M and 732.3M as 732.3M, because a G suffix crashes it with a ValueError. Do not enqueue a chain successor; the planner owns this chain.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.
