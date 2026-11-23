---
unit: donations-playbook-t1-2026-11-23-001
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-23T09:52:29Z
expires_at: 2026-11-23T10:00:00Z
planned_for:
not_before: 2026-11-23T13:10:00Z
window: playbook card test T1 tap from live 1 of 30 run only if the count is 1 or 2
est_minutes: 10
serves: playbook card test T1 for OD-20261123-15
chain_id: playbook-t1-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:49Z
  duration_seconds: 
  executor:
  summary: retired by the planner: T1 ran as an operator continuation at 10:12:44Z, record 1012-t1-test
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: playbook card test T1 for OD-20261123-15

## Brief (planner for the Researcher, assignment A-20261123-0945, OD-20261123-15 verifier, test T1)

serves: playbook card test T1 for OD-20261123-15

Falsification test of alliance-donations card R1 and digest rule 5: does a tap from a live 1/30 count land? Follow `_records_/2026-11-22/research/donation-tap-test.md` exactly (about 11 steps, about 8 if the entry is 1/30). The test table is `_records_/2026-11-22/research/playbook-card-tests.csv`.

Place: run right after a regular donations unit that stopped at 1/30, and ONLY if the entry count N you read is 1 or 2 with no timer hiding it; otherwise stop at once, record N and the time, and count the unit as not run. One Donate tap from live 1/30, no second tap, screenshots at once, +4 s and +10 s. Tech EXP or the top-bar badge rising 0.1K after the tap means the tap landed.

Spend: coin only, 800 per landed tap, two taps at most; never diamonds, never the diamond button. Record N, seconds since the previous tap, EXP and badge before and after, and the button state per shot.

Red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No purchase, no diamond spend, nothing that is not in the brief. Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
