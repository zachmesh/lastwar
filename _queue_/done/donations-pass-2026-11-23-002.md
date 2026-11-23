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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T21:15:37Z
lease_until: 2026-11-23T21:35:37Z
result:
  status: done
  started_at: 2026-11-23T21:15:37Z
  finished_at: 2026-11-23T21:19:17Z
  duration_seconds: 220
  executor: operator
  summary: Second refill test: entry count 10/30 as registered, ten coin taps 21:16:15Z to 21:17:28Z, first timer 00:00:19 at 21:17:38.083Z ending 21:17:57.08Z on the 20-minute grid; H20 holds
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/2115-queue-run.md and 2115-queue-run.csv; run 20261123T211537Z-beb4f6
  follow_up: the Alliance screen left open: one cleanup run; next grid points 21:37:57 and 21:57:57; the run stops at max_cost near 0.29 USD, so a pass should split or close earlier
  stats:
    target: entry count to the second, spend the live count, first timer on the grid
    achieved: entry 10/30 at 21:16:11.083Z, 10 taps, timer ends 21:17:57.08Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.291140 USD
    verified: yes
    run_id: 20261123T211537Z-beb4f6
    run_steps: 21
    actions_done: 36
    actions_refused: 0
    cost_usd: 0.291140
    device_takeovers: 0
    entry_count: 10
    taps: 10
    timer_end_utc: 21:17:57.08
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, donation pass, refill one per 20 minutes)

serves: PL-04

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/` (digest first). Spend the live count and stop: PARTIAL if early, FAILED if the panel is not reached; coin only, never the diamond Donate; witnessed taps only. Route: the Alliance shield (ground it fresh), Techs, War tab. If the entry count is under 6, RELEASE this unit unrun (`queue.py release --unit <this unit>`) and write the count and the time.

CLOSE (`_records_/2026-11-22/research/donation-close-amendment.md`): a count needs a live read in the same unit; after the last tap it is hidden. Close DONE when the live count before the last tap was 1/30, the Donate turned green to grey with a timer, and the timer's end (read time plus timer) lies on the 20-minute grid within 3 s; a 0.1K rise of the badge item or Tech EXP corroborates when in the same frame but is not required. Write the timer, its read time and the last tap's UTC time. Off the grid or unread: close unverified unless a witness rose. Never write a count after the last tap or derive one.

REFILL [M] (`_records_/2026-11-22/alliance-donations/1745-queue-run.md`): one refill per 20 minutes on the grid 17:57:57Z plus 20 minutes times n. Predicted entry count = the count left after the previous pass plus the grid points passed since its last tap. Pass 002 at 21:15:00Z predicts 10 with the first timer ending 21:17:57; an entry after 21:17:57 gives 11 and a timer ending 21:37:57, 12 from 21:38, 13 from 21:58. Log to the second: the entry count and time, every tap, the first cooldown timer after the last tap and its read time (within one minute), and the count left. A count below the prediction is logged 'elsewhere' (the owner's phone shares the count), unflagged, unless the shortfall exceeds 6 in a window with no owner activity.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
