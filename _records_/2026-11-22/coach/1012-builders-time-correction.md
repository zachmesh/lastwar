---
title: Correction - the four builders free tonight at 23:20Z, and the window margins
created: 2026-11-23T18:15:00Z
modified: 2026-11-23T18:15:00Z
version: 1.0.0
description: Coach correction of the builders-free time carried in two committed notes and two tables, the effect on the idle numbers, and the margin of every named trigger to the quiet windows after the re-timing
status: done
activity: coach
run_id: coach-2026-11-23-1012
trigger: coordinator urgent correction of 18:13Z
started_at: 2026-11-23T18:09:00Z
finished_at: 2026-11-23T18:15:00Z
duration_seconds: 360
verified: no
grounded_in:
  - source: _records_/2026-11-22/building-queues/1806-queue-run.md as relayed by the coordinator at 18:13Z
  - source: plan-triggers.csv, slot-idle-intervals.csv and trigger-window-margins.csv in this folder
---

# Builders free tonight

**The correction.** The four Training Base Lv.25 builders finish at 23:20:12Z to 23:20:24Z today, not at 2026-11-24T09:20Z. The 09:20 was the Oil Well upgrade's duration, 09:20:18, read as a clock time; the operator's two readings of Time Left (05:13:04 to 05:13:15 at 18:07:08Z, and 06:29:20 to 06:29:31 at 16:51Z) both give 23:20Z. I carried the wrong time from the handover without reading the digits myself.

**Where my files had it.** Two committed notes stand as written, because records are immutable, and this note corrects them: [conformance report 2](0501-conformance-report-2.md) (the line on builders idle, "to 2026-11-24T09:20Z") and [quiet windows](0710-quiet-windows.md) (the margin "builders free 09:21Z, 56 minutes after QW4"). Two living tables are corrected in place, history in git: [plan-triggers.csv](plan-triggers.csv), where trigger T6 now reads 23:20:12Z with the next builds due by 01:20Z, and the basis text of slot-idle-minutes.csv.

**Effect on the idle numbers.** None retroactively: the figures used the builds' start, about 06:25Z, not their finish. From 23:20:12Z the four builders are an open idle interval in [slot-idle-intervals.csv](slot-idle-intervals.csv), counted automatically until the next builds start. If the builds started at 09:20Z as carried, four builders would sit idle 10 hours, 2,400 slot-minutes, 42 percent of a day's builder minutes; re-timing avoids it.

## Margins to the quiet windows ([table](trigger-window-margins.csv))

Builders free 23:20Z: 4 h 30 min after QW3 ends and 8 h 40 min before the 08:00Z window tomorrow, so the daily window no longer collides with them. All 16 named triggers are clear of every window: the pass at 21:15Z, the Lv.27 batch at 19:56Z, the one-shot at 23:21Z, the nine re-timed Oil Well levels, both Output V Completes and the Lv.30 batch. Closest to a window: chain -002 opens 11-24T08:41Z, 16 minutes after the daily window, and -007 opens 11-26T07:24Z, 36 minutes before it.

## The check I add

Plan adherence trigger T6: the next builder starts must land by 01:20Z; I read it from the building-queues records tomorrow.
