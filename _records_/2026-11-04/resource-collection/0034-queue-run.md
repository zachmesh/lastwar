---
title: Harvest queue run ticker-0034
created: 2026-11-04T08:50:00Z
modified: 2026-11-04T08:50:00Z
status: failed
---

# Harvest unit harvest-2026-11-03-2203, failed, ticker-0034

Session window: unit claimed 2026-11-04 00:34 local; game work
about 00:35 to 00:50 local. No base view was ever reached, so no
bubble was collected and no HUD figure was read.

## Own-PR check first

- Open records PR for today, PR 258 (records/2026-11-04, opened
  by the ticker-0004 pass): body names Owner:
  lastwar-pr-integrator, zero comments. Nothing addressed to
  this job, nothing to fix, no reply owed.

## Zombie seeding

- Not seeded. No zombie-invasion unit sits in inbox or claimed,
  and the chain closed on 2026-10-30 (unit 066: Events hub with
  no Zombie Invasion tab). The activity metadata bars a fresh
  chain until the tab is seen live again; this pass never
  reached a live Events hub, so no seed was made.

## What happened

- Mac mini (Zhen's Mac mini) online; computer session cc-396.
  At entry the LastWar window showed a "Server disconnected.
  Please restart the game." dialog; its Confirm quit the app,
  the known crash path for that dialog, with state intact.
- Relaunch showed a SYSTEM ANNOUNCEMENT dialog, "Update
  complete, please restart the game." (login screen header:
  Version 1.0.366 (908), Asset Version 2167.1512...). Its
  Confirm gave "Restarting game, please wait..." and then the
  login screen with a TIPS dialog: "The server is under
  maintenance. Please wait a moment, we'll be back with you
  shortly!" plus the footer "Login failed. Please retry or
  contact support." The account line behind the dialog still
  read "Signed in as HidingAnt504".
- Two Confirm retries, the second after a 2.5 minute wait and
  aimed at the OCR-grounded Confirm point (634,568): the
  maintenance dialog persisted unchanged both times, about
  4 minutes apart. Login is impossible while the server is in
  maintenance; this is a game-server state, not a device-access
  failure and not the different-device dialog (which never
  appeared).
- The pass ends after this one unit: every further unit would
  hit the same login wall, so re-attempting another type
  inside this pass would only repeat the blocker. The next
  tick retries login.

## What was not done (failed, tracker untouched)

- The full edge-drag harvest sweep of the Nov 1 rule was not
  started: left-side coin and stone buildings, drone-component
  bubbles, EXP and screw bubbles, and the armed-truck loot
  check were all unreached. The previous harvest unit
  (2026-11-03-1803, ticker-2034, partial) already left the
  sweep incomplete, so the sweep is now two units behind.
- No diamonds, money, speedup, or paid button was touched. No
  Delete All, no assembly, no teleport. No truck work was
  probed; truck work belongs to the trucks unit under
  one-unit-one-type.

## Evidence and follow-up

- Evidence: this file; login-screen screenshots in the pass
  working files (maintenance dialog, twice).
- Follow-up: no new Issue filed - server maintenance is a
  transient external state, not a queue failure mode. If it
  persists across ticks, the next pass names it as a repeated
  blocker. The harvest sweep resumes at the next tick that
  reaches the base view.
- Result stats: target full base sweep, achieved 0 bubbles
  (login blocked by server maintenance), resources_gained
  none, verified yes for the maintenance dialog read live
  twice, blocker_category f (missing precondition: game
  server under maintenance).
