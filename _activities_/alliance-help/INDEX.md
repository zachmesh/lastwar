---
title: Alliance Help
created: 2026-10-25T18:58:00Z
modified: 2026-11-03T15:45:00Z
level: L1
version: 1.19.0
description: Alliance Help All and individual ally helps, one activity folder for help knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (0940 help unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1226 help unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1722 help unit)
  - source: alliance-help execution record 2026-11-01 2127 queue run (ticker-2104 unit, done, Help All pressed with only own requests visible)
  - source: ticker-0034 alliance-help execution record 2026-11-02 0039 queue run
  - source: ticker-0834 alliance-help execution record 2026-11-02 0836 queue run (done, Help All pressed, header 400 of 1000 unchanged)
  - source: alliance-help execution record 2026-11-02 1220 queue run (ticker-1204 unit, done, toast fired with 0 counted helps)
  - source: alliance-help execution record 2026-11-02 1741 queue run (ticker-1729 unit, partial, Healing Help request unhelped)
  - source: ticker-2034 alliance-help execution record 2026-11-02 2038 queue run (done, base-screen bubble, Alliance red dot is not remaining help)
  - source: alliance help execution record 2026-11-02 2311 queue run
  - source: ticker-0304 alliance-help execution record 2026-11-03 0308 queue run (done, header 980 unchanged by Help All)
  - source: ticker-0434 perception-scout execution record 2026-11-03 0446 queue run (observe-only, Help panel 1,240/1,000 over gate, four Bears Lair requests 30/30)
  - source: ticker-0704 alliance-help execution record 2026-11-03 0710 queue run (done, base-screen bubble, header 1,240/1,000 unchanged by Help All)
---


# Alliance help

## What this activity is

Pressing Help for allies in the Alliance help page. This folder
accumulates help knowledge - where the page lives, how the daily mission
counts helps, and any caps. Executions are recorded in
`_records_/<date>/alliance-help/`, one file per execution.

## How it is done

- Open Alliance, then the Help page.
- Press Help All. Individual helps are used only if Help All is not offered.
- Foreground precondition, recorded by the retro of 2026-10-31 -
  the 2026-10-31 1030 unit never opened the Alliance panel
  because Chrome stayed frontmost and background taps did not
  reach the Alliance button. Two no-change taps end the
  background-input method inside the unit under queue rule R2 -
  bring the game window to the foreground and re-observe before
  tapping again. The same-day later units recovered, so this
  blocker is transient, not a dead entry route.

## Standing instruction from the owner

- Whenever the alliance help icon shows waiting requests, click it
  and press Help All. The owner set this on 2026-10-25 - do not
  leave helps unpressed in any round or check.
- Clarified by the owner the same evening - the help icon on
  screen can be clicked directly whenever it becomes available,
  in any session and at any moment, autonomously. Do not wait for
  a round or a check, and do not ask first.
- The easiest form of the rule, owner taught later the same
  evening - on the main base screen a help bubble pops up at the
  lower right when allies request help. Click it the moment it
  appears; it works the same Help All, but it is easier on the
  main screen than opening the Alliance panel. The owner pointed
  out missed bubbles twice before this was learned, so treat the
  lower right of the base screen as a watch point in every
  session.
- What the bubble looks like, verified in game on 2026-10-26 -
  a yellow speech-bubble tile showing a hand holding a green
  missile, sitting immediately to the left of the Alliance
  shield button at the lower right of the base screen. One tap
  on the tile centre pressed the helps - the game answered
  Allies are very grateful for your assistance and the tile
  disappeared. If unsure what the help icon is, this tile is
  the reference; web guides describe the same control as the
  holding-hands icon at the bottom right.

## What is known from 2026-10-25

- Help All was pressed once in the round and cleared the waiting helps.
- The daily mission Help Allies 5 Times completed at 12 of 5 as displayed,
  so helps from other pages also count toward that mission.
- The red dot on the base Alliance button signals waiting helps.
  In the afternoon sweep the Help page header read Today's points
  gained from Alliance Help 400 of 1,000. Requests included allies
  building (another commander on a Lv.25 Farmland, Kkkayyyyy) and this
  account's own two requests - Lv.30 Drill Ground and Lv.30
  Aircraft Center - both already at 30 of 30, so a player cannot
  help their own requests. Help All cleared the allies' requests
  and the page answered Allies are very grateful for your
  assistance.
