---
unit: vip-login-chest-2026-11-26-001
regular: vip
activity: vip-rewards
segment: 2
priority: 1
created_at: 2026-11-26T09:11:34Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T09:15:00Z
window: vip login chest, one plain free claim (steer a 09:10z)
est_minutes: 4
serves: upkeep
chain_id: login-chest-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T09:16:40Z
lease_until: 2026-11-26T09:36:40Z
result:
  status: done
  started_at: 2026-11-26T09:16:40Z
  finished_at: 2026-11-26T09:18:40Z
  duration_seconds: 120
  executor: operator
  summary: VIP login chest: already taken today (the chest icon is drawn open with no Claim; the panel says logged in 8 days in a row, collect 200 VIP points tomorrow); VIP13 points 1,706,340 of 2,000,000; the Daily Freebie countdown 16:42:47 read only; no Claim pressed; the profile page's text not recorded; drags 0. state_change: no. state_read: VIP13 login chest drawn open with no Claim; points 1,706,340 of 2,000,000; Daily Freebie countdown 16:42:47 | step 6 | 09:17:14Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/vip-rewards/0916-queue-run.md and 0916-queue-run.csv; run 20261126T091641Z-c5d473
  state_read: VIP13 login chest drawn open with no Claim; points 1,706,340 of 2,000,000; Daily Freebie countdown 16:42:47 | step 6 | 09:17:14Z
  state_change: no
  follow_up: the next login collection at 02:00Z
  stats:
    target: claim the VIP login chest once
    achieved: already taken: verified nothing-to-do
    resources_gained: none
    points: 0
    costs: none spent; model 0.14875 USD
    verified: yes
    run_id: 20261126T091641Z-c5d473
    run_steps: 12
    actions_done: 4
    actions_refused: 0
    cost_usd: 0.14875
    device_takeovers: 0
    claims: 0
    vip_points: 1706340
    freebie_countdown: 16:42:47
    avatar_taps: 1
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2,3,5
  stats_missing: []
  stats_warnings: []
---

# vip

Serves: upkeep

One-off VIP login chest claim, NOT the daily freebie walk. Definition: `_activities_/vip-rewards/` (its `rule-digest.md` first); routes: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, VIP LOGIN CHEST: a plain free Claim, Steer A 09:10Z)

serves: upkeep

VIP LOGIN CHEST: ONE plain free Claim, once. The Daily Freebie is already claimed this server day (its countdown read 16:59:10 at 09:00:51Z): read the countdown only, do not tap it. Never a purchase or a diamond line.
ROUTE: (1) In the base frame look for a separately tappable VIP badge or label beside the avatar (a crown or 'VIP n' text): identify it by its glyph or text, never by a coordinate from memory, and tap THAT. (2) ONLY IF there is none: ONE tap on the avatar. THE PROFILE PAGE SHOWS THE OWNER'S IN-GAME NAME: NO record, summary, frame description or state_read carries the name or ANY text of the profile's header: write 'the profile page' only. If the 'You're very popular' dialog shows: 'Awesome!' once, then continue. In the profile tap ONLY the VIP entry. (3) In the VIP panel read the LOGIN CHEST's label and reward by TEXT first: no price, no gem or diamond icon, not Buy, Upgrade, Activate or Renew; tap its Claim ONCE; read the popup by text and close it by its X or a plain Confirm. Also read the VIP points (1,706,340 of 2,000,000 at 09:00Z) and the next level's reward by name if the panel shows it. (4) Any other surface: the X or the blue back arrow, and STOP. The avatar is never tapped for any other purpose. Never VIP Exclusive, the points plus button, the cart or the VIP Store. Close by the X to the base. CLOSE by 3170: DONE for a claim (`--state-change yes`) or a verified nothing-to-do (`--state-change no`); the `state_read:` line carries no profile text; else PARTIAL.
A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
