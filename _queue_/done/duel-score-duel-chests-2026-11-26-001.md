---
unit: duel-score-duel-chests-2026-11-26-001
regular: duel-score
activity: alliance-duel
segment: 2
priority: 1
created_at: 2026-11-26T17:01:14Z
expires_at: 2026-11-26T17:11:30Z
planned_for:
not_before: 2026-11-26T17:08:00Z
window: duel chest row, two routes (steer a 17:00z)
est_minutes: 5
serves: PL-05
chain_id: duel-chests-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-26T17:11:30Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the chest row was read by alliance-duel/1707 (route A worked: the cyan left arrow, three taps to page 1: all three chests open, nothing to claim); this unit would repeat it
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# duel-score

Serves: PL-05

## Brief (definition pointer, from the roster)

One-off duel chest read. Definition `_activities_/alliance-duel/` (its `rule-digest.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, DUEL CHEST ROW, Steer A 17:00Z: both routes approved in the Coach's order)

serves: PL-05

On the VS duel panel: (1) FIRST write whether the different-device dialog is on screen, with the UTC time (no tap). Read the personal daily total, each chest threshold (40,000, 150,000, 540,000) and Today's Theme name. If the chest row is NOT on the page shown (it stayed on page 4 of 4 at 16:50Z; swipes failed; a page-dot click is refused):
ROUTE A: take a 6x crop of the carousel's LEFT edge for a CYAN arrow (the mirror of page 1's right arrow). If one shows: a plain tap on it, AT MOST THREE.
ROUTE B, only if A fails: ONE held drag on the carousel card itself (mouse down, a 1 s hold, ONE move of about 250 px, a 1 s hold, mouse up: the Alliance Duel panel, not the map), AT MOST ONE try.
NEVER 'Go', a spin (the Infinite Roulette card) or any red-gem price tag (8,020 / 9,530 / 18,100: the early-open prices).
When the chest row is on screen read it in ONE frame: each chest reached, glowing, claimed or locked.
(2) CLAIM: each glowing or claimable chest: ONE plain 'Claim' (the button on that chest, no price, no gem icon); write the personal total before and after each claim and read the popup BY TEXT, every row, for the Coach's table (the contents test the 540,000 chest's 18,100 gem-tag value); close it by the X, or Confirm ONLY a plain 'Congratulations' with NO price. NEVER a Claim on anything with a price, never Buy, Go or Draw. If all three read already claimed: write it. If the total is not the daily one, the states show it.
(3) Not here: the weekly score and the roulette. CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim or a verified nothing-to-do with a `state_read:` line; else PARTIAL; `--state-change yes` if a chest was claimed.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.50 USD.
