---
unit: donations-pass-2026-11-23-001
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-23T14:53:23Z
expires_at: 2026-11-23T18:55:00Z
planned_for:
not_before: 2026-11-23T17:44:00Z
window: donation pass count about 5 to 7 refill one per 35 minutes
est_minutes: 14
serves: upkeep
chain_id: pass-2026-11-23
chain_seq: 1
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

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/` (read its `rule-digest.md` first). Spend the live count and stop: DONE when spent or already spent at entry; PARTIAL when you stop early; FAILED when the panel is never reached; coin only, never the diamond Donate; count only witnessed taps. Route: the Alliance shield (ground it fresh), Techs, War tab. NO hand tap may precede this pass.

REFILL TEST [D], pre-registered by the Coach (`_records_/2026-11-22/coach/refill-test-prereg.csv`): count = 1 + grid points passed since 14:57:57.397Z. H35 (2,100 s) predicts entry count 5 at 17:45Z with the first timer ending 17:52:57, 6 at 17:55Z, 7 at 18:30Z. H20 (1,200 s) predicts 9 at 17:45Z (timer ends 17:57:57), 9 at 17:55Z, 11 at 18:30Z (ends 18:37:57). Anything else means no fixed grid.

THE DECISIVE OBSERVATION IS THE GRID PHASE, NOT THE COUNT (`_records_/2026-11-22/research/donation-refill-addendum.md`): the first timer end after the pass lands on the grid whatever was consumed. Read that timer WITHIN ONE MINUTE of the last tap and write its read time to the second. Count 9 with an end near 17:57:57 is a clean 20-minute grid; a lower count means counts used elsewhere (a phone tap) or partial accrual. Log to the second: entry count and time, every Donate tap, the first timer and its read time, the count left; say H35, H20 or neither.

OPTIONAL TAIL: start between 17:44Z and 17:48Z. After spending the count, if the timer is under 9 minutes, wait it out, read the count (predict 1/30), tap once more (about 1,000 coin) and read the second timer: about 34:30 if the period is 35 minutes, about 19 if 20. Wait at most 10 minutes; otherwise skip the tail and say so.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
