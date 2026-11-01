---
title: Truck Plunder
created: 2026-10-25T20:12:00Z
modified: 2026-11-01T09:36:45Z
level: L1
version: 1.9.0
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
