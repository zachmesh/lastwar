---
title: Timing lessons from the first lab slot
created: 2026-11-23T12:10:00Z
modified: 2026-11-24T15:08:00Z
version: 1.2.0
level: L3
description: Seven rules from the lab 1 incident of 2026-11-23, covering finished research, the desktop gate, local input pauses, the cost of searching and the order of reads
status: unverified
grounded_in:
  - source: operator record _records_/2026-11-22/research-queue/1144-queue-run.md
  - source: Steer A alarm of 2026-11-23 12:08Z on the idle lab
---

# Timing lessons

1. **A finished research waits for Complete** and registers power only when pressed: the lab sat done from 11:42:55Z to 11:53:00Z and the +3,900 landed only then. Schedule a Complete unit at each node's exact finish time. Defense Training VIII no longer exists: the other device cancelled it before 12:56Z. Whether a finished building upgrade also waits for a tap is unread; the 09:20Z read of the builders and Total Power on 11-24 settles it before any later start.
2. **Gate refusals.** The D-024 desktop gate refused the start until 11:52:41Z. At every refusal the operator captures the run-lock status JSON (run.seat, startedAt) and sends it to the cu team, so we see who held it.
3. **Local input pauses.** The pause at 11:53:16Z is matched against /tmp/hid-idle.log by the coach.
4. **Search costs more than the action.** One Complete took 0.484 USD in five runs because the unit hunted for an unknown node. A start of a known node comes first; a survey is a separate read-only unit.
5. **Existence before build.** Count what exists before forecasting an unlock (F-006 and F-007 are scored misses for this).
6. **A power lump needs an attributing read.** +197,337 appeared between 11:53Z and 12:51Z with the operator stood down: other-device play moves power in lumps (as on 11-08 and 11-09). Read the Power Details breakdown before and after every window, collect first, so the category that moved names the cause (F-138).
7. **An idle-looking barracks may hold a finished batch.** The Lv.24 barracks read idle and blocked while 274 T8 waited; one pistol press per barracks per read, when room could exist, collected +291,262 (record 0351). Press the barracks before you plan to train into the room. The toast means a finished batch waits; an empty queue opens the Train panel (coach 1454, one control, four positives).

