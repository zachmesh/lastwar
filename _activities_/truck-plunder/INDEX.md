---
title: Truck Plunder
created: 2026-10-25T20:12:00Z
modified: 2026-11-11T05:32:17Z
level: L1
version: 1.41.0
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
  - source: ticker-2104 truck-plunder execution record 2026-11-02 2120 queue run (partial, station-tap entry, counters 4/5 and 4/4, fifth dispatch shortfall)
  - source: ticker-2334 truck-plunder execution record 2026-11-02 2347 queue run (partial, station-tap entry failed, counters not read)
  - source: ticker-0334 truck-plunder execution record 2026-11-03 0344 queue run (partial, station-tap entry failed again, grounding mislabels Furnace and Wall)
  - source: ticker-0334 secret-missions execution record 2026-11-03 0346 queue run (done, unsnapped exact-centre entry lesson; incidental live trade counters 4/5)
  - source: ticker-1204 truck-plunder execution record 2026-11-03 1211 queue run (done, trade quota 5 of 5 and plunder quota 4 of 4 full, UR dispatched as rolled)
  - source: ticker-1834 truck-plunder execution record 2026-11-03 1846 queue run (partial, new trade day 0 of 5 and 0 of 4 at 18:34 entry, 3 dispatches, 2 plunders, trade counters reset with the about-18:00 rollover, Issue #242 follow-up)
  - source: ticker-0234 truck-plunder execution record 2026-11-04 0242 queue run (done, quotas full at entry, WORLD-corner entry route)
  - source: ticker-0534 truck-plunder execution record 2026-11-04 0538 queue run (done, quotas full at entry, badged vehicle icon entry, WORLD-corner route qualified)
  - source: ticker-0834 truck-plunder execution record 2026-11-04 0845 queue run (done, quotas full 5/5 and 4/4 at entry, trade-icon grounding mislabel opens Secret Command Post)
  - source: pre-reset zero sweep execution record 2026-11-07 1824 queue run (first pass, trucks line 18 unverified, both R3 checkpoints passed with the counts unread; record commit 840094b6ad on records/2026-11-07)
  - source: ticker-0404 perception-scout execution record 2026-11-08 0415 queue run (partial, alliance remainder, Trucks panel reached by entry tap)
  - source: ticker-0504 perception-scout execution record 2026-11-08 0512 queue run (done, bus icon tap-verified Trucks, dot clears on open, record commit 111f7e954 on records/2026-11-08)
  - source: ticker-0534 perception-scout execution record 2026-11-08 0542 queue run (done, blue truck/bus icon is Trucks, 0/5 trades, 4 own + 4 others waiting, 0022 white-truck mapping corrected); record commit 707bcec0d8 on records/2026-11-08
  - source: ticker-0534 truck-plunder execution record 2026-11-09 0541 queue run (partial, trade entry blocked in current column set, both methods failed, WORLD-corner route re-confirms the 0538 correction, counters not re-read, shortfall carried 4/5 and 1/4; record commit a9b838c5ed on records/2026-11-09)
  - source: zero-sweep 002 execution record 2026-11-09 1748 queue run (partial, 5 of 23 ledger lines read live, trucks 4/5 dispatch 1/4 plunder live, trade entry route measured in the current icon set; record commit 2f4d783d8 on records/2026-11-09)
  - source: ticker-1910 sync record 2026-11-09 (trucks-2026-11-09-1457 fix-up expired unrun, window passed before execution, reaped 19:14 in the ticker-1910 pass; record commit e05c662bd on records/2026-11-09)
  - source: ticker-2230 truck-plunder execution record 2026-11-09 2250 queue run (partial, 4 returned trucks settled 2 UR + 2 SR, 2026-11-9 18:00 Reward Recovery claimed, Trade Count 0/5 on the new trade day, dispatch 5 UR and plunder 4 fall to the next unit; record commit 70248cbb7 on records/2026-11-09)
  - source: ticker-0234 truck-plunder execution record 2026-11-10 0248 queue run (partial, first Mega Mode execution end to end on a UR day, 4 UR dispatched, 1 plunder won, Trade Count 4/5, Plunder Count 1/4; record commit 2802653981 on records/2026-11-10)
  - source: ticker-0504 truck-plunder execution record 2026-11-10 0513 queue run (partial, Reward Recovery 2026-11-7 record claimed, 1 SSR plunder won, Trade Count 4/5, Plunder Count 2/4; record commit 19608e2c9e on records/2026-11-10)
  - source: ticker-0334 troop-training execution record 2026-11-10 0337 queue run (partial, Duel screen read live inside the training unit - Dispatch UR Trade Truck +300,000, Perform 1 UR Secret Task +225,000, superseding the 100,000 Handbook rate; record commit b7e79a62 on records/2026-11-10)
  - source: ticker-1343 truck-plunder execution record 2026-11-10 1411 queue run (partial, all 4 returned UR trucks settled HUD-verified, Trade Count 4/5, Plunder Count not re-read, 5th dispatch and plunders resume next unit; record commit b2c2b7a43 on records/2026-11-10)
  - source: 2026-11-10 daily retro, execution-knowledge action A-2026-11-10-01 (Issue #300): never write an expected or Handbook-rate score into stats.points; points holds live-read scored gains only
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
- Station-building entry, measured 2026-11-02 (2120 unit):
  with the column set carrying no trade slot (green face /
  pickup / dish / hammer), fresh visual grounding put the
  station building at norm 352-630 x 105-285, and a tap at
  its centre [491,195] opened Intercity Trade directly on
  the Others' Trucks view, with no settlement pending.
  Use this route before hunting the column set flip when
  the column carries no trade slot.
- Station-tap qualification, 2026-11-03 (0344 unit): the
  [491,195] station tap is no-change for the second
  consecutive trucks unit after 2347, so it must not be
  re-tapped blindly. Fresh grounding in the same unit
  mislabelled buildings as the station: [488,378]
  selected High-temp Furnace Lv.30, [637,170] selected
  Wall Lv.26 with the same unidentified two-button popup
  (home icon, up arrow) seen at 2347, and [357,200] was
  no-change. Do not re-tap [491,195], [488,378],
  [637,170] or [357,200] blindly. Next variant, from the
  same pass (see the 0344 section below): an unsnapped
  exact-centre tap on the trade icon, not a snapped tap
  on a grounded station point - snapped taps in the left
  column mis-route, as the 0346 secrets unit proved.
- Working entry route, 2026-11-03 (0821 unit): on the
  current base framing, the left-column icon at norm
  53,555 - the speech-bubble icon above the truck slot
  in that set - opened Intercity Trade directly. This
  route was not tried in the 0344 unit and resolves the
  entry blocker tracked as Issue #218; the next unit
  reopens the trade screen by this route first. The
  truck icon at norm 53,657 opened Secret Command Post
  (Secret Mobile Squad, Your Tasks, Mega Refresh and
  Mega Deploy buttons - none tapped), not trade: do not
  use it for trade entry. The old station points from
  the 0344 unit were not re-tapped. Detail in the 0821
  section below.
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

- 2026-11-03 1211 unit: the badged vehicle icon at norm
  55,589 opened Intercity Trade on the first tap, on the
  Others' Trucks view. This settles the stale-window
  question left by the 2026-10-30 evening units: the icon
  they found dead opens the trade screen when it carries
  a badge. Find it by the badge and the vehicle-front
  glyph, not by a fixed point - the column set rotates.
- 2026-11-03 1846 unit: the same badged vehicle-front icon
  at norm 54,568 opened Intercity Trade directly on the
  Your Truck view on the first tap, confirming the 1211
  route a second time at a nearby point in a different
  column set (hammer 2/4, flasks 1/2, green face, badged
  vehicle-front, white pickup badge 9, radar dish badge 4,
  hammer, chest). Find it by badge and glyph, not by a
  fixed point.

- Working entry route, 2026-11-04 (0242 unit): when the left-column vehicle-front icon carries NO badge, it does not open trade - a tap at norm 54,568 only panned the base map and a tap at the grounded centre 55,578 did nothing, matching the 2026-10-30 evening no-badge pattern. The route that worked: a tap at norm 913,940, on the bottom-right WORLD corner of the base screen, opened Intercity Trade directly on the Others' Trucks view. Next trucks units try this WORLD-corner route first when the column icon carries no badge. The mechanism (why that corner opens trade) is unverified, only the observed result. (2026-11-09 0541 correction: the WORLD-corner route is NOT a direct trade entry - the 0538 unit's tap at 913,940 opened the World map, not trade, and the 0541 unit re-tried it and again reached only the World map. The standing instruction above to try the WORLD-corner route first is superseded; do not cite 913,940 as a trade entry. The badgeless-icon rule itself stands - the 0541 tap at the grounded train-front centre (55,594) only panned the base map, a third confirmation of the rule after 0242 and the 2026-10-30 evening pattern.) Do not re-tap the station building at 592,189 blindly: it produced no change in this framing, a third framing failure for station taps after 2347 and 0344. Detail in the 0242 section below.
- Working entry route, 2026-11-09 (1748 zero-sweep read, 17:40): in the current icon set the blue truck-front icon at norm y about 573 opens Intercity Trade directly on the first tap; the jeep icon below it is the Secret Command Post, not trade. This resolves the entry block the 0541 unit hit in the same day's earlier column set (badgeless train-front icon only panned the map, WORLD-corner route opened only the World map). Find the trade icon by glyph and badge, not by a fixed point - the column set rotates; re-ground fresh in every unit.
- Working entry route, 2026-11-09 (2250 trucks unit, about 22:31): the trade icon - blue circle, white truck glyph, red badge 4 - grounded fresh at norm (55,575) in the base left column, opened Intercity Trade on the Your Truck tab on the first tap. Third badged-icon entry datapoint in two days (1211 at 55,589, 1846 at 54,568); the point drifts with the column set, so re-ground fresh in every unit.

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
- Mega Mode dispatch (UR days), observed end to end 2026-11-10 (0248 unit, Issue #565): on the Your Truck tab the Mega Mode button opens two tabs. Mega Refresh lists the four slot rolls with rarity and journey time (0248 rolls: No.1 R 04:08:02, No.2 N 03:40:04, No.3 N 03:48:04, No.4 N 04:26:21 - none UR, so all four needed refreshes). A first refresh costs 3 Trade Contracts per truck (dialog-confirmed before spending); a re-refresh of an already-refreshed truck costs 1 (inferred from the button readings 9/158, 6/149, 3/149, 1/146). The 0248 unit spent 12 contracts in total (stock 158 to 146) and all four rerolled UR (No.1 04:37:27, No.2 04:16:08, No.4 03:42:29, No.3 03:53:44). The "Refresh all to Reindeer Sleigh Ride" checkbox was left unchecked; what it does is unobserved. Mega Dispatch shows preassigned escorts (Squad 1 25.20M, Squad 3 20.37M, Squad 2 19.08M, Squad 4 16.54M); Select All, Dispatch Selected, Confirm ("about to dispatch 4") dispatches all four at once - "All current trade trucks have been dispatched. Time for a coffee break!", Today's Dispatches 4/5, Trade Count 4/5. Expected duel score 4 times 300,000 = 1,200,000 (CORRECTED 2026-11-10 0337: the Duel screen reads Dispatch UR Trade Truck +300,000 live, superseding the 100,000 Handbook rate in tools/duel_schedule.json; the duel-score unit verifies the personal total live). Mega Mode does NOT convert a held roll to UR (0821 finding stands); it refreshes the slots until UR lands, then dispatches them as a batch.
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
- Settlement values, measured 2026-11-09 (2250 unit, 4 returned trucks settled by opening each Truck Details; all four read "The vehicle is safe and secure", none plundered): UR-scale cargo pays iron 3.8M, food 3.8M, coin 2.4M; SR pays iron 2.5M, food 2.5M, coin 1.6M. Settlement totals for the 4 trucks: iron 12.6M, food 12.6M, coin 8.0M, badge 500 x8 in total (x1 to x3 per truck), plus chests, red gems and 5m speed-ups. The rarity label of the first truck was unread behind the CONGRATULATIONS banner - read the label before the banner covers it, or take the cargo figures as the scale signal.
- Details-panel paging: the Truck Details panel pages with the side "<" / ">" arrows and the bottom-left blue arrow (previous). The control receipt's no_change_observed flag is UNRELIABLE for this panel - the SR-to-UR page reported no change yet the screenshot proved the page had turned, so verify paging on the screenshot, never on the receipt flag. Tapping outside the panel does not close it; a unit may end with the panel open on the last truck, which is harmless - the next unit re-reads the trade screen fresh.
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
  red dot while a record waits. (2026-11-09 2250 update: the 2026-11-9 18:00 record claimed - 1 unstarted transport, the old day's 5th dispatch shortfall: badge 500 x3, chest x2, gold chest x10, iron 1.5M, food 1.5M, coin 972.5K, plus 5m speed-up tiles, CONGRATULATIONS verified. The old trade day therefore closed 4/5 dispatched with the 1 unstarted transport recovered. The 2026-11-8 record did NOT expand - two taps on its header and toggle produced no change - so its claim state is unverified; an unexpandable record is not proof of nothing waiting, and the next trucks unit re-checks it.)

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
  server day and resets at the same absolute boundary as the
  duel day: 02:00 UTC, about 18:00 local in PST (19:00 local in
  PDT before the 2026-11-02 daylight-saving end). CORRECTED
  2026-11-03 1846 (Issue #242 follow-up): the 1846 unit entered
  at 18:34 local reading Today's Trade Count 0/5 and Your
  Plunder Count Today 0/4, live on screen, after the 1211 unit
  had closed the same counters at 5/5 and 4/4 at 12:11 - the
  reset had already happened by 18:34, so the standing 19:00
  local wall-time reading cannot stand. The 19:00 references in
  the dated sections below (including the 1211 section's
  "ends at 19:00" framing) are superseded in the same sense
  and stand as history only. These
  are quotas to fill, not caps to stay under. (2026-11-09 2250 corroboration: Trade Count 0/5 read live at about 22:31 on the new trade day, and tools/duel.py reports duel day 2, Base Expansion, ending 2026-11-10 18:00 PT with UR dispatches scoring 100,000 each - the about-18:00 rollover holds for a second day.)
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
- Mega Mode is a VIP privilege - the VIP screen lists Activate the Mega Mode of Trade Trucks among the VIP 13 privileges, and this account is VIP 13, so Mega Mode is unlocked here (confirmed 2026-10-25 on the VIP screen, see [vip-rewards](../vip-rewards/INDEX.md)). OBSERVED END TO END 2026-11-10 (0248 unit, ticker-0234, duel day 2 Base Expansion, Issue #565): Mega Mode has two tabs, Mega Refresh and Mega Dispatch. Mega Refresh lists the four slot rolls with rarity and journey time; a first refresh costs 3 Trade Contracts per truck (dialog-confirmed, 9 for a 3-truck batch, 3 for one truck), and a re-refresh of an already-refreshed truck costs 1 (inferred from the button readings 9/158, 6/149, 3/149, 1/146 - inferred, not measured). Mega Dispatch shows preassigned escorts and dispatches all four slots at once (Select All, Dispatch Selected, Confirm). The fifth daily trade is a second wave after trucks return, NOT a Mega-only fifth - all four slots were out after the Mega dispatch and the 5th dispatch waits on returns.

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

## What the 2026-11-02 1845 unit added - trade entry blocked in current column set, partial

- Unit trucks-2026-11-02-1457 by ticker-1834, session
  about 18:35 to 18:43, status partial, tracker untouched.
  Evidence in
  `_records_/2026-11-02/truck-plunder/1845-queue-run.md`.
- Device dialog, two takeovers in this unit: Confirm was
  tapped at its measured centre, norm 501,568, twice; the
  app exited after each takeover as the owner rule
  expects, was reopened, and the base stayed clean after
  the second takeover, with no third dialog in this unit.
  Grounding lesson, consistent with (not contradicting)
  the 1810 measured-centre rule: OCR coordinates in this
  control channel are already 0 to 1000 normalised, not
  window pixels - do NOT rescale them. The earlier
  mis-read in this unit rescaled them and sent two taps
  to norm 780,597, near the dialog right edge, which did
  nothing. Tap coordinates come from measured grounding
  boxes or OCR element positions in tap space, never from
  a rescaled or image-pixel conversion.
- Left column re-grounded fresh from the current
  screenshot: green face at norm 53,577, white pickup at
  53,639, radar dish at 53,707, hammer below. No blue
  train-front trade icon is present in this set, and no
  left-column icon carries a trade badge.
- Tap at norm 52,553 (the 0935 and 1325 grounding) opened
  the season warming panel (Location final temp 6.5
  degrees C, Permafrost Area, Alliance Furnace), not
  trade. The panel was closed with its X, first at
  896,152 missed, then at 915,150 closed it. The
  0416 train-front premise at 52,552 does NOT transfer
  to this set: 52,553 here opens the season panel.
- World map route tried next, per the 0114 successor
  instruction: WORLD opened the map centred on the own
  base [AP3x]Bears Lair, showing alliance bases only and
  no trade entry on that view. BASE returned to the base
  screen.
- White pickup at 53,639 opened the Secret Command Post
  (Secret Mobile Squad, Your Tasks), as the metadata
  predicts, not trade. Its back arrow returned to the
  base. No Mega button was touched.
- Successor direction, standing under queue rule R2: do
  NOT re-tap the points above. The next trucks unit must
  find the set-flip control or another trade entry route
  before any column tap, and re-ground the column from a
  fresh screenshot.
- The 2026-10-30 hypothesis still fits: the trade slot
  surfaces only while a returned truck awaits settlement,
  and none awaited here (Trade Count already 5 of 5 at
  the 1325 close).
- Counters NOT read live in this unit: the trade screen
  was never entered. The plunder shortfall of 1 (Plunder
  Count 3 of 4, Trade Count 5 of 5) is carried from the
  1325 record only, NOT re-read, and is not claimed as a
  live figure.
- Ended-day close: the trade day ended at 19:00 local,
  under 20 minutes after this unit closed, so the
  shortfall expired unfilled at the reset. The next
  trucks unit is a new trade day and must read both
  counters live on entry; no new-day counter is claimed
  here.

## What the 2026-11-02 2120 unit added - station-tap entry, counters 4 of 5 and 4 of 4, partial

- Unit trucks-2026-11-02-1857 by ticker-2104, session
  about 21:05 to 21:20, status partial, dispatch
  shortfall 1 remains, tracker untouched for the
  shortfall. Evidence in
  `_records_/2026-11-02/truck-plunder/2120-queue-run.md`.
- Entry breakthrough: no left-column point was
  re-tapped, per the 1845 successor instruction.
  Fresh visual grounding put the station building at
  norm 352-630 x 105-285, and a tap at its centre
  [491,195] opened Intercity Trade directly on the
  Others' Trucks view. This is a new, working entry
  route for the current column set (green face /
  pickup / dish / hammer, no trade slot).
- Supersession, in favour of the newest verified
  record: this entry succeeded with no settlement
  pending, so the 2026-10-30 hypothesis that the
  trade slot surfaces only while a settlement pends
  is superseded as an entry rule. The 1845 section's
  "hypothesis still fits" line stands as that unit's
  read only; it is not the standing rule. The
  column-set flip question below stays open, but it
  no longer blocks entry - the station tap answers
  the 1845 successor direction.
- Counters, read live at entry and unchanged at
  close: Your Plunder Count Today 4/4, Today's Trade
  Count 4/5. The counters are the source of truth.
  Four trucks are out: two SR blue, two SSR purple,
  the SSR pair carrying flame markers for looting en
  route. No returned truck awaited settlement.
- Mega Mode inspected, nothing spent: Mega Refresh
  lists the four out trucks (No.1 SR 01:00:57 left,
  No.2 SR 00:50:11, No.3 SSR 01:14:39, No.4 SSR
  00:56:57) with a "Refresh all to Reindeer Sleigh
  Ride" checkbox and Refresh Selected 0/165 -
  nothing selected or refreshed, no contract spent.
  Mega Dispatch reads "All current trade trucks have
  been dispatched. Time for a coffee break!",
  Today's Dispatches 4/5, with Select All / Dispatch
  Selected greyed.
- Fifth dispatch waits for the first return, about
  00:50 away at read time (about 22:10 local). This
  is a UR duel day (day 2, Base Expansion), so that
  dispatch must be UR; whether the Mega Dispatch
  bulk route or a single-slot roll produces the UR
  truck is still unobserved, because no slot was
  free to try it on. Next unit: settle first if the
  returned truck needs it, then dispatch the freed
  slot as UR.
- Counters provenance, explicitly not inferred: how
  the new trade day reached 4/5 and 4/4 before this
  unit is not established in this record - no agent
  trucks record sits between 1845 (previous day
  close 5/5, 3/4) and this unit. The record notes it
  may be owner evening play, when the 1834 pass was
  contested twice. Do not attribute the gap to any
  unit.
- Reward Recovery checked: the 2026-10-31 19:00
  record (3 unstarted transports) reads CLAIMED; no
  new record waits. Nothing claimed in this unit.
  No diamonds, no Trade Contracts, no paid button,
  no alliance mate plundered.


## What the 2026-11-02 2347 unit added - entry failed, station tap not stable, partial

- Unit trucks-2026-11-02-2257 by ticker-2334, session
  about 23:41 to 23:47, status partial, entry failed.
  Evidence in
  `_records_/2026-11-02/truck-plunder/2347-queue-run.md`.
- Entry failure, in detail: the 2120 unit entered
  Intercity Trade by tapping the station building
  at norm [491,195]. This unit tried that exact tap
  twice (once before and once after a title-bar
  focus tap as the foreground pivot) - both
  no-change. A visually grounded station box (norm
  395-860 x 120-355) tapped at its centre [627,237]
  selected a squad parking slot ("2nd Squad Lv.20")
  and opened a two-button popup (vehicle icon, up
  arrow) with no labels. Neither button was tapped -
  the popup's meaning was not established and a
  wrong tap could march a squad. The popup was
  dismissed by tapping empty ground; the base view
  returned unchanged. A further tap at [662,163]
  (upper station structure) was also no-change.
  That is two no-change entry taps, so the
  background-input method was ended inside this
  unit under queue rule R2; the title-bar focus
  pivot did not change the outcome for the
  [491,195] tap.
- Correction, in favour of the newest verified
  record: the 2120 station-tap entry is qualified,
  not erased. The [491,195] tap worked at 2120 and
  failed twice at 2347 on the same trade day, so it
  is a framing-dependent entry point, not a stable
  one. The next unit must re-ground the station
  hotspot on the live base framing first, and must
  not re-tap the [491,195] / [662,163] points
  blindly. The squad-slot popup (vehicle icon, up
  arrow) is unidentified until a labelled read
  proves what it opens - do not tap its buttons.
  Foreground variant not yet tried: moving the
  covering Chrome window aside before tapping.
- Counters were NOT read this unit - entry never
  reached the trade screen, so no counter values
  are asserted here. Last read counters (2120
  unit): Trade 4/5, Plunder 4/4, with the first
  return due about 22:10 local. A return and
  settlement may therefore be pending, but that is
  the 2120 read, not a fresh observation - do not
  quote it as a 2347 reading.
- Outcome: partial, dispatch shortfall carried
  forward (not a miss: the trade day runs to 19:00
  local 2026-11-03, and later trucks units keep
  trying entry). No dispatch, no plunder, no
  settlement performed. No diamonds, no Trade
  Contracts, no paid button, no plunder.
  Blocker category f (missing precondition - trade
  screen entry not reached). Computer session
  dropped mid-pass and restarted with no game
  state lost; no "active on a different device"
  dialog appeared. Game left on the base screen.



## What the 2026-11-03 0344 unit added - entry failed again, grounding mislabels buildings, partial

- Unit trucks-2026-11-03-0257 by ticker-0334, session
  about 03:34 to 03:44, status partial, entry failed.
  Evidence in
  `_records_/2026-11-03/truck-plunder/0344-queue-run.md`.
  GitHub Issue #218 filed in this unit (labels play,
  knowledge) for this repeated failure mode.
- Entry failure, in detail: the 2120 station tap at norm
  [491,195] was tried first and was no-change, matching
  the 2347 unit - the second consecutive trucks unit for
  which the old station point does nothing. Fresh visual
  grounding put a station box at norm 398-578 x 308-448;
  tapping its centre [488,378] selected High-temp
  Furnace Lv.30, not a station. After panning the base
  (drag [500,400] to [500,650]), grounding put a station
  box at norm 545-730 x 105-235; tapping its centre
  [637,170] selected Wall Lv.26, with the same
  unidentified two-button popup (home icon, up arrow)
  seen in the 2347 unit. Neither button was tapped.
  After a second pan (drag [600,400] to [300,400]),
  grounding put a station box at norm 280-435 x 140-260;
  tapping its centre [357,200] was no-change. The
  furnace and wall popups were dismissed by tapping
  empty ground; no furnace was turned on or off and no
  upgrade was touched.
- The left column in this unit was re-grounded fresh and
  carries no trade slot in this set: hammer 2/4, flasks
  2/2, green face 6.5 degrees C at norm 53,483,
  light-blue train front with a red dot at norm 61,563,
  white pickup at norm 61,643, satellite dish with
  badge 11 at norm 62,723, hammer below. Per the
  2026-10-30 evening units, the train-front icon neither
  opens trade nor flips the set, so it was not tapped.
- The foreground variant suggested by the 2347 unit
  (moving the covering Chrome window aside) was not
  attempted: this control channel sends input in the
  background and never brings the game to the front, so
  that variant is not available from here.
- Counters were NOT read live in this unit: the trade
  screen was never entered, so no live counter is
  asserted here. Carried, not re-read, from the 2120
  unit: Trade 4/5, Plunder 4/4, for the trade day ending
  19:00 local 2026-11-03, so the 1-dispatch shortfall
  remains unfilled. Corroboration, not trucks work: the
  secrets unit of the same pass (0346) saw Trade 4/5
  with four trucks out incidentally while exiting trade
  screens opened by snapped taps - that read matches the
  carried 4/5 but was not acted on as trucks work.
- Duel posture: day 2, Base Expansion, UR truck
  dispatches score (Handbook 100,000 each); trucks go UR
  today, contracts permitting. The fifth dispatch, when
  entry succeeds, must still be UR (Mega UR only per the
  unit window). A returned truck may await settlement;
  that is not established in this unit.
- Outcome: partial, entry failed, dispatch shortfall
  carried forward (not a miss: the trade day runs to
  19:00 local 2026-11-03, and later trucks units keep
  trying entry). No dispatch, no plunder, no settlement
  performed. No diamonds, no Trade Contracts, no paid
  button, no plunder, no dispatch. Tracker untouched
  (partial units do not mark the tracker).
  Blocker_category: e (repeated blocker - trade screen
  entry method). Next trucks unit: do not re-tap
  [491,195], [488,378], [637,170] or [357,200] blindly.
  Until Issue #218 is answered, later units should spend
  their budget on finding a verified Intercity Trade
  entry route for the current base framing rather than
  repeating these four points - first variant to try, by
  analogy with the 0346 secrets entry: an unsnapped
  exact-centre tap on the trade icon, since snapped taps
  in the left column demonstrably land on the wrong slot.
  Game left on the base screen, panned east from its
  starting framing by the two drags in this unit.

## What the 2026-11-03 0821 unit added - trade entry by the 53,555 route, one SR settled, SSR held for the UR chase, partial

- Unit trucks-2026-11-03-0657 by ticker-0804, session
  about 08:04 to 08:21, status partial, quota shortfall
  carried forward (not a miss: the trade day runs to
  19:00 local 2026-11-03, and later trucks units keep
  trying). Evidence in
  `_records_/2026-11-03/truck-plunder/0821-queue-run.md`.
  No "active on a different device" dialog appeared. No
  diamonds, no paid button, no plunder, no dispatch in
  this unit.
- Duel posture: day 2, Base Expansion, from tools/duel.py
  at unit start. UR truck dispatches score (Handbook
  100,000 each); trucks go UR today, contracts
  permitting. Radar posture stack. Window on the unit:
  duel day 2 - UR trucks, Mega UR only.
- Entry, SUCCESS by a new route: the left-column icon at
  norm 53,555 on the current base framing - the
  speech-bubble icon above the truck slot in that set -
  opened Intercity Trade directly. This route was not
  tried in the 0344 unit and is the entry breakthrough
  for the repeated entry blocker tracked as Issue #218.
  The truck icon at norm 53,657 opened Secret Command
  Post (Secret Mobile Squad, Your Tasks, Mega Refresh
  and Mega Deploy buttons - none tapped), not trade. Do
  not use it for trade entry. The old station points
  from the 0344 unit (491,195 and 488,378 and 637,170
  and 357,200) were not re-tapped. The entry blocker
  itself is resolved by the 53,555 route; Issue #218
  stays open, and closure belongs to the daily retro,
  with evidence.
- Counters read live on entry: Today's Trade Count 4 of
  5; Your Plunder Count Today 4 of 4 (full). The
  1-dispatch shortfall is the only open quota item, and
  the trade day runs to 19:00 local 2026-11-03.
- Settlement: Mega Mode from the road view first showed
  Mega Refresh with four Arrived trucks (SR, SR, SSR,
  SSR) and Mega Dispatch showing no dispatchable truck
  ("All current trade trucks have been dispatched",
  Today's Dispatches 4 of 5). The first road truck,
  tapped at its trailer centre (352,450 - a tap at
  352,415 on its chest icon did nothing), opened Truck
  Details: SR, Intercity Trade Reward, cargo iron 2.5M,
  food 2.5M, coin 1.6M, chests 20 x3 and a red diamond
  item 1. Battle History: 2026-11-2 20:05:30,
  [EoBH]jeffr46 Power 41.9M, Plunder Failed - delivered
  in full. Opening the details settled the truck and
  freed its slot. The other three arrived trucks were
  not settled in this unit: the freed slot's dispatch
  panel took the remaining unit time. Settlement tap
  lesson: tap the trailer centre, not the chest icon.
- Fifth dispatch, UR chase, SSR held, not dispatched:
  the freed slot's dispatch panel first rolled R (iron
  2.0M, food 2.0M, coin 1.2M, arrives 04:20:52, Escorts
  Squad 1, free refresh available). Free refresh: R to
  SR (iron 2.5M, food 2.5M, coin 1.6M, badge 500 x1,
  arrives 04:33:00). Contract refresh 1: SR to SR (iron
  2.5M, food 2.5M, coin 1.6M, badge 500 x1, arrives
  04:01:35, contracts 165 to 164). Contract refresh 2:
  SR to R (iron 2.0M, food 2.0M, coin 1.2M, arrives
  03:53:19, contracts 164 to 163). Contract refresh 3:
  R to SSR (iron 3.0M, food 3.0M, coin 1.9M, badge 500
  x3, chest 25, arrives 03:52:51, contracts 163 to 162).
  The SSR roll was verified still held after closing
  and reopening the slot panel (arrives 03:52:51
  unchanged), so it survives across units. Mega Mode
  tapped from the dispatch panel only reopens the Mega
  summary; Mega Dispatch still lists no dispatchable
  truck. Mega Mode does not convert a roll to UR, as far
  as this unit could observe.
- The SSR was NOT dispatched: this is a UR duel day and
  SSR is not UR. Spending more contracts chasing UR, or
  dispatching the SSR and forfeiting the UR duel points,
  is left to the next trucks unit - the quota deadline is
  19:00 local, not this unit. No Trade Contract spending
  beyond the 3 refreshes above; no diamonds spent
  anywhere.
- Outcome: partial, quota shortfall carried forward.
  Settled in this unit: 1 truck (SR, above). Dispatched
  in this unit: none. Plundered: none. Counters at close,
  live: Trade 4 of 5, Plunder 4 of 4. Held roll at close:
  SSR, arrives 03:52:51, in the freed slot; contracts
  162 remaining. Tracker untouched (partial units do not
  mark the tracker). Blocker_category: h (by-design
  partial - quota work resumed across units) with e noted
  for the entry history; the entry blocker itself is
  resolved by the 53,555 route above.
- Next trucks unit: reopen the trade screen by the
  53,555 route, settle the remaining arrived trucks if
  any are still unsettled, then either continue the UR
  chase from the held SSR roll or dispatch the SSR
  before the 19:00 deadline - do not re-tap the old
  station points or the 53,657 Secret Post icon for
  trade entry. Game left on the base screen.
- Gap: already tracked as GitHub Issue #218 (labels
  play, knowledge). The executor commented this route
  and these counters onto #218, and this run comments
  the fold onto #218 as well; the issue stays open,
  and closure belongs to the daily retro, with evidence.

## What the 2026-11-03 1211 unit added - quotas full, badged-icon entry, UR dispatched as rolled, done

- Ticker-1204, unit trucks-2026-11-03-1057, about
  12:06 to 12:11 local, status done. Evidence in
  `_records_/2026-11-03/truck-plunder/1211-queue-run.md`.
- Entry: base view left column, measured fresh: green
  face, then the light-blue vehicle-front icon with red
  badge 1 at norm about 55,589, then the white pickup,
  then the radar dish with badge 11, then the hammer.
  One tap at 55,589 opened Intercity Trade on the
  Others' Trucks view. This settles the stale-window
  question left by the 2026-10-30 evening units: the
  icon they found dead opens the trade screen when it
  carries a badge. The 0821 route (53,555) and this
  badged-icon point are two verified entries; find the
  icon by badge and glyph, not by a fixed point alone.
- Live counters read on screen: Your Plunder Count
  Today 4/4, already full at entry, nothing to plunder;
  Today's Trade Count 4/5 at entry, 5/5 after this
  unit's dispatch. Both counters are live screen reads
  in this unit, not tallies.
- Duel posture applied: tools/duel.py at entry reports
  duel day 3, theme Age of Science, scoring actions
  today research, valor badges, drone component chests
  and radar claims, and truck dispatches do not score
  today. The unit's window text still reads "duel day
  2 - UR trucks, Mega UR only". That text is stale:
  the live posture is day 3, so the non-UR day rule
  governed this unit (dispatch SR or above only, free
  refresh first, then Trade Contract refreshes until
  reached). The stale window text is noted here for the
  planner pass, not acted on. See also the
  alliance-duel profile open question: the duel panel
  itself reads theme Base Expansion with a timer
  pointing to about 18:00 on 2026-11-03, which does not
  match the tool's day-3 report - the tool output is
  unresolved there, and this unit's dispatch needed no
  resolution because the roll below already cleared the
  SR bar.
- Dispatch: Your Truck view showed four empty slots.
  First slot tapped. Panel rolled UR as rolled: iron
  3.8M, food 3.8M, coin 2.4M, journey 03:18:02, Squad 1
  escort, free refresh still unused. UR already clears
  the SR bar, so no refresh was spent and the truck was
  dispatched as rolled with Let's Go. After dispatch:
  Today's Trade Count reads 5/5, banner "No more
  dispatches available", one gold truck on the road. No
  Trade Contract spent, no diamond spent.
- Other checks: Recover button on the trade screen
  showed no red dot, so no Reward Recovery record was
  waiting. Nothing claimed there. No plunder action:
  Plunder Count already 4/4, and the standing shard
  rule was not needed this unit.
- Outcome: done. Trade quota 5/5 and plunder quota 4/4
  both full for this trade day. Tracker marked done for
  trucks. Costs: about 5 minutes of unit time, 0 Trade
  Contracts, 0 diamonds.

## What the 2026-11-03 1846 unit added - new trade day, 3 dispatches, 2 plunders, partial

- Ticker-1834, unit trucks-2026-11-03-1457, about 18:34 to
  18:46 local, status partial. Evidence in
  `_records_/2026-11-03/truck-plunder/1846-queue-run.md`.
  No diamonds spent, no paid button tapped, no Mega Mode
  dispatch.
- Entry: base view left column, measured fresh: hammer 2/4,
  flasks 1/2, green face, light-blue vehicle-front icon with
  a red dot, white pickup badge 9, radar dish badge 4,
  hammer, chest. One tap at norm 54,568 on the vehicle-front
  icon opened Intercity Trade directly on the Your Truck
  view, matching the 1211 unit: the icon opens trade when
  it carries a badge.
- Live counters, the reset correction: at entry Today's
  Trade Count 0/5, Your Plunder Count Today 0/4; at close
  3/5 and 2/4. Both pairs are live screen reads, not
  tallies. The 1211 unit had filled the counters to 5/5 and
  4/4 at 12:11 local for its trade day, so the counters
  reset between 12:11 and 18:34 - with the about-18:00
  rollover (Issue #242), not at 19:00. The standing quota
  rule above is corrected accordingly, and the counters
  stay the source of truth: this unit worked the new trade
  day's quotas from zero.
- Duel posture applied: tools/duel.py at entry reported
  duel day 3, theme Age of Science, day ends 2026-11-04
  19:00 local - that end time is the pre-PR-243 tool reading
  and is NOT adopted (PR 243, merged 2026-11-03 18:45 local,
  moved the boundary to absolute 02:00 UTC). The unit's
  window text still read "duel day 2 - UR trucks, Mega UR
  only": stale, not followed. Live posture is duel day 3,
  so the non-UR rule governed: dispatch SR or above only,
  free refresh first, then Trade Contract refreshes until
  reached, no Mega dispatch.
- Dispatches, 3: SSR as rolled (iron 3.0M, food 3.0M, coin
  1.9M, journey 03:52:51, Squad 3); N, free refresh to R,
  one Trade Contract to UR (iron 3.8M, food 3.8M, coin
  2.4M, journey 04:17:13, Squad 2, contracts 162 to 161);
  N, free refresh to R, one Trade Contract to SR (iron
  2.5M, food 2.5M, coin 1.6M, journey 04:09:57, Squad 4,
  contracts 161 to 160). Total Trade Contracts spent: 2.
- Plunders, 2: SSR truck of [RoSt], Lv.26, guard 6.7M,
  gold UR-shard stack of 10 at the sixth of eight slots,
  yield iron 531.5K, food 531.5K, coin 337.0K, plus three
  item stacks, shard stack did not drop; SSR truck of
  [FRVP]The X Mansion, Lv.28, guard 9.8M, gold UR-shard
  stack of 3 at the second of eight slots (left side, the
  harder position, but the SSR target on this list pass),
  yield iron 570.2K, food 570.2K, coin 363.0K, plus three
  item stacks, shard stack did not drop. Combined: iron
  1,101.7K, food 1,101.7K, coin 700.0K, six item stacks,
  no UR shards.
- Tap lessons, binding for the next unit: the gold truck
  standing on the Your Truck road at entry, with a chest
  icon above it, was still there at close - a tap on its
  body at norm 444,415 produced no change, its chest icon
  was not tapped and the Mega Mode settlement path was not
  tried. Next unit tries the chest icon first, since the
  quota order says settle returned trucks first; whether
  that gold truck is a returned truck awaiting settlement
  or an outbound truck is unverified here. Gold trucks on
  the Others' Trucks road resisted body taps twice at norm
  615,342 and 618,350 with no change (rule R2 pivot: a
  different truck was tried instead, and its card opened).
  Quick Plunder's true centre is norm 600,885, measured
  from an enlarged crop - the (460,867) tap lands in the
  gap between Plunder! and Quick Plunder. The second
  plunder target's card needed a second tap: the first at
  norm 467,226 did nothing, the second at norm 467,245
  opened it.
- Remaining shortfall, carried to the next trucks unit:
  dispatch 3/5, with all four road slots now occupied
  (gold, purple SSR, UR, SR) - no further dispatch is
  possible until a truck returns and is settled, so the
  next unit settles first, then dispatches. Plunder 2/4,
  two plunders remain, targets permitting. Recover button
  not checked on its own panel in this unit (the road view
  at close showed no red dot on Recover in the screenshots,
  but no live read was taken there - unverified, not
  claimed).

## What the 2026-11-04 0242 unit added - WORLD-corner entry route, quotas full, done

- Ticker-0234, unit trucks-2026-11-03-2257, about 02:38 to 02:42 local, status done, quotas already full at entry, no action needed. Evidence in `_records_/2026-11-04/truck-plunder/0242-queue-run.md`. No diamonds spent, no paid button tapped, no Mega Mode dispatch.
- Duel posture applied: tools/duel.py at entry reports duel day 3, theme Age of Science, day ends 2026-11-04 19:00 local. Scoring actions today are research, valor badges, drone component chests and radar claims. Truck dispatches do not score today, so the non-UR day rule would have governed any dispatch (SR or above only) - but no dispatch was needed or made.
- Entry, new route found, and a dead route confirmed: the left-column vehicle-front icon (grounded fresh at norm 54,577, no red badge visible on it in this view) did not open trade - a tap at norm 54,568 only panned the base map, and a tap at the grounded centre 55,578 produced no change. A tap at norm 55,531 opened the season warming panel instead (the green-face icon sits above the vehicle icon, grounded at norm 54,494), and the panel was closed with its X on the first tap. This matches the 2026-10-30 evening pattern: the vehicle icon tap does nothing when it carries no badge. Background input is not the cause here - the same session's shop taps all landed in the previous unit.
- A tap on the station building (norm 592,189) produced no change, a third framing failure for station taps after 2347 and 0344. Do not re-tap station points blindly.
- Entry that worked: a tap at norm 913,940, on the bottom-right WORLD corner of the base screen, opened Intercity Trade directly on the Others' Trucks view. Next trucks units try this route first when the left-column icon carries no badge. The mechanism (why that corner opens trade) is unverified, only the observed result.
- Live counters read on screen: at entry Today's Trade Count 5/5, Your Plunder Count Today 4/4. Both quotas are full, so no dispatch and no plunder was made in this unit. At close: unchanged, 5/5 and 4/4. Both pairs are live screen reads, not tallies.
- Attribution gap, recorded not smoothed over: the previous local trucks record (2026-11-03 1846 unit) closed at Trade 3/5, Plunder 2/4, so the quotas were filled between then and this entry by passes whose records are not in this working tree. This record does not attribute the fill to any specific pass.
- Settlement check: Your Truck road shows two trucks out and two free slots, with the banner "No more dispatches available." The right-hand truck's card was opened (a tap on the left truck's body produced no change, as in the 1846 unit): own SR truck, [AP3x] Bears Lair Lv.30, guard 25.1M, arrives in 01:52:13, cargo including badge stacks, iron 2.5M, food 2.5M, coin 1.6M. It is outbound, not returned, so nothing was settled. No chest icon stands above either road truck. The Recover button carries no red dot, and one tap on it produced no panel, so no Reward Recovery record is waiting to be claimed.
- Outcome: done. Trade quota 5/5 and plunder quota 4/4 both full for this trade day. No Trade Contract spent, no diamond or money spent, no alliance mate plundered, no Mega Mode used. Costs: about 4 minutes of unit time.
## Open questions

- What a Mega dispatch does differently, and what the fifth daily
  trade is. Mega Mode itself is a VIP 13 privilege, unlocked on this
  account. The owner dispatch rule for Alliance Duel UR days (Mega
  Mode, UR trucks only) is recorded above but not yet executed. (2026-11-03 0821 update: Mega Mode tapped from the dispatch panel only reopens the Mega summary and Mega Dispatch still lists no dispatchable truck, and Mega Mode does not convert a held roll to UR as far as that unit could observe - the dispatch-difference question itself is still open.) (2026-11-10 0248 update: ANSWERED - Mega Mode is a batch refresh plus batch dispatch of all four slots (see the Scope paragraph and the 0248 section below); the fifth trade is a second wave after returns, not a Mega-only fifth. The "Refresh all to Reindeer Sleigh Ride" checkbox was left unchecked and its effect is still unobserved; the expected 1,200,000 duel score (CORRECTED 2026-11-10 0337: Duel screen reads +300,000 per UR dispatch, superseding the 100,000 Handbook rate) still awaits a live duel-score read. Issue #565. (2026-11-10 0435 update: VERIFIED - the duel-score unit read the personal total 1,650,000 at 04:35, up from 450,000 at the 01:51 read, a rise of 1,200,000 matching 4 UR dispatches at the live 300,000 rate; the 300,000-per-dispatch live rate is confirmed by the personal-total read. The 'Refresh all to Reindeer Sleigh Ride' checkbox effect stays unobserved. Commented on Issue #565 by this run.))
- Whether the 2026-10-25 Alliance Duel day scored UR truck
  dispatches - the daily duel category was not verified that day,
  so the evening dispatches ran under normal day handling.
- Whether the collapsed 2026-10-20 Reward Recovery record was
  already claimed - its toggle did not expand on 2026-10-25.
- What flips the base left-column icon set to the set that carries the trade slot (2026-11-02 1845 update: the 1845 set - green face / pickup / radar dish / hammer - carries no train-front icon at all and no trade badge; 52,553 opens the season warming panel, not trade; the successor must find the set-flip control or another entry route first) (2026-11-02 2120 update: the station-building tap at [491,195] opens Intercity Trade directly for this column set, so entry no longer depends on finding the set flip; the flip itself stays unknown) - the 0114 unit's set (green face / bus-train-front / pickup / walkie-talkie / hammer / chest) carries no speech-bubble truck glyph, and the 22:31 entry point [55,584] does not transfer to it. (2026-11-02 0416 update: for this set the premise is corrected - the train-front icon at [52,552], reached after a title-bar foregrounding tap, is the trade entry; the flip question remains for sets where no train-front icon is present.)
- Station-tap entry stability (2026-11-02 2347 update):
  the [491,195] station tap that entered trade at
  2120 failed twice at 2347, so entry is
  framing-dependent and must be re-grounded on the
  live base view each unit; the squad-slot popup
  (vehicle icon, up arrow) reached from a station-box
  centre tap is unidentified and its buttons must
  not be tapped. This belongs to this profile's open
  questions until a later unit re-grounds a working
  entry point - no new Issue filed yet, because the
  next trucks unit retries entry first with the
  re-grounding and the Chrome-window-aside variant.
  (2026-11-03 0344 update: the station tap failed a
  second consecutive unit and grounded station points
  mislabelled Furnace Lv.30 and Wall Lv.26, so the
  re-grounding retry is exhausted as a variant on its
  own; GitHub Issue #218 is now open for this failure
  mode, and the next variant is the unsnapped
  exact-centre tap proposed by the 0344 section above.
  The Chrome-window-aside variant is not available from
  the background control channel, per the 0344 record.)
  (2026-11-03 0821 update: the entry blocker itself is
  resolved - the left-column icon at norm 53,555, the
  speech-bubble icon above the truck slot, opened
  Intercity Trade directly, a route not tried in the
  0344 unit, so the unsnapped-variant proposal was not
  needed; the 53,657 truck icon opens Secret Command
  Post, not trade. Issue #218 stays open pending retro
  closure with evidence, but later units reopen trade
  by the 53,555 route first and do not re-tap the old
  station points.)
  (2026-11-04 0242 update: the station tap at 592,189 again produced no change in a third framing, while the WORLD-corner tap at 913,940 opened trade directly when the column icon was badgeless - see the 0242 section below. The WORLD-corner route is now the first route to try for a badgeless column icon, ahead of any station re-tap. Issue #218 stays open pending retro closure with evidence.)
  (2026-11-04 0538 update: the WORLD-corner claim is qualified - a tap at norm 913,940 in the 0538 unit opened the World map, not trade directly, so the 0242 note is not reproduced as written; it may have tapped through from the World view. The 0538 entry that worked was the badged vehicle icon at norm 55,578, the same centre the 0242 unit tapped badge-less with no effect. See the 0538 section below.) (2026-11-08 0415 update: the left-column blue vehicle icon at norm 46,562 opens the Trucks panel, not the station - a Trucks-panel route, distinct from the 53,555 Intercity Trade entry; see the 0415 section below.) (2026-11-08 0512 update: the bus icon at grounded norm (49,575) opens the Trucks panel a third tap-verified time, and its dot clears on open - the Trucks identity is settled and the 0022 radar read is superseded; see the 0512 section below.) (2026-11-09 0541 update: the WORLD-corner route was re-tried and again opened only the World map, re-confirming the 0538 correction; the standing Working entry route section's instruction to try it first is now corrected in place. The next unit arrives with a changed method - a foreground click variant on the icon, or the station-area route - and re-reads both counters live first.)

## What the 2026-11-04 0538 unit added - quotas full, badged-icon entry, WORLD-corner route qualified

- Ticker-0534, unit trucks-2026-11-04-0257, about 05:34 to 05:39 local, status done, quotas already full at entry, no action needed. Evidence in `_records_/2026-11-04/truck-plunder/0538-queue-run.md`. No "active on a different device" dialog appeared.
- Duel posture applied: tools/duel.py at entry reports duel day 3, theme Age of Science, day ends 2026-11-04 19:00 local. Scoring actions today are research, valor badges, drone component chests and radar claims. Truck dispatches do not score today, so the non-UR day rule would have governed any dispatch (SR or above only) - but no dispatch was needed or made, and no Mega Mode dispatch was used.
- Entry, corrected and qualified: a tap at norm 913,940 on the bottom-right WORLD corner opened the World map, not trade directly (the 0242 unit's route note is not reproduced as written - it may have tapped through from the World view). Returned to base with the BASE corner tap at the same norm. Left column grounded fresh from an enlarged crop: hammer 2/4, flasks 2/2, green face 6.5C, light-blue vehicle-front icon with a red dot, white pickup with a red dot, satellite dish, hammer. The vehicle-front icon at norm 55,578 - the same centre the 0242 unit tapped while badge-less with no effect - opened Intercity Trade directly on the Your Truck view now that it carries a red dot. This confirms the 1211/1846 rule again: the badged vehicle icon opens trade. Correction recorded: the 0242 WORLD-corner point is a World-map opener, not a direct trade entry; the open-questions note for that route is qualified accordingly, and later units must not cite 913,940 as a direct trade entry.
- Live counters read on screen: at entry Today's Trade Count 5/5, Your Plunder Count Today 4/4. Both quotas are full, so no dispatch and no plunder was made in this unit. At close: unchanged, 5/5 and 4/4. Both counters are live screen reads in this unit, not tallies.
- Settlement check: Your Truck road shows two trucks out and two free slots, with the banner "No more dispatches available." Neither road truck carries a chest icon above it, so no returned truck awaits settlement. The Recover button carries no red dot on either the Your Truck or the Others' Trucks view, so no Reward Recovery record is waiting to be claimed.
- No Trade Contract spent, no diamond or money spent, no alliance mate plundered, no Mega Mode used. Costs: about 5 minutes, no stamina or items spent.

## What the 2026-11-04 0845 unit added - quotas full again at entry, trade-icon grounding mislabel opens Secret Command Post

- Unit trucks-2026-11-04-0657 by ticker-0834, about 08:44 to 08:45 local, status done. Evidence in `_records_/2026-11-04/truck-plunder/0845-queue-run.md`. Computer session cc-439 dropped mid-pass and was restarted as cc-440 with no game state lost. No different-device dialog appeared.
- Duel posture applied: tools/duel.py at entry reported duel day 3, theme Age of Science. Truck dispatches do not score today, so the non-UR day rule would have governed any dispatch (SR or above only) - but no dispatch was needed or made, and no Mega Mode dispatch was used. Note: the tool's day-end time (19:00 local) is the disproven tool time from Issue #242; the panel countdown is authoritative (see the 0839 duel section). The rule application is unaffected because no dispatch was made.
- Entry, grounding mislabel repeated: a visual grounding put the trade icon at norm 53,625, but tapping it opened the Secret Command Post instead. Nothing inside it was tapped - no secret task was started - and the panel was left with a left-edge swipe back to the base. This matches the activity note that the column slot opens the Secret Command Post in one set, and the secrets entry note that the same slot opens the post. A tap at norm 55,578 - the centre the 0538 unit used - opened Intercity Trade directly on the Your Truck view. The badged vehicle icon opens trade, as in 0538.
- Live counters read on screen: at entry Today's Trade Count 5/5, Your Plunder Count Today 4/4. Both quotas are full, so no dispatch and no plunder was made in this unit. At close: unchanged, 5/5 and 4/4. Both counters are live screen reads in this unit, not tallies. This is the second quotas-full trucks unit today (0538, 0845).
- Settlement check: Your Truck road shows two trucks out and two free slots, with the banner "No more dispatches available." Neither road truck carries a chest icon above it, so no returned truck awaits settlement. The Recover button carries no red dot on the Your Truck view, so no Reward Recovery record is waiting to be claimed.
- No Trade Contract spent, no diamond or money spent, no alliance mate plundered, no Mega Mode used. Game left on the base view.

## What the 2026-11-07 1824 sweep added - truck counts still unread at 18:24, both R3 checkpoints passed unverified

- Unit zero-sweep-2026-11-07-1730 by ticker-1734, about 18:06 to 18:24 local, status partial. Evidence in `_records_/2026-11-07/daily-activities/1824-queue-run.md`. No truck was dispatched or plundered and no truck count was read in this unit: the sweep is verification-only and does not execute task types.
- Trucks line 18, not at zero and unverified: no live truck count today - the 0257, 0657 and 1057 units all expired unexecuted. Rule R3 checkpoint note: both the six-hour and the two-hour checkpoints passed with the counts still unverified. Fix-up trucks-2026-11-07-1857 sits in inbox.
- Reading warning: this sweep gives zero evidence about the truck counts. It must NOT be read as a quota state - the 0845 section's 5/5 dispatch and 4/4 plunder close stands as the last live read (2026-11-04), and the 5-of-5 / 4-of-4 daily quotas are unverified for 2026-11-07.
- Follow-up: the 1857 fix-up unit reads the counts in its own slot; the 18:30 final sweep re-walks the line.


## What the 2026-11-08 0415 scout read added - left-column vehicle icon opens the Trucks panel, Trade Count 0/5

- Scout unit scout-scout-2026-11-02-008 by ticker-0404, about 04:15 to 04:19 local, status partial (alliance remainder of the stale 2026-11-02 post-reset pass). Evidence in `_records_/2026-11-08/perception-scout/0415-queue-run.md` (commit 614096a6 on records/2026-11-08). Observe-only; nothing dispatched or plundered. The trucks regular owns dispatch and plunder work and its units are queued.
- Left-column blue vehicle icon at norm (46, 562) opens the Trucks panel, NOT the station: "Today's Trade Count: 0/5", "Filter out trucks from your Warzone" checked, four yellow trucks under Others' Trucks, Mega Mode button, both tabs badged 4, History and Recover buttons.
- Distinction from the station entry problem (Issue #218): the icon is a Trucks-panel route, not a station route - the station tap instability in #218 is untouched by this read. The 53,555 Intercity Trade entry from the 0821 unit and the 55,578 badged-icon entry from the 0538 unit are the trade entries; this (46, 562) point is a third, panel-level route that lands on the Trucks panel itself.
- No quota state is claimed from this read: Trade Count 0/5 at 04:19 is a same-day read, not a close, and the 5-of-5 / 4-of-4 daily quotas are unverified for 2026-11-08.
- Game left safe: game left on the base screen (Trucks panel closed). Nothing dispatched or plundered. No Assemble, no teleport.


## What the 2026-11-08 0512 scout read added - bus icon tap-verified Trucks a third time, dot clears on open, Trade Count 0/5

- Scout unit scout-midday-scout-mid-2026-11-03-006 by ticker-0504, about
  05:05-05:12 local, status done. Evidence in
  `_records_/2026-11-08/perception-scout/0512-queue-run.md` (commit
  111f7e954 on records/2026-11-08). Observe-only; nothing dispatched
  or plundered. The trucks regular owns dispatch and plunder work and
  its units are queued.
- Left-column blue bus icon at grounded norm (49,575) opens the Trucks
  panel - the third tap-verified confirmation (0404 at 04:19, now
  0512). This settles the 0440 unit's icon identity disagreement in
  favour of Trucks: the 0022 "radar" read is superseded. The icon is
  a Trucks-panel route, not a station route - the station tap
  instability in Issue #218 is untouched by this read.
- Trucks panel about 05:10: "Today's Trade Count: 0/5", "Filter out
  trucks from your Warzone" checked, four yellow trucks under
  Others' Trucks, Mega Mode button, "Others' Trucks" / "Your Truck"
  tabs each badged 4, History and Recover buttons.
- The plain red dot CLEARED after opening the panel: on return to the
  base screen the bus icon carries no dot. The dot is the
  unviewed-Trucks-panel signal - opening the panel clears it with no
  dispatch or plunder needed.
- No quota state is claimed from this read: Trade Count 0/5 at 05:10
  is a same-day read, not a close, and the 5-of-5 / 4-of-4 daily
  quotas are unverified for 2026-11-08.
- Game left safe: base screen. Nothing dispatched or plundered. No
  Assemble, no teleport.

## What the 2026-11-08 0542 scout read added - blue truck/bus icon is Trucks, screen state read live, white-truck mapping corrected

- Scout unit scout-midday-scout-mid-2026-11-03-005 by ticker-0534, about
  05:40 to 05:50 local, status done. Evidence in
  `_records_/2026-11-08/perception-scout/0542-queue-run.md` (commit
  707bcec0d8 on records/2026-11-08) and the appended section of
  `_records_/2026-11-03/perception-scout/observation.md`. Observe-only;
  nothing dispatched, plundered or claimed. This is a confirmatory re-read
  - the same unit file already ran as the 0512 unit by ticker-0504 - tracked
  as GitHub Issue #446 (tooling); the reads below are live second reads.
- The blue truck/bus icon (4th icon down the left column) opens the Trucks
  screen: "Today's Trade Count: 0/5", "Filter out trucks from your Warzone"
  checked, four own yellow trucks waiting on the road, "Mega Mode" button,
  "Others' Trucks" / "Your Truck" tabs each badged 4, History button
  top-right, Recover button bottom-left (itself carrying a red dot, routed
  to this regular - the Recover dot is not in this unit's window). The dot
  on the icon is this regular's dispatch/plunder availability signal - 0 of
  5 trades done today, 4 own trucks waiting to dispatch and 4 others'
  trucks to plunder. This is the fourth tap-verified confirmation of the
  blue-icon Trucks identity (0404, 0415, 0512, 0542) and the third
  consecutive 0/5 Trade Count read (0415, 0512, 0542) - the day's dispatch
  quota is still untouched at 05:40 local.
- CORRECTION: the 0022 unit mapped the white truck icon to the trucks
  regular. That mapping is superseded by this live navigation - the white
  truck (5th icon down the left column) opens the Secret Command Post, not
  Trucks; the blue truck/bus icon opens Trucks. The 0845 section's
  "trade-icon grounding mislabel opens Secret Command Post" framing was
  already corrected by the 0532 run (the white truck genuinely opens the
  Secret Command Post; there was no mislabel, only the wrong expectation)
  and this unit confirms it live. The 0022 record and the 2026-11-03
  observation file carry the corrected mapping (appended by the ticker
  pass).
- Chain scout-mid-2026-11-03 complete: the 3-dot carry was its last open
  item. No successor enqueued.
- Game left safe: game left on the base screen. Nothing dispatched or
  plundered.

## What the 2026-11-09 0541 unit added - trade entry blocked in current column set, both methods failed, counters not re-read, shortfall carried

- Unit trucks-2026-11-09-0257 by ticker-0534, about 05:41 to 05:50 local, status partial. Evidence in `_records_/2026-11-09/truck-plunder/0541-queue-run.md` (commit a9b838c5ed on records/2026-11-09). The unit moved to `_queue_/done/` by the ticker.
- Duel posture applied: tools/duel.py at entry reports duel day 1, theme Radar Training, day ends 2026-11-09 18:00 local, radar posture release. Truck dispatches do not score today, so the non-UR day rule governed (dispatch SR or above only, plunder UR or SSR trucks carrying UR shards with guard below Squad 1 at 24.96M). No Mega Mode dispatch was used or attempted.
- Entry - blocked, two methods failed. Base screen about 05:42: food 540.1M, iron 864.9M, coin 42.9M, gold 13.22K, diamonds 6,077, power 149,217,331, VS timer 12:18:35. Left column, re-grounded fresh on the live screenshot, top to bottom: hammer 1/4, flasks 1/2, light-blue train/bus front icon, white pickup, walkie-talkie with red badge 1, hammer, chest. The train-front icon carries NO red badge in this set.
- Method 1: title-bar tap at norm (180,15), then a tap on the freshly grounded train-front centre norm (55,594). The tap only panned the base map to the station area (golden train, Abŷss Apex, 00:27:31) - the trade screen did not open. This matches the 0242 no-badge pattern and re-confirms the standing rule a third time: a badgeless vehicle-front icon does not open trade.
- Method 2 (changed variant): a tap at norm (913,940) on the bottom-right WORLD corner, the 0242 WORLD-corner route. It opened the world map (alliance territory, [AP3x]Bears Lair base centre, March Queues 1/4), not Intercity Trade - the 0242 route did not reproduce in this framing. This re-confirms the 0538 correction a second time: 913,940 is a World-map opener, not a direct trade entry. Returned to base with the BASE button. Per queue rule R2, both methods end inside this unit; the next trucks unit must arrive with a changed method (a foreground click variant on the icon, or the station-area route) rather than repeating either point.
- CORRECTION, standing section: the Working entry route section above still told units to try the WORLD-corner route first when the column icon carries no badge. That instruction is superseded - the 0538 unit corrected it and this unit re-confirmed the correction, and this unit followed the stale instruction before its own read. The section now carries the dated correction; later units must not cite 913,940 as a trade entry.
- Counters - not re-read live. Today's Trade Count and Your Plunder Count Today were NOT read live in this unit: the trade screen never opened. The standing shortfall is carried from the 0250 unit's close (02:50 PT, read live then): Trade Count 4/5, Plunder Count 1/4. No counter is overwritten here, and no tally is derived - the next trucks unit re-reads both counters live on the trade screen first.
- Dispatch shortfall 1: all four slots were occupied at the 0250 close (dispatched about 02:40-02:50, arrivals about 06:30-07:00), so the 5th dispatch awaits a return or a Mega Mode dispatch, still an open question - not attempted in this unit. Plunder shortfall 3: no plunder fought in this unit. Reward Recovery was not checked: the Recover button sits on the trade screen, which never opened. R3 quota checkpoint: the trade day ends 18:00 PT; the 6-hour checkpoint falls at 12:00 PT and the 2-hour checkpoint at 16:00 PT, so no checkpoint is due in this unit and no priority escalation is raised now.
- Reading the blocker: the icon carries no badge, and the 1211/1846 precedent says the badgeless icon does not open trade - so this looks like a column-set availability issue (the trade slot is not surfaced in the current set), not a tap-accuracy issue. The set may rotate later in the day; the next unit re-grounds the column fresh before deciding.
- No diamonds or money spent. No Trade Contract spent. No truck dispatched, no plunder fought, no alliance mate touched. No login or verification was demanded, no different-device dialog appeared, and no password or Touch ID step was used.
- Result stats: target dispatch 5, plunder 4, achieved dispatch 0, plunder 0 (nothing completed in this unit; the carried shortfall dispatch 4/5, plunder 1/4 is the 0250 unit's live close, not a re-read here, so no trade_count or plunder_count is stated), points 0, resources_gained none, costs none, about 9 minutes of unit time, verified no, blocker_category e.
- Follow-up: the next trucks unit arrives with a changed entry method (foreground click variant on the icon, or the station-area route), re-grounds the column fresh, and re-reads both counters live on the trade screen first.

## What the 2026-11-09 1748 unit added - zero-sweep read, trucks 4/5 dispatch 1/4 plunder live, shortfall carried, fix-up raised to priority 1

- Unit zero-sweep-2026-11-09-1730 by ticker-1734, about 17:38 to 17:48 local, status partial - the sweep reads only, nothing claimed, no truck dispatched or plundered. Evidence in `_records_/2026-11-09/daily-activities/1748-queue-run.md` (commit 2f4d783d8 on records/2026-11-09). The trucks line (line 18) is one of the 5 lines read live in this unit.
- Counters read live on the trade screen: Today's Trade Count 4/5 (four trucks out on Your Truck tab), Your Plunder Count Today 1/4 (Others' Trucks tab). Unchanged from the 0250 unit's live close at 02:50 - no dispatch and no plunder has landed in the about 15 hours between the reads. Shortfall with the trade day ending at the 19:00 reset: dispatch -1, plunder -3.
- Fix-up: trucks-2026-11-09-1457 raised to priority 1 (expires 18:57); the executor runs it next in this pass. One inbox unit raised, no new unit enqueued - every unread line already had a queued unit.
- Entry route, measured in the current icon set: the blue truck-front icon at norm y about 573 opens Intercity Trade directly on the first tap; the jeep icon below it is the Secret Command Post, not trade. This resolves the entry block the 0541 unit hit earlier today (badgeless train-front icon only panned the map; WORLD-corner route opened only the World map). See the updated Working entry route entry.
- No diamonds or money spent. No Trade Contract spent.
- Result stats (sweep unit): target 23, achieved 5, resources_gained none, costs 10min-device-session, verified no, blocker_category h, lines_read 5, lines_nonzero 4, units_raised_priority1 1.

## What the 2026-11-09 1910 sync added - fix-up trucks-1457 expired unrun, trade-day shortfall closes unfilled

- Sync record in the ticker-1910 pass, about 19:14 local: the fix-up unit trucks-2026-11-09-1457 (raised to priority 1 by the 1748 sweep, expires 18:57) was reaped as expired - `_queue_/done/trucks-2026-11-09-1457.md` records status expired, window passed before execution, 0 attempts, finished 19:14 in the ticker-1910 pass (commit e05c662bd on records/2026-11-09). No truck was dispatched and no plunder was fought in this pass.
- CORRECTION: the 1748 section's "the executor runs it next in this pass" did not happen - the unit expired before execution. The ended trade day's shortfall (dispatch 4/5, plunder 1/4, shortfall -1/-3, last read live 17:40) closes unfilled; the counters reset with the new trade day at the 19:00 reset. No further fix-up is owed for the ended day.
- No diamonds or money spent. No Trade Contract spent.
- Result stats: target dispatch 5, plunder 4, achieved dispatch 4, plunder 1 for the ended trade day (shortfall -1/-3), verified yes (same-pass live reads), blocker_category none.

## What the 2026-11-09 2250 unit added - 4 settlements and the 18:00 Reward Recovery claim, dispatch and plunder unstarted, partial

- Unit trucks-2026-11-09-1857 by ticker-2230, about 22:31 to 22:50 local, status partial. Evidence in `_records_/2026-11-09/truck-plunder/2250-queue-run.md` (commit 70248cbb7 on records/2026-11-09). Computer session cc-354.
- Entry: the trade icon - blue circle, white truck glyph, red badge 4 - grounded fresh at norm (55,575) in the base left column, opened Intercity Trade on the Your Truck tab on the first tap. Third badged-icon entry datapoint in two days (1211 at 55,589, 1846 at 54,568); the point drifts with the column set, so re-ground fresh in every unit. HUD at base entry: food 582.7M, iron 906.5M, coin 70.1M, diamonds 13.22K, stamina 118, power 146,751,949.
- Duel posture: tools/duel.py reports duel day 2, Base Expansion, day ends 2026-11-10 18:00 PT; UR truck dispatches score 100,000 each; radar posture stack. Today is a UR dispatch day: UR only through Mega Mode.
- Counters: Trade Count 0/5 on the new trade day after the about-18:00 reset - second-day corroboration of the Issue #242 rollover (the 1846 read was day one). Plunder Count was not read; the Others' Trucks tab was not reached.
- Reward Recovery: the 2026-11-9 18:00 record claimed (1 unstarted transport, the old day's 5th dispatch shortfall): badge 500 x3, chest x2, gold chest x10, iron 1.5M, food 1.5M, coin 972.5K, plus 5m speed-up tiles; CONGRATULATIONS verified. The old trade day therefore closed 4/5 dispatched with the 1 unstarted transport recovered. The 2026-11-8 record was not expanded (two taps on its header and toggle produced no change); its claim state is unverified, and the next trucks unit re-checks it.
- Settlements: 4 returned trucks settled by opening their Truck Details (each open pays the reward; all four read "The vehicle is safe and secure", none plundered) - UR-scale iron 3.8M, food 3.8M, coin 2.4M (2 trucks: one badge 500 x1, one badge 500 x3); SR iron 2.5M, food 2.5M, coin 1.6M (2 trucks, badge 500 x1 each). Settlement totals: iron 12.6M, food 12.6M, coin 8.0M. With the recovery claim, the unit gained iron 14.1M, food 14.1M, coin 8.97M, badge 500 x8 in total.
- Details-panel paging: the panel pages with the side "<" / ">" arrows and the bottom-left blue arrow (previous). The control receipt's no_change_observed flag is UNRELIABLE for this panel - the SR-to-UR page reported no change yet the screenshot proved the page had turned. Verify paging on the screenshot, never on the receipt flag. Tapping outside the panel does not close it; the unit ended with the panel open on the 4th truck, which is harmless - the next unit re-reads the trade screen fresh.
- Not done: dispatch 0 of 5 new UR trucks (Mega Mode, duel day 2) - the yard is clear after the 4 settlements and no slot was used; plunder 0 of 4, Plunder Count unread. Both fall to the next trucks unit.
- No diamonds or money spent. No Trade Contracts spent. No paid button tapped. No login or verification demanded, no different-device dialog appeared.
- Result stats: target settle 4, dispatch 5, plunder 4, achieved settled 4, dispatched 0, plundered 0, resources_gained iron 14.1M, food 14.1M, coin 8.97M, badge 500 x8, costs 19m wall, no stamina, no diamonds, no contracts, verified yes, blocker_category h, trucks_settled 4, recovery_claimed 1, trade_count 0, plunder_count unread, device_takeovers 0.

## What the 2026-11-10 0248 unit added - first Mega Mode execution, 4 UR dispatched, 1 plunder won, partial

- Unit trucks-2026-11-09-2257 by ticker-0234, about 02:36 to 02:48 local, status partial. Evidence in `_records_/2026-11-10/truck-plunder/0248-queue-run.md` (commit 2802653981 on records/2026-11-10; issue numbers named in commit 2167966207). Duel day 2, Base Expansion - UR truck dispatches score 300,000 each live (CORRECTED 2026-11-10 0337: the Duel screen reads Dispatch UR Trade Truck +300,000, superseding the 100,000 Handbook rate in tools/duel_schedule.json; see the correction note at the end of this section).
- Entry: base-screen left column, blue truck-front icon with red badge 4, grounded at norm 52,569. Trade screen opened on Others' Trucks; Your Truck tab showed 4 empty slots and the Mega Mode button.
- Counters, read live on the trade screen: entry Today's Trade Count 0/5, Your Plunder Count Today 0/4, yard empty, no returned truck to settle. Close: Trade Count 4/5, Plunder Count 1/4, both read live in this unit.
- Mega Mode, first execution of the standing UR-day rule (see the dispatch section above for the mechanics): Mega Refresh rolls No.1 R 04:08:02, No.2 N 03:40:04, No.3 N 03:48:04, No.4 N 04:26:21; all four refreshed to UR (batch 1 No.1, No.2, No.4; batch 2 No.3 alone); 12 Trade Contracts spent (158 to 146), no diamonds; escorts Squad 1 25.20M, Squad 3 20.37M, Squad 2 19.08M, Squad 4 16.54M; four gold UR trucks visible on the road on the Your Truck view. Expected duel score 1,200,000 (4 times 300,000, corrected live rate), VERIFIED live by the 0435 duel-score read (personal total 1,650,000 at 04:35, up 1,200,000 from the 01:51 read of 450,000; commented on Issue #565). The "Refresh all to Reindeer Sleigh Ride" checkbox was left unchecked, unobserved. Filed as knowledge Issue #565 by this unit; this fold answers it.
- Plunder: attempt 1 [BROT]TPM01, UR, Lv.30, guard 11.2M, three UR shard stacks (100 x1 at positions 1, 2, 6) - Quick Plunder opened battle prep (25.20M vs 11.25M); the Battle tap showed the toast "The target has disappeared" and a second tap did nothing; the truck was gone from the road. No plunder counted - a listed target can vanish between inspection and Battle. Attempt 2 [STCL]De Stenenman, UR, Lv.30, guard 24.6M (prep 24.69M), two 500 x3 UR shard stacks at right-side cargo positions 5 and 6, arrives in 01:49 - Quick Plunder, Battle (25.20M vs 24.69M), Mission Completed. Yield, read live on the rewards screen: iron 951.8K, food 951.8K, coin 607.5K, 5m speedups x10 in four stacks (5, 2, 2, 1), UR shard 500 x3 plus Extra x3 (6 total), one blue chest x1. Plunder Count 1/4 after Return.
- Not done: dispatch 1 of 5 still open - all four slots are out until the trucks return (dispatches 03:42 to 04:37, plus the return leg), so the 5th dispatch is a second wave, not available now. Plunder 3 of 4 still open. Reward Recovery (Recover button, bottom left of the trade screen) still carries a red dot - not checked in this unit. (2026-11-10 0513 update: checked - the 2026-11-7 18:00 record claimed; the 2026-11-6 18:00 record's claim state is unverified, follow-up for the next trucks unit.)
- Coordinate lesson: one Return tap missed because pixel coordinates were passed where the control expects normalized 0-1000 coordinates; re-grounded at norm 662,893 and it worked. Coordinates for computer.control are always normalized.
- Mid-unit transient, about 02:51 during the No.3 refresh confirm: an observe call failed "target app exited or restarted", but LastWar was still running (pid 1908) and the refresh dialog was still up. No different-device dialog was seen in this unit; kick count 0.
- No diamonds spent. No other unit's work touched.
- Result stats: target dispatch 5, plunder 4, achieved dispatch 4, plunder 1, resources_gained iron 951.8K, food 951.8K, coin 607.5K, UR shards 500 x6, 5m speedups x10, blue chest x1, points 1200000 (live-read duel gain: 4 UR dispatches at the live 300,000 rate read 2026-11-10 0337, verified by the 0435 duel-score read of the personal total rising 1,200,000 - not an expected figure), costs 12 Trade Contracts, about 12 minutes, verified yes (counters and rewards read live in-unit), blocker_category h (by-design partial - the 15 minute unit cap closed the quota mid-way; dispatch 4/5, plunder 1/4, remainder resumes in the next trucks unit).
- CORRECTION 2026-11-10 0337 (this run): the 100,000 Handbook rate for a UR truck dispatch is superseded by the live Duel screen read of +300,000 per dispatch (0337 record, evidence `_records_/2026-11-10/troop-training/0337-queue-run.md`, commit b7e79a62). The 0248 expected score is therefore 1,200,000, not 400,000. The screen also reads Perform 1 UR Secret Task +225,000 (first live UR secret-task rate; the Handbook Legendary figure is 75,000, a different tier). tools/duel_schedule.json still carries the 100,000 rate; the tool-data correction belongs to the tool-developer (flagged on Issue #565). The duel-score unit's live personal-total read is the verification. The older posture lines in this profile that quote the Handbook 100,000 as tool-reported values stand as history of what the tool said; the live rate above governs. (2026-11-10 retro action A-2026-11-10-01, Issue #300: stats.points holds live-read scored gains only - never write an expected or Handbook-rate score into stats.points. The 1,200,000 in the 0248 stats above stands under this rule because the 0435 duel-score unit verified the +1,200,000 rise live on the personal total; it is a live-read gain, not an expected figure. The original 400,000 (4 x 100,000 Handbook) was the instance the retro cites. Future units: expected scores go in prose as expected, never in stats.points. Verification: the next retro's window points total contains no unit whose points is a Handbook-rate product; recheck 2026-11-11 retro.)

## What the 2026-11-10 0513 unit added - recovery claimed, 1 SSR plunder won, partial, 5th dispatch awaits returns

- Unit trucks-2026-11-10-0257 by ticker-0504, 05:05 to 05:13 local, status partial. Evidence in `_records_/2026-11-10/truck-plunder/0513-queue-run.md` (commit 19608e2c9e on records/2026-11-10). Computer session cc-402 on the owner Mac mini. Duel day 2, Base Expansion - UR truck dispatches score 300,000 each live (see the 0337 correction above; this unit's header still cites the stale 100,000 Handbook rate from tools/duel.py - no scoring impact, no dispatch this unit).
- Counters, read live on the trade screen: entry Today's Trade Count 4/5, Your Plunder Count Today 1/4. Close: Today's Trade Count 4/5, Your Plunder Count Today 2/4. Both read live in this unit.
- Reward Recovery: Recover button (red dot) opened the REWARD RECOVERY panel. First tap at norm 65,830 produced no change; re-grounded at norm 100,857 and the panel opened (R2 pivot - fresh measured centre). The 2026-11-7 18:00 record claimed (1 unstarted transport): puzzle piece x1, badge 500 x6, chest x1, purple chest x25, iron 1.9M, food 1.9M, coin 1.2M. CONGRATULATIONS verified, CLAIMED stamp read on the record afterwards. The 2026-11-6 18:00 record: its toggle tap flipped the arrow but the record content did not expand or scroll into view, so its claim state is unverified. Follow-up for the next trucks unit: scroll the recovery list and verify the 2026-11-6 record.
- Dispatch: none. All four slots are out - four gold UR trucks visible on the Your Truck road, two flame-marked (plundered en route). The 5th dispatch is a second wave and awaits the returns (dispatched 02:36 to 02:48, journeys about 3:42 to 4:37 plus the return leg, so roughly 07:00 to 09:00 local or later).
- Plunder: target SSR truck #2090 [heb] ...320942090, Lv.19, guard 2.4M (prep screen 2.45M), arrives in 03:04:00. Cargo: chest x10, item x1, gold bar x1, iron 1.1M, food 1.1M, coin 591.0K, two slots already crossed out. No UR shard stacks visible in the cargo row. First Quick Plunder tap at norm 548,848 hit the Food cargo tile and opened its tooltip instead; dismissed it with a road tap and re-grounded Quick Plunder at norm 545,881 (R2 pivot). Quick Plunder opened battle prep: Squad 1 25.20M vs 2.45M, five Lv.150 heroes checked. Battle, Mission Completed. Yield, read live on the rewards screen: iron 389.0K, food 389.0K, coin 197.0K, item x1. No UR shards, as the cargo carried none. Plunder Count 2/4 read live after Return.
- Token lease expired 13:20:08Z mid-unit; re-acquire was refused outside the 60 second renewal window (Issue #461). No other pass could take the token before the next tick at 13:30Z, so the unit continued on the claim lease to 13:25:14Z. The token must be released at pass end regardless.
- No different-device dialog seen in this unit; kick count 0. No diamonds or money spent, no Trade Contracts spent. No new UR dispatch this unit, so 0 new duel points.
- Result stats: target dispatch 5, plunder 4, achieved dispatch 4, plunder 2, resources_gained iron 2.289M, food 2.289M, coin 1.397M (plunder 389.0K/389.0K/197.0K plus recovery 1.9M/1.9M/1.2M), badge 500 x6, chest x1, purple chest x25, puzzle piece x1, item x1, points 0, costs no contracts, no stamina, no diamonds, about 9 minutes wall (inside the 15 minute cap), verified yes (counters and rewards read live in-unit), blocker_category h (by-design partial - the 15 minute unit cap closed the quota mid-way; dispatch 4/5 awaiting returns, plunder 2/4, remainder resumes in the next trucks unit), trucks_settled 0, recovery_claimed 1, trade_count 4, plunder_count 2.

## What the 2026-11-10 1411 unit added - all 4 returned UR trucks settled, HUD-verified, 5th dispatch and plunders resume next unit, partial

- Unit trucks-2026-11-10-1057 by ticker-1343, about 13:59 to 14:11 local, status partial. Evidence in `_records_/2026-11-10/truck-plunder/1411-queue-run.md` (commit b2c2b7a43 on records/2026-11-10). Computer session cc-465 on the owner Mac mini.
- Duel posture: duel day 2, theme Base Expansion, from tools/duel.py --json: day ends 18:00 local, 4.0 hours left at the read. Window: duel day 2 - UR trucks, Mega UR only. NOTE: this unit's header cites UR truck dispatches at 100,000 each from the Handbook rate - that rate is superseded by the 0337 live Duel screen read of +300,000 per dispatch (see the 0337 correction in the 0248 section). This is the second post-correction stale citation after the 0513 unit's header; flagged on Issue #565 by this run. No scoring impact here - no dispatch this unit.
- Counters, read live on the trade screen: entry Today's Trade Count 4/5; close Today's Trade Count 4/5 - no new dispatch this unit, so the count is unchanged. Plunder Count was NOT re-read in this unit: the Others' Trucks tab was never opened. Last live read 2/4 at 05:13. The next trucks unit must re-read it live before plundering.
- Entry: base-screen left column, the blue speech-bubble icon carrying a truck glyph with red badge 2, grounded at norm (55,573) - the same slot that held badge 4 at the 02:36 entry. The enlarged crop confirmed the glyph is a truck, not mail. Trade screen opened on Your Truck: four gold UR trucks on the road, two flame-marked (plundered en route).
- Settlement - all four returned UR trucks paid out. Truck 1 settled by opening its Truck Details (tap on the truck body at norm (366,452); a first tap at (366,410) hit the chest icon and did nothing): CONGRATULATIONS overlay, Squad 4 escort, iron 2.8M, food 2.8M, coin 1.8M - looted en route from 3.8/3.8/2.4. Truck 2 settled by paging right once (norm (981,515)): intact UR, iron 3.8M, food 3.8M, coin 2.4M, puzzle x1, red gem 100 x1, puzzle x1, gold chest x10, badge 500 x3, x3, x3. A second right-arrow tap at the same point produced no change (R2 pivot): instead of a third identical tap, the unit backed out to the road view - and the yard showed four empty slots with green + signs. No returned truck remained to tap.
- History Dispatch tab confirms the four 02:42:47 UR trucks and their final cargo: two intact at 3.8/3.8/2.4, two looted at 2.8/2.8/1.8 with crossed items.
- HUD reconciliation proves all four cargoes landed: base HUD before the unit read food 615.9M, iron 938.8M, coin 84.1M; after the unit food 629.2M, iron 952.1M, coin 92.6M - deltas +13.3M, +13.3M, +8.5M, matching the four-truck total of 13.2M / 13.2M / 8.4M within HUD rounding. Had only two trucks settled, the delta would have been about +6.6M / +6.6M / +4.2M.
- OPEN OBSERVATION - how trucks 3 and 4 cleared: only trucks 1 and 2 were settled by an explicit Truck Details view in this unit, yet the yard was empty afterwards and the HUD proves all four cargoes landed. The mechanism is unverified: either opening one details view settles every returned truck at once, or the second right-arrow tap did page and settle truck 3 while its screenshot looked identical to truck 2 (both intact UR trucks share the same cargo template), and the road view then cleared the last one - or the yard clears on view. Next trucks unit: watch whether a single details view clears the whole yard, and record the yard state after each settlement instead of assuming one truck per view.
- Not done - resumes next trucks unit. 5th dispatch (Mega Mode, UR only) not done: the yard is empty with four free slots, so the dispatch is available now. Trade Count 4/5. Plunder not done: Plunder Count not re-read this unit, last live 2/4 at 05:13. Two plunders remain against the quota. Reward Recovery not opened this unit: the 2026-11-6 18:00 record verification from the 05:13 follow-up is still open. The Recover button showed no red dot in the road screenshots, but that was not verified by opening the panel.
- Live reads: base screen after the check - Total Power 148,765,970, coin 92.6M, food 629.2M, iron 952.1M, diamonds 6,207, stamina 120. The trade icon badge now reads 1 (was 2 at entry).
- No diamonds or money spent. No Trade Contracts spent. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target dispatch 5, plunder 4, achieved dispatch 4, plunder 2 (plunder 2 is the last live read at 05:13, not re-read in this unit), resources_gained iron 13.3M, food 13.3M, coin 8.5M (HUD delta across the four settlements), points 0 (no new dispatch this unit), costs no contracts, no stamina, no diamonds, about 12 minutes, verified yes (counters, cargo and HUD delta read live in-unit), blocker_category h (by-design partial - the 15 minute unit cap closed the quota mid-way), trucks_settled 4 (2 by explicit details view, 4 cargoes HUD-verified landed), trade_count 4, plunder_count 2 (last live read 05:13, not re-read), follow_up re-read Plunder Count live and plunder to 4/4; dispatch the 5th UR truck by Mega Mode; verify the 2026-11-6 recovery record; watch whether one details view settles the whole yard.
