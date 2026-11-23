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
serves: PL-04
chain_id: pass-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T17:45:03Z
lease_until: 2026-11-23T18:05:03Z
result:
  status: done
  started_at: 2026-11-23T17:45:03Z
  finished_at: 2026-11-23T17:49:14Z
  duration_seconds: 251
  executor: operator
  summary: Entry count 9/30 at 17:45:43.410Z, nine coin taps (last 17:47:04.217Z), first timer ends 17:57:57 on the 20-minute grid: H20 confirmed, H35 rejected; tail skipped (first timer 10:41)
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/1745-queue-run.md and 1745-queue-run.csv; run 20261123T174509Z-2a6969
  follow_up: refill grid is 20 minutes (14:57:57.397Z + k x 1,200 s): next points 18:17:57 and 18:37:57; scribe: update the refill rule and the 1441 note; tail not run
  stats:
    target: spend the live donation count with coin only and read the first timer to test H35 against H20
    achieved: 9 taps, 9,000 coins, count 9 to 0, first timer end 17:57:57 (H20)
    resources_gained: 9,000 coin spent on alliance tech donations
    points: 0
    costs: none spent; model 0.281303 USD
    verified: yes
    run_id: 20261123T174509Z-2a6969
    run_steps: 23
    actions_done: 21
    actions_refused: 0
    cost_usd: 0.281303
    device_takeovers: 0
    entry_count: 9
    entry_time: 17:45:43.410Z
    taps: 9
    coin_spent: 9000
    first_timer_end: 17:57:57
    refill_hypothesis: H20
    tail: skipped
    rules_used: 1,2,3,4,6
  stats_missing: []
  stats_warnings: []
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, donation pass, the refill test)

serves: PL-04

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/` (read its `rule-digest.md` first). Spend the live count and stop: DONE when spent or already spent at entry; PARTIAL when you stop early; FAILED when the panel is never reached; coin only, never the diamond Donate; count only witnessed taps. Route: the Alliance shield (ground it fresh), Techs, War tab. NO hand tap may precede this pass.

REFILL TEST [D], pre-registered by the Coach (`_records_/2026-11-22/coach/refill-test-prereg.csv`): count = 1 + grid points passed since 14:57:57.397Z. H35 (2,100 s) predicts entry count 5 at 17:45Z with the first timer ending 17:52:57, 6 at 17:55Z, 7 at 18:30Z. H20 (1,200 s) predicts 9 at 17:45Z (timer ends 17:57:57), 9 at 17:55Z, 11 at 18:30Z (ends 18:37:57). Anything else means no fixed grid.

THE DECISIVE OBSERVATION IS THE GRID PHASE, NOT THE COUNT (`_records_/2026-11-22/research/donation-refill-addendum.md`): the first timer end after the pass lands on the grid whatever was consumed. Read that timer WITHIN ONE MINUTE of the last tap and write its read time to the second. Count 9 with an end near 17:57:57 is a clean 20-minute grid; a lower count means counts used elsewhere (a phone tap) or partial accrual. Log to the second: entry count and time, every Donate tap, the first timer and its read time, the count left; say H35, H20 or neither.

OPTIONAL TAIL: start between 17:44Z and 17:48Z. After spending the count, if the timer is under 9 minutes, wait it out, read the count (predict 1/30), tap once more (about 1,000 coin) and read the second timer: about 34:30 if the period is 35 minutes, about 19 if 20. Wait at most 10 minutes; otherwise skip the tail and say so.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
