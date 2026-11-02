---
title: Truck Plunder
created: 2026-10-25T20:12:00Z
modified: 2026-11-02T21:44:07Z
level: L1
version: 1.18.0
description: Intercity Trade trucks, dispatching own trucks and plundering the trucks of others, one activity folder for trade knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming a plunder and truck task, 2026-10-25
  - source: web guides on Intercity Trade and trade trucks, read 2026-10-25
  - source: owner teach-in on plunder target selection and dispatch rules, evening of 2026-10-25
  - source: evening dispatch and plunder executions on the new server day, 2026-10-25
  - source: owner standing rule on non-UR day dispatch - SR or above only, ticket refreshes authorized until reached, 2026-10-26
  - source: owner rule on daily truck quotas - dispatch 5 and plunder 4 every trade day, note it in the metadata and resolve misses, 2026-10-30
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1053 trucks unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1352 trucks unit)
  - source: incidental trucks-view read in the alliance-train execution record 2026-11-01 1813 queue run (not a trucks unit)
  - source: daily retro 2026-11-01, trucks 1457 expiry and counter tension (issues 147 and 148)
  - source: ticker-2212 trucks execution record 2026-11-01 2231 queue run
  - source: ticker-0104 truck-plunder execution record 2026-11-02 0114 queue run (partial, trade-screen entry blocker)
  - source: ticker-0404 truck-plunder execution record 2026-11-02 0416 queue run (partial, trade entry corrected)
  - source: ticker-0934 truck-plunder execution record 2026-11-02 0935 queue run (partial, dispatch quota filled, plunder shortfall 2 remains)
  - source: ticker-1307 truck-plunder execution record 2026-11-02 1325 queue run (partial, leftmost shard stack x3 pays in full, plunder shortfall 1 remains)
---

# Truck plunder - Intercity Trade

## What this activity is

The Intercity Trade system has two halves in one screen. Your Truck
dispatches the account trade trucks on hours long journeys for cargo
rewards. Others' Trucks lists the trucks of other players, which can be
plundered in battle for a share of their cargo. This folder
accumulates both halves. Executions are recorded in
`_records_/<date>/truck-plunder/`, one file per execution.

Not to be confused with the Armed Truck at the base gate, whose
accumulated loot belongs to
[`resource-collection`](../resource-collection/INDEX.md), or with the
alliance train, registered as
[`alliance-train`](../alliance-train/INDEX.md) - in Season 2 a golden
train also runs on this screen as a trade vehicle.

## How to enter

- On the base screen, the left icon column carries a truck icon with a
  red count badge - the badge showed 4 at first entry on 2026-10-25.
  Icon rows shift as badges change, so find it by the truck glyph, not
  by position alone.
- The icon column carries two shortcut sets, learned the hard way on
  the evening of 2026-10-25 - the same slot opened the Secret Command
  Post in one set and Intercity Trade in the other. Tapping the route
  icon above the truck slot flipped the set. Always verify the screen
  that actually opened before tapping further.
- Set identification, re-verified 2026-10-26 (1057 run) - in the set
  currently shown, the column reads top to bottom - green face
  (season warming panel), white pickup (Secret Command Post - the
  pickup is the Secret Mobile Squad vehicle, NOT the trade truck),
  satellite dish with a red count badge (radar), hammer (build
  palette), walkie-talkie (Missions). No trade slot exists in this
  set, and the flip described above was not reproduced that run -
  the trade screen could not be entered at all. When the trade
  slot is absent, check whether anything can actually be pending
  before spending the run hunting - at a full Trade Count and
  Plunder Count for the trade day, nothing can be.
- Set identification, re-verified 2026-10-28 (0257 run) - in the set
  then shown, the column reads top to bottom - green face (season
  warming panel), blue truck-front icon with a red badge (Intercity
  Trade; the badge read 4 with four trucks out), white pickup
  (Secret Command Post, its badge 4 matching the four task cards),
  satellite icon with badge 1 (radar), hammer (build palette). Each
  was confirmed by the screen it opened. Icon centres in the
  642 by 951 window sat near norm y 605 (trade), 657 (secret post)
  and 720 (radar) in that set.
- The screen opens on Others' Trucks. Bottom tabs switch between
  Others' Trucks and Your Truck. A refresh button at top right
  rerolls the plunder list, and History shows past trades and fights.
- Foreground precondition, recorded by the retro of 2026-10-31 -
  on 2026-10-31 the 1030 gifts unit, the 1030 help unit and the
  1057 truck unit all failed entry with Chrome frontmost, and
  background input does not reliably reach the game. Two
  no-change taps end the background-input method inside the
  unit under queue rule R2 - the next variant is to bring the
  game window to the foreground and re-observe before tapping
  again, never a third identical background tap. A later
  2026-10-31 truck record notes background input reaching the
  game throughout, so foreground is a pivot variant, not a
  claim that background input never works.

## How it is done - dispatching

- Your Truck shows four slots. Tap a free slot plus sign to open the
  INTERCITY TRADE - TRUCK panel for that truck.
- The panel rolls a rarity and a cargo list, shows the journey time,
  and preassigns an escort squad. Escorts rotate - the four dispatches
  on 2026-10-25 took Squads 1, 3, 2 and 4 in that order. The panel
  states no unit losses in truck escort battles.
- The dice button refreshes the roll. Each truck gets one free
  refresh per day - proven on the evening of 2026-10-25, when all
  four trucks of the new server day showed the Free tag in turn (at
  noon only the first truck had been refreshed, which made it look
  like one per day). After a truck free refresh is spent, its dice
  prices further refreshes at 1 Trade Contract each (stock 127
  observed). Spending contracts on refreshes is authorized only
  under the standing non-UR day rule below (owner, 2026-10-26);
  diamonds are never spent on refreshes.
- A refresh replaces the whole roll and can downgrade it - observed
  the same evening, when a free refresh took one truck from SR down
  to N. Refresh low rolls (N, R); think twice before gambling an SR.
- Tapping Let's Go on a low rarity truck while its free refresh
  remains raises a TIPS dialog - the rarity of your current truck is
  low, and you still have free refresh attempts, skip the refresh
  and depart now. Cancel returns to the panel to refresh; Confirm
  departs as rolled. Seen for R and SR rolls.
