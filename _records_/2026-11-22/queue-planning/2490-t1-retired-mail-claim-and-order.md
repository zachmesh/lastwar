---
title: Queue Planning T1 Retired Mail Claim And Order Fix 2490 2026-11-23
created: 2026-11-23T02:19:00-08:00
modified: 2026-11-23T02:19:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the Researcher's T1 ran as a continuation - the 13:10Z T1 unit retired, the second trial kept conditional, a short Mail claim staged for the train arrival reward, and the Age of Oil unit ordered ahead of the routine claims
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0219-t1-mail-order
trigger: coordinator message with the T1 result and the train boarding
started_at: 2026-11-23T02:16:00-08:00
finished_at: 2026-11-23T02:19:00-08:00
verified: the T1 record read; the pool simulated at 5 minutes per growth read before and after the order fix; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1012-t1-test.md
  - source: _activities_/mail-rewards/rule-digest.md
---

# T1 retired, Mail claim, order fix, 2490

## 1. T1

The test ran at 10:12:44Z as an operator continuation: one Donate tap from a live 1/30 landed (Tech EXP and the badge rose 0.1K, and a cooldown timer of about 5 minutes replaced the count), which refutes card R1 and digest rule 5 on one trial. `donations-playbook-t1-2026-11-23-001` is retired: its expiry is set to 10:00Z and `sync` closes it as expired. `-002` stays, window 14:20Z to 16:20Z, only if the Researcher asks for a second tap, which must come at least 60 minutes after 10:12:44Z, not before 11:13Z, and by name right after a donations unit. The refill rate of about one count per 20 minutes stays a guess until a second read; my donations cadence is unchanged.

## 2. Mail claim

A train boarded at 10:14Z, so the Train arrival reward mail is claimable from about 10:25Z. `mail-2026-11-23-1017` (10:27Z to 11:35Z, 5 minutes) claims it by the mail digest rules: claim only, Delete All never, Cancel on the TIPS popup. Simulated at 5 minutes per growth read it runs at about 10:56Z.

## 3. Order fix

The four routine units I extended to 10:30Z were created before the Age of Oil unit, so they sorted ahead of it and it would have expired unrun at 10:30Z. Now `-022` expires at 10:29Z, ahead of them, and the four routine units expire at 10:55Z. Simulated: nothing expires, `-022` runs at about 10:19Z, the lab conversion at 11:44Z, the Secrets claim at 12:50Z and power slot B at 13:04Z.
