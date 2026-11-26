---
unit: scout-midday-bubble-probe-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-26T11:49:31Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T12:45:00Z
window: bubble probe, three named bubbles one tap each (steer a 11:48z)
est_minutes: 12
serves: snapshot
chain_id: bubble-probe-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off bubble probe (not the midday walk); definition `_activities_/perception-scout/`.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, BUBBLE PROBE, the interaction step of OD-20261125-05, Steer A 11:48Z)

serves: snapshot

Steer A lifts 'tap no bubble over a building' for THESE THREE NAMED BUBBLES ONLY, ONE TAP EACH, IN THIS ORDER: (1) the 'NEW!' bubble at about (520,860) in the HOME frame, glyph and label read first in a frame: if it sits on the framed News Center portrait (bottom centre right), DO NOT tap it (its back arrow does not respond: three units hit it) and write the glyph read; (2) ONE wrench bubble below the home frame (pan down first); (3) ONE of the FIVE question-mark figures at the aircraft field, right of the HQ (pan right first): confirm the question mark and the figure in a frame, tap the FIGURE (not the bubble), read the recruit card.
PANS: start on blank road ground, about (330,640); ONE message per pan: mouse_move to the start point, left_mouse_down, wait 1 s, ONE move of about 175 px, wait 1 s, left_mouse_up, a screenshot after. At most FOUR pans; back to HOME by WORLD then BASE (one tap each). A pan that flings or moves nothing: STOP.
FOR EACH TAP read the panel or popup BY TEXT (name, offer, reward, price). A plain free claim, collect or help control: press it ONCE. DO NOT PRESS: a price, a diamond or gem icon, Buy, Unlock, Upgrade, Activate, Speed Up, Join, Go to the world, an attack, rally or march, a team or alliance request that is not the daily Help, a consent or share dialog, a recruit that costs tickets or diamonds (write the cost and stop). Close by the X or back arrow; write what it offered. NEVER the green up arrow.
One route-card line per bubble: what it is, plain claim or not, reward, cost.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the three taps read, with a `state_read:` line; else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
