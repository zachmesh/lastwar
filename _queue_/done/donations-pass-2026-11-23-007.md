---
unit: donations-pass-2026-11-23-007
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-24T03:40:53Z
expires_at: 2026-11-24T18:45:00Z
planned_for:
not_before: 2026-11-24T17:30:00Z
window: donation pass about 3.5 hours after the previous
est_minutes: 10
serves: PL-04
chain_id: pass-2026-11-23
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T17:50:29Z
lease_until: 2026-11-24T18:10:29Z
result:
  status: done
  started_at: 2026-11-24T17:50:29Z
  finished_at: 2026-11-24T17:54:24Z
  duration_seconds: 235
  executor: operator
  summary: Donation pass 007 done: entry count 11/30 at 17:51:02.6Z, 11 coin Donate taps ending 17:52:37.038Z (live count 1/30 before the last tap), the cooldown 00:05:07 read at 17:52:50.2Z ends 17:57:57.2Z on the grid point within 0.2 s; HUD re-read first (coin 19.4M); tram badge none; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/1750-queue-run.md and 1750-queue-run.csv; run 20261124T175029Z-06335d
  state_change: yes
  follow_up: the next grid point 17:57:57.4Z refills one; the next pass about 18:50Z
  stats:
    target: spend the live count and stop; coin only
    achieved: 11 taps, count spent, timer on the grid
    resources_gained: none
    points: 0
    costs: none spent; model 0.296212 USD
    verified: yes
    run_id: 20261124T175029Z-06335d
    run_steps: 22
    actions_done: 34
    actions_refused: 0
    cost_usd: 0.296212
    device_takeovers: 0
    entry_count: 11
    taps: 11
    last_tap_utc: 17:52:37.038
    timer_end_utc: 17:57:57.2
    tram_badge: none
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# donations

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (definition pointer, from the roster)

This unit is the regular `donations`: Alliance tech donations - every run: donate with the coin button to the recommended tech whenever today coin donations remain (never diamonds); claim the daily donation reward when claimable. Its definition is the activity folder `_activities_/alliance-donations/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, donation pass, refill one per 20 minutes)

serves: PL-04

Policy `_records_/2026-11-22/team-operations/2532-donations-tracker-policy.md`; activity `_activities_/alliance-donations/`. Spend the live count and stop: PARTIAL if early, FAILED if the panel is not reached; coin only, never the diamond Donate; Route: the Alliance shield (ground it fresh), Techs, War tab. If the entry count is under 6, RELEASE this unit unrun (`queue.py release --unit <this unit>`) and write the count and the time.

CLOSE (`_records_/2026-11-22/research/donation-close-amendment.md`): a count needs a live read in the same unit; after the last tap it is hidden. Close DONE when the live count before the last tap was 1/30, the Donate turned green to grey with a timer, and the timer's end (read time plus timer) lies on the 20-minute grid within 3 s; a 0.1K rise of the badge item or Tech EXP corroborates when in the same frame, not required. Write the timer, its read time and the last tap's UTC time. Off the grid or unread: close unverified unless a witness rose. Never write a count after the last tap or derive one.

REFILL [M] (`_records_/2026-11-22/alliance-donations/1745-queue-run.md`): one refill per 20 minutes on the grid 17:57:57Z plus 20 minutes times n. Predicted entry count = the count left after the previous pass plus the grid points passed since its last tap. Log: entry count and time, every tap, the first timer after the last tap and its read time (within a minute), the count left. A count below the prediction is logged 'elsewhere' (the owner's phone shares it), unflagged, unless over 6 short with no owner activity.

A TIPS dialog about another device: STOP, report, never Confirm.
Cost cap, stated: 0.60 USD.