- Standing dispatch rules, owner taught 2026-10-25 and refined
  2026-10-26 - on days when UR truck dispatches count toward the
  Alliance Duel score, dispatch through Mega Mode and send UR
  trucks only. On all other days (non-UR days), dispatch SR or
  above only, as follows.
  - A truck that already rolls SR, SSR or UR is dispatched as
    rolled. Do not spend its free refresh - it already meets the
    bar, and a refresh can downgrade it.
  - A truck that rolls below SR (N or R) is refreshed until it
    reaches SR, SSR or UR, then dispatched. Use the free refresh
    first; if the roll still has not reached SR or above, keep
    refreshing with tickets at 1 Trade Contract each until it
    does. This ticket spending is standing-authorized by the
    owner (2026-10-26) for this purpose; no per-run approval is
    needed. No cap was stated.
  - Because a refresh replaces the whole roll, a chase can pass
    through several low rolls - keep going until SR or above
    lands, then dispatch immediately without further refreshes.
- Let's Go dispatches. Journeys observed ran about 4 to just under 5
  hours. Rewards land when the truck arrives.

## How rewards are delivered

- A returned truck settles when its Truck Details are opened -
  observed end to end on the evening of 2026-10-25, closing the
  earlier inference that delivery was automatic. Tapping a returned
  truck on the Your Truck view opens TRUCK DETAILS headed Intercity
  Trade Reward, and a Congratulations overlay pays the cargo out.
  Left and right arrows page through the returned trucks one by one;
  each page shows the escort squad, the delivered cargo, and a
  status line - the vehicle is safe and secure, or a Battle History
  naming each successful plunderer with time and power, the items
  they took listed below, and the looted cargo slots crossed out in
  red. Reviewing all four noon trucks cleared the yard to empty
  slots, and the HUD reconciled - food 319.7M to 334.7M and iron
  311.7M to 326.7M across the settlements, the evening plunders and
  harvests combined. Settlement therefore waits for the return leg,
  not just the outbound arrival estimate - the noon trucks,
  dispatched 12:32 with 4 to 5 hour estimates, were found returned
  by about 20:47.
- History is the ledger. Its Dispatch tab shows each truck cargo
  with green gained amounts and red crossed items for whatever was
  plundered off it en route; its Plunder tab logs the escort battles
  both ways, including Defense Failed records naming the attacker.
  Looted trucks show flame markers on the Your Truck road view.
- Reward Recovery - the Recover button at the lower left of the
  trade screen covers a different case, unstarted transports. The
  system completes missed dispatches itself at partial value and
  holds the proceeds in a REWARD RECOVERY panel, one record per
  day, only the last 7 records retained. Claimed free on
  2026-10-25 for the 2026-10-24 record (5 unstarted transports -
  iron 7.6M, food 7.6M, coin 4.8M plus items). Check this panel
  whenever the trade screen is open; the Recover button carries a
  red dot while a record waits.

## How it is done - plundering

- On Others' Trucks, tap the center of the truck body itself - the
  owner corrected side taps that missed the vehicle. Its card shows
  the owner, warzone, level, guard power, arrival countdown, rarity
  and cargo. Tapping the first truck ever also runs a one time Monica
  tutorial on Quick Plunder.
- Plunder! marches on the World Map. Quick Plunder fights on the spot
  with the preset squad and is otherwise identical, per the tutorial.
  Quick Plunder still opens a battle preparation screen - press
  Battle to fight. The yield is a random subset of the cargo, not
  all of it.
- The objective of plundering is to maximize the probability of
  winning UR shards - the purple 500 point badge stacks in a cargo
  list. Owner teach-in, evening of 2026-10-25, and now the standing
  target rule.
- Only UR and SSR trucks carry UR shards, so hunt only those. Color
  cue on the road view - gold is UR, purple is SSR (blue is SR,
  green is R, white is N).
- The target guard power must sit below this account highest squad -
  Squad 1 at 24.96M as observed. Lower is better.
- The more UR shard stacks in the load, the better, and position
  matters - a shard on the right side of the cargo row is much
  easier to win, while a shard in the leftmost or second from left
  slot is hard to plunder.
- 2026-11-02 1325 qualification, in favour of the newest verified
  record: a lone leftmost shard stack is NOT a no-go when the
  guard is trivial and the quota is short - the 1325 Quick Plunder
  against SSR #2092 [OOPz]hawk237 (Lv.25, guard 5.5M) won the full
  leftmost purple 500 UR shard stack x3. Position still governs
  probability, but it no longer disqualifies a trivial-guard target
  when the day's plunder quota is unfilled; take it rather than
  leaving the quota short.
- If no suitable target is on the road, tap the refresh button at
  the top right of the Others' Trucks screen to reroll the list and
  check again, repeating until a suitable target appears.
- A truck that was already plundered shows the taken items crossed
  out in its card - seen on a recheck of the same evening first
  target, whose two badge stacks were crossed and whose resources
  had dropped.
- Evidence the rule works, 2026-10-25 - the first three plunders of
  the evening, aimed at ordinary weak trucks before the teach-in,
  yielded 1 to 2 shards between them. The fourth, picked by the
  rule - a UR truck of another commander, Lv.30, guard
  16.5M, carrying three shard stacks - yielded badge 500 times 6
  plus an Extra badge times 3, nine shards in one fight.

## Cadence

- Daily caps. Dispatch - the header counts Today's Trade Count out of
  5, with four truck slots seen. Plunder - Your Plunder Count Today
  out of 4.
- Because journeys run about 4 to 5 hours, a second dispatch wave the
  same day is possible if the round is run early. Plunder whenever the
  daily round runs, targets permitting.

## Daily quotas - owner rule, 2026-10-30

- Every trade day, fill both counters in full - dispatch trucks
  until Today's Trade Count reads 5 of 5, and plunder until Your
  Plunder Count Today reads 4 of 4. The trade day follows the
  server day and resets at 19:00 local with the duel day. These
  are quotas to fill, not caps to stay under.
- Every trucks unit reads both counters on entering the trade
  screen and works the shortfall in this order - settle returned
  trucks first, then dispatch until the Trade Count is full, then
  plunder until the Plunder Count is full. The quality rules are
  unchanged - SR or above on non-UR days (free refresh first, then
  Trade Contract refreshes until reached), UR only through Mega
  Mode on UR days; plunder targets stay UR or SSR trucks carrying
  UR shards with guard power below Squad 1 and shards plentiful
  and right sided, refreshing the list at top right until a
  suitable target appears.
- The counters on the trade screen are the source of truth for
  the day's progress - never a tally derived across unit records.
  A unit that runs out of its 15 minutes with a quota unfilled
  records the live counters, stays partial, and the next trucks
  unit resumes the same shortfall.
