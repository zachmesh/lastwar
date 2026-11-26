---
unit: secrets-rescue-depot-claim-2026-11-25-001
regular: secrets
activity: secret-missions
segment: 2
priority: 1
created_at: 2026-11-25T03:16:37Z
expires_at: 2026-11-27T02:00:00Z
planned_for: 2026-11-25T10:01:28Z
not_before:
window: claim the rescue and oil depot tasks and re-deploy, after the oil well hand-off
est_minutes: 8
serves: PL-17
chain_id: rescue-depot-claim-2026-11-25
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T08:56:30Z
lease_until: 2026-11-26T09:16:30Z
result:
  status: done
  started_at: 2026-11-26T08:56:30Z
  finished_at: 2026-11-26T08:59:01Z
  duration_seconds: 151
  executor: operator
  summary: Secrets claim: the in-game Claim once at 08:56:53.8Z (the four finished tasks: UR Rescue Missing Agent, SSR Search for Missing Refugees x2, SSR Protect Refugee Camp) paid Resource Chest x300, Refined Iron Module 135, Hero EXP 16.3M, Treasure Map Fragments #2 x2, #7, #1 and #4, 5m Research Speed-up x50, Upgrade Ore 1.0K, SSR Hero Universal Shard x2, Skill Medal 2.1K (the top row may be missing); the Secret Task Report shows another alliance's player plundered the task rewards at 08:40Z (purple chest x1, green item x15, EXP 123.9K) and an ally helped claim at 08:03Z; Mega Deploy and Mega Refresh greyed (nothing to deploy); Assist Allies 5/5; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/0856-queue-run.md and 0856-queue-run.csv; run 20261126T085630Z-8b87ff
  state_change: yes
  follow_up: the post has nothing to deploy now (Mega Deploy greyed); Hidden Treasures shows a badge 1: a restock
  stats:
    target: claim the finished tasks and re-deploy
    achieved: one Claim taken; nothing pending to re-deploy
    resources_gained: Resource Chest x300; Refined Iron Module 135; Hero EXP 16.3M; 5m Research Speed-up x50; Upgrade Ore 1.0K; SSR Hero Universal Shard x2; Skill Medal 2.1K; Treasure Map Fragments
    points: 0
    costs: none spent; model 0.145579 USD
    verified: yes
    run_id: 20261126T085630Z-8b87ff
    run_steps: 11
    actions_done: 4
    actions_refused: 0
    cost_usd: 0.145579
    device_takeovers: 0
    claims: 1
    plundered_report: 08:40Z by another alliance
    mega_deploy: greyed
    tram_badge: bare
    drags_tried: 0
    rules_used: 1,2,3,5
  stats_missing: []
  stats_warnings: []
---

# secrets

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `secrets`: Secret missions - claim finished (one Claim takes all), Mega Deploy the rest (UR Only off; on duel UR days Mega Refresh first), check Reward Recovery. Its definition is the activity folder `_activities_/secret-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, CLAIM the rescue and oil depot tasks, right after the Oil Well hand-off, PL-17)

serves: PL-17

The UR RESCUE TEST SUBJECT Lv.5 ends 07:13:02Z and the UR CAPTURE THE OIL DEPOT Lv.5 07:13:06Z: ONE claim takes both. A finished secret task is exposed to plunder from its end (04:16Z on 11-25): CLAIM FIRST, redeploy after. Opens 07:13:30Z, p1; Avoid 08:00Z-08:25Z and 09:58Z-10:05Z. Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims every finished task); a task not finished: claim nothing, write the time left. Read the claim POPUP FROM ITS TOP (a frame before any scroll, one after: rows above may be missing); write every row with its count; quote the SECRET TASK REPORT lines (who as shown, when, what: plunder and ally help; the owner's own name never). Then re-deploy with Mega Deploy; write the new timers and the claim time. No diamond or item spend, no Mega Refresh; Plunder Others is PvP: never tapped. No Backpack or box-count read.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do state with a `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change yes` if a claim was taken.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