- Evening, new server day - the Help page header points had reset
  (Today's points gained read 20 of 1,000 when opened), confirming
  the help points tally is a daily counter. Help All cleared the
  new requests (Ripper Apex on a Lv.23 Missile Vehicle Base,
  K워니 on a Lv.22 Smelter, among others), after which the rows
  turned into reduced-time displays.

## What is known from 2026-11-01

Measured in the 0135 help unit (ticker-0134, window mode
642x951, no different-device dialog). Outcome: done.

- Background-input nuance, same pass as the 0139 mail
  failure: the game window was already open in window mode
  but covered by a Chrome window, with
  UserNotificationCenter frontmost. A title-bar click at the
  visible left segment did not change the frontmost app, but
  background input to the selected Last War window reached
  the game, so the unit proceeded on background input and
  every tap was verified by a fresh observation. This
  refines the 2026-10-31 foreground note above: background
  input is screen-dependent, not uniformly dead - panel
  screens accepted it in this pass while the base-screen
  right rail did not (see mail-rewards, 0139).
- The game opened on the Alliance Gifts panel, all listed
  gifts already Claimed. The back arrow returned to the
  Alliance menu, where the Help tile carried a red dot.
- Help page opened from the Alliance menu. Header read
  live: Today's points gained from Alliance Help 80/1,000.
  The visible requests were all the account's own (Bears
  Lair, each 30/30), which cannot be helped by the account
  itself.
- Help All pressed once. The game answered "Allies are very
  grateful for your assistance." A second observation still
  read 80/1,000, so the panel was closed and reopened rather
  than trusting the first re-read: the reopened header read
  live 160/1,000, confirming Help All added 80 points in
  this unit. Lesson: after Help All, close and reopen the
  panel for the confirming re-read; a single re-read can
  lag behind the true header.
- Note for the next unit: the Help tile red dot at menu
  entry did not correspond to visible ally requests in the
  list shown; the points gain confirms ally helps were
  cleared by Help All. A red dot is not proof of a visible
  request row, and a list of only own requests is not proof
  that Help All did nothing - read the header before and
  after.
- Incidental observation from the 0139 mail unit, not an
  action of that unit: while it opened, the Help panel
  header read 360/1,000, up from the 160/1,000 live re-read
  that closed this help unit; the rise came from allies
  helping this account's requests between units, not from
  any action in the mail unit. Do not count inter-unit
  help-received rises as help-given gains.



## What the 2026-11-01 0940 unit added

- Performed, ticker-0934, session about 09:39 to 09:41:
  Help All pressed. Entry from the Alliance Gifts screen
  left by the previous gifts unit: the back arrow at norm
  45,965 returned to the Alliance panel, and the Help tile
  grounded fresh on this unit's own screenshot at norm
  676,514 (close to the 2026-10-31 units point of 687,504)
  opened the Help page at once.
- Help page header read "Today's points gained from
  Alliance Help: 540/1,000". Every visible request was
  this account's own, each already at 30/30: Lv.28 Drill
  Ground building, Precision Targeting II research, Lv.30
  Aircraft Center building, Morale research. A player
  cannot help their own requests.
- Help All at norm 498,757 was pressed anyway per the
  standing rule, and the game answered "Allies are very
  grateful for your assistance!". The header still read
  540/1,000 after the press and the list still showed only
  the own 30/30 requests, so no further ally request was
  left waiting in this unit. Contrast with the 0135 unit,
  where a close-and-reopen re-read revealed a lagging
  header: here the own-only list composition corroborates
  the unchanged header, so the conclusion rests on list
  plus header together, not on a single re-read alone.
- The Help panel was closed with its X at norm 826,205,
  leaving the game on the Alliance panel. Nothing else
  spent - no diamonds, no money, no speedup items burned,
  no building or research started, no Assemble.

## What the 2026-11-01 1226 unit added

- Performed, ticker-1204, session about 12:26, status
  partial: the game was already on the Alliance panel
  from the gifts unit, and the Help entry carried a red
  dot, so waiting requests were present. No Help All
  press happened, so no help count or points figure is
  reported.
- Help entry route, failed in this session: the Alliance
  panel Help button was tapped three times with no change
  - twice at the start of the unit (norm 629,467 and
  695,471) and once more after re-entering the Alliance
  panel (695,471). The base-screen help bubble tile left
  of the Alliance shield button was tapped twice with no
  change either (norm 819,667 and 819,675); the tile
  stayed visible and no "Allies are very grateful" toast
  appeared. The control layer itself advised after the
  second bubble tap that background clicks do not reach
  some controls and suggested a foreground element click
  or keyboard instead; the game canvas exposes no
  accessibility element for these controls, and a LastWar
  open_app request returned outcome unknown with no
  verified change, so no further identical tap was made.
