---
unit: scout-midday-growth-snapshot-2026-11-23-003
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:48:57Z
expires_at: 2026-11-23T08:44:00Z
planned_for:
not_before: 2026-11-23T08:00:00Z
window: growth snapshot F1 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T08:35:30Z
lease_until: 2026-11-23T08:55:30Z
result:
  status: done
  started_at: 2026-11-23T08:35:30Z
  finished_at: 2026-11-23T08:37:10Z
  duration_seconds: 100
  executor: operator
  summary: Run 20261123T083521Z-a5a70f (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 6 steps), read-only; started 08:35:22Z, claim landed 08:35:30Z after the claim gate asked for a read receipt. Drill Ground Lv.28 to 29: Unit Count +7,600 to +7,800 (+200 per level), Power 165,800 to 196,200, coin 9.6M of 119.0M (short), iron 1.0G of 144.5M (met), prerequisite Lv.29 Headquarters met, original 39d 01:53:19, Upgrade 18d 09:21:34, Finish Now 228,514 diamonds. Headquarters Lv.30 to 31: Power 388,300 to 452,000, Hero Level Cap 150 to 155, Hero HP +15,000 to +16,000, Hero Attack +714.3 to +761.9, prerequisite Lv.1 Base Expansion not met (Research), oil 434,160 of 1.2M, iron 1.0G of 1.3G, original 111d 18:21:40, Upgrade 52d 14:17:16, Finish Now 1,850,185 diamonds; a Hero Defense row and a fourth cost row were cut off. Nothing pressed; panels closed with their X. 6 steps, 12 actions done, 0 refused, 6.5 s model time per step, 0.073632 USD. No takeover. Game on the base, no radial menu.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0035-queue-run.md and sidecar 0035-queue-run-detail.md; run 20261123T083521Z-a5a70f; frames _tools_/state/cu_growth_f1_dg_0035.png and cu_growth_f1_hq_0035.png
  follow_up: Drill Ground gains only +200 Unit Count per level (about 27 levels to absorb the 5,306 healed troops); Headquarters needs the Base Expansion research, 1.2M oil and 1.3G iron first; the HQ Hero Defense row and fourth cost row are unread
  stats:
    target: read the HQ and Drill Ground upgrade panels: cost, time, gain (F1)
    achieved: both panels read; Drill Ground fully, Headquarters except one stat row and one cost row cut off
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.073632 USD; nothing spent, nothing pressed
    verified: yes
    surfaces_walked: 2
    items_observed: 34
    run_id: 20261123T083521Z-a5a70f
    run_steps: 6
    actions_done: 12
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 0.073632
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot F1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit F1, order 3. Question: What do the HQ and Drill Ground upgrades cost, take and add?

Route: Tap building body, green up-arrow opens the Upgrade panel; read every line; close by X or left-edge swipe-back (drag 20,500 to 200,500); second building the same way.

Read: Level from and to; power from and to; iron, food, coin; prerequisites with check marks; original and effective time; Unit Count or hero level cap line; Finish Now figure.

Budget: at most 8 steps and 10 minutes. Notes: Reading only: never Upgrade or Finish Now. Prior panel X failed under background clicks (2026-11-09), so use swipe-back if X fails once. Copy each prerequisite row with its check mark into extra_gain. Copy each prerequisite row with its check mark into extra_gain. Do not press Upgrade on either building.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.
