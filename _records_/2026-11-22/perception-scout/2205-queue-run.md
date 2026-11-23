---
title: Perception scout queue run 2205
created: 2026-11-23T06:08:00Z
modified: 2026-11-23T06:08:00Z
version: 1.0.0
description: Read-only observation of the To-do List, operator seat, Server Time read against the UTC wall clock, offset UTC minus 2 hours, Zombie Siege 23:15 server time
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T060519Z-0b19d8, 2026-11-23T06:05Z
  - source: run screenshots step-0001.png and step-0003.png under /Users/zhenchen/.computer-use/runs/20261123T060519Z-0b19d8, whose capture stamps in events.jsonl give the UTC time of each read, final frame saved as _tools_/state/cu_todo_2105.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T06:05:19Z
  - source: queue.py token-acquire and token-release around the run, no unit claimed
---

# Perception scout queue run 2205

- Read-only observation, assignment A-20261123-0604-operator, not a queue unit. The
  question: when is Zombie Siege, and what is the offset between the To-do List's
  Server Time and our clock. Measured rows are in the sidecar
  [2205-queue-run-detail.md](2205-queue-run-detail.md).
- Status: done. Nothing was claimed, and nothing was tapped but navigation.
- Run `20261123T060519Z-0b19d8`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 6, ended `completed` after 4 steps. Actions done 3, refused 0, failed 0,
  one action per turn. Model time 4.56 s per step. Cost 0.057193 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar. The first base frame had no
  "Boarding closes in" banner, so the new boarding rule did not trigger.
- Route: one tap on the blue clock building below the VS timer opened the To-do
  List. A drag of the list did not move it. The panel's own X closed it, and the base
  screen shows again.
- Offset, the answer: the header read Server Time 04:05:26 on the capture stamped
  06:05:26.78Z, and 04:05:34 on the capture stamped 06:05:34.78Z. Server time is
  UTC minus 2 hours, to the second, on both reads.
- Zombie Siege: 23:15 server time on 2026-11-23, which is 01:15Z on 2026-11-24 and
  17:15 PT on 2026-11-23. That is 45 minutes before the 18:00 PT reset. The profile's
  earlier "23:15" was server time, and it agrees. The row carries a Go button and no
  status text.
- Other entries for today, server time: Alliance Train 04:08, Winter Battlefield
  09:00, Alliance Exercise 21:00. UTC and PT equivalents are in the sidecar. More rows below Zombie Siege are unknown; the list would not drag.
- The Alliance Train at 04:08 server time is 06:08Z. It matches the boarding banner
  seen at 06:01Z, whose boarding closed about 06:03Z, about 4.5 minutes before
  departure.
- Not touched: every Go button, the VS medallion, the mid-base trophy bubble.
- Red lines held: no claim, no speedup, no diamonds, no purchase, no attack, rally,
  march or Arena, no Alliance Wars, no diplomacy.
- Follow-up: none owed. Issue #814 can record the offset UTC minus 2 hours and Zombie
  Siege at 01:15Z.