- Entry failure does not close the day. When the trade slot has
  rotated out of the visible icon set, spend the unit on entry -
  identify which slot, if any, carries the blue truck-front icon
  with a red badge in the current set before tapping, and try the
  route flip described in How to enter. Later trucks units the
  same day keep trying; a quota still unfilled in the last hours
  of the trade day is a miss and is reported as one, with the
  reason, in the unit record and the round summary.
- First application, 2026-10-30 - the trade day that began
  2026-10-29 19:00 local stood at dispatch 1 of 5 and plunder
  0 of 4 at 05:29 local, after two units failed to enter the
  trade screen at all. A catch-up unit was enqueued the same
  morning to work the shortfall.
- Entry point corrected, 2026-10-30 13:05 unit - the blue
  truck-front icon with red badge 1 grounded at norm
  53,555 on that base view (the 07:50 unit's 52,620 did
  nothing; the column shifts, so re-ground it every unit),
  after a title-bar tap. The truck-panel dice centre
  grounds at norm 810,417 (taps near 380 hit its top edge
  and do nothing). That unit dispatched two trucks, both
  N free-refreshed to SR and SSR, moving Trade Count
  1 of 5 to 3 of 5 with no Trade Contract spent, and read
  Plunder Count 0 of 4 untouched at close.
- Icon identification corrected, 2026-10-30 evening
  (2052 and 2124 units) - enlarged crops of the left
  column show the light-blue front icon is a TRAIN
  front (windshield, headlights, cowcatcher), not a
  truck, and the white vehicle below it is a pickup.
  The column set green face / train / pickup / dish /
  hammer carries no trade slot, and tapping the train
  icon neither opens anything nor flips the set
  (verified twice, screenshots compared - the set is
  identical before and after). Both evening units
  failed to enter the trade screen at 53,555 and at
  55,582 while all four trucks were en route with no
  settlement pending. Unverified hypothesis: the
  trade slot surfaces in the column only while a
  returned truck awaits settlement - every successful
  entry on 2026-10-30 (1305, 1728, 2017) had one
  pending. Next trucks unit: check for a pending
  settlement first; if none, look for the trade
  entry on the World map or via the station area
  instead of re-tapping the train icon.
  Correction 2026-11-01 (0124 unit, below): this hypothesis is
  superseded - the trade slot entered with no returned truck
  pending. Availability follows the icon set, not settlement
  pending; the train-icon set above still carries no trade slot.

- Entry and dispatch, 2026-11-01 0124 unit (ticker-0104,
  window mode 642x951, no different-device dialog). Duel day
  7, Off day settlement, so non-UR rules apply: dispatch SR
  or above, plunder UR or SSR with guard below Squad 1 at
  24.96M. Outcome partial: three trucks dispatched, quota
  shortfall carried forward.
- Trade entry, corrected in-unit: a fresh crop of the left
  column shows the blue delivery-truck icon with red badge 4
  above the white pickup (Secret Command Post, badge 9) and
  the radar dish (badge 4). A tap at norm 55,630 snapped to
  the pickup and opened SECRET COMMAND POST instead; no
  secrets work was done there, and the screen was backed out
  at once. The retry used the freshly measured truck centre
  norm 55,596 with snap off, and the Intercity Trade screen
  opened. Lesson carried forward: the truck centre sits near
  norm y 596 in this icon set, and a snapped tap near 630
  lands on the pickup. Re-ground the centre every unit - the
  column shifts between sets and between days, and the
  2026-10-30 centres (53,555; 52,620; 55,582) do not transfer.
- Live counters on entry, current trade day (reset 19:00 on
  2026-10-31): Today's Trade Count 0/5, Your Plunder Count
  Today 1/4. Your Truck yard held four empty slots, no
  returned truck to settle, so the order was dispatch first
  (settle first, then dispatch, then plunder - with nothing
  to settle, dispatch leads). The 1/4 plunder figure was
  already on the counter at entry; its actor is unrecorded
  in the unit and is not attributed here.
- Dispatch 1: rolled UR as rolled, cargo iron 3.8M, food
  3.8M, coin 2.4M, arrives in 04:04:31, Escort Squad 1. First
  Let's Go tap at norm 335,925 missed low and closed the
  panel without dispatching; the panel was reopened and
  Let's Go tapped at its measured centre norm 340,875, and
  the count moved to 1/5 with a gold truck on the road. No
  refresh spent. Note the distinct centres: Let's Go at
  340,875 is not the truck-panel dice centre (810,417).
- Dispatch 2: rolled N, free refresh to R, then a 1 Trade
  Contract refresh to UR (stock 156 to 155), cargo 3.8M,
  3.8M, 2.4M, arrives in 04:29:12, Escort Squad 3. Let's Go
  at norm 340,875 moved the count to 2/5.
- Dispatch 3: rolled N, free refresh to SR (blue), cargo
  iron 2.5M, food 2.5M, coin 1.6M, arrives in 04:21:54,
  Escort Squad 2. Let's Go at norm 340,875 moved the count
  to 3/5. No contract spent on this truck.
- Close of unit, live counters: Trade Count 3/5, Plunder
  Count 1/4 (plunder not attempted in this unit - the pass
  budget closed first). One empty slot remains, plus the
  fifth dispatch after a truck returns. Shortfall carried
  forward: dispatch 2 more, plunder 3 more, before the
  19:00 deadline. Tracker untouched; the next trucks unit
  resumes the same shortfall.
- Correction to the 2026-10-30 evening hypothesis above:
  the trade slot does NOT surface only while a returned
  truck awaits settlement. The 0124 unit entered with four
  empty slots and nothing to settle, in a set carrying the
  blue delivery-truck icon above the pickup. The 2026-10-30
  evening observation stands only as a description of its
  own set (green face / train / pickup / dish / hammer
  carries no trade slot); it is not a general availability
  rule. When the trade slot is absent from the visible set,
  the set - not settlement pending - is what to investigate
  first.


## Scope and availability

- Rarities run N, R, SR, SSR, UR per the guides. All five observed in
  game by the evening of 2026-10-25. Road view colors - white N,
  green R, blue SR, purple SSR, gold UR. Higher rarity carries more
  and better cargo, and only SSR and UR carry UR shard stacks.
- Each truck can be plundered at most twice across the server, per the
  guides, unverified here.
