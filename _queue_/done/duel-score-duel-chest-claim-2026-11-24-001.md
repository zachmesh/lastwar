---
unit: duel-score-duel-chest-claim-2026-11-24-001
regular: duel-score
activity: alliance-duel
segment: 2
priority: 1
created_at: 2026-11-25T00:19:54Z
expires_at: 2026-11-25T01:45:00Z
planned_for:
not_before: 2026-11-25T00:40:00Z
window: claim the 7.2m personal chest once the total reads 7.2m held as insurance for the speed up unit
est_minutes: 3
serves: snapshot
chain_id: duel-chest-claim-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 1
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at: 
  finished_at: 2026-11-25T02:00:59Z
  duration_seconds: 
  executor: 
  summary: window passed before execution
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# duel-score

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `duel-score`: Alliance Duel score - read the personal daily total on the VS duel panel and record it against the 3,600,000 target (stats target/achieved/gap, live read only); the last read before the daily reset (02:00 UTC) is the day closing figure; read-only, never grind, spend or buy. Its definition is the activity folder `_activities_/alliance-duel/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE 7.2M CHEST CLAIM, insurance, held)

serves: snapshot

DO NOT RUN until the Coordinator names this unit: it is for the case the speed-up unit ended before the claim (cost cap, time or a stop); else press nothing.
Facts [M]: the speed-up unit adds 750 a 5m tile (7,024,500 at 00:13Z); the 7,200,000 chest (closed, gold; preview: Valor Badge x400, UR Hero Universal Shard x1, Tactical Master Supply Box x15, Lv.3 Drone Component) turns claimable at 7,200,000. Claim by 01:45Z. ONE RUN.
(1) Open the VS panel by the duel-score route. FIRST read the personal total and the 7,200,000 chest's state. Under 7,200,000 or not claimable: tap NOTHING, close 'not claimable: total <value>'.
(2) A frame BEFORE with the UTC time. At 7,200,000 or more with the chest claimable: ONE plain Claim tap on the 7,200,000 chest ONLY (not another threshold's chest).
(3) Read the popup by TEXT (every row, item NAME and QUANTITY). Close it by its X, or Confirm ONLY a plain 'Congratulations' with NO price. NEVER a Claim on anything with a price, never Buy, Go or Draw.
(4) Any price, dialog or other app: STOP. `--state-change yes` if claimed, else no; a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
