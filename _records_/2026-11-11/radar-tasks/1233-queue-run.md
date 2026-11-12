# Radar tasks queue run 1233 (ticker-1204)

Unit: radar-2026-11-11-1003. Status: done.
Activity: radar-tasks. Posture: RELEASE (duel day 3, Age of
Science; tools/duel.py confirms radar_posture release, radar
claims score today).

## Entry - first-try success

- The game was left on the world map by the zombie unit. BASE
  button (919,962) back to base (Total Power 149,218,973).
- The dish was re-grounded fresh from a current screenshot:
  centre norm (53,720), matching the 0505 unit's (53,718) and
  the 0141 unit's (53,707) - the column is stable. One tap
  opened the radar on the first attempt.
- Entry verified by screen: Lv.13, radar points 415, stored
  1/40, stamina 88/120, restore "12 Radar Task(s) will be
  restored in 05:03:58". Points moved 403 (0505 close) to 415
  since 05:18 - 12 tasks were claimed by intervening units;
  the live read governs.

## Release cycle - 3 executed, 12 claimed, stored 0/40

- Bottom bar at entry: "You can complete 3 tasks, requires 30
  Stamina" with Quick Execute. Note the stored-count puzzle:
  stored read 1/40 yet the bar offered 3 tasks, and stamina
  fell exactly 88 to 58 (3 x 10) - the stored counter's
  semantics against the bar's offer count do not line up;
  recorded live, not modelled. (Adjacent open question: the
  bottom-bar offer-selection rule.)
- Quick Execute tapped once; the bar flipped to "11 task
  rewards can be claimed" with Claim All. Claim All tapped:
  CONGRATULATIONS popup, points 415 to 426, stored 1/40 to
  0/40. Rewards this batch: radar tokens 110, EXP 13.0M, blue
  crystal 774, skill medals 3.2K, iron 3.7M, food 2.1M, coin
  2.3M.
- The bar then read "1 task rewards can be claimed". Claim All
  tapped again: CONGRATULATIONS popup, points 426 to 427.
  Rewards: radar tokens 10, EXP 2.6M, skill medals 800, iron
  1.3M, coin 182.4K.
- After the second claim the bottom bar is gone - no Claim All,
  no Quick Execute. Stored 0/40, points 427, stamina 58.
- Restore line alternates between two readings: "12 Radar
  Task(s) will be restored in 05:01:51" and "Fully restore at
  11-12 17:39:11 local time" - both recorded live in this unit.
- Mystery Supply Box: a banner on the closing screen read
  "Obtained 5000 Diamonds from Mystery Supply Box. The rumor
  turns out to be true!" - a +5,000 diamond gain inside the
  claim flow (no spend, no priced button). Diamonds were 6,717
  at the zombie unit's entry; the banner is the evidence for
  the gain, the new total was not re-read on the HUD.

## Pins - inventoried at entry, none standing at close

- Entry pin inventory (8 pins on this map view):
  - two portrait pins top centre-left, alliance-labelled
    [AP3x]Comandante... and [AP3x]TrapQueen97, orange rings
  - grey skull pin (340,320) with red dot
  - grey fist pin (160,410) with red dot
  - grey skull pin (460,410) with red dot
  - blue skull pin (145,600)
  - grey fist pin (175,600) with red dot
  - green fist pin (270,630) with red dot
  - brown portrait pin bottom-left (86,757) - the 0505 unit's
    unresponsive pin (its (129,780)) was not re-tapped here;
    the R2 pivot (long-press or pan) was not needed
- Closing map view: NO pins visible anywhere on the island.
  The 12 Claim All rewards covered the finished-task pins'
  rewards - the bar counts (11, then 1) against stored 1/40
  only make sense with the map pins' rewards in the claim
  totals. No pin was tapped individually; their closing read
  is "claimed through Claim All, none standing in the closing
  view". The 0141/0505 standing set (orange arrow, purple
  axe, orange axe) was not in this view; if a later unit finds
  pins standing in another pan, they are a new inventory, not
  this unit's leftovers.
- Duel score was NOT read before or after (no VS panel visit),
  so the duel delta test (10,000 vs 30,000 per task) is still
  owed.

## Outcome

Done. Release cycle exhausted: stored 0/40, no bar offer,
points 415 to 427 (+12 claims), no pins standing in the
closing view. No diamonds or money spent. No priced button
tapped. No other activity's rewards touched. Tracker marked
done for the radar regular.

## Result stats

- target 12, achieved 12, resources_gained radar tokens 120,
  EXP 15.6M, blue crystal 774, skill medals 4.0K, iron 5.0M,
  food 2.1M, coin 2.48M, diamonds 5000 (banner-read), costs
  stamina 88 to 58 plus about 7 minutes, verified yes,
  tasks_claimed 12, tasks_executed 3, pins_inventoried 8,
  pins_worked 0, free_stamina_claims 0, radar_points_before
  415, radar_points_after 427, stored_before 1, stored_after
  0, stamina_before 88, stamina_after 58, duel_score_before
  not-read, duel_score_after not-read, entry_attempts 1,
  device_takeovers 0
