---
title: Cadence part 1
created: 2026-11-23T06:53:20Z
modified: 2026-11-23T06:53:20Z
version: 0.1.0
sequence: 5
description: While the event is live, play it as much as possible - the owner wants the
---
## Cadence

- While the event is live, play it as much as possible - the owner
  wants the maximum coin yield, not a single token attempt.
- Coin measurement (added 2026-10-28 after the owner asked for
  the collected total) - every zombie unit records the exact
  coin panel reading at its start and at its end in its result
  stats (coin_before, coin_after). The activity's yield is
  judged on those deltas, never on HUD-rounded figures. As of
  the first two executions the verified yield is zero - the
  Lv.10 target card carries no coin line, and coins appear only
  as a possible drop in the reward pools.
- Parallel teams, owner instruction 2026-10-28 - dispatch
  multiple teams in parallel. Do not send one squad, wait for
  its return, then send the next - keep as many squads
  marching on nearby zombies simultaneously as the game
  allows, so kills and rewards accumulate faster inside each
  unit's 15 minutes. Record how many squads ran in parallel
  as the stat squads_parallel. Enforcement, owner check
  2026-10-28 - units 001 to 004 in fact ran with
  squads_parallel 1, which does not meet this instruction.
  From unit 005 onward parallel dispatch is mandatory where
  the game allows it - a unit that still records
  squads_parallel 1 must state in its summary why parallel
  dispatch was impossible, and any game-side cap found
  (march queue limit, stamina supply, march slots) is
  recorded here with the observed number. Unit 005
  (2026-10-28) also could not dispatch - the wave was
  exhausted and Search answered not found, so its
  squads_parallel is 0 for lack of targets, which is not a
  cap. MEASURED by unit 007 on 2026-10-28 - the March
  Queues bar reads 0/4 with no squad out and 1/4 with one
  out, so the march queue cap is 4 squads. The binding
  constraint in the 11:42Z wave was different (unit 006) -
  two extra marches failed at the March tap with the
  toast "The target location has changed. Please try
  again." and charged no stamina; Search targets in a
  fresh wave move or are taken within tens of seconds,
  so a dispatch that pauses to read screens loses its
  target. Batched click sequences (Events, Search,
  attack, March in one action batch, no screenshot reads
  in between) dispatched cleanly twice in units 006 and
  007 - that is now the standard dispatch method, and a
  parallel attempt should batch the second squad's whole
  sequence the same way immediately after the first
  March. (2026-11-10 2219 update: parallel dispatch missed again in the Glacieradon variant - while Squad 1 was out, a tap at 498,505 opened a Teleport/Profession tile menu instead (the map had shifted under the aim point) and the follow-up at 450,350 opened a Lv.28 Ironhead card;