---
title: Zombie Invasion Execution 2026-10-28 1347 Queue Run
created: 2026-10-28T20:47:00Z
modified: 2026-10-28T20:47:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 019 - partial, fresh wave found and a Lv.10 target card opened but the March button never dispatched through background clicks and a Return keypress quit the game, recovered cleanly with state intact, no stamina spent, no kill, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1347 queue unit 019

A single task unit, executed by executor ticker-1334 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-019,
chain zombie-2026-10-28, chain sequence 19, priority 4.
Session window about 13:35 to 13:47 America/Los_Angeles.
Status — partial; the unit found the fresh wave and opened a
Lv.10 target but dispatched no squad, so the work resumes
as a fresh unit and the tracker is left untouched.

## What was observed

- Open — world map, coin HUD 51.4M, stamina 114, no march
  out. Unit 018's carried exact coin is 51,462,936; no fresh
  exact coin panel read was obtained in this unit (see the
  coal panel note below), and no coin moved, so the carried
  figure stands for both ends of this unit.
- Wave state — the first Search answered "Monsters not
  found nearby. Try again later." with the next wave about
  2:46 out, so the previous wave's nearby supply was
  exhausted. After the wave arrived, a second Search found
  a Lv.10 Invading Zombies target at once.
- Target card — Lv.10 Invading Zombies beside an alliance
  member base, Guaranteed Reward medal x10, book 1.3K,
  hero EXP 263.0K, iron 268.0K, food 268.0K, stamina cost
  10, despawn timer 11:57:50. Crossed-swords tap pinned
  at about 506,715, matching unit 017's 500,712.
- Deploy panel — Squad 1 selected, 25.05M against
  670.00K, Easy Win, march time 00:00:07, stamina 115,
  cost minus 10. March button at about 498,741.
- Dispatch failure, control channel — the March button
  was tapped three times with no change each time
  (stamina stayed 115, panel stayed open), and the
  channel twice reported that background clicks do not
  reach this control. The earlier taps in this unit
  (Events, Search, back, crossed-swords) all landed, so
  the failure is specific to this button in this window
  state, not a general loss of control. The window stayed
  background throughout, frontmost app
  UserNotificationCenter, and open_app attempts returned
  outcome_unknown without visibly bringing it forward.
- App quit on Return — following the channel guidance to
  try the keyboard, one Return keypress quit Last War
  outright (target_app_exited). Do not repeat keyboard
  input to this app: Return joins Esc and Ctrl-Cmd-F on
  the do-not-use list for Last War on this Mac. The game
  was reopened at once under a fresh session and came
  back to the base view with state intact, as expected
  for server-side state; no stamina was spent and no
  march was in flight, so nothing was lost.
- Coal panel detour — a tap meant for the gold coin icon
  opened the Coal detail panel instead (Coal owned
  1,758,840, resource items 44.0K). Its X resisted two
  background taps and closed only after an open_app
  attempt; successors should not chase the exact coin
  panel through the top bar mid-unit when the HUD
  already confirms the carried figure and nothing moved.
- LOOT and chests — no LOOT badge was observed (no
  march queue bar was seen in this unit's views) and no
  rows were claimed; the 3 owned Coin Chest (SSR) and
  the medal balance were not re-read. Nothing bought, no
  diamonds or money spent, no speedup or stamina item
  burned.
- Totals — zombies_killed 0, coins_collected 0,
  coin_before 51,462,936 carried, coin_after 51,462,936
  carried, medals_before 50 carried, medals_after 50
  carried, chests_opened 0, squads_parallel 0 (no squad
  dispatched), cleared false (the fresh wave arrived and
  a Lv.10 target was open on the map when the unit
  ended). The unit ended at its 15 minute cap, not on a
  cleared area.

## Follow-up for the successor

- Dispatch first, then parallelize: the fresh wave's
  Lv.10 targets are open now, so the successor should go
  straight to Events, Search, crossed-swords at about
  506,715, and March at about 498,741 — and if the March
  button again ignores background taps, try bringing the
  window forward before any keyboard input, which is
  banned for this app after this unit's quit.
- Do not spend the unit re-reading the exact coin panel:
  the carried 51,462,936 stands until a LOOT claim moves
  it, and the claim itself verifies the step.
