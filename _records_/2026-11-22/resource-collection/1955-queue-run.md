---
title: Harvest queue run 1955
created: 2026-11-23T04:08:00Z
modified: 2026-11-23T04:08:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-22-1803, operator seat, run blocked before any game input
status: run-failure
grounded_in:
  - source: cu_bridge start and status on run 20261123T035508Z-9e1961, 2026-11-23T03:55Z to 03:58Z
  - source: run trajectory events.jsonl and screenshots under /Users/zhenchen/.computer-use/runs/20261123T035508Z-9e1961
  - source: queue.py token-acquire, claim and read on the live pool, 2026-11-23T03:56Z to 04:06Z
---

# Harvest queue run 1955

- Executor: operator seat (continuous-play team, first live play unit), unit
  harvest-2026-11-22-1803, claimed 2026-11-23T04:15:04Z lease, token held to
  2026-11-23T04:09:55Z.
- Status: failed. Zero game input dispatched, zero bubbles collected, nothing
  verified. The unit was not consumed by play - the run never reached a
  clickable game surface.
- Run: `20261123T035508Z-9e1961`, desktop, apps `com.lastwar.ios`,
  max-steps 20, max-minutes 15, max-cost 1.0 USD. Started 03:55:08Z, ended
  03:57:38Z. Steps 2, actions done 0 / blocked 1 / skipped 5, cost 0.065507 USD.
  View URL at start `http://127.0.0.1:60962/?token=4d63127026f406136ec8eeafaf8484af`
  (human-only control link, now closed).
- What blocked it:
  - Step 0 observation url was `app:com.apple.UserNotificationCenter`, not
    `com.lastwar.ios`: a system notification surface held the frontmost layer
    while the game window sat behind it.
  - Step 1 planned a left click at screen (179,337). The computer-use policy
    refused it with rule `excluded:terminal`, resolved app
    `com.googlecode.iterm2`, `attempted false`, `completed false`. No click
    reached the game.
  - Step 2 planned a click at (306,427) and was skipped; the bridge then
    reported state `taken_over` with `waiting_for_person` null and stayed there
    with no further trajectory events.
  - The bridge `stop` at 04:05Z returned the run `finished` / `cancelled`.
    This is cleanup of this seat's own run, not game input.
- Screen at run time (run screenshot, 1920x1080): Last War window about
  64,32 to 634,992 on the base view. HUD food 732.3M, iron 1.1G, gold 35.3M,
  diamonds 8,336, power 150,080,120, stamina 120, builders 0/4, research 2/2,
  visible ready bubbles over the farms, mines and workshops - so the harvest
  target was present and uncollected.
- Verification: none. No HUD delta is claimed, no bubble is claimed collected,
  and the "before" reading is the run's own screenshot, not a fresh entry read.
- Evidence: run screenshot `/Users/zhenchen/.computer-use/runs/20261123T035508Z-9e1961/screenshots/step-0001.png`
  (also saved by the bridge as `_tools_/state/cu_last.png`), trajectory
  `events.jsonl` of the same run. No image is committed to the repository
  (account privacy).
- Resolution owed before the next unit: the game must be frontmost with no
  system dialog above it, and no human input on the Mac, or the policy will
  either refuse the click target or hand the run over. The 19:55 observation
  read succeeded because it took no action - reading is not blocked by this,
  clicking is.
- No diamonds or money spent, no paid offer opened, no attack, no diplomacy.
- Tracker: not touched (the unit was re-produced by the next sync).
- Follow-up: the next operator unit should start only when the game window is
  frontmost and idle; if the frontmost layer is still a notification surface,
  report blocked without starting a run.
