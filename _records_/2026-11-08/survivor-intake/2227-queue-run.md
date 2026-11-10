---
title: Survivor intake queue run 2227
created: 2026-11-09T06:27:00Z
modified: 2026-11-09T06:27:00Z
level: L0
version: 1.0.0
description: Ticker-2201 survivors unit, gate line unverified, area dialog not a recruit
status: unverified
---

# 2227 queue run - Survivor intake

Executor: ticker-2201. Unit: survivors-2026-11-09-0446.
Session window about 22:19 to 22:27 America/Los_Angeles.

## Performed

- This unit is the gate-line re-read after unit
  survivors-2026-11-08-1803, whose taps opened no dialog.
- Panned the base view twice to the right edge to reach the
  front gate (road out through the perimeter wall, top
  right). No line of survivors with question-mark bubbles
  was visible at the gate. One lone figure stood on the
  road just inside the wall, with no bubble above them.
- Tapped that figure (grounded from a cropped enlargement
  of the gate area): a dialog opened showing a blonde
  zombie woman, "Area No.168", text "True dread struck me
  upon seeing the eyes of the zombies." No Recruit button,
  no other button. A tap on the dialog itself did not
  dismiss it; a tap on empty base ground closed it.
- The dialog is an area-info dialog, not a survivor
  recruit card and not a dialog-survivor line. No
  survivor was recruited, no supplies handed over, and
  Quick Dispatch did not run (no intake happened).
- The gate line state is therefore still unverified: the
  lone figure carries no question-mark bubble, and the
  only tap response was an area dialog. This continues the
  standing blocker (22 of 22 survivor units partial in
  the queue era; the immediately preceding unit's taps
  also opened no dialog). Per the activity metadata the
  line needs a named re-read rather than a presumed
  close. No re-read unit is enqueued here - the next
  ticker sync re-produces the regular, and the line
  should be re-grounded from the gate, not from this
  figure.

## Closing reads

- Gate line: no question-mark bubbles seen. One figure,
  no bubble, tap opened "Area No.168" dialog. Recruits: 0.

## Outcome

Partial. Gate line unverified; no intake completed.

## Correction (same pass, before commit)

- The session window above is wrong: the unit ran 22:18 to
  22:24 America/Los_Angeles (unit duration about 6 minutes),
  not 22:19 to 22:27. The costs line should read
  6m_wall_no_stamina. The closing findings (no question-mark
  bubbles, Area No.168 dialog, 0 recruits) are unaffected.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs 6m_wall_no_stamina, verified no,
  blocker_category c, recruits 0, gate_line_verified false,
  device_takeovers 0
