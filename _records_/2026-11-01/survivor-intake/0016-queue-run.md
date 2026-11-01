---
title: Survivors queue run
created: 2026-11-01T07:16:00Z
modified: 2026-11-01T07:16:00Z
version: 1.0.0
description: Ticker unit survivors-2026-10-31-2203, partial, gate line never verified
status: partial
---

# Survivors - ticker-0004, 2026-11-01 00:06 to 00:16 local

Unit: survivors-2026-10-31-2203. Status: partial. Nothing recruited,
nothing collected, tracker untouched. The next tick re-produces the
regular, since it is still due.

## What was observed

- Own-PR check first: no open PR is owned by this job. Open PR 15
  belongs to lastwar-pr-catchall-owner (privacy redaction, no
  comments) and open PR 16 is the pr-integration 2345 run record
  for records/2026-10-31. Nothing addressed to this job.
- Queue sync reaped 0, expired 0, produced 0 new units; all 20 due
  regulars were already queued. No zombie chain was seeded: the
  Zombie Invasion event ended at about the 19:00 reset on
  2026-10-30 (chain unit 066 closed the chain) and no Zombie
  Invasion tab is live.
- The game window was already in 642x951 window mode. Its title-bar
  click and activate did not bring it to the front (Speedtest
  stayed frontmost), but that proved not to be the blocker: a tap
  on the Events icon opened the Events screen, so background
  canvas input does reach the game.
- Base view at entry was zoomed into the central helicopter pad,
  the same view the 23:34 harvest unit could not pan. No survivor
  figure, question-mark bubble or gate line was visible in it, and
  a visual-grounding pass found nothing. One drag (500,500 to
  200,500) produced no view change - the pan method failed again,
  matching the harvest unit's three failed drags.
- Side observation, not acted on (one unit, one type): the Events
  screen showed a Hero Advancement Arms Race phase, Contest
  Segment Lv.29-30, score 6,000 against thresholds 2,000 / 4,000 /
  12,000, chest 1/2, about 02:49 left. That phase belongs to the
  queued arms-race unit, not this one; nothing was claimed there.

## The Escape error and recovery

- Two taps on the Events back arrow produced no change, and the
  guidance said background clicks do not reach some controls. An
  Escape key press was then tried to leave the Events screen.
  That was an error: Escape quit Last War outright, the same
  crash behaviour the standing lessons already record for Esc
  and Ctrl-Cmd-F on this app. It must not be used again.
- The game was relaunched with open_app. It returned straight to
  the base screen with no fresh login, no verification code and
  no "active on a different device" dialog, so no kick was needed
  and the session is intact. HUD unchanged throughout: food
  289.2M, iron 477.2M, coin 10.6M.
- The relaunched base view was wider and different - a winter
  area with buildings, a NEW! speech bubble and a road with
  vehicles at the top - but a second visual-grounding pass for
  the gate line timed out after 180 seconds, and the unit cap
  was nearly up, so no tap was risked on an unverified point.

## Closing

- Gate line state: unverified, not presumed. No recruit was
  tapped, no Quick Dispatch was run, no purchase or diamond
  button was touched. Blocker category: tap/pan method (c), with
  the Escape crash as a self-inflicted incident inside the unit,
  fully recovered.
- Standing blocker note: survivor units closed partial 22 of 22
  in the queue era through 2026-10-31, and this unit makes the
  pattern continue. The changed methods tried here were a fresh
  grounding attempt, an Events tap proving canvas input works,
  and a relaunch that reset the camera to a wider view. The
  remaining changed method for the next unit is a slow manual
  drag (mouse down, stepped move, mouse up) or a scroll zoom-out
  on the relaunched wider view, starting from that view rather
  than re-entering the zoomed pad view - and never Escape.
- Game left on the base screen (relaunched view).
