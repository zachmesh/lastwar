---
title: Timing lessons from the first lab slot
created: 2026-11-23T12:10:00Z
modified: 2026-11-23T12:10:00Z
version: 1.0.0
level: L3
description: Five rules from the lab 1 incident of 2026-11-23, covering finished research, the desktop gate, local input pauses, the cost of searching and the order of reads
status: unverified
grounded_in:
  - source: operator record _records_/2026-11-22/research-queue/1144-queue-run.md
  - source: Steer A alarm of 2026-11-23 12:08Z on the idle lab
---

# Timing lessons

1. **A finished research waits for Complete** and registers power only when pressed: the lab sat done from 11:42:55Z to 11:53:00Z and the +3,900 landed only then. Schedule a Complete unit at each node's exact finish time. Lab 2 (Defense Training VIII) finishes about 2026-11-26T07:19Z (PL-10). Whether a finished building upgrade also waits for a tap is unread; the 09:20Z read of the builders and Total Power on 11-24 settles it before any later start.
2. **Gate refusals.** The D-024 desktop gate refused the start until 11:52:41Z. At every refusal the operator captures the run-lock status JSON (run.seat, startedAt) and sends it to the cu team, so we see who held it.
3. **Local input pauses.** The pause at 11:53:16Z is matched against /tmp/hid-idle.log by the coach.
4. **Search costs more than the action.** One Complete took 0.484 USD in five runs because the unit hunted for an unknown node. A start of a known node comes first; a survey is a separate read-only unit.
5. **Existence before build.** Count what exists before forecasting an unlock (F-006 and F-007 are scored misses for this).
