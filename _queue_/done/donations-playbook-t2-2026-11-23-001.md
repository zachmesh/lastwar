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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T14:32:16Z
lease_until: 2026-11-23T14:52:16Z
result:
  status: partial
  started_at: 2026-11-23T14:32:16Z
  finished_at: 2026-11-23T14:34:39Z
  duration_seconds: 143
  executor: operator
  summary: Donation cost test T2, run 20261123T143216Z-36b641 (claude-gateway/claude-sonnet-5-5, 14 steps; claimed 14:32:16Z): read-only, Donate never pressed; coin cost per tap 200 at level 1/10 (Quick Training), 300 at 2/10 (Expert Trainer), 800 at 7/10 (Rallied HP), diamond 2 each, reward 50 tech EXP + 50 contribution; with T1 (600 at 5/10) the formula 100 x (level + 1) fits at levels 1, 2, 5, 7, no mismatch; levels 3, 4, 6, 10 not available on screen; coin 12.5M unchanged.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/1432-t2-test.md and 1432-t2-test.csv; run 20261123T143216Z-36b641
  follow_up: levels 3, 4, 6 and 10 stay unread (no node shows them now): the formula is a fit on four levels
  stats:
    target: falsification test of coin cost 100 x (level + 1) at levels 1, 3, 4, 6, 10
    achieved: levels 1, 2 and 7 read; no mismatch
    resources_gained: none
    points: 0
    costs: model 0.190465 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T143216Z-36b641
    run_steps: 14
    actions_done: 24
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 0.190465
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: none
  stats_missing: []
  stats_warnings: []
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
