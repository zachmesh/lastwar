---
unit: duel-score-duel-chest-preview-tap-2026-11-24-001
regular: duel-score
activity: alliance-duel
segment: 2
priority: 1
created_at: 2026-11-24T23:46:38Z
expires_at: 2026-11-25T00:20:00Z
planned_for:
not_before: 2026-11-24T23:46:00Z
window: one tap on the 7.2m personal chest icon to read its reward preview held for steer a
est_minutes: 3
serves: snapshot
chain_id: duel-chest-preview-tap-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 1
claimed_by: operator
claimed_at: 2026-11-24T23:47:32Z
lease_until: 2026-11-25T00:07:32Z
result:
  status: done
  started_at: 2026-11-24T23:47:32Z
  finished_at: 2026-11-24T23:49:32Z
  duration_seconds: 120
  executor: operator
  summary: Duel 7,200,000 chest preview (one tap approved by Steer A): 'Valued: 67800' with Valor Badge x400, UR Hero Universal Shard x1, Tactical Master Supply Box x15 and a Lv.3 Drone Component row cut off (quantity unread, further items unread); the 2,600,000 and 3,600,000 chests draw no reward text; the personal total 7,017,000; nothing pressed inside the preview; the tram icon not drawn; drags 0. state_change: no. state_read: 7,200,000 chest preview: Valued 67800; Valor Badge x400; UR Hero Universal Shard x1; Tactical Master Supply Box x15; Lv.3 Drone Component row cut off | step 5 | 23:48:04Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-duel/2347-queue-run.md and 2347-queue-run.csv; run 20261124T234732Z-f23db1
  state_read: 7,200,000 chest preview: Valued 67800; Valor Badge x400; UR Hero Universal Shard x1; Tactical Master Supply Box x15; Lv.3 Drone Component row cut off | step 5 | 23:48:04Z
  state_change: no
  follow_up: the Strategist prices the chest from these lines; the Drone Component quantity and any further items stay unread (the popup needs a scroll)
  stats:
    target: read the 7,200,000 chest's preview by one tap
    achieved: preview read; four item rows, the fourth cut off
    resources_gained: none
    points: 0
    costs: none spent; model 0.125785 USD
    verified: yes
    run_id: 20261124T234732Z-f23db1
    run_steps: 11
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.125785
    device_takeovers: 0
    claims: 0
    chest_value_gems: 67800
    valor_badge: 400
    ur_hero_universal_shard: 1
    tactical_master_supply_box: 15
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# duel-score

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `duel-score`: Alliance Duel score - read the personal daily total on the VS duel panel and record it against the 3,600,000 target (stats target/achieved/gap, live read only); the last read before the daily reset (02:00 UTC) is the day closing figure; read-only, never grind, spend or buy. Its definition is the activity folder `_activities_/alliance-duel/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE 7.2M CHEST PREVIEW: ONE tap, approved by Steer A 23:46Z)

serves: snapshot

Facts [M] (23:44Z): the VS panel opens on Today's Theme; the total is 7,017,000; the 2,600,000 and 3,600,000 chests are open (claimed); the 7,200,000 chest is closed and gold, tags 24,900, 46,900 and 67,800. ONE RUN.
(1) Open the VS panel by the duel-score route. FIRST read the personal total and the time left: at 7,200,000 or more a tap could CLAIM: tap NOTHING, close 'total reached: no tap'.
(2) A frame BEFORE with the UTC time: write the three tags and any reward line shown by plain reading (names, quantities), the 2,600,000 and 3,600,000 chests included.
(3) Tap ONCE the icon of the chest whose threshold reads 7,200,000: not a Claim button, not another threshold's chest, even if marked claimable.
(4) A frame AFTER: read the preview by TEXT only: title, every item NAME and QUANTITY (digits cropped at 6x from the SAVED frame), what the 67,800 tag labels, any button label or price line. Close it by its X or the blue back arrow. NEVER a Claim, Go, Buy or any button in it; no second tap.
(5) Any price, dialog or diamond count: STOP. `--state-change no`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