- The list offers a filter that excludes trucks from the own warzone.
  It was on.
- Season scope unconfirmed - the trade screen is snowy in Season 2 and
  other players run golden trains as trade vehicles, so parts of this
  system may be season shaped. Truck trade itself is a permanent
  system per the guides.
- Mega Mode is a VIP privilege - the VIP screen lists Activate the
  Mega Mode of Trade Trucks among the VIP 13 privileges, and this
  account is VIP 13, so Mega Mode is unlocked here (confirmed
  2026-10-25 on the VIP screen, see
  [vip-rewards](../vip-rewards/INDEX.md)). What a Mega dispatch does
  differently is still unobserved. The fifth trade in the daily
  count of 5 may be a Mega dispatch - open question below.

## What is known from 2026-10-25

Observed in game on this account, first execution 2026-10-25.

- Dispatch one - rolled N, the single free refresh of the day rerolled
  it to SSR. Cargo - iron 3.0M, food 3.0M, coin 1.9M, plus chests,
  badges and items. Journey about 4 hours 7 minutes, Squad 1 escort.
- Dispatch two - rolled UR as rolled. Iron 3.8M, food 3.8M, coin 2.4M
  plus chests and badges. About 4 hours 39 minutes, Squad 3.
- Dispatch three - UR. Iron 3.8M, food 3.8M, coin 2.4M. About 4 hours
  52 minutes, Squad 2.
- Dispatch four - UR. Iron 3.8M, food 3.8M, coin 2.4M. About 4 hours
  53 minutes, Squad 4. Trade Count ended at 4 of 5.
- Plunder - one Quick Plunder against the N truck of another commander, the relevant warzone, Lv.28, guard power 7.6M. Won with no difficulty.
  Yield - iron 273.4K, food 273.4K, coin 173.9K, chest 20 and chest 20
  marked Extra, from a listed cargo of 1.0M iron, 1.0M food, 695.7K
  coin, two chest stacks and a badge stack that did not drop. Plunder
  Count ended at 1 of 4.
- Trade Contract stock seen in the train thank dialog the same day -
  127. None were spent.
- Evening arrival check (about 18:12 to 19:10) - all four trucks
  still out; two UR trucks looted en route by another commander (the relevant warzone) and another commander (the relevant warzone),
  their ledgers reduced to iron 2.8M, food 2.8M, coin 1.8M with two
  and three cargo items crossed out; the SSR and one UR intact. A
  Reward Recovery record for 2026-10-24 was claimed the same visit.
  Detail in the 1812 arrival check execution record.

Evening of 2026-10-25, new server day (detail in the 2047 evening
settlement and dispatch execution record).

- Settlement - the four noon trucks were found returned and were
  settled by opening their Truck Details one by one. SSR delivered
  in full (iron 3.0M, food 3.0M, coin 1.9M). The intact UR delivered
  in full (3.8M, 3.8M, 2.4M). The two looted UR trucks delivered
  2.8M, 2.8M, 1.8M each - Battle History showed another commander (131.6M)
  at 15:26:44 and another commander (124.6M) at 16:19:03, each
  having taken iron 951.8K, food 951.8K, coin 607.5K plus items; one
  item in one looter list was stamped Reclaimed.
- Reward Recovery - the 2026-10-25 19:00 record (1 unstarted
  transport) was claimed. Puzzle piece times 1, chest times 25,
  gold chest times 20, iron 1.5M, food 1.5M, coin 972.5K.
- Dispatches, Trade Count 0 of 5 to 4 of 5 - truck one rolled N, its
  free refresh made SSR (3.0M, 3.0M, 1.9M), Squad 1. Truck two
  rolled R, free refresh changed the cargo but kept R (2.0M, 2.0M,
  1.2M), Squad 3. Truck three rolled SR, its free refresh downgraded
  it to N (1.2M, 1.2M, 810.0K), Squad 2. Truck four rolled N, free
  refresh made SR (2.5M, 2.5M, 1.6M), Squad 4. Arrivals about 3
  hours 44 minutes to 4 hours 34 minutes out.
- Plunders, Plunder Count 0 of 4 to 4 of 4 - another commander N truck,
  Lv.29, guard 7.7M, won, iron 285.7K, food 285.7K, coin 180.2K,
  badge times 1 plus Extra badge times 1. another commander, Lv.27,
  guard 8.0M, won, 534.1K, 534.1K, 335.5K, chest times 20, badge
  times 1. A an alliance SSR truck, Lv.28, guard 13.9M, won, 655.7K,
  655.7K, 417.4K plus items. another commander UR truck,
  Lv.30, guard 16.5M, won, 951.8K, 951.8K, 607.5K, UR shards times
  6 plus Extra times 3. A another commander truck at guard 19.8M was
  inspected and passed over as too strong for the shard rule.

## Limits

- No diamond spending on refreshes, ever. Trade Contract spending
  on refreshes is allowed only under the standing non-UR day rule
  above (refresh until SR or above is reached); any other contract
  spending needs the owner approval.
- Plunder targets follow the shard rule above - UR or SSR trucks
  only, guard below Squad 1 power, shards plentiful and right sided.
  Do not plunder alliance mates, and stop at the daily cap.


## What the 2026-11-01 1053 unit added

- Unit trucks-2026-11-01-0657 by ticker-1034, session
  about 10:40 to 10:53, status partial. Duel day 7, Off
  day settlement, so non-UR rules apply: dispatch SR or
  above, plunder UR or SSR with guard below Squad 1 at
  24.96M. No different-device dialog.
- Entry, re-grounded fresh in-unit: the blue
  delivery-truck icon in a speech bubble with red badge 3
  sits above the white pickup and the radar dish; its
  measured centre norm 52,571 opened Intercity Trade at
  once with snap off. Foreground first: an observe call
  had flipped the target to a frontmost Chrome window, and
  a title-bar left-segment tap at norm 180,15
  re-foregrounded the game before the trade tap. This is
  the foreground pivot variant of the 2026-10-31 retro
  note, not a new rule.
- Live counters, current trade day (reset 19:00 on
  2026-10-31, ends 19:00 today): Today's Trade Count 3/5,
  read on the Your Truck tab, and Your Plunder Count
  Today 1/4, read on the Others' Trucks tab. These match
  the 0124 unit close exactly, so no counter moved between
  the two units and no contradiction stands. Your Truck
  road view showed the three trucks dispatched at 01:24
  still on the road (two gold, one blue - the UR, UR and
  SR dispatches of the 0124 unit) plus one empty dashed
  slot with a plus sign. No returned truck was presented
  for settlement; tapping a truck body opened no details
  card, same as the 2048 unit.
