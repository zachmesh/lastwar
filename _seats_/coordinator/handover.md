---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T08:20:00Z
level: L2
version: 0.7.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, the growth Epic, in-flight landings and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 08:20Z (Mac UTC; the owner gateway's time labels ran ahead of the Mac clock, so quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s); the 4-hour Secrets claim reminder `schedule-7565d79f-3d26-4c36-a3f9-54375f517d85` (08:51Z; a backup unit is staged).
- TEAM.yaml 0.7.0: 10 roster rows (coordinator plus operator `session-7f6dd658-ebba-4854-9a29-e2f173975825`, scout, researcher, planner, coach, toolsmith, scribe, integrator `session-bc838015-7852-464e-8cab-cf2fcc70a335`, strategist `session-5b02c501-8fd0-4186-a5b6-2ff5e3b3c3b4`). Steer A (`session-eb024f72-e661-4a77-9303-66af95dbcfd1`) is the owner gateway, steer and watchdog, not a seat. Respawn an operator past 88 percent context. Check the target id before every send.

## How a tick runs

`queue.py next`, check, dispatch in one turn; one unit, one reply; chain on each verified reply; no-op while the operator plays. Sonnet, 8 steps, one action per turn. Pre-start `killall -9 UserNotificationCenter NotificationCenter`. Never stop the game; decide operational choices and tell Steer A afterwards. Fixed: no purchase, diamond spend, speed-up, PvP, diplomacy or ally exchange. The stale-tool guard (issue 694) refuses `next` and `enqueue` when `queue.py` differs from origin's; a bounded disclosed bypass `LASTWAR_QUEUE_ALLOW_STALE_TOOL=1` is allowed until PR 876 merges or 09:15Z.

## Growth Epic (867) and its rules

Strategy v2.0 (capacity first; the strategist owns it) is unverified. Measured: Total Power 150,211,809 (Hero 44.1, Unit 42.3, Building 6.5, Drone 3.9, Tech 3.2 percent); 5,306 healed troops sit in the hospital because the Drill Ground is full (about 8.7M power); coin is bursty (35.3M at 04:03Z, 9.6M at 07:48Z; 16M to 26M a day between bursts). Decision records 2350 and 2401: resource-only starts under the 3x rule above the floors (food 100M, iron 150M, coin 10M), read first, collect first, press Complete, never cancel a running item. HOLD: no coin-costly start until the owner answers the coin split; conversion of resource chests to coin is just in time.

## In flight

PR 876 (tool landing, Integrator); then rebuild the records branch on the new origin tip (local main holds all 26 scribe branches); scribe lands strategy v2.0; operator on the inventory read; capacity reads T2, F1, P2; Black Market and season-clock reads pending in the scout's table; lab frees about 11:43Z, builders 2026-11-24T09:20Z; a collect unit for the Lv.27 batch at 19:55Z.

## Privacy

Only the owner's own in-game name is forbidden (convention 2.0.0); the tree is redacted; counts and paths only in messages.

## Open owner decisions

The coin split; any Black Market purchase (currency first).

## Lessons

Verify others' figures before building on them; deliver untracked records before a landing; take `next` without re-reading history.
