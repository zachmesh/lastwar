---
unit: glittering-market-2026-11-01-0501
regular: glittering-market
activity: glittering-market
segment: 3
priority: 1
created_at: 2026-11-01T05:01:30Z
expires_at:
planned_for:
not_before:
window: owner-named 2026-10-31, unlocated, escalation rule R5
est_minutes: 10
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-0504
claimed_at: 2026-11-02T13:05:08Z
lease_until: 2026-11-02T13:25:08Z
result:
  status: partial
  started_at: 2026-11-02T13:05:08Z
  finished_at: 2026-11-02T13:08:37Z
  duration_seconds: 209
  executor: ticker-0504
  summary: Glittering Market not located: Events tabs (Arms Race, Desert Battlefield, Wanted Boss, Community) and Mall tabs (incl. Gold Brick Mall, paid packs only) searched, no entry; unverified per R1, tracker untouched
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-02/glittering-market/0508-queue-run.md
  follow_up: none
  stats:
    located: false
    screens_searched: events-mall-base
---

# glittering-market

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Task - locate the Glittering Market and work it

Owner-named on 2026-10-31, with the standing direction to collect
from it daily and maximize. Read
`_activities_/glittering-market/INDEX.md` first. The market has
never been opened - its only trace is a mail titled Glittering
Market Unclaimed, taken by Event Claim All inside mail units on
2026-10-27, 2026-10-29 and 2026-10-30. That mail is residue, not
participation, and it does not complete this unit.

1. Locate the entry. Candidates in order - the Events screen and
   its tabs, the Store and its sections, then any base-screen
   icon carrying the market name. Record where the entry is and
   the screen it was reached from.
2. Read the market live - what it sells or gives, its currency,
   any daily free claim, the refresh rule and cost, and the
   exchange list.
3. Process everything claimable or exchangeable for today under
   the standing red lines - no spending of diamonds, rubies or
   money without owner approval.
4. Record the execution under `_records_` for the
   glittering-market activity and backfill the mechanism into
   `_activities_/glittering-market/INDEX.md` in the same pass -
   entry point, currency, daily free claim, refresh rule and
   exchange list.
5. If the market cannot be located, record the screens searched,
   close as unverified under rule R1 of the queue design, and
   say so in the result - the item stays named in the round
   summary under rule R5 until it closes.