- Dispatch, blocked on the slot tap - audit class c, a
  tap-method blocker, not a red-line miss: the empty-slot
  plus sign was tapped at norm 714,414 and 714,418 (two
  no-change taps), then at 714,460, then double-clicked
  at 714,418 - every tap showed no change on the second
  observation. No dispatch panel opened, so no roll, no
  refresh and no Trade Contract was spent, and no truck
  was dispatched in this unit. This refines the standing
  "tap a free slot plus sign" step: those points, in the
  current window, did not open the panel. The next trucks
  unit must arrive with a changed method (a
  foreground-first tap, or a re-measured slot point in
  the current 763 by 1050 window) rather than repeating
  these points. The window geometry itself is new against
  the standing 642 by 951 window - coordinates here are
  norm, so they transfer in proportion, but slot points
  must still be re-measured fresh each unit.
- Plunder was not attempted: the unit budget closed on
  the dispatch block, so the plunder shortfall stands.
  Outcome partial, counters unchanged at dispatch 3/5
  and plunder 1/4. Shortfall carried forward: dispatch 2
  more, plunder 3 more, before the 19:00 deadline.
  Tracker untouched; the next trucks unit resumes the
  same shortfall. Nothing paid, no diamonds spent, no
  Mega Mode used, no alliance mate plundered. Game left
  on the trade screen, Your Truck tab.

## What the 2026-11-01 1352 unit added

- Unit trucks-2026-11-01-1057 by ticker-1334, session
  about 13:46 to 14:00, status partial. Duel day 7, Off
  day settlement, so non-UR rules apply: dispatch SR or
  above, plunder UR or SSR trucks carrying UR shards with
  guard below Squad 1 at 24.96M. No different-device dialog.
- Entry, re-grounded fresh in-unit: the blue
  delivery-truck icon in a speech bubble with red badge 3
  sits at norm 48,565 and opened Intercity Trade at once.
  Slot points shift between units - the 1053 centre
  52,571 and this 48,565 differ - so re-measure the entry
  icon fresh each unit, never reuse a prior point.
- Live counters at entry, current trade day ending 19:00
  today: Today's Trade Count 3 of 5, Your Plunder Count
  Today 1 of 4, matching the 1053 unit exactly, so no
  counter moved between the two units.
- Dispatch, 1053 blocker closed: the empty-slot plus sign
  was re-measured fresh at norm 625,440 and opened the
  truck panel at once. This closes the 1053 tap blocker -
  the 1053 points near 714 failed in that window, but the
  step itself works when the point is measured in the
  current window. The standing rule stands: measure the
  plus sign fresh each unit, never reuse old points.
- Rolls in this unit: the panel first rolled R (iron
  2.0M, food 2.0M, coin 1.2M, Squad 4 escort). A free
  refresh downgraded it to N (iron 1.2M, food 1.2M, coin
  810.0K). Two Trade Contract refreshes followed, R then
  SR, spending 2 contracts (stock 155 to 153). The SR roll
  (iron 2.5M, food 2.5M, coin 1.6M, arrives in 03:43:56,
  Squad 4) was dispatched at once with Let's Go, not Mega
  Mode. Trade Count read live after dispatch: 4 of 5.
- Plunder, shortfall carried forward: Plunder Count read
  live 1 of 4, unchanged. First list inspected: SSR
  #2104 [GOMP]4FINGAZ, Lv.27, guard 15.5M, passed over
  because its cargo shows no UR shard stacks; a second
  card, #2091 [OlyM]Conan416, Lv.28, guard 79.6M, passed
  over as far above Squad 1. The list was refreshed once.
  On the new list the two purple SSR trucks at the top of
  the road did not open their cards after two corrected
  taps (norm 400,225 then 400,240), so no further target
  could be inspected in this unit. This is a tap-method
  blocker (audit class c): the next trucks unit must
  arrive with a changed method for top-of-road trucks
  (element tap, or a re-measured body centre after the
  toast banner clears) rather than repeating these points.
- Outcome partial, counters at close read live: dispatch
  4 of 5, plunder 1 of 4. Shortfall carried forward:
  dispatch 1 more and plunder 3 more before the 19:00
  deadline. Tracker untouched; the next trucks unit
  resumes the same shortfall. No plunder fought, no
  alliance mate plundered, no Mega Mode used, no diamonds
  spent. Game left on the trade screen, Others' Trucks tab.

## Unresolved counter tension - 2026-11-01 1813 incidental read

- The 1813 train unit opened the trucks view by a mis-tap
  on the left column (see alliance-train 1.8.0) and read
  Today's Trade Count 0/5 there. That read conflicts with
  the trucks 1352 close the same trade day (dispatch 4 of
  5, plunder 1 of 4), and no trucks unit ran between the
  two reads, so no dispatch, plunder or reset explains a
  move from 4 to 0 before the 19:00 reset.
- Second read, same tension: the 1849 final zero sweep read
  Today's Trade Count 0/5 again on the truck screen at
  about 18:35, and recorded it as read, not reconciled,
  against the same 13:52 4/5 read. Two post-1352 reads now
  show 0/5, both from non-trucks-unit entries, and neither
  explains a move from 4 to 0 before the 19:00 reset.
- The 0/5 reads are recorded here as an unresolved tension,
  NOT as a quota update: the trade-screen counters from
  trucks units remain the source of truth for the quota,
  and the standing shortfall stays dispatch 1 more and
  plunder 3 more before the 19:00 deadline. The next trucks
  unit must re-read both counters live on the trade screen
  and explain the discrepancy in its record - whether the
  mis-tap view showed a different counter, a different tab,
  or a genuine reset - before any counter is overwritten.
- Retro addendum, 2026-11-01 daily retro: the unit that
  could have resolved the tension, trucks 1457, expired
  unexecuted at 18:57 local (afternoon starvation, not
  outage - the ticker executed other units through the
  afternoon), and the sweep fix-ups expired at the
  19:00 reset with it. The Nov 1 trade day therefore
  closes with the tension unresolved: dispatch unknown
  between 0 and 4 of 5, plunder 1 of 4 on the last
  trucks-unit read. Next trucks unit instruction
  restated: open on the trade screen first, read both
  counters live, and name the reconciliation in its
  record before dispatching or plundering anything.
  Tracked in retro issue #148; the sweep fix-up
  expiry in issue #147.



