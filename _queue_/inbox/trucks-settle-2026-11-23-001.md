---
unit: trucks-settle-2026-11-23-001
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T13:45:21Z
expires_at: 2026-11-23T16:00:00Z
planned_for:
not_before: 2026-11-23T14:20:00Z
window: own trade trucks settle and re dispatch no plunder contract floor 200
est_minutes: 10
serves: upkeep
chain_id: settle-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, own trade trucks settle and re-dispatch, no plunder, coordinator 13:44Z)

serves: upkeep

Own trucks only. The trade trucks came home from 13:34Z (the UR truck about 13:45Z, the last about 14:18Z) and there is no own-trucks settle unit until 00:30Z. Open Intercity Trade by the left-column vehicle icon (entry as in `_records_/2026-11-22/truck-plunder/0953-queue-run.md`). Settle every returned truck by opening its Truck Details, claim Reward Recovery at the red dot, read Today's Trade Count, then dispatch to fill the slots by the truck-plunder profile's standing rules (`_activities_/truck-plunder/rule-digest.md`, rules 2 to 6): SR or above as rolled; on a UR duel day only UR, in Mega Mode; below SR take the one Free refresh, then Trade Contract refreshes.

CONTRACT FLOOR: 200 Trade Contracts must remain; 266 were held at the last read, each refresh costs 1, so at most about 66 refreshes. Read the contract count before every refresh and stop at 200. Never a diamond refresh or any price in diamonds or money; no speed-up.

No Plunder of other players' trucks in this unit; the plunder sessions are separate units. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with an empty-ground tap such as (400,640); never WORLD with a menu open low. Write per truck its rarity, cargo and the dispatch time to the second. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
