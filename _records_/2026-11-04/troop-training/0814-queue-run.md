---
title: Troop training queue run 0814
created: 2026-11-04T16:14:00Z
executor: ticker-0804
unit: training-2026-11-04-0603
status: partial
---

# Troop training - 2026-11-04 08:14 local

Unit: training-2026-11-04-0603 (regular training,
activity troop-training). Session: Mac mini Last War
window, computer sessions cc-435 and cc-436 (the
first session closed mid-unit and was restarted;
no device contention). No "active on a different
device" dialog appeared on entry; no takeover was
needed.

## Work done

- Changed method versus the 0440 unit (queue rule
  R2): inherited points were NOT trusted. The
  0440 tent point (585,548) was tried once and
  selected Arena Lv.1 in this framing, not a
  barracks, proving again that tent points do not
  transfer across camera framings. The grounded
  Drill Ground candidate (722,610) produced no
  panel. Every later tap was grounded fresh on
  the live frame of that moment.
- Barracks verified, 1 of 4: after a drag-pan
  down (drag from (300,500) to (300,300) on the
  base screen, which moved the view down to the
  tent row), a fresh-grounded tent tap selected
  Barracks Lv.20 with its button row (paw,
  pistol, green upgrade arrow never tapped).
  Its middle button opened the Building Details
  panel, not a Train Units panel: Training
  Count +613, matching the T7 count in the
  activity metadata for the fourth barracks,
  instructors Alexis, Joe, Jolene and Anthony,
  no training timer shown in Details. This
  button mapping differs from the 0440 record
  (paw Details, pistol Train Units); in this
  frame the middle button behaved as Details.
  The panel was closed with its X; nothing was
  queued, dispatched or spent.
- Framing instability, measured: closing the
  Details panel returned the camera to a
  different framing, so re-tapping the same
  tent point (660,893) opened the chat panel
  instead of the tent. The chat panel was closed
  at once with its back arrow; nothing was
  typed, sent, opened or acted on there, and no
  chat content is recorded here. A second
  drag-pan down restored the tent row, but two
  further fresh taps on tent candidates
  ((467,727) grounded, and (592,831) read off
  the live frame) selected nothing, and the
  unit's time was then spent.
- HUD resources at end, unchanged by this unit:
  food 415.2M, iron 745.8M, coins 15.2M, power
  150,028,269. No batch was queued and no
  Train Units panel was reached, so the
  Drill Ground Full toast was neither
  reconfirmed nor cleared in this unit; the
  0440 live confirmation still stands as the
  latest Drill Ground read.

## Why partial, not done

- 0 of 4 barracks queued, 1 of 4 verified
  (Lv.20 Details only), so the "keep every
  barracks busy" standard is unmet. Tracker
  untouched, per the rule for partial units;
  the next tick re-produces training and
  resumes from the findings below.
- Follow-up for the next training unit: do not
  reuse any point from this unit or 0440 across
  a panel close or a camera move - re-ground
  the tent on the frame in front of you after
  every panel close. The open questions, in
  order: (1) which button in the current
  framing actually opens Train Units, since
  the middle button opened Details here;
  (2) the Drill Ground clearing method, still
  unknown. This is the known tent / Drill
  Ground blocker already tracked as Issue 150;
  no new issue filed, and the framing
  instability finding belongs as a comment
  there if the next unit confirms it again.
- No new Issue was filed: this unit produced
  no new task, gap or failure mode beyond the
  Issue 150 blocker it worked.

## Red lines

Nothing spent at all; no Train button completed
a queue, no Finish Now, no green upgrade
shortcut, no building started, no squad
dispatched, no other activity's work done, no
chat message sent.

## Result stats

- target 4, achieved 0, resources_gained 0 batches,
  costs 0, verified no, blocker_category e
- barracks_checked 1, batches_queued 0,
  device_takeovers 0
