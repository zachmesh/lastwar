---
title: Conformance report 2 - the loop at 12:58Z
created: 2026-11-23T13:05:00Z
modified: 2026-11-23T13:05:00Z
version: 1.0.0
description: Second coach conformance report with the six KPIs and the tag-text check at 12:58Z Mac UTC, the donations count under the tracker policy, and the drift list; published late
status: done
activity: coach
run_id: coach-2026-11-23-0501-report
trigger: coordinator assignment A-20261123-0830-coach, daily 12:00Z report
started_at: 2026-11-23T12:56:00Z
finished_at: 2026-11-23T13:05:00Z
duration_seconds: 540
verified: no
grounded_in:
  - source: _queue_ parsed at 12:58Z; the operator growth ledger and the alliance-donations records
  - source: _knowledge_/growth-plan and strategy/plan-of-record.csv, items PL-01 to PL-18
---

# Conformance report 2

Late: due 12:00Z, published about 13:05Z; no wake reached the coach between 10:58Z and 12:55Z. Figures: [kpis](conformance-kpis.csv), [slots](slot-idle-minutes.csv), [triggers](plan-triggers.csv), [drift](drift-list.csv). Calibration is in [report 1](0501-calibration-report.md).

**(a) Coverage.** Executed units with a serves tag: 27 of 34 in 6 h (79.4%, up from 9.4%), 27 of 78 in 24 h. Serving a growth action: 4 of 34 (3 fill idle slot, 1 capacity source). Queue: 77 units, 22 growth actions (28.6%), 17 read or measure, 4 system-test, 34 upkeep (44.2%). Busy slot-minutes started by a plan item: 0 of 7,854. The first state-changing growth action with a power effect is the Complete on Unlock Oil Well at 11:53:00Z, +3,900.

**(b) Idle, 24 h.** All slots 39.4% (5,106 of 12,960): builders 57.1%, labs 2.6%, training 40.3%. Last 6 h: 13.4%; builders 0 (four Training Base builds to 2026-11-24T09:20Z), labs 10.4%, training 33.3%. Lab 1 has been idle since 11:42:55Z: Complete pressed, no restart recorded.

**(c) Adherence.** 2 of 2 triggers past due were met: the slot A read (unfixed) and the Complete, 10 minutes after the finish. Pending: slot B opens 13:00Z; the lab restart (Food Output V, PL-04) is due 13:53Z.

**(d) Partials.** 52.9% in 6 h (18 of 34), 52.6% in 24 h (41 of 78). Growth-chain units: 12 of 20 partial. Growth blockers: c tap method 10, f missing precondition 2. All units, 24 h: h 16, c 12, f 6, e 5.

**(e) Power.** Per day by category cannot be set until a second fixed-state breakdown: since 07:47Z only tech moved (+3,900, one event, [M]). Fixed-state reads: 0 of 1 collect-first; slot B is 13:00Z to 15:00Z.

**(g) Tag text.** 44 of 87 building-read rows carry name and level (51%, from 39%); 7 of 16 CSVs carry none. The tap-method blockers (c) are the same failure: 10 of 12 growth partials.

**Donations, policy 2532.** Rolling 24 h to 13:01Z: 5 queue units (done 1, partial 3, failed 1) and the T1 test; 28 witnessed taps of 28 logged. None since 10:12Z.

**(f) Drift, new.**
- D10: the snapshot log stopped at 10:23Z, 2 h 35 min.
- D11: lab 1 idle since 11:42:55Z, high until restarted.
- D12: a stale Extra Drill Ground row in the lever table.
- D13: tags are free text, not PL-ids.
- D14: this report was late.

Closed: D1 and the D5 wording (now one growth action, not none).