- Foreground precondition refined: this failure is
  control-specific, not session-wide - background input
  reached every other control used in this pass
  (Alliance, Gifts, Claim All, tabs, back arrows) but
  not Help. The next help unit needs a verified
  foreground session before tapping Help, not just a
  retry of the same taps. This extends, and does not
  supersede, the 2026-10-31 foreground note above: the
  0135 unit proved background input can work on panel
  screens, and this unit proves Help is the control it
  does not reach.
- Changed method per queue rule R2: after the two
  no-change Help taps the unit switched entry route to
  the base-screen bubble tile, and after that route also
  failed twice it re-entered the Alliance panel for one
  final Help tap instead of repeating the bubble tap.
- No rule R2 metadata rewrite is triggered by this unit:
  this is not a third consecutive partial for help - the
  previous help unit of the day (help-2026-11-01-0630)
  closed done. The blocker is named here for the next
  unit, and the tracker is untouched, so the next tick
  re-produces this regular.

## What the 2026-11-01 1722 unit added

- Performed, ticker-1704, session about 17:19 to 17:22
  (session cc-70 after the first computer session closed
  between units), status done: checked and Help All
  pressed.
- Header read live: Today's points gained from Alliance
  Help 1,040 of 1,000 - already over the daily tally.
  The tally display can read above 1,000; 1,000 is the
  displayed target, not a cap that stops the count. The
  daily help cap question stays open - this read does
  not answer what helpers or helped players receive.
- Visible requests were all the account's own (Bears
  Lair): Lv.30 Aircraft Center building, Precision
  Targeting II research, Morale research, Lv.28 Drill
  Ground building. A player cannot help their own
  requests - and Help All was pressed anyway per the
  standing rule. The game answered with the "Allies are
  very grateful for your assistance" toast, read live in
  the post-tap observation. Standing rule clarified by
  this unit: press Help All even when only own requests
  are visible; the toast confirms the press registered.
- This unit closes the 1226 failure mode for this
  control: Help, which background input could not reach
  in the 1226 unit, was reached and pressed here after
  the session change between units. The 1226 foreground
  precondition is not superseded - the session, not the
  tap, changed - but Help is reachable in a fresh
  session, so a Help failure is not a dead entry route.
- No diamonds or money spent, no red line touched.

## What the 2026-11-01 2127 unit added

- Done (checked and Help All pressed): unit
  help-2026-11-01-1830 by ticker-2104, third unit of the
  same pass after the training partial and the gifts done.
  Help page header read live: Today's points gained from
  Alliance Help 80 of 1,000, before and after the tap.
- Visible requests were all the account's own (Bears
  Lair): Lv.30 Aircraft Center building, Morale research,
  Precision Targeting II research, Lv.28 Drill Ground
  building. A player cannot help their own requests, and
  no ally request was visible - and Help All was pressed
  anyway per the standing rule and the 1722 precedent.
  After the tap the four rows read 30/30 (they read
  reduced-time displays before the tap); the header tally
  stayed 80 of 1,000, as expected with no ally request to
  help. The grateful toast was not captured in the
  post-tap screenshot, so no toast wording is claimed
  here - unlike the 1722 unit, where the toast was read
  live. No diamonds or money spent, no red line touched.
  Evidence in `_records_/2026-11-01/alliance-help/2127-queue-run.md`.



## What the 2026-11-02 0039 unit added

- Unit help-2026-11-01-2230 by ticker-0034, session about
  00:34 to 00:39, status done. The game was already open on
  the Alliance Gifts panel, all listed gifts already
  Claimed; the back arrow returned to the Alliance menu,
  where the Help tile carried a red dot.
- Help entry correction: two taps at norm 717,447 and
  755,450 produced no navigation, and a back-arrow tap
  also left the Alliance panel unchanged. The Help tile
  was then re-grounded from the proven coordinates of
  recent help units and tapped at norm 676,514 - the same
  point that opened the page at once in the 2026-11-01
  0940 unit - which opened the Help page at once. The
  earlier misses were a coordinate error (taps above the
  tile), not a dead entry route. Lesson: when Help taps
  miss, re-ground from the proven 676,514 point before
  concluding the route is dead.
