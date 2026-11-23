---
title: Decision - how the donations unit is counted under a refilling pool - 2026-11-23 10:32Z
created: 2026-11-23T02:32:00-08:00
modified: 2026-11-23T02:35:00-08:00
level: L3
version: 0.1.0
description: The coordinator's tracker policy for alliance donations after the T1 test - the pool is spent each unit, the day total is witnessed landed taps, and a spent-count close counts as done
status: done
activity: team-operations
run_id: team-operations-2026-11-23-1032-donations-policy
trigger: researcher rulings on the close rule (_records_/2026-11-22/research/donation-close-ruling.md), test T1 (1012-t1-test.md)
started_at: 2026-11-23T02:30:00-08:00
finished_at: 2026-11-23T02:35:00-08:00
verified: the rulings and the T1 test are read; the refill interval itself is NOT measured (the profile's one count per 20 minutes is a guess, rule 8 logs it)
---

# Donations tracker policy (coordinator)

## Decision

- **The pool is spent, not a daily quota.** There is no target of 30 taps a day: the count refills over time (interval still a guess), so each donations unit spends the live count and stops; the cadence follows the refill log of digest rule 8.
- **Day total** = the number of WITNESSED landed taps in the 24-hour window (a tap counts when the live count fell by one, or on the last tap when the green Donate turned grey with a timer and Tech EXP or the badge rose 0.1K). Never a count written after the last tap, derived by arithmetic or taken from the footer (the researcher's ruling 1).
- **Unit status.** DONE when the unit closes with the count spent (green to grey with a timer, witness read) or finds the count already spent (timer visible at entry, nothing to tap). PARTIAL when it stops before the count is spent (turn budget, interruption) with the taps logged. FAILED when the panel is never reached. An entry at 1/30 closes flagged uncalibrated.
- **Cost.** Coin only; the diamond Donate is never pressed.

## Who acts

The planner keeps the 2-hour cadence until two refill reads exist; the coach counts done by this rule and reports the day total of witnessed taps; the scribe writes the rule into the digest.
