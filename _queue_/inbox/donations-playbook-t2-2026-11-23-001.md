---
unit: donations-playbook-t2-2026-11-23-001
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-23T09:52:31Z
expires_at: 2026-11-23T14:45:00Z
planned_for:
not_before: 2026-11-23T10:00:00Z
window: playbook card test T2 coin cost against node level read only
est_minutes: 10
serves: playbook card test T2 for OD-20261123-15
chain_id: playbook-t2-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: playbook card test T2 for OD-20261123-15

## Brief (planner for the Researcher, assignment A-20261123-0945, OD-20261123-15 verifier, test T2)

serves: playbook card test T2 for OD-20261123-15

Read-only falsification test of the digest's unverified item, coin cost per tap equals 100 x (node level + 1). Follow `_records_/2026-11-22/research/donation-cost-test.md` exactly (8 steps). The test table is `_records_/2026-11-22/research/playbook-card-tests.csv`.

Alliance shield, Techs, War tab. Level 5 is already read (Rapid Siege 5/10 at 600 coin in `_records_/2026-11-22/alliance-donations/1012-t1-test.md`, a fit), so skip it. Open a node showing 1/10 (predict 200), then read any node showing 3, 4, 6 or 10, dragging the tree up if needed. Each time read the level and the coin Donate number, then close with the panel X. Record node, level, coin cost, diamond cost and reward text, one line per panel. One mismatch refutes the formula; write the pair down.

Spend: nothing. Never press Donate, never the diamond button; a stray Donate tap costs one donation, at most 1000 coin.

Red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No purchase, no diamond spend, nothing that is not in the brief. Do not enqueue a chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