- Help page header read live: Today's points gained from
  Alliance Help 240/1,000. Every visible request was the
  account's own (Bears Lair, each 30/30): Precision
  Targeting II research, Morale research, Lv.28 Drill
  Ground building, Lv.30 Aircraft Center building. A
  player cannot help their own requests.
- Help All pressed once at norm 498,733 per the standing
  rule. No "Allies are very grateful" toast was seen and
  the header still read 240/1,000 on the immediate
  re-read. Verification by reopening, per the 2026-11-01
  0135 unit: the panel was closed with its X and reopened
  from the Alliance menu, and the reopened header still
  read live 240/1,000, confirming no points were gained
  in this unit. The reopened rows showed "Time reduced"
  displays instead of 30/30 bars. Conclusion method,
  corroborating the 0940 unit: an unchanged header plus
  an own-only list plus Time-reduced rows together mean
  no ally request was left waiting in the visible list -
  unlike the 0135 unit, where the reopened header
  revealed a lagging gain.
  Evidence in `_records_/2026-11-02/alliance-help/0039-queue-run.md`.

## What the 2026-11-02 0836 unit added

- Unit help-2026-11-02-0630 by ticker-0834, session about
  08:34 to 08:37, status done. Help All pressed; no ally
  request was waiting. Evidence in
  `_records_/2026-11-02/alliance-help/0836-queue-run.md`.
- Help entry, centre tap beats a top-edge miss: the Alliance
  panel was already open on game entry, a first tap at the
  Help button's top edge produced no change, and a second
  tap at the visually grounded button centre, norm
  (688,500), opened the Help page. The Chrome window
  covering the game window did not block the centre tap
  and no foreground switch was needed; this qualifies the
  foreground precondition in How it is done above, in the
  same direction as the 2026-11-01 0135 panel-screen
  background-input note - panel screens accepted the tap
  here, while the base-screen right rail did not in the
  0139 mail failure.
- Help page header read live: Today's points gained from
  Alliance Help 400 of 1,000, unchanged before and after
  Help All. The visible list held only this account's own
  four requests (Bears Lair: Lv.28 Drill Ground building,
  Lv.30 Aircraft Center building, Morale research,
  Precision Targeting II research), all at 30/30 on entry.
  A drag scroll of the list surfaced no further rows, so
  no ally request was waiting.
- Help All pressed at norm (500,775). No toast and no
  points change followed, which matches no ally request
  waiting. The player's own requests cannot be helped by
  the player; after the press their rows showed Time
  reduced displays, as in the 0039 unit. The Help page
  was left open; the Alliance panel behind it still
  showed the Help entry without a waiting-request badge
  change to verify beyond the header counter.

## What the 2026-11-02 1220 unit added

- Unit help-2026-11-02-1030 by ticker-1204, session
  12:18 to 12:20, status done. Evidence in
  `_records_/2026-11-02/alliance-help/1220-queue-run.md`.
- Help All pressed at norm (500,775). Header read
  live before and after: Today's points gained from
  Alliance Help 400 of 1,000, unchanged, so 0 helps
  counted. The visible list held only this account's
  own four requests - the same four the 0836 unit
  listed (Lv.28 Drill Ground building, Lv.30 Aircraft
  Center building, Morale research, Precision
  Targeting II research) - all at 30/30 after the
  press. A drag scroll surfaced no further rows, so no
  ally request was verified waiting.
- Toast correction: the press DID produce the toast
  "Allies are very grateful for your assistance" with
  0 counted helps. The toast therefore proves nothing
  in either direction - it can fire with no counted
  help, and its absence in the 0836 unit does not by
  itself prove no help was waiting either. The header
  points counter governs: a counted help moves it,
  the toast does not. This qualifies the 0836 unit's
  no-toast reading above; it does not erase it.
- Entry nuance: from the Alliance Gifts screen left
  over from the previous unit, the back arrow at norm
  55,949 returned to the Alliance panel first try.
  That is screen-specific - it contrasts the 0817
  gifts unit, where panel back-arrow taps produced no
  change - so a working back arrow on one screen is
  not evidence it works on another. The Help page was
  left open.


## What the 2026-11-02 1741 unit added

- Unit help-2026-11-02-1430 by ticker-1729, session about
  17:33 to 17:41, status partial. Evidence in
  `_records_/2026-11-02/alliance-help/1741-queue-run.md`.
- Entry grounding correction: the first three taps on the
  Help button missed because they were measured too high
  (norm y 431 to 433); the visual grounding of the Alliance
  screenshot put the Help button centre at norm 686,531,
  and a tap there opened the Help page. That centre is
  consistent with the measured Help box centre 687,500
  recorded the same pass by the donations unit (inside the
  Help box 508-866, 465-536), so the two readings settle
  the panel grounding rather than conflicting.
