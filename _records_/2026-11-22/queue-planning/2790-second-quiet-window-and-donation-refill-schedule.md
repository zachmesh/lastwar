---
title: Queue Planning Second Quiet Window And The Donation Refill Schedule 2790 2026-11-23
created: 2026-11-23T06:56:00-08:00
modified: 2026-11-23T06:56:00-08:00
level: L0
version: 1.0.0
description: Planner pass for the second cu quiet window 17:10Z to 17:25Z and for the donation refill datum of one count per 35 minutes - five scan expiries extended and the donation passes rescheduled with an entry-count prediction
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0656-quiet2-donations
trigger: coordinator message 14:51Z
started_at: 2026-11-23T06:51:00-08:00
finished_at: 2026-11-23T06:56:00-08:00
verified: every inbox unit tested against 17:10Z to 17:40Z; the prediction formula computed at four times; word counts under 450; validate exit 0
grounded_in:
  - source: coordinator message 14:51Z (operator run of donations-2026-11-23-0603)
---

# Second quiet window and the donation refill schedule, 2790

## 1. Quiet window 17:10Z to 17:25Z

Five scans had a window or expiry in 17:10Z to 17:40Z; nothing else did. Expiries extended by 25 minutes: `trucks-plunder-scan-2026-11-23-005` 17:20Z to 17:45Z (already moved once for the first window), `-006` 17:40Z to 18:05Z, `-007` 17:30Z to 17:55Z, `-008` 17:50Z to 18:15Z, `-009` 18:10Z to 18:35Z. The too-soon rule stays in all nine.

## 2. The donation refill [D, unverified]

The entry of 8/30 at 14:39:00.956Z and the earlier last-tap timer ending 10:17:57Z are 16,800 s apart, which is 8 x 2,100 s: one refill per 35 minutes fits the eight counts, not one per 20. With a count of 1/30 and the last-tap timer ending 14:57:57Z, the predicted count is 1 + floor(minutes / 35): 3/30 at 16:30Z, 5/30 at 17:45Z, 6/30 at 18:03Z, 7/30 at 18:30Z. That is about 41 taps a day at full use, so passes every three and a half hours spend the same taps in fewer runs.

## 3. The schedule

`donations-pass-2026-11-23-001` (17:45Z to 18:30Z), `-002` (21:15Z to 22:15Z) and the existing `donations-2026-11-23-1630` (00:30Z to 02:00Z on 2026-11-24) each carry the policy 2532 rules and the refill test: write the entry count and the UTC time to the second, compare with the prediction (for a later pass, the count left plus floor(minutes since the last-tap timer end / 35)), write 'refill model mismatch' if it differs by 2 or more, and at the last Donate tap write the cooldown timer, the UTC time and the count left. The 00:30Z unit had lost its logging block when `plan` re-minted it.

## 4. Open

The roster will mint a donations unit for the 18:03Z window at the next `plan`; it would run at a count of about 1 and should be retired when it appears, since the 17:45Z pass covers it. The Researcher's rule 8 is settled only if the 17:45Z to 18:30Z entry count matches the prediction.
