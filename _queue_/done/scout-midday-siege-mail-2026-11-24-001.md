---
unit: scout-midday-siege-mail-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T06:40:12Z
expires_at: 2026-11-24T12:00:00Z
planned_for:
not_before: 2026-11-24T06:45:00Z
window: read only the two zombie siege report mails rewards and loss split no claim
est_minutes: 8
serves: PL-07
chain_id: siege-mail-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T06:45:02Z
lease_until: 2026-11-24T07:05:02Z
result:
  status: done
  started_at: 2026-11-24T06:45:02Z
  finished_at: 2026-11-24T06:47:38Z
  duration_seconds: 156
  executor: operator
  summary: Both Zombie Siege Report mails (2026-11-23 17:48:00) read: Alliance defended 1,623 waves (rewards include EXP 45.5M), Individual held off 20 waves; no troops, casualties, Claim button or cooldown in either; the rewards equal the 04:04:55Z mail claim (already received); drags 1, cancelled 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0645-queue-run.md and 0645-queue-run.csv; run 20261124T064629Z-f7ed5d
  follow_up: no claim remains; the casualties are only in the horde battle report (owner side -4,953) and the Hospital
  stats:
    target: read the two Zombie Siege Report mails: troops, casualties, rewards, result, claim presence
    achieved: rewards and results read, troops and casualties not in the mails
    resources_gained: none
    points: 0
    costs: none spent; model 0.199 USD
    verified: yes
    run_id: 20261124T064629Z-f7ed5d
    run_steps: 16
    actions_done: 22
    actions_refused: 0
    cost_usd: 0.199
    device_takeovers: 0
    drags_tried: 1
    drags_cancelled: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-07

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the two Zombie Siege Report mails, PL-07)

serves: PL-07

Lead: `_records_/2026-11-22/mail-rewards/0636-queue-run.md` found TWO 'Zombie Siege Report' mails in the ALLIANCE mail list, not opened: they probably carry the REWARDS and the loss split that the horde battle report did not show. 10 steps at most.

Open the Alliance mail list and each of the two mails, SCROLLED. For each write: the date and time to the second; the troops sent; the casualties (wounded, dead); the REWARDS with counts; the result text; whether an attachment or Claim button is PRESENT (read its presence only: NEVER press Claim, a claim is a later unit if the owner and Steer A agree); the cooldown text. Opening marks a mail read: accepted. Never Delete, Forward or Reply.

Drag rule: taps first; a drag only from a blank margin; write the drag count. NOT inside 08:00Z to 08:25Z (the cu window), 07:00Z to 07:15Z (the donation pass) or 07:35Z to 07:58Z (the depot claim): if the clock is inside one, wait. The TIPS 'Enable notifications' dialog: take a frame, identify Cancel BY ITS TEXT, one tap; never Enable Now; any other unrecognised dialog: stop. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.
Tag text beside every number; none means [G].
Cost cap, stated: 0.40 USD.