- Help page header read live: Today's points gained from
  Alliance Help 440 of 1,000. Visible rows at entry: four
  own (Bears Lair) requests, all already time-reduced -
  Morale research, Precision Targeting II research, Lv.30
  Aircraft Center building, Lv.28 Drill Ground building.
  A player cannot help their own requests.
- New failure mode, first of its kind: one ally request
  below the own rows, papillon707, Need Healing Help, with
  no time-reduced label and no individual Help button on
  its row. Help All pressed twice at norm 498,731 produced
  no observed change (no toast, header still 440 of 1,000),
  and a tap on the papillon707 row itself at norm 498,631
  (the rule R2 pivot) also changed nothing. Result: 0 helps
  verified given; the Healing Help request remains unhelped
  and its mechanism is unknown. This differs from the three
  earlier help units of 2026-11-02 (0345, 0836, 1220), which
  closed done with no ally request waiting.
- Remaining work, carried: determine how a Healing Help
  request is helped - whether Help All covers it at all, or
  whether it needs a different surface such as the hospital -
  then help it. Do not record Help All as clearing Healing
  Help requests until a unit verifies it.


## What the 2026-11-02 2038 unit added - done through the base-screen bubble

- Unit help-2026-11-02-1830 by ticker-2034, session
  about 20:34 to 20:38, status done. Waiting helps
  present at entry were cleared through the
  base-screen bubble, the standing easiest form of
  this rule. Evidence in
  `_records_/2026-11-02/alliance-help/2038-queue-run.md`.
- Base screen showed the help bubble at the lower
  right, the yellow tile with a hand holding a green
  missile, immediately left of the Alliance shield
  button, as described in the activity metadata.
- Bubble centre tap (window coordinates about 821,
  720): the first tap attempt sent no input because
  the control observation was stale; a fresh
  observation followed by the same tap succeeded,
  so this was a tool retry, not a game blocker.
- The game answered with the toast "Allies are very
  grateful for your assistance", and a re-screenshot
  confirmed the help bubble had disappeared.
- Completion-criterion note: the Alliance button
  still showed a red dot after the press; that dot
  also covers other alliance notifications and was
  not counted as remaining help requests, since the
  bubble itself was gone and the toast confirmed the
  Help All action. Bubble gone plus toast equals
  done; an Alliance red dot alone is not remaining
  help.
- Help page header points tally was not read in this
  unit; no helps count or points figure is claimed.
  No items spent, no diamonds or money touched, no
  red line approached.


## What the 2026-11-02 2311 unit added - done, Help All toast but 0 countable helps

- Unit help-2026-11-02-2230 by ticker-2304, session
  about 23:11 to 23:12, status done. Evidence in
  `_records_/2026-11-02/alliance-help/2311-queue-run.md`.
- Navigation correction, from the Alliance Gifts
  screen: the back arrow's first two taps (35,902)
  and (40,902) produced no navigation. Per queue
  rule R2 the method changed: a fresh screenshot
  re-grounded the arrow glyph centre at (62,920),
  and that tap returned to the Alliance panel. The
  earlier taps had landed on the tile's top-left
  edge, not on the glyph. Lesson: tap the glyph
  centre, not the tile edge, for this back arrow.
- Opened Help from the Alliance panel. Header read
  live before the press: Today's points gained from
  Alliance Help 760 of 1,000. Pressed Help All. The
  game answered "Allies are very grateful for your
  assistance".
- Header re-read live after the press: still 760 of
  1,000, unchanged. The visible rows were all this
  account's own requests (Bears Lair: Morale
  research, Lv.30 Aircraft Center building, Healing
  Help, Lv.27 Drill Ground building), each showing
  30 of 30 after the press. A player cannot help
  their own requests, so the unchanged header means
  this press delivered no newly countable ally help
  in the list shown; no ally request row was visible
  in the list shown.
- Completion-criterion note: the grateful toast
  alone is not delivery proof. Helps verifiably
  delivered by this press: 0 by the header counter.
  The header re-read is the count; a toast with an
  unchanged header means the press found no ally
  request to help. Closed the Help panel back to the
  Alliance panel.


## What the 2026-11-03 0308 unit added - done, header 980 unchanged by Help All, toast again not proof

- Ticker-0304, unit help-2026-11-03-0230, about 03:08
  local, status done. Evidence in
  `_records_/2026-11-03/alliance-help/0308-queue-run.md`.