## What the 2026-11-01 2231 unit added

- Unit trucks-2026-11-01-1857 by ticker-2212, session
  about 22:21 to 22:31, status partial. Tracker untouched,
  as partial units do not mark the tracker. Game left on
  the trade screen, Others' Trucks tab.
- First trucks unit of the new trade day (began 19:00
  local), and the counter-tension resolution: at entry,
  Today's Trade Count 0 of 5, Your Plunder Count Today
  0 of 4, read live on the trade screen by a trucks unit
  - the read the retro addendum required. No returned
  truck awaited settlement - the Your Truck yard held
  four empty slots. The 0/5 entry counters are the new
  trade day's reset counters, not a revision of the
  ended day: the ended day's tension (1352 close 4/5
  against the 1813 and 1849 incidental 0/5 reads)
  closed unresolved at the 19:00 reset with trucks 1457
  expired, and this unit's counters belong to the new
  day. The old tension is therefore closed as
  unresolvable for the ended day, not carried as a live
  shortfall - the live shortfall is this unit's close
  (see below). Tracked in retro issues #147 and #148;
  no new issue filed here.
- Entry re-grounded fresh: the base left column
  re-grounded from an enlarged crop - the blue
  delivery-truck icon in a speech bubble with red badge
  4 sits at norm [55,584] (the 1352 point [48,565] has
  shifted with the column) and opened Intercity Trade at
  once. The white pickup below it (badge 8) is the Secret
  Command Post vehicle, not the trade truck - a
  look-alike note for the next entry.
- Dispatch, one truck sent: the first empty-slot plus
  sign measured fresh at norm [335,442] opened the truck
  panel at once. The panel rolled SR as rolled - iron
  2.5M, food 2.5M, coin 1.6M, arrives in 04:11:18, Squad 1
  escort. The free refresh was deliberately not spent:
  SR already meets the non-UR day bar. Let's Go raised
  the expected TIPS dialog (low rarity, free refresh
  remaining); Confirm departed as rolled, not Mega Mode.
  No diamonds spent, no Trade Contract spent. Duel-day
  rule in force: duel day 1, Radar Training (radar
  release day), so non-UR rules apply - dispatch SR or
  above, plunder UR or SSR trucks carrying UR shards
  with guard below Squad 1.
- Plunder, one fight won: changed method for opening
  road trucks (R2, after the 1352 top-of-road failures)
  - the purple SSR truck body centre at norm [545,326]
  opened its card at once. Target: SSR #2091 [SS12]
  goobiedog, Lv.27, guard 3.6M (screenshot read; the
  compact OCR garble "73.6M" is wrong), cargo with two
  UR shard 500 stacks x3 each on the right side. Guard
  far below Squad 1 at 24.96M, so the shard rule is met.
  Quick Plunder, Battle at 25.12M vs 3.66M, Mission
  Completed. Loot, read live on the victory screen:
  iron 557.5K, food 557.5K, coin 350.0K, UR badge 500 x6,
  puzzle piece x1. No alliance mate plundered (the gold
  [AP3x]Skinner Box train on the road was left alone).
- Close counters read live: Trade Count 1 of 5, Plunder
  Count 1 of 4. Shortfall carried forward: dispatch 4
  more, plunder 3 more before the trade day ends 19:00
  on 2026-11-02.

## What the 2026-11-02 0114 unit added - entry blocker, partial

- Unit trucks-2026-11-01-2257 by ticker-0104, session
  about 01:09 to 01:13, status partial: the trade screen
  could not be entered, so no counter was read live, no
  truck was dispatched and no plunder was made. Tracker
  untouched (partial units do not mark the tracker).
  Blocker category e (repeated blocker, entry method).
- Column set on this view, re-grounded fresh on the
  current screenshot, top to bottom: green face, blue
  bus/train-front icon, white pickup (red badge 8),
  walkie-talkie (red badge 2), hammer, chest. No icon in
  the column carries a speech-bubble delivery-truck
  glyph with a badge in this view, unlike the 22:31
  unit's [55,584] entry point. This is the column-set
  flip already recorded for 2026-10-30 evening: the
  current set carries no trade slot, and the flip
  control that summons the trade set is still unknown.
