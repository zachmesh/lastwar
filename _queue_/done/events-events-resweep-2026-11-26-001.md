---
unit: events-events-resweep-2026-11-26-001
regular: events
activity: event-claims
segment: 2
priority: 2
created_at: 2026-11-26T15:27:51Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T15:36:00Z
window: events re-sweep, the scrolled tab bar (coordinator 15:30z)
est_minutes: 6
serves: upkeep
chain_id: events-resweep-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T15:41:16Z
lease_until: 2026-11-26T16:01:16Z
result:
  status: done
  started_at: 2026-11-26T15:41:16Z
  finished_at: 2026-11-26T15:47:00Z
  duration_seconds: 344
  executor: operator
  summary: Events re-sweep: the full bar is The Age of Oil, Arms Race, Black Market, Black Market Challenge ('!'), Desert Battlefield, Zombie Invasion (dot 1), Wanted Boss and Community; the tabs with a dot or '!' and the Age of Oil opened: Zombie Invasion (a Store dot only), the Age of Oil (stage 3, both tasks done, ends about 2026-11-30T02:00:01Z, no Claim seen), Black Market Challenge (725/745, Go To rows): no plain green Claim; nothing pressed; Wanted Boss and Community not opened (no dot); drags 7. state_change: no. state_read: eight tabs; Age of Oil stage 3 no Claim; BM Challenge Go To rows; Zombie Invasion Store dot only | step 12 | 15:43:18Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/event-claims/1541-queue-run.md and 1541-queue-run.csv; run 20261126T154117Z-0604c2
  state_read: eight tabs; Age of Oil stage 3 no Claim; BM Challenge Go To rows; Zombie Invasion Store dot only | step 12 | 15:43:18Z
  state_change: no
  follow_up: the Age of Oil lower rows were not scrolled; Wanted Boss and Community unopened (no dot)
  stats:
    target: see every Events tab and claim plain Claims
    achieved: verified nothing claimable
    resources_gained: none
    points: 0
    costs: none spent; model 0.264484 USD
    verified: yes
    run_id: 20261126T154117Z-0604c2
    run_steps: 16
    actions_done: 12
    actions_refused: 0
    cost_usd: 0.264484
    device_takeovers: 0
    claims: 0
    tabs_seen: 8
    events_badge: 1
    tram_badge: not drawn
    drags_tried: 7
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# events

Serves: upkeep

## Brief (definition pointer, from the roster)

One-off events re-sweep. Definition `_activities_/event-claims/` (its `rule-digest.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, EVENTS RE-SWEEP, Coordinator 15:30Z)

serves: upkeep

The Events hub opens on the remembered tab with the TAB BAR SCROLLED, so tabs are hidden. DRAG THE TAB BAR (a plain drag, no hold, one message per drag) until EVERY tab name has been seen, and write the full list left to right with each tab's red dot or '!'. The 15:18Z sweep read only Black Market, Black Market Challenge, Desert Battlefield and Zombie Invasion; the Age of Oil (stages 1 to 3 reached at 09:05Z, no Claim then), a cut-off 'B' tab with a red '!' and 'Wanted B...' were never read.
Open EACH tab that has a dot or '!' and the Age of Oil: press a plain green 'Claim' ONLY. NEVER Go, Buy, Redeem, Join or any price. The Lottery tab is NEVER opened (a full-window loading screen, no back arrow). The Thanksgiving turkey tickets (6 at last read) are NOT redeemed: write the balance with the UTC time. The Thanksgiving Event Store, Lottery and Gift of Thanks: press NONE; Arms Race chests are priced: never; the Black Market tabs: read only. Write what each tab shows. This brief replaces the earlier one that named tabs the bar did not show.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken Claim or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.45 USD.
