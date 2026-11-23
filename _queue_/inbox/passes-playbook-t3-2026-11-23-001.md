---
unit: passes-playbook-t3-2026-11-23-001
regular: passes
activity: shop-claims
segment: 3
priority: 2
created_at: 2026-11-23T09:52:32Z
expires_at: 2026-11-23T15:45:00Z
planned_for:
not_before: 2026-11-23T13:30:00Z
window: playbook card test T3 check-in Go one foreground click stop if a browser takes the front
est_minutes: 10
serves: playbook card test T3 for OD-20261123-15
chain_id: playbook-t3-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: playbook card test T3 for OD-20261123-15

## Brief (planner for the Researcher, assignment A-20261123-0945, OD-20261123-15 verifier, test T3)

serves: playbook card test T3 for OD-20261123-15

Falsification test of shop-claims digest rule 9: does the check-in FREE GIFT Go pay in game? Follow `_records_/2026-11-22/research/checkin-go-test.md` exactly (8 steps). The test table is `_records_/2026-11-22/research/playbook-card-tests.csv`. This is the riskiest of the three, because the web store is a purchase surface and focus may be lost.

Run `lsappinfo front` first: LastWar must be frontmost, or stop. Shop from the base cart icon, Hot Deals tab, wait for the check-in page, ground Go from a screenshot, then ONE foreground click on Go and no second click. Screenshots at once and +3 s, with `lsappinfo front` after each.

STOP RULES: if another app takes the front, touch nothing in it and record needs-owner. Any login, account link or payment prompt: stop. No price button, Renew, Extension or Take All. Press only a button labelled Claim, Collect or OK if a reward popup appears.

Spend: nothing.

Red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No purchase, no diamond spend, nothing that is not in the brief. Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
