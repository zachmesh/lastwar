---
title: T1 result - a tap from a live 1/30 lands, decision on a second trial
created: 2026-11-23T02:24:00-08:00
modified: 2026-11-23T02:24:00-08:00
level: L0
version: 1.0.0
description: Verifier reading of the operator test T1 result, the evidence already in the records on the cooldown timer, the decision not to run trial 002 and the rule rewrite for the scribe
status: unverified
grounded_in:
  - source: operator record _records_/2026-11-22/alliance-donations/1012-t1-test.md and its CSV
  - source: eleven taps from 1/30 in donation records of 2026-10-31 to 2026-11-23, rows in donation-timer-evidence.csv
---

# T1 result - a tap from a live 1/30 lands

**Verdict: closed as refuted.** One landing was the criterion. The 10:12:44Z tap moved Tech EXP 7.8K to 7.9K and the badge 82.8K to 82.9K within 2.9 s. Card R1 and digest 5 are refuted; the sixth EXP-verified landing from 1/30. Limit: Rapid Siege node, no calibration tap.

**What earlier records already say** (11 taps, sidecar):
- Not a fixed cooldown: ten timers read 4:50 to 48:50, and two taps in one unit showed 4:50 then 18:58. Five taps in 37 s showed no timer until the last: grey plus timer marks a spent count [inference].
- Not a daily lock: the button turned green again and a later tap landed (11-11 0434, tap 4).
- A count read after the timer was 1/30 in four units, never 2/30 or 0/30, including after the EXP-verified 11-10 landing: zero plus one refill.

**Trial 002: not needed.** A count read after the timer cannot separate "landed, then one refill" from an eaten tap as EXP can, and four such reads exist. This tap's post-timer read comes free at the next donations entry; record its time, and log timer and entry counts for the refill interval.

**Rewrite for the scribe.** Card R1 and digest 5: "Donate while the count reads 1 or more; a tap from a live 1/30 lands. After the last tap read Tech EXP and badge; grey Donate with a timer means the count is spent. Status tested, 2026-11-23, 1012-t1-test.md."

**Decision for the coordinator.** R6 closes only on a live count, which the last tap now always hides, so every unit would close unverified. Keep R6, or accept two moved witnesses plus the grey timer.

**T2 side data:** Rapid Siege 5/10 costs 600, a fit; level 1 is still owed.
