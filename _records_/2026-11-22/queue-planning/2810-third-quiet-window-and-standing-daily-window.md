---
title: Queue Planning Third Quiet Window And The Standing Daily Window 2810 2026-11-23
created: 2026-11-23T07:04:00-08:00
modified: 2026-11-23T07:04:00-08:00
level: L0
version: 1.0.0
description: Planner pass for the third cu quiet window 18:35Z to 18:50Z and the standing daily quiet window 08:00Z to 08:25Z from 2026-11-24 - the extensions applied, the donations unit rule, and the daily checks that keep every unit out of the quiet windows
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0704-third-window
trigger: coordinator message 14:58Z
started_at: 2026-11-23T07:00:00-08:00
finished_at: 2026-11-23T07:04:00-08:00
verified: every inbox unit tested against 18:25Z to 19:15Z today and 08:00Z to 08:40Z on 2026-11-24 with the tool's unit list; validate exit 0
grounded_in:
  - source: coordinator message 14:58Z
---

# Third quiet window and the standing daily window, 2810

## 1. Today 18:35Z to 18:50Z

Expiry extended by 25 minutes on 13 units: scan `trucks-plunder-scan-2026-11-23-009` (18:35Z to 19:00Z); the five :57 units events, passes, secrets, treasures and trucks (18:57Z to 19:22Z); the six 14:30Z-group units duel-score, gifts, help, mail, star-ceremony and train, and `donations-pass-2026-11-23-001` (18:30Z to 18:55Z). The last seven expire five minutes before the window opens, so a slightly late operator would otherwise have run into it; the coordinator named the 18:30Z mail. Scan `-008` expires 18:15Z and is unchanged.

## 2. Donations

The roster has not yet minted a donations unit for the 18:03Z window; `plan` does that at its next run. The schedule is `donations-pass-2026-11-23-001` (17:44Z to 18:55Z), `-002` (21:15Z to 22:15Z) and `donations-2026-11-23-1630` (00:30Z to 02:00Z on 2026-11-24). Any other donations unit is retired when it appears, and the coordinator skips any donations unit not in this list. The optional tail is already in `-001`: stated cost cap 0.40 USD, estimate 14 minutes, and a rule to skip the tail if the first timer is over 10 minutes.

## 3. Standing window 08:00Z to 08:25Z from 2026-11-24

Only one staged unit is near it: the third Oil Well collection (05:30Z to 08:30Z), extended to 09:00Z so it can run before 08:00Z or after 08:25Z. The builder units open at 09:22Z. Daily pass rule: after every `plan`, test the new units for a window or expiry in 08:00Z to 08:40Z and extend by 30 minutes; none may need the operator inside the window.