- Taps tried, all with no screen change, and NOT to be
  repeated by the successor under queue rule R2:
  [53,595] snapped; [53,555] snapped; [55,584] with snap
  disabled (the 22:31 unit's successful method);
  title-bar tap [180,15] followed by [55,584] snap
  disabled (the 1053 unit's foregrounding variant).
  Successor instruction from the unit record: try a
  different entry route first - the World map trade
  entry or the station area - and re-ground the column
  from a fresh screenshot before any column tap. If the
  column set has flipped, identify the flip control
  before tapping a vehicle icon.
- Quota carried from the 22:31 unit on 2026-11-01, NOT
  re-read live here: Trade Count 1 of 5, Plunder Count
  1 of 4 at that unit's close, trade day ending 19:00 on
  2026-11-02. Shortfall still open: dispatch 4 more,
  plunder 3 more before the day ends. Duel posture for
  this day: Duel day 1, Radar Training (radar release
  day), so non-UR rules apply - dispatch SR or above
  only, plunder UR or SSR trucks carrying UR shards
  with guard below Squad 1.
  Evidence in `_records_/2026-11-02/truck-plunder/0114-queue-run.md`.

## What the 2026-11-02 0416 unit added - trade entry corrected, quotas 3 of 5 and 2 of 4

- Unit trucks-2026-11-02-0257 by ticker-0404, session
  about 04:05 to 04:16, status partial: the trade-day
  quotas are not yet full, so the tracker is untouched
  (partial units do not mark the tracker).
- ENTRY CORRECTION, in favour of the newest verified
  record, superseding the 0114 section above: in this
  column set the train-front icon IS the trade entry.
  The column was re-grounded fresh on the live base
  screenshot - green face [54,493], light-blue
  train-front icon [52,552], white pickup [54,617] -
  and the route that worked was a title-bar tap
  [180,15] first, followed by a tap on the freshly
  grounded train-front centre [52,552], which opened
  Intercity Trade at once. Correction to the 0114
  record and to the 2026-10-30 evening finding: the
  0114 taps at [55,584] missed the centre by about 30
  pixels vertically, and the snapped [53,555] tap
  predates the foregrounding variant, so the 0114
  failure was point plus foregrounding, not a missing
  slot - the set the 0114 unit read as slot-less does
  carry the trade entry. The World map route was tried
  first and rejected: it showed alliance bases and no
  trade entry, so the game was returned to base.
  Successor instruction: re-ground the icon fresh every
  unit, and use the title-bar foregrounding tap before
  the icon tap if a background tap does nothing.
- Proximity note, not a settled identity: this
  train-front point [52,552] sits 4 pixels from the
  alliance-train profile's station icon point (52,548).
  Whether the two units tapped the same column slot
  acting differently by context, or two neighbouring
  icons, is unresolved - do not copy one profile's
  point into the other unit's entry step without
  verifying the screen that opens.
- Counters, read live: at trade-screen entry Today's
  Trade Count 1 of 5 and Your Plunder Count Today 1
  of 4; after settling the returned truck and
  dispatching twice, Trade Count 3 of 5; after the
  plunder below, Plunder Count 2 of 4. Shortfall
  carried forward: dispatch 2 more, plunder 2 more
  before the trade day ends 19:00 on 2026-11-02.
- Settlement, one returned truck: the 22:31 SR truck
  returned, Squad 1 escort, iron 2.5M, food 2.5M, coin
  1.6M, chests 20 plus 20 plus 20, red gem 50 x1, badge
  500 x1, status line "The vehicle is safe and
  secure" - not plundered en route. This matches the
  22:31 dispatch, so the settlement is verified, not
  assumed.
- Dispatch, two trucks sent: slot one rolled N (iron
  1.2M, food 1.2M, coin 810K, Squad 1), free refresh to
  R, then one Trade Contract refresh to SSR (iron
  3.0M, food 3.0M, coin 1.9M, arrives 04:21:54, Squad
  1), dispatched at once. Slot two rolled SSR as
  rolled (same cargo, arrives 03:58:30, Squad 3); the
  free refresh was deliberately not spent, and no TIPS
  dialog appeared on Let's Go. Slot three left open on
  an N roll (iron 1.2M, food 1.2M, coin 810K, Squad 2)
  after a free refresh to R and one Trade Contract
  refresh back to N; the next trucks unit continues it
  with contract refreshes until SR or above, per the
  standing rule. Trade Contract stock 163 to 161, two
  spent in this unit, no diamonds spent, no paid
  button tapped.
- Plunder, one fight won: first card checked and
  rejected under the shard rule - SSR #2092 [NROM]
  Masoncy, Lv.27, guard 11.9M, cargo gold bars, chests
  and resources but no UR shard 500 stacks. Second
  card, after one list refresh: SSR #2088, Lv.26,
  guard 3.3M (screenshot read; the compact OCR
  "73.3M" is wrong, the same garble pattern as the
  2231 unit's "73.6M"), cargo with three UR shard 500
  stacks x3 each, guard far below Squad 1 at 24.96M,
  so the shard rule is met. Quick Plunder, Battle at
  25.12M vs 3.38M, Mission Completed. Loot, read live
  on the victory screen: iron 531.5K, food 531.5K,
  coin 337.0K, UR badge 500 x9, Extra red gem x1. No
  alliance mate plundered (the gold [AP3x] train on
  the road was left alone). A stray tap meant for
  empty road opened the red gem 100 tooltip ("100
  Diamonds, Owned: 905") - harmless, no Use tapped,
  no diamonds spent.
  Evidence in `_records_/2026-11-02/truck-plunder/0416-queue-run.md`.


## What the 2026-11-02 0935 unit added

- Unit trucks-2026-11-02-0657 by ticker-0934, session about
  09:35 to 09:48, status partial: the dispatch quota is
  filled but the plunder quota is not, so the tracker is
  untouched. Evidence in
  `_records_/2026-11-02/truck-plunder/0935-queue-run.md`.
- Entry: the game was found on the Events hub Code 87 page.
  The hub back arrow only responded once its centre was
  re-measured at norm (158,947); earlier taps near
  (97,906) missed the button. Lesson repeated from the
  dice button: tap measured centres, not edges. This
  bears on the event-claims hub back-arrow open question
  - point accuracy, not background clicks alone, may be
  the cause there too.
- Trade entry: the badged icon in the left column,
  grounded at norm (51,571) with badge 2 at entry. A tap
  at (54,546), near the top edge of the same icon, did
  nothing; the centre tap opened Intercity Trade directly
  on the Your Truck view. The game window had been moved
  to x1270 so its left column cleared the covering Chrome
  window; it was restored to 79,30 at unit close.
- Counters, read live: at trade-screen entry Today's Trade
  Count 3 of 5, Your Plunder Count Today 2 of 4 (the same
  counters the 0416 unit closed with); at close Trade
  Count 5 of 5, Plunder Count 2 of 4, and the screen
  confirms "No more dispatches available." No returned
  truck awaited settlement: the road showed two SSR
  trucks out and two empty slots, and the screen carried
  no settlement prompt.
- Dispatches (2, quota filled): Slot 1 rolled N (iron
  1.2M, food 1.2M, coin 810.0K); the free refresh rerolled
  it to SR (iron 2.5M, food 2.5M, coin 1.6M); dispatched
  at once, Squad 2 escort, Trade Count 3 of 5 to 4 of 5.
  Slot 2 rolled SSR as rolled (iron 3.0M, food 3.0M, coin
  1.9M); the free refresh was deliberately not spent;
  dispatched at once, Squad 4 escort, Trade Count 4 of 5
  to 5 of 5. Trade Contracts spent: 0. No diamonds spent,
  no paid button tapped.
- Plunder (0 this unit, shortfall 2 remains): one target
  inspected and passed - SSR #2092 [SOVN]bassslayer,
  Lv.26, guard 5.7M, arriving in about 1 hour. Its cargo
  row showed chests, iron 1.5M, food 1.5M, coin 1.0M and
  three crossed-out slots, with no UR shard stack visible,
  so it fails the shard rule and was left alone. The
  golden train on the road ([MYpp] train) was not
  inspected: it stays a candidate for the next unit's
  shard hunt (it is not an alliance train, but its cargo
  was never read). Reason the shortfall stands: the
  unit's 15 minutes were spent on entry and the two
  dispatches; no battle was started rather than overrun
  the unit cap. The next trucks unit works the plunder
  shortfall first, hunting a UR or SSR truck with
  visible, right-sided UR shard stacks. The trade day
  ends at 19:00 local, so the shortfall is not a
  last-hour miss.
- Duel posture: Duel day 1, Radar Training (radar release
  day), from tools/duel.py at unit start. Non-UR day
  rules applied: dispatch SR or above only (free refresh
  first, then Trade Contracts until reached), plunder UR
  or SSR trucks carrying UR shards with guard below
  Squad 1.

## What the 2026-11-02 1325 unit added - leftmost shard stack pays in full

- Unit trucks-2026-11-02-1057 by ticker-1307, session
  about 13:07 to 13:25, status partial: one plunder done,
  one plunder shortfall remains, so the tracker is
  untouched (partial units do not mark the tracker).
  The next trucks unit resumes the last plunder; the
  trade day ends at 19:00 local. Evidence in
  `_records_/2026-11-02/truck-plunder/1325-queue-run.md`.
- Duel posture: Duel day 1, Radar Training (radar
  release day), from tools/duel.py at unit start.
  Non-UR day rules applied: dispatch SR or above only,
  plunder UR or SSR trucks carrying UR shards with
  guard below Squad 1.
- Entry: the game was found on the Mall Monthly Pass
  page (left over from the passes unit). The $24.99
  Monthly Pass Extension and every other price tag were
  left untouched. The back arrow at the screen corner
  returned the game to the base; the first corner tap
  only opened a small avatar badge, the second tap at
  the arrow itself went back - the same corner-tap
  hazard as the 0844 train unit's avatar circle and the
  1226 mail unit's back-arrow centre. Background input
  reached the game throughout.
- Trade entry: the badged icon in the left column,
  grounded at norm 52,553 (badge 2 at entry); the
  centre tap opened Intercity Trade directly on the
  Your Truck view. This matches the 0935 grounding
  (51,571) within column shift, and sits 5 pixels from
  the alliance-train station point (52,548) - the third
  near-coincidence (0416: 52,552; 1325: 52,553) for the
  open identity question, still unresolved: do not copy
  one profile's point into the other unit's entry step
  without verifying the screen that opens.
- Counters, read live: at trade-screen entry Today's
  Trade Count 5 of 5 ("No more dispatches available"),
  Your Plunder Count Today 2 of 4 (the same counters
  the 0935 unit closed with); at close Today's Trade
  Count 5 of 5, Your Plunder Count Today 3 of 4, read
  live on the Others' Trucks header after the battle.
- Settlement and dispatch: no returned truck awaited
  settlement - the Your Truck road showed four trucks
  out (two SSR, one SR, one purple with a flame marker)
  and no settlement prompt. No dispatch: Trade Count
  already 5 of 5.
- Plunder (1 this unit, shortfall 1 remains): inspected
  and passed, first list: UR #2088 [OFAJ] Lv.27, guard
  11.5M, arrives in 03:44. Cargo: gold chest x10 twice,
  puzzle x1, iron 2.1M, food 2.1M, coin 1.3M, two slots
  already crossed out. No purple 500 UR shard stack
  visible, so it fails the shard rule and was left
  alone. Inspected and passed, first list: SSR #2088
  [4017] Lv.30, guard 24.8M, arrives in 03:33. Cargo:
  blue chest x1, gold chest x10, gold bar x1 twice, red
  gem x100 x1, puzzle x1, iron 3.0M, food 3.0M. No
  purple 500 UR shard stack visible, and the guard sits
  only just below Squad 1, so it was left alone. List
  refreshed once (top-right refresh, free) and
  inspected: SSR #2092 [OOPz]hawk237, Lv.25, guard
  5.5M, arrives in 02:33. Cargo carries one purple 500
  UR shard stack x3 in the leftmost slot, plus chest
  x25, gold chest x10, iron 2.0M, food 2.0M. Guard far
  below Squad 1 (25.12M in the battle prep screen),
  not an alliance mate, own-warzone filter on.
  Plundered by Quick Plunder.
- Battle: Squad 1 25.12M vs guard 5.53M, easy win -
  the battle-screen Squad 1 figure matches the 0416
  battle read. Rewards read live on the Mission
  Completed screen: iron 505.5K, food 505.5K, coin
  324.0K, 5-minute speedups 2 plus 1 plus 2 plus 3 plus
  2, puzzle x1, chest x25, and Extra purple 500 UR
  shard x3 - the full leftmost shard stack dropped
  despite the hard position.
- SHARD-RULE QUALIFICATION, in favour of the newest
  verified record, superseding any reading of the
  position rule as a disqualifier: a leftmost single
  stack is not a no-go when the guard is trivial and
  the quota is short; it paid all 3. Position still
  governs probability, but it no longer disqualifies a
  trivial-guard target when the day's plunder quota is
  unfilled - take it rather than leaving the quota
  short. The standing rule text above is qualified
  accordingly, not silently overwritten.
- Card UI notes: the side arrows on the truck card did
  not page to the next truck (one no-change tap, not
  repeated); tapping another truck body on the road
  switched the card instead. Tapping empty road did not
  close the card.
- Outcome: status partial, plunder shortfall 1 remains.
  Red lines held: no diamonds, no Trade Contracts, no
  paid button, no alliance mate plundered. The 6-hour
  quota checkpoint (13:00) found the plunder quota
  short, so the next trucks unit (1457 slot) is raised
  to priority 1 under queue rule R3.
- Zombie seeding: not enqueued. The Zombie Invasion
  event ended 2026-10-30 and the Events hub carries no
  Zombie page; the chain stands at 66 done units with
  no pending unit, and no new chain was seeded on an
  ended event.

## Open questions

- What a Mega dispatch does differently, and what the fifth daily
  trade is. Mega Mode itself is a VIP 13 privilege, unlocked on this
  account. The owner dispatch rule for Alliance Duel UR days (Mega
  Mode, UR trucks only) is recorded above but not yet executed.
- Whether the 2026-10-25 Alliance Duel day scored UR truck
  dispatches - the daily duel category was not verified that day,
  so the evening dispatches ran under normal day handling.
- Whether the collapsed 2026-10-20 Reward Recovery record was
  already claimed - its toggle did not expand on 2026-10-25.
- What flips the base left-column icon set to the set that carries the trade slot - the 0114 unit's set (green face / bus-train-front / pickup / walkie-talkie / hammer / chest) carries no speech-bubble truck glyph, and the 22:31 entry point [55,584] does not transfer to it. (2026-11-02 0416 update: for this set the premise is corrected - the train-front icon at [52,552], reached after a title-bar foregrounding tap, is the trade entry; the flip question remains for sets where no train-front icon is present.)
