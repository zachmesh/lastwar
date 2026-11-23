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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T15:10:45Z
lease_until: 2026-11-23T15:30:45Z
result:
  status: skipped-needs-owner
  started_at: 2026-11-23T15:10:45Z
  finished_at: 2026-11-23T15:17:06Z
  duration_seconds: 381
  executor: operator
  summary: Test T3: ONE foreground click on the check-in Go at 15:11:14.951Z swiped the banner to its second slide (POINTS 1000) with no reward popup, no Claimed state and no counter change, and Google Chrome took the front at 15:11:15; the harness consent request (new_app) was not answered, the run was stopped, nothing in Chrome was touched; digest rule 9 supported by one click; LastWar not frontmost, needs-owner
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1511-queue-run.md and 1511-queue-run.csv; run 20261123T151100Z-91131b
  follow_up: the owner clicks the LastWar Dock icon (or the coordinator approves _tools_/mac_lastwar_front.sh); the researcher reads the verdict (rule 9 supported, one click); the +3 s shot was not taken
  stats:
    target: T3 one foreground click on the check-in Go: reward popup, Claimed or counter change while LastWar stays frontmost
    achieved: click made; no in-game reward; Chrome took the front (digest rule 9 supported, one click)
    resources_gained: none
    points: 0
    costs: none spent; model 0.034873 USD
    verified: yes
    blocker_category: f missing precondition (a browser took the front, needs-owner)
    run_id: 20261123T151100Z-91131b
    run_steps: 3
    actions_done: 5
    actions_refused: 0
    cost_usd: 0.034873
    device_takeovers: 0
    rules_used: 9
    rule_failed: none
    rule_gap: none
  stats_missing: []
  stats_warnings: []
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: playbook card test T3 for OD-20261123-15

## Brief (planner for the Researcher, assignment A-20261123-0945, OD-20261123-15 verifier, test T3)

serves: playbook card test T3 for OD-20261123-15

Falsification test of shop-claims digest rule 9: does the check-in FREE GIFT Go pay in game? Follow `_records_/2026-11-22/research/checkin-go-test.md` exactly (8 steps). The test table is `_records_/2026-11-22/research/playbook-card-tests.csv`. This is the riskiest of the three, because the web store is a purchase surface and focus may be lost.

Run `lsappinfo front` first: LastWar must be frontmost, or stop. Shop from the base cart icon; the tab row on 2026-11-23 has NO Hot Deals tab (Official Event | Weekly Deal | Super Monthly Pass | Weekly Pass | Diamond | G, record `_records_/2026-11-22/shop-claims/1457-queue-run.md`), so open the tab that shows the check-in FREE GIFT page (at most 3 tab taps; if none shows it, stop 'blocked by route' and click nothing), wait for the check-in page, ground Go from a screenshot, then ONE foreground click on Go and no second click. Screenshots at once and +3 s, with `lsappinfo front` after each.

STOP RULES: if another app takes the front, touch nothing in it and record needs-owner. Any login, account link or payment prompt: stop. No price button, Renew, Extension or Take All. Press only a button labelled Claim, Collect or OK if a reward popup appears.

Spend: nothing.

Red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No purchase, no diamond spend, nothing that is not in the brief. Do not enqueue a chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
