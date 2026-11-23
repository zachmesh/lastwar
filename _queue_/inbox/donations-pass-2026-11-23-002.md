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
serves: upkeep
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

serves: upkeep

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/` (read its `rule-digest.md` first). Spend the live count and stop: DONE when it is spent or already spent at entry; PARTIAL when you stop early; FAILED when the panel is never reached; an entry at 1/30 closes flagged uncalibrated; coin only, never the diamond Donate; count only witnessed taps. Route: the Alliance shield (ground it fresh), Techs, War tab.

REFILL TEST, the Researcher's sharp test (`_records_/2026-11-22/research/donation-refill-check.md`) [D, unverified]: if the count refills one per 2,100 s, refills fall on a grid from 14:57:57Z: 15:32:57, 16:07:57, 16:42:57, 17:17:57, 17:52:57, 18:27:57, 19:02:57, and every 35 minutes after. Predicted entry count = 1 + grid points passed since 14:57:57Z (5 at 17:45Z, 6 at 17:55Z, 7 at 18:30Z); for a later pass use the count left plus the grid points passed since the previous timer end. Log with the UTC time to the second: the entry count and time, each Donate tap, the last-tap timer value with the time you read it (so its end time can be computed), and the count left. The new timer should END on a grid point within 3 seconds. Write 'refill model mismatch' if the entry count is off by 2 or more.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is (400,640). A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