- From the Alliance Gifts screen, backed out to the
  Alliance panel and opened Help at the visually grounded
  position.
- Help page header read Today's points gained from
  Alliance Help 980 of 1,000. The listed requests were
  all this account's own (Bears Lair, 30 of 30):
  Precision Targeting II research, Lv.30 Aircraft Center
  building, Morale research, and Healing Help.
- Pressed Help All. The game answered "Allies are very
  grateful for your assistance". The header stayed 980
  of 1,000 afterwards, and the own requests then showed
  time reduced instead of 30 of 30. This re-confirms the
  2311 resolution: the grateful toast alone is not
  delivery proof, and the header re-read (980 before and
  after) supersedes any toast-counted reading, since the
  visible rows were all the account's own requests.
- No individual help was tapped, no other screen was
  changed.


## What the 2026-11-03 0446 scout walk added - observe-only, Help panel over the gate

- Ticker-0434 perception-scout unit, about 04:42 to 04:46
  local, observe-only: the Help panel was opened on a
  grounded tap at (687,497) and nothing was tapped there.
  Evidence in
  `_records_/2026-11-03/perception-scout/0446-queue-run.md`.
- Help page header read Today's points gained from
  Alliance Help 1,240/1,000, already over the 1,000 gate,
  against 980/1,000 at the 0308 unit: the header moves
  between units and the gate is passed for the day.
- The listed requests were all this account's own (Bears
  Lair, 30/30): building Lv.27 Drill Ground, building
  Lv.30 Aircraft Center, Morale research, Precision
  Targeting II research (fourth row partly cut off).
  Help All button present, observed only, not tapped, so
  no delivery claim is made from this walk. The Help dot
  maps to the help regular (already queued) with nothing
  new to claim here.

## What the 2026-11-03 0710 unit added - done through the base-screen bubble, header 1,240 unchanged

- Ticker-0704, unit help-2026-11-03-0630, about 07:05
  to 07:10 local, status done. Evidence in
  `_records_/2026-11-03/alliance-help/0710-queue-run.md`.
- Base screen at entry: power 149,940,141, stamina 120,
  March Queues 0/4, coins 5.9M on the HUD. The help
  bubble was present at the lower right, immediately
  left of the Alliance shield: grounded box norm
  778,654 to 873,738, centre 825,696. One tap at the
  bubble centre pressed the waiting helps: the game
  answered "Allies are very grateful for your
  assistance" and the bubble cleared on the next
  screenshot. Background input reached the game on the
  first tap; no foreground recovery was needed. One
  click without an observation id was rejected by the
  control channel before any input was sent; the retry
  carried a fresh observation id.
- Verification on the Alliance Help page, read live:
  header "Today's points gained from Alliance Help:
  1,240/1,000", matching the 0446 scout read, already
  over the 1,000 gate. All listed rows are this
  account's own Bears Lair requests (Lv.27 Drill
  Ground, Lv.30 Aircraft Center, Morale research,
  Precision Targeting research), each carrying a green
  "Time reduced" badge; no ally rows were pending. A
  Help All tap on that page left the header unchanged
  at 1,240/1,000, confirming no further ally help was
  waiting. This re-confirms the 2311 and 0308
  resolution: the grateful toast alone is not delivery
  proof, and the header re-read supersedes any
  toast-counted reading.
- Entry correction for the next unit: a first tap at
  norm 657,455 on the Alliance panel landed above the
  Help button and changed nothing; the Help button's
  grounded box is norm 507,490 to 865,574, centre
  686,532, and that tap opened the Help page.
  Eyeballed y estimates run low on this panel; use
  grounded box centres, not estimates. The centre is
  consistent with the 0446 scout's grounded 687,497.
- Result statistics: target 1, achieved 1, verified
  yes. Nothing claimed beyond the helps, nothing
  bought, no diamonds or money spent. Costs: 251
  seconds, no stamina or items spent. Note on the
  record itself: the unit file's evidence path was
  first written as 0717-queue-run.md at completion
  time and corrected to 0710-queue-run.md, and the
  costs stat was added to the unit file by hand after
  completion, since the complete call did not carry it
  - a record-hygiene note, not a play claim.

## Open questions

- The daily help cap and what helpers and helped players each receive.
- How a Healing Help request is helped (Help All, or a different surface such as the hospital) - first seen 2026-11-02 1741, papillon707 request unhelped after two Help All presses and a row tap.
