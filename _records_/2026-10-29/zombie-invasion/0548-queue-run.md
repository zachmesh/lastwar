---
title: Zombie Invasion Execution 2026-10-29 0548 Queue Run
created: 2026-10-29T12:48:00Z
modified: 2026-10-29T12:48:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 043 - partial, two Lv.10 kills claimed in-unit for 536,000 coins, squads_parallel 1 sequential, Store medal balance re-read live at 2900 resolving the unit 041 derivation conflict, Coin Chest redemption deferred again after a grounded Redeem tap did not respond
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0548 queue unit 043

A single task unit, executed by executor ticker-0534 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-043,
chain zombie-2026-10-28, chain sequence 43, priority 4.
Session window about 05:34 to 05:48 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. Both kills dispatched in this unit were
resolved and claimed inside it, and the march queue
was empty at the close. The Coin Chest redemption is
deferred, not done — see below.

## What was observed

- Open — the game was already on the Zombie Invasion
  event page, live with 1 day 13:24:48 left and the
  next wave in 00:06:08. No different-device dialog
  appeared at any point. Computer sessions dropped
  twice mid-unit (cc-237, then cc-238) and were
  replaced by cc-238 and cc-239 without loss, the
  same timeout pattern units 040 to 042 recovered
  from. The wave arrived during the unit: the
  countdown reset to about 1 hour (00:59:50 read)
  at about 05:41, and Search then found targets on
  demand.
- First Search, before the wave — with the wave
  still minutes out, a Search tap at 275,925
  produced no visible change; the wave was
  exhausted, matching unit 005's not-found answer.
  No kill was attempted on that Search.
- Store and medals, conflict resolved — the Store
  header read live at 2900 medals, confirming unit
  042's live read and settling the conflict with
  unit 041's derived 1220: the 1220 derivation was
  wrong (stale base), 2900 is the balance. The gold
  Coin Chest (SSR) row reads 160 medals, Limit 98.
  Its Redeem tap at the visually grounded point
  742,293 produced no change and no dialog, the
  third unresponsive Redeem in two units (unit 042
  twice, this unit once at a grounded point), so no
  medals were spent and the redemption stays
  deferred for the successor to attempt by another
  route. The owned Coin Chest (SSR) count was not
  re-verified this unit, and no owned chest was
  opened — their backpack location is still unknown.
- Kill 1, Squad 1 — Search found a Lv.10 card
  (Suggested Power 670,000, stamina cost 10, medal
  x10, EXP 263.0K, iron 268.0K, food 268.0K,
  despawn about 11:59:38). Crossed-swords at
  498,699 opened the deploy panel (Squad 1,
  25.05M Vs 670.00K, Easy Win, Unit Count 2,231 of
  2,231, march time 00:00:10, stamina 24). March
  taps at 498,726 and at the grounded 500,735 both
  produced no change, and the control channel
  advised background clicks do not reach some
  controls. A keyboard Return was then tried and
  the game quit outright — Return crashes this app
  like Esc, and must never be used again. The app
  was relaunched (new window, same account, Total
  Power 149,351,992, no dialog) with state intact.
  March at 500,755 dispatched at once (march queue
  1 of 4, 00:00:10). Lesson: the March button's
  effective point is its lower edge, about 755
  normalized, not its visual centre — taps at 726
  and 735 land above the active area.
- Kill 2, Squad 1, sequential — while returning
  through Events (which opened directly on the
  Zombie Invasion tab this time) and Search, Squad
  1 had already completed its round trip: the
  second deploy panel again showed Squad 1
  selected (tab 1 highlighted, no red X),
  25.05M, Easy Win, march time 00:00:15,
  stamina 15. March at 500,755 dispatched. The
  parallel attempt therefore ran sequential in
  effect: the first squad's 10 to 15 second round
  trip finished during the Events and Search
  navigation for the second dispatch, so no two
  squads were ever out at once. squads_parallel
  is 1 for this stated reason, not a march cap
  (the queue cap remains 4, read 0 of 4 at the
  close).
- Claim — gift badge 2 read on the march queue
  bar. A tap at 311,205 selected a map element
  instead of opening LOOT; the grounded point
  317,215 from unit 042 opened it at once. Two
  rows, Lv.10 at X:985 Y:968 and Lv.10 at
  X:980 Y:954, coin 268.0K each. Claim All at
  498,760, blue button with no price tag.
  After the claim the coin HUD read 100.3M
  (truncated display), food 221.2M to 221.7M
  and iron 407.4M to 408.0M, each consistent
  with two 268.0K rows landing.
- Coin totals — coin_before 99,819,332 is unit
  042's last exact read, corroborated by the
  99.8M HUD at this unit's start and by no
  spending in between; it was not re-read as an
  exact panel figure this unit. coin_after
  100,355,332 is derived (99,819,332 plus
  536,000), consistent with the truncated 100.3M
  HUD after the claim. Both figures are labelled
  so.
- Stamina — 25 at the base screen after
  relaunch, minus 10 for kill 1 to 15, minus 10
  for kill 2 to 5, plus 1 regen to 6 at the
  close. No refill was needed: 6 stamina
  remains, and no unit conclusion about
  exhausted refills was required. Backpack
  stamina item counts were not re-read this
  unit.
- Medals — medals_before 2900 read live in the
  Store; medals_after 2920 derived (2900 plus
  this unit's 20). The Store 50-stamina item
  was not re-checked this unit.
- Sighting only, not acted on — passing through
  Events landed once on the Hero Advancement
  Arms Race page (current phase, score 0,
  chests at 2,000, 4,000 and 12,000 points,
  phase timer about 01:15:54). No Arms Race
  work was done in this zombie unit, and the
  page was left untouched.
- Cleared — false. The fresh wave was still
  producing targets on demand (two Searches,
  two Lv.10 cards), and the next wave was about
  59 minutes out at the close. Successor unit
  044 enqueued to start now.

## Result statistics

- zombies_killed: 2
- cleared: false
- coin_before: 99819332 (unit 042 exact read, HUD corroborated)
- coin_after: 100355332 (derived, see above)
- coins_collected: 536000
- medals_before: 2900 (read live in the Store)
- medals_after: 2920 (derived, see above)
- chests_opened: 0
- squads_parallel: 1
- tasks_badge: 2
- stamina_end: 6
