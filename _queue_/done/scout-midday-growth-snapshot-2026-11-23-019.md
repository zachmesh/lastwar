---
unit: scout-midday-growth-snapshot-2026-11-23-019
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:17:24Z
expires_at: 2026-11-23T09:40:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot SC1 read only nothing bought
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 19
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T09:32:51Z
lease_until: 2026-11-23T09:52:51Z
result:
  status: done
  started_at: 2026-11-23T09:32:51Z
  finished_at: 2026-11-23T09:37:30Z
  duration_seconds: 279
  executor: operator
  summary: Season clock SC1 read, run 20261123T093538Z-b998eb (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 8 steps; a first run 20261123T093311Z-a59935 ended on an unanswerable model question after 1 step and was stopped, bridge daemon restarted), read-only: no countdown icon under the VS button (column Thanksgiving Event, Events, Warzone Duel, VS 16:24:22, Alliance, Mail, Inventory), no Obelisk or chrono text anywhere, Events tabs listed, Black Market 20d 16:23:47 ends 2026-12-14T02:00Z, Black Market Challenge and Age of Oil stage-3 cards 6d 16:23:54 end 2026-11-30T02:00Z, base clock tower 2 h behind UTC (server clock UTC-2, unverified). Nothing bought, claimed or transferred.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0935-sc1-season-clock.md and _records_/2026-11-22/growth/0935-sc1-season-clock.csv; run 20261123T093538Z-b998eb
  follow_up: Season 3 date not readable from the base; Age of Oil end and a 14-day season icon unseen; Obelisk not found
  stats:
    target: read the season countdown icon, Obelisk text and event timers
    achieved: timers read and ends computed, no season icon and no Obelisk found
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.149719 USD in two runs; nothing spent
    verified: yes
    run_id: 20261123T093538Z-b998eb
    run_steps: 8
    actions_done: 11
    actions_refused: 0
    model_s_per_step: 5.4
    cost_usd: 0.149719
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot SC1, Story 868, from the scout's unit table)

serves: snapshot (Story 868)

Read-only unit SC1. Queue placement: After BM1. Read-only.

Question: What exactly does the countdown icon under the Duel VS button read, and what does the Obelisk chrono story say, so the Season 3 date can be fixed?

Route: Base screenshot first: right-edge column (Events, VS with timer, the countdown icon with text beneath, Alliance, Mail, Inventory); read the icon picture and text exactly. Tap that icon once, read the page, its header, tabs and timers; back arrow. Events hub: every tab name and timer, drag the tab bar both ways, the main timer on The Age of Oil tab. Obelisk: look for that name on the base, in the hub and behind the countdown icon.

Read: Icon picture, exact text, days left, read time in UTC; page header, tab names, any day number, season name, starts in or ends in text; The Age of Oil timer; Black Market timer as a cross-check; Obelisk text and day, or not found; base clock building against wall time.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-sc1-season-clock.csv, schema l_clock. Copy each countdown as shown with its frame time so the end is computed, not guessed. On 2026-11-09 the icon showed a Season II globe, 6d 07:13:29, and opened the Transfer Surge page; its Ideal Environment, Easy Alliance Changes and Talk and Connect buttons are warzone transfer and alliance moves, never tap them (S3). The icon may have changed since. No record mentions an Obelisk or chrono story, so give it two steps at most and write not found. Research, unverified: 2026-12-13 may be the Age of Oil end (day 91), and a 14-day icon is expected about Dec 20 to 27.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Buy nothing, open nothing, press no Claim. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
