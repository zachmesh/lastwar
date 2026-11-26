---
unit: duel-score-newday-duel-2026-11-26-001
regular: duel-score
activity: alliance-duel
segment: 2
priority: 1
created_at: 2026-11-26T04:09:22Z
expires_at: 2026-11-26T09:00:00Z
planned_for:
not_before: 2026-11-26T04:16:00Z
window: new day duel chests, one plain claim on a reached chest, after the radar
est_minutes: 2
serves: upkeep
chain_id: newday-duel-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T04:39:09Z
lease_until: 2026-11-26T04:59:09Z
result:
  status: done
  started_at: 2026-11-26T04:39:09Z
  finished_at: 2026-11-26T04:40:45Z
  duration_seconds: 96
  executor: operator
  summary: Duel new day, theme Train Heroes: personal total 0 at 04:39:40Z; chests 40,000, 150,000 and 540,000 all closed (red-gem prices never pressed): no chest reached, nothing claimed; scoring rows Hero Recruitment +4,500, UR Hero Shard +25,000, SSR Hero Shard +8,750, SR Hero Shard +2,500, Skill Medal +25, Hero EXP +2.5, diamond packs +30; the different-device dialog never showed; drags 0. state_change: no. state_read: duel total 0, chests 40,000 150,000 540,000 closed with no claim control; theme Train Heroes | step 5 | 04:39:40Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-duel/0439-queue-run.md and 0439-queue-run.csv; run 20261126T043909Z-94ddf0
  state_read: duel total 0, chests 40,000 150,000 540,000 closed with no claim control; theme Train Heroes | step 5 | 04:39:40Z
  state_change: no
  follow_up: the total rises with hero shard use; the first chest at 40,000
  stats:
    target: claim a reached chest
    achieved: no chest reached: verified nothing-to-do
    resources_gained: none
    points: 0
    costs: none spent; model 0.124197 USD
    verified: yes
    run_id: 20261126T043909Z-94ddf0
    run_steps: 10
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.124197
    device_takeovers: 0
    claims: 0
    personal_total: 0
    theme: Train Heroes
    chest_thresholds: 40000,150000,540000
    tram_badge: icon drawn without a badge
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# duel-score

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `duel-score`: Alliance Duel score - read the personal daily total on the VS duel panel and record it against the 3,600,000 target (stats target/achieved/gap, live read only); the last read before the daily reset (02:00 UTC) is the day closing figure; read-only, never grind, spend or buy. Its definition is the activity folder `_activities_/alliance-duel/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, DUEL CHESTS of the new day, Steer A 04:05Z)

serves: upkeep

Per the activity digest. On the VS duel panel, tapping only what is named here:
(1) FIRST write whether the different-device dialog is on screen, with the UTC time (no tap). Read the personal daily total, every chest threshold shown with its state (closed, claimable or open) and Today's Theme name.
(2) CLAIM: a chest that reads claimable (its threshold reached): ONE plain Claim tap on THAT chest only; write the personal total before and after each claim; read the popup by TEXT, every row; close it by its X, or Confirm ONLY a plain 'Congratulations' with NO price. NEVER a Claim on anything with a price, never Buy, Go or Draw. No chest preview here.
(3) NOT in this unit: the weekly score and the roulette. CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do state with a `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change yes` if a chest was claimed.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
