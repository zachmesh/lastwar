---
title: Troop training queue run 1147
created: 2026-11-04T19:47:00Z
executor: ticker-1134
unit: training-2026-11-04-1003
status: partial
---

# Troop training - 2026-11-04 11:47 local

Unit: training-2026-11-04-1003 (regular training,
activity troop-training). Session: Mac mini Last War
window, computer sessions cc-453 then cc-454 (the
first session dropped mid-unit and was reopened;
no data was lost). No "active on a different
device" dialog appeared. Chrome was the frontmost
app on the Mac during this unit; background input
to the Last War window still dispatched.

## Work done

- Tent search on the live fullscreen base frame,
  four grounded taps, no barracks panel opened:
  norm (368,545), norm (435,465), norm (555,460)
  and norm (438,545). Each tap dispatched, but
  no building label and no button row (paw
  Details, pistol Train, green upgrade arrow)
  appeared in the following screenshots, so no
  TRAIN UNITS panel was ever reached.
- One drag (norm start (450,550) to (650,350))
  did not move the base view; the framing stayed
  identical across screenshots.
- No barracks queue state was verified, no batch
  was queued, and no Drill Ground figure was read
  live in this unit, so no Drill Ground Full state
  is claimed here. The tent-location blocker is
  already tracked as Issue 150, so no new issue
  was filed for this repeat of a known blocker.
- One early click was refused for focus reasons
  ("user working in another window") and one
  click was refused for a stale observation; both
  were retried and the following taps dispatched.
  Neither refusal is recorded as an access failure.

## Follow-up for the next training unit

- The fullscreen 1920x1080 framing does not match
  the 2026-11-03 success frame, where a grounded
  tap at norm (630,592) selected Barracks Lv.27.
  The next unit should re-ground on its own live
  frame rather than reuse any point from this unit,
  and should try the windowed (non-fullscreen)
  Last War window if the fullscreen frame keeps
  refusing to select a tent.

## Red lines

Nothing spent, nothing queued, no Finish Now, no
green upgrade shortcut, no squad dispatched, no
other activity's work done.

## Result stats

- barracks_checked 0, batches_queued 0,
  device_takeovers 0
