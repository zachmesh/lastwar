---
unit: donations-pass-2026-11-23-002
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-23T14:53:26Z
expires_at: 2026-11-23T22:15:00Z
planned_for:
not_before: 2026-11-23T21:15:00Z
window: donation pass about 3.5 hours after the previous refill test
est_minutes: 8
serves: PL-04
chain_id: pass-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, donation pass, the refill test)

serves: PL-04

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/` (read its `rule-digest.md` first). Spend the live count and stop: DONE when it is spent or already spent at entry; PARTIAL when you stop early; FAILED when the panel is never reached; an entry at 1/30 closes flagged uncalibrated; coin only, never the diamond Donate; count only witnessed taps. Route: the Alliance shield (ground it fresh), Techs, War tab.

REFILL TEST [D, unverified], pre-registered by the Coach (`_records_/2026-11-22/coach/refill-test-prereg.csv`): from the previous pass's count left and its timer end, write BOTH predictions (H35: one refill per 35 minutes; H20: one per 20 minutes) beside the actual entry count and say which fits: H35, H20 or neither. The first timer end after your pass is the decisive observation: read it within one minute of the last tap, with its read time to the second. Log with the UTC time to the second: the entry count and time, every Donate tap, the last-tap timer with the time you read it, and the count left.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
