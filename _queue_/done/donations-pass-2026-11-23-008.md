---
unit: donations-pass-2026-11-23-008
regular: donations
activity: alliance-donations
segment: 1
priority: 2
created_at: 2026-11-24T11:42:55Z
expires_at: 2026-11-24T22:20:00Z
planned_for:
not_before: 2026-11-24T21:05:00Z
window: donation pass about 3.5 hours after the previous
est_minutes: 10
serves: PL-04
chain_id: pass-2026-11-23
chain_seq: 8
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T21:21:41Z
lease_until: 2026-11-24T21:41:41Z
result:
  status: done
  started_at: 2026-11-24T21:21:41Z
  finished_at: 2026-11-24T21:25:31Z
  duration_seconds: 230
  executor: operator
  summary: Donation pass 008: front log (Google Chrome before the front script at 21:21:29.1Z, LastWar after at 21:21:32.3Z), entry count 11/30 at 21:22:14.3Z, 11 coin Donate taps ending 21:23:57.198Z (live count 1/30 before the last tap), the cooldown 00:13:49 read at 21:24:08.4Z ends 21:37:57.4Z on the grid point within 0.1 s; HUD re-read first (coin 25.0M); the question-mark bubble beside the pickup a white speech bubble with a black '?' (read only); tram icon not drawn; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/alliance-donations/2121-queue-run.md and 2121-queue-run.csv; run 20261124T212141Z-6414ea
  state_change: yes
  follow_up: the next grid point 21:37:57.4Z refills one (12 from 21:37:57Z); the next pass about 22:25Z after the calm window
  stats:
    target: spend the live count and stop; coin only
    achieved: 11 taps, count spent, timer on the grid
    resources_gained: none
    points: 0
    costs: none spent; model 0.318326 USD
    verified: yes
    run_id: 20261124T212141Z-6414ea
    run_steps: 23
    actions_done: 33
    actions_refused: 0
    cost_usd: 0.318326
    device_takeovers: 0
    entry_count: 11
    taps: 11
    last_tap_utc: 21:23:57.198
    timer_end_utc: 21:37:57.4
    front_before: Google Chrome 21:21:29.083Z
    front_after: LastWar 21:21:32.251Z
    tram_badge: icon not drawn
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

REFILL [M] (`_records_/2026-11-22/alliance-donations/1745-queue-run.md`): one refill per 20 minutes on the grid 17:57:57Z plus 20 minutes times n. Predicted entry count = the count left after the previous pass plus the grid points passed since. Log: the entry count with its time to the SECOND (the Coach's series), every tap, the first timer after the last tap and its read time, the count left. A count below the prediction is logged 'elsewhere' (the owner's phone shares it), unflagged, unless over 6 short.

A TIPS dialog about another device: STOP, report, never Confirm.
Cost cap, stated: 0.60 USD.
