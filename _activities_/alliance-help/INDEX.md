---
title: Alliance Help
created: 2026-10-25T18:58:00Z
modified: 2026-11-10T06:47:13Z
level: L1
version: 1.35.0
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
  - source: ticker-1104 alliance-help execution record 2026-11-03 1121 queue run (done, bubble press, header 1240 over 1000 unchanged, Help All no requests yet)
  - source: ticker-1706 alliance-help execution record 2026-11-03 1716 queue run (done, Help All cleared one ally row, bubble first tap lost to foreground switch)
  - source: ticker-0204 alliance-help execution record 2026-11-04 0208 queue run (done, Alliance centre 931,709 re-confirmed, 880,720 miss recorded, header 520/1000 on new trade day)
  - source: ticker-0434 alliance-help execution record 2026-11-04 0451 queue run (done, bubble tile 814,688 left of shield 932,695, one tap clears)
  - source: ticker-0834 alliance-help execution record 2026-11-04 0837 queue run (done, Help All pressed, header 620/1,000 unchanged, red dot is own requests awaiting allies)
  - source: ticker-1224 alliance-help execution record 2026-11-04 1235 queue run (failed, Mac screen-capture channel failure, no game input dispatched, not authorization, not a different-device dialog)
  - source: ticker-0134 survivor-intake execution record 2026-11-05 0134 queue run and ticker-0204 alliance-gifts execution record 2026-11-05 0204 queue run (windowed 1920x1080 on an inactive Space, not native fullscreen - corrects the 1235 section wording)
  - source: ticker-1020 alliance-help execution record 2026-11-07 1038 queue run (failed, Mac mini back online, last_seen fresh 2026-11-07T18:19:37Z, Last War window 1920x1080 at (0,-360) on an inactive Space, capture failure; Mission Control recovery lesson and Ctrl+Right does not switch Spaces; Issue 282 class, not Issue 284)
  - source: ticker-1727 alliance-help execution record 2026-11-07 1736 queue run (done, Help All pressed from the base-screen bubble at norm 827,707, header 560/1,000, own requests only; record commit 69997e12a1 on records/2026-11-07)
  - source: ticker-1352 alliance-help execution record 2026-11-08 1413 queue run (done, Help All pressed, Help red dot cleared, points counter stayed 0/1,000 before and after, helps count not claimed; record commit bf20e1a48 on records/2026-11-08)
  - source: ticker-2201 alliance-help execution record 2026-11-08 2214 queue run (done, Help All pressed twice, points 100/1,000 to 360/1,000, header counter lag resolved, list scrolls; record commit 8960535c on records/2026-11-08)
  - source: ticker-0034 alliance-help execution record 2026-11-09 0100 queue run (done, Help All pressed once, one ally request cleared, header 360/1,000 unchanged in-session, own rows 30/30, base-screen bubble tile (609,713) no-change, Help (523,507), Help All (488,778), session cc-197 dropped, cc-200 recovery; record commit 77db994162 on records/2026-11-09)
  - source: ticker-0404 alliance-help execution record 2026-11-09 0419 queue run (done, Help All cleared one ally request, header 520/1,000 unchanged at close; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-1004 alliance-help execution record 2026-11-09 1019 queue run (partial, Alliance button unresponsive to background clicks in fullscreen, six taps in four variants, duplicate LastWar window 508052, Help All not reached, red dot waiting; record commit 09e4f0863 on records/2026-11-09)
  - source: ticker-1822 alliance-help execution record 2026-11-09 1846 queue run (done, bubble plus Help All cleared 2 ally requests, header 140 of 1000 unchanged; record commit 6761c35d1 on records/2026-11-09)
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
- Fullscreen Alliance-button failure, 2026-11-09 1019: in fullscreen 1920x1080 the Alliance shield button did not respond to six background taps in four variants (coordinate clicks, hold, second window), while the green menu arrow at (484,975) did respond to background input - background clicks reach some controls and not others in fullscreen. Two LastWar windows exist (489932 titled "Last War", 508052 empty title); the duplicate window may be part of the blocker. Changed method for the next unit: exit fullscreen to the native 642x951 window and retry the Alliance tap there, or find a click_element route if an Alliance label element appears in the observation. Do NOT repeat the fullscreen background-click sequence.

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
- What the "Today's points gained from Alliance Help" header counter counts: ANSWERED 2026-11-08 2214 - it counts the helps Help All delivers, but it does NOT update inside one open Help session: after each Help All press the header still showed the pre-press value until the page was closed and reopened (100/1,000 in-session after the first press, 340/1,000 after reopen; 340/1,000 in-session after the second, 360/1,000 after reopen). The 1413 unit's 0/1,000 read before and after was a stale in-session read, not a narrower count. Closing figures for help units must be read after a page reopen. (The 1413 section is left standing as the record of what was observed then.)


## What the 2026-11-03 1121 unit added - done through the base-screen bubble, header 1240 unchanged, Help All no requests yet

- Ticker-1104, unit help-2026-11-03-1030, about
  11:15 to 11:18 local, status done. Evidence in
  `_records_/2026-11-03/alliance-help/1121-queue-run.md`.
- Entry: base screen at entry showed the help bubble
  at the lower right, immediately left of the Alliance
  shield, grounded fresh at norm (823,700) -
  matching the 0710 unit grounded centre (825,696).
  One tap at the bubble centre pressed the waiting
  helps: the game answered Allies are very grateful
  for your assistance (captured in the control
  channel OCR) and the bubble was gone on the next
  screenshot.
- Verification on the Alliance Help page, read live:
  header Todays points gained from Alliance Help
  1,240 over 1,000, unchanged from the 0710 close.
  All listed rows are this account own Bears Lair
  requests (Lv.27 Drill Ground, Lv.30 Aircraft
  Center, Precision Targeting II research), each
  carrying a green Time reduced badge; no ally rows
  were pending. A Help All tap on that page
  (grounded (500,779)) answered No help requests yet,
  confirming no further ally help was waiting.
- Session: computer session cc-342 (carried from the
  gifts unit, dropped between units) restarted as
  cc-344 with no state lost. No different-device
  dialog.
- Entry notes carried forward: the Alliance button
  grounded centre on the base view is (931,709); the
  Help button grounded centre on the Alliance panel
  is (686,532), as recorded by the 0710 unit. Exited
  with the Help panel X to the Alliance panel, then
  the panel back arrow (164,931) to the base screen.
- Consistency note, not a contradiction: the header
  is unchanged despite the bubble press, but the
  header already reads above its 1,000 cap
  (1,240 over 1,000), so a bubble press is not header
  proof - the same lesson as the 0308 unit (Help All
  toast is not proof either). No earlier claim
  superseded.


## What the 2026-11-03 1716 unit added - done, one ally row cleared, bubble first tap lost to a foreground switch

- Ticker-1706, unit help-2026-11-03-1430, about 17:08
  to 17:16 local, status done. Evidence in
  `_records_/2026-11-03/alliance-help/1716-queue-run.md`.
  No different-device dialog.
- Base screen at entry: the game window 642x951 was
  already the target but a Chrome about blank window had
  covered its left part; a title-bar tap brought it to
  the foreground. The first tap on the bubble tile
  immediately left of the Alliance shield, grounded fresh
  at window (825,688), did NOT press the helps: the next
  screenshot still showed the tile and the Alliance red
  dot, with only a transient "Achievements 8/16
  Completed" tooltip. Cause not proven; the tap may have
  been consumed by the window-focus transition. Lesson,
  new for the bubble route: a bubble tap that leaves the
  tile and the red dot in place has not taken effect -
  verify on the next screenshot and go through the
  Alliance panel instead of re-tapping blindly. This
  qualifies the 0710 and 1121 bubble successes, where
  one tap sufficed with no foreground switch in between.
- Visual-estimate error, quantified this pass: two taps
  about 80px below the grounded Alliance centre opened
  Mail (a President Mail letter, read only, and then the
  Mail category menu). Both were exited with the back
  arrow only, with no delete, no claim and no purchase.
  Lesson: trust grounded coordinates over visual
  estimates on this screen - this pass's visual y
  estimates ran about 80px low, while every grounded tap
  landed correctly. This strengthens the 0710 note that
  eyeballed y estimates run low on the Alliance panel.
- Grounded window coordinates this pass: Alliance shield
  centre (928,688), Help button (688,493), Help All
  (500,779). Help All matches the 1121 grounded point
  exactly; the shield centre sits near the 1121 (931,709)
  point, session drift as usual, not a correction.
- Help page header read live: Today's points gained from
  Alliance Help 1,240/1,000, matching the 0710 and 1121
  reads. Help All was tapped and the game answered
  "Allies are very grateful for your assistance" and the
  AMD Commander Lv.25 Iron Mine row disappeared from the
  list - a verified ally help delivered, the first
  row-clearance delivery since the 1121 no-requests
  press. The remaining rows are this account's own Bears
  Lair requests (Lv.30 Aircraft Center, Lv.27 Drill
  Ground, Precision Targeting II research), each with a
  green "Time reduced" badge; a player cannot help their
  own requests, so nothing further was waiting.
- Consistency note, not a contradiction: the header
  stayed 1,240/1,000 on the single re-read after the
  press even though a row verifiably cleared. Per the
  2026-11-01 0135 reopen rule, a single re-read can lag
  behind the true header, and this unit did not
  close-and-reopen to re-read it, so no claim is made
  that the counter stopped moving above the gate. Row
  clearance is the delivery proof here; the header
  re-read alone is not.
- Exited with the Help panel X to the Alliance panel.
  Nothing spent, no red line touched.

## What the 2026-11-04 0208 unit added - Alliance centre (931,709) re-confirmed, header 520/1000 on new trade day

- Unit help-2026-11-03-2230 by ticker-0204,
  02:04 to 02:08 local, status done. No "active on
  a different device" dialog appeared; the base
  screen carried a "Signed in as HidingAnt504"
  toast, confirming the owner's account.
- Entry: the help bubble was present at the lower
  right, immediately left of the Alliance shield.
  One tap at the bubble tile answered "Allies are
  very grateful for your assistance" and the tile
  was gone on the next screenshot.
- Grounding correction inside this unit: the first
  two Alliance-button taps at (880,720) produced no
  panel change (rule R2 ends that method). The
  (880,720) point lands left of the shield, on the
  small round icon below it. Re-grounding from the
  2026-11-03 1121 record gave the Alliance button
  centre as (931,709); one tap there opened the
  panel. Future units should use (931,709) for
  Alliance, (686,532) for Help on the panel, and
  (500,779) for Help All on the Help page. This is
  consistent with the 1716 note that the shield
  centre sits near the 1121 (931,709) point,
  session drift as usual - not a new correction to
  the shield centre itself, but (880,720) is now a
  recorded miss, not a usable Alliance point.
- Verification on the Alliance Help page, read
  live: header "Today's points gained from
  Alliance Help: 520/1,000". This is the first
  sub-gate read after the 2026-11-03 1,240/1,000
  reads, on the new trade day - not a
  contradiction, the daily counter resets. All
  listed rows are this account's own Bears Lair
  requests (Defense Training VIII research, Lv.30
  Aircraft Center building, Weapon Training VIII
  research, Lv.27 Drill Ground building), each
  carrying a green "Time reduced" badge; no ally
  rows were pending. A Help All tap on that page
  answered "No help requests yet", confirming no
  further ally help was waiting.
- Exited with the Help panel X to the Alliance
  panel, then the panel back arrow (164,931) to
  the base screen. Nothing spent.

## What the 2026-11-04 0451 unit added - bubble tile (814,688) left of the shield, one tap clears

- Unit help-2026-11-04-0230 by ticker-0434, 04:51 local, status done. The computer session dropped between units and was restarted (cc-415 to cc-418); no game state was lost. No "active on a different device" dialog appeared.
- Base screen watch point checked: the help bubble tile was present at the lower right, grounded at norm (814,688), immediately left of the Alliance shield button grounded at norm (932,695) - against the 0208 Alliance centre (931,709), the shield centre drifts per session as usual.
- One tap on the bubble tile centre pressed Help All: the game answered with the toast "Allies are very grateful for your assistance!" and the tile disappeared from the base screen, verified on the following screenshot (Alliance shield remains, help tile gone). No Help page was opened, no individual helps were needed, and no count of helped allies was displayed by the game - the toast and the vanished tile are the verification, not a number. Tracker marked done. Nothing spent.

## What the 2026-11-04 0837 unit added - Help All pressed, header 620/1,000 unchanged, red dot is own requests awaiting allies

- Unit help-2026-11-04-0630 by ticker-0834, about 08:35 to 08:37 local, status done. Evidence in `_records_/2026-11-04/alliance-help/0837-queue-run.md`. No diamonds, money, speedups or other spending. No different-device dialog appeared.
- Entry, foreground lesson repeated: the game was already on the Alliance panel at entry (left by the previous unit). The Help tile carried a red dot. A first background tap on Help did not navigate (window covered by Chrome); a second tap at the measured Help tile centre opened the Help page, matching the standing foreground lesson for this activity.
- Header, read live: Today's points gained from Alliance Help 620/1,000. Visible requests were all this account's own, each already 30/30 and therefore not helpable by this account: Lv.30 Aircraft Center building, Defense Training VIII research, Weapon Training VIII research, Lv.27 Drill Ground building - the same four own rows as the 0208 and 0451 units. A list drag did not reveal further rows.
- Help All pressed once. Header unchanged after the press at 620/1,000, so no ally help was actually available to press in this unit; the red dot reflects the own requests awaiting other allies, not pressable ally requests. This repeats the 0208 lesson (Alliance red dot is not remaining help) on the Help page itself.
- Help panel closed with the X, back to the Alliance panel. Nothing spent.

## What the 2026-11-04 1235 unit added - NEW failure mode: screen-capture channel failure before any observation, failed

- Unit help-2026-11-04-1030 by ticker-1224, about 12:24 to 12:27 local, status failed (access-failed). Evidence in `_records_/2026-11-04/alliance-help/1235-queue-run.md`. This is a NEW failure class for this activity, distinct from every foreground and tap failure recorded above: the unit never reached an observation at all.
- Capture sequence, all failed with the same error: activate LastWar, computer.observe, open_app LastWar, computer.observe again, computer.control describe, and a screenshot action - every screen-capture step failed with "Failed to start stream due to audio/video capture failure". Device state at the time: Mac online, LastWar app running fullscreen, Google Chrome frontmost; connection health connected on both native and web transports.
- Classification, stated explicitly: this is a screen-capture channel failure, NOT a missing owner authorization and NOT a different-device dialog (no such dialog appeared). It does not contradict the foreground notes above - those concern taps that dispatch but do not reach a control, while here no screenshot existed to tap from.
- No game input was dispatched and no tap was sent, so no in-game state changed. Help All was NOT pressed and no help count was read; nothing observed is claimed.
- Retry rule satisfied: at least 3 capture attempts were made in this pass (activate plus repeated observe, describe and screenshot attempts) before the access failure was recorded.
- Follow-up from the record itself: the tracker is untouched per the failed-unit rule, the regular remains due, and the next tick re-produces it as a fresh unit with this unit retried first. If the capture failure persists across passes, it escalates as a device-channel fault, not as a repeat of the same taps.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh) and by the 0734 arms-race and 0804 donations records on the same day (thirty-seventh and thirty-eighth occurrences, probe OFF_SCREEN_WINDOW, Chrome observing normally in the same sessions). The View menu lists "Enter Full Screen", so the app is NOT in native fullscreen: it is a windowed 1920x1080 window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission.
- Superseded in this profile: the "LastWar app running fullscreen" wording in the 1235 section above. The rest of that section stands unchanged: the capture sequence, the classification (a screen-capture channel failure, not authorization and not a different-device dialog), and the follow-up rule.
- Follow-up corrected: the unblock is getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step. This correction changes no Help state: no help count was read in the 1235 unit and none is asserted here.

## What the 2026-11-07 1020 unit added - Mac back online, window off-Space, capture failure returns (Issue 282 class, not 284)

- Unit help-2026-11-07-0630 by ticker-1020, about 10:23 to 10:39 local, status failed (access-failed, screen-capture channel failure). Evidence in `_records_/2026-11-07/alliance-help/1038-queue-run.md`. No Help All was pressed, no help count or points figure was read, and no game input was dispatched to Last War at all. Nothing was claimed, spent or changed in the game.
- What changed since the 1003 failure: the Mac mini is back online. device.list at about 10:23 local showed Zhen's Mac mini online with last_seen 2026-11-07T18:19:37Z, fresh. The 1003 pass failed with the Mac offline (last_seen frozen at 2026-11-05T15:36:52Z, Issue 284, one-hundred-sixth consecutive access-failed pass). This pass is NOT that failure: the device answers, the computer-use channel works, and the blocker moved to the game window itself. Connection health on both native and web transports: connected and healthy. The one-hundred-six-pass offline streak ends with the 1003 pass.
- The blocker: the Last War window (1920x1080, window_id 160366) sits at global (0, -360) and reports window_on_screen false. Every capture attempt failed with "Failed to start stream due to audio/video capture failure" - the off-screen window pixel stream, the same class as the 2026-11-04 1235 unit and the 2026-11-05 correction (windowed 1920x1080 window on an inactive Space). This is NOT a missing owner authorization and NOT a different-device dialog: no such dialog appeared at any point.
- Recovery attempts, all in this pass: Activate LastWar, observe, open_app LastWar, describe - capture failure each time, window not on screen. set_window_frame to (0, 0, 1920, 1080) was refused: it needs a fresh observation, which the capture failure blocks. Activating Finder (window 168864, helper) worked once and produced a full observation - proving the channel itself is alive.
- NEW LESSON - never open Mission Control as a recovery step: open_app Mission Control (first launch) opened the overview; every later activate and observe then failed with geometry_mismatch origin_delta 256+, agent_display false, and all key input gated on observation_required. A second open_app Mission Control closed the overview and the observation channel recovered - launching Mission Control twice toggles it. Do NOT open Mission Control unless the overview itself is the work; if it is open, a second launch closes it and restores observation. Mission Control overview itself cannot be observed or clicked through this channel: observe fails with no target window while it is open, and input stays gated on a fresh observation. Its thumbnails are not reachable from here.
- NEW LESSON - background Ctrl+Right does NOT switch Spaces: the key went to the Finder column view (CUHelper textfield selected, no Space change). Background keyboard input reaches the selected window, not the system Space switcher. No Space-switch route through this channel worked.
- The known reliable unblock stands (2026-11-05 correction): the owner clicking the LastWar Dock icon once brings the window to the active Space. That step needs the owner at the Mac; it was not available in this detached pass. No Dock icon was clicked blind: the icon position is unverified and a blind Dock click could activate the wrong app.
- Side effects of this pass: none in the game. Outside the game: Mission Control was opened and closed twice (left closed, verified by a working Finder observation afterwards). One Finder column-view selection changed (CUHelper textfield selected by the Ctrl+Right test); no file was opened, renamed or moved. The Mac was left with the Finder helper window observable and Mission Control closed.
- Follow-up: tracker untouched per the failed-unit rule; the regular remains due and the next tick re-produces it as a fresh unit. If the window is still off-Space at the next pass, the owner clicking the LastWar Dock icon once is the unblock. This is a different failure mode from Issue 284 (Mac offline): the device is online and the window is off-Space. The Mission Control and Ctrl+Right lessons above are channel rules for every activity, not only Help: they are commented onto Issue #282 with this occurrence so the other capture-failure sections can pick them up.

## What the 2026-11-07 1736 unit added - done through the base-screen bubble, header 560/1,000, own requests only

- Unit help-2026-11-07-1430 by ticker-1727, about 17:29 to 17:36 local, status done. Evidence in `_records_/2026-11-07/alliance-help/1736-queue-run.md`. Computer session cc-20, LastWar already running; Chrome frontmost at entry, LastWar selected for background input and the taps landed (no foreground repair needed this unit).
- Base screen showed the yellow help tile immediately left of the Alliance shield button at the lower right. One tap on its fresh-grounded centre (norm 827,707) pressed Help All: the game answered "Allies are very grateful for your assistance!" and the tile disappeared from the base screen. Against the 0451 grounding (814,688), the tile centre drifts per session as usual - re-ground per session, never reuse a stored point.
- Verification on the Alliance Help page (Alliance, then Help): "Today's points gained from Alliance Help: 560/1,000" read live. The list held only this account's own requests, all showing reduced-time displays - Defense Training VIII research 10:02:00, Lv.27 Drill Ground 1d 03:17:41, Lv.30 Aircraft Center 3d 23:58:04, Missile Mastery II research 15:00:22 - so no ally request waited after the press. The panel Help All button was left untouched: nothing remained that it could press.
- Alliance panel at entry read [AP3x] The Apex, Leader Abyss Apex, Power 13,327,864,949, Members 96/100.
- Figures read live: Power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M, stone 25.0M, 922.2K; stamina 79; diamonds 3,702.
- No diamonds, money, speedups or paid buttons were used. No login or verification was demanded, and no different-device dialog appeared.
- Follow-up: the 1742 gifts unit in this same pass found Help carrying a fresh red dot after this Help All - new requests arrived during the pass, so a later help unit re-checks; the red dot is not read as remaining help from this unit.

## What the 2026-11-08 1413 unit added - Help All pressed, red dot cleared, points counter stayed 0/1,000 (open question)

- Unit help-2026-11-08-1030 by ticker-1352, about 14:08 to 14:13
  local, status done. Evidence in
  `_records_/2026-11-08/alliance-help/1413-queue-run.md` (commit
  bf20e1a48 on records/2026-11-08).
- No help bubble was visible on the base screen at entry, but the
  Alliance button carried a red dot, so the Help page was opened via
  Alliance, Help (red dot on the Help entry).
- HELP popup read live: "Today's points gained from Alliance Help:
  0/1,000". The visible rows were only this account's own four
  requests (Bears Lair - Missile Mastery II research, Lv.27 Drill
  Ground, Defense Training VIII research, Lv.30 Aircraft Center),
  each already showing "Time reduced" (helped by allies). The list
  does not scroll - no further rows exist below.
- Help All pressed: the game answered "Allies are very grateful for
  your assistance!". The Help entry's red dot is GONE on the
  Alliance panel afterwards (verified live against the pre-press
  panel, where Help carried a dot) - the waiting requests were
  cleared.
- ANOMALY - points counter still 0/1,000 (open question, added to
  the Open questions list): the header counter read 0/1,000 both
  before and after the Help All press, even though the toast fired
  and the red dot cleared. Either the counter updates with a lag, or
  it counts something narrower than the pressed helps. The number of
  helps actually delivered is therefore NOT claimed here - only the
  dot-clear and the toast are the verified evidence. The next help
  unit should re-read the counter at entry to see whether it has
  moved. Recorded in the profile's open questions, not filed as a new
  Issue (the gap belongs to this profile). Context: the counter has
  read 1,240 over 1,000 (2026-11-03 1121 unit) and 560/1,000
  (2026-11-07 1736 unit) after Help All presses, so a 0/1,000 read
  that does not move after a successful Help All is new.
- Note: the Alliance Gifts entry shows a fresh red dot again (a "Doom
  Walker Loot received!" toast arrived during this unit) - new gifts
  keep arriving; that is the next gifts unit's work, not this unit's.
- Closing reads: Help All pressed, toast confirmed, Help red dot
  cleared, points counter 0/1,000 (unexplained, see anomaly).
  Returned to the base screen (power 149,850,353). No diamonds,
  money, speedups or other spending. No alliance diplomacy, no
  assembly, no teleport.
- Result stats: target 1, achieved 1, resources_gained none, costs
  5m_wall_no_stamina, verified yes, blocker_category none,
  helps_pressed unverified_count, help_points 0,
  help_red_dot_cleared true.

## What the 2026-11-08 2214 unit added - Help All twice, points 100 to 360, counter lag resolved, list scrolls

- Unit help-2026-11-08-1830 by ticker-2201, about 22:03 to 22:09 local, status done. Evidence in `_records_/2026-11-08/alliance-help/2214-queue-run.md` (commit 8960535c on records/2026-11-08).
- Base screen at entry: no help bubble visible, but the Alliance button carried a red dot, so the Help page was opened via Alliance, Help (red dot on the Help entry).
- HELP popup read live at entry: "Today's points gained from Alliance Help: 100/1,000". The four visible rows were only this account's own requests (Bears Lair - Missile Mastery II research, Lv.27 Drill Ground, Defense Training VIII research, Lv.30 Aircraft Center), each already at 30/30.
- Help All pressed: the game answered "Allies are very grateful for your assistance!". The header still read 100/1,000 in the same open session.
- Help page closed and reopened: header now read live 340/1,000, a gain of 240 points from the first Help All.
- Scrolling the list down revealed a fifth row below the fold: Abyss Apex, "Need help with building Lv.28 Oil Well", shown white with no "Time reduced" label - still pending after the first press.
- Help All pressed a second time: the toast fired again. The header still read 340/1,000 in-session, and the Abyss Apex row was gone from the list on the next scroll check.
- Help page closed and reopened a second time: header now read live 360/1,000, a further gain of 20 points.
- Closing state verified live: points 360/1,000, only the four own 30/30 rows remain in the list, no pending ally request visible. No diamonds, money, speedups or other spending. No alliance diplomacy, no assembly, no teleport.
- CORRECTION (1) - the list DOES scroll: the 1413 section's "The list does not scroll - no further rows exist below" is superseded. Scrolling the list down in this unit surfaced a fifth row below the fold (Abyss Apex, Lv.28 Oil Well, still pending after the first Help All press). A unit that reads only the visible rows can miss a pending ally request. The 1413 section is left standing as the record of what was observed then.
- CORRECTION (2) - the counter lag is resolved: the 1413 open question (header counter 0/1,000 before and after a successful Help All) is answered. The points header does NOT update inside one open Help session: after each Help All press it still showed the pre-press value until the page was closed and reopened. This explains the 1413 0/1,000 anomaly - that unit read the counter only in-session. Closing figures for help units must be read after a page reopen. The Open questions entry is updated to record the resolution.
- Correction, from the record itself: the unit ran 22:03 to 22:09 local, about 6 minutes (duration_seconds 334), not 22:04 to 22:14. The closing figures (points 100 to 360) are unaffected.
- Result stats: target 1, achieved 1, resources_gained 260 Alliance Help points, costs 6m_wall_no_stamina, verified yes, blocker_category none, points_before 100, points_after 360, points_gained 260, helps_pressed unverified_count, help_red_dot_cleared true, device_takeovers 0.

## What the 2026-11-09 0100 unit added - Help All cleared one ally request, header 360/1,000 unchanged in-session, bubble tile not the entry

- Unit help-2026-11-08-2230 by ticker-0034, about 00:57 to 01:00 local, status done. Evidence in `_records_/2026-11-09/alliance-help/0100-queue-run.md` (commit 77db994162 on records/2026-11-09).
- Help page read live at entry: "Today's points gained from Alliance Help: 360/1,000". Four rows - three own (Bears Lair: Missile Mastery II research, Defense Training VIII research, building Lv.30 Aircraft Center) and one ally (building Lv.21 Crystal Factory).
- Help All pressed once: toast "Allies are very grateful for your assistance!"; the ally row is gone; the three own rows read 30/30. The header still read 360/1,000 at the closing read, so no points increase is claimed - the single cleared ally request is the verified outcome. This is consistent with the 2214 resolution (the header does not update inside one open Help session; closing figures must be read after a page reopen) - the 0100 unit read the header only in-session, so 360/1,000 is not a closing figure.
- Entry correction: the base-screen help bubble tile (tan tile immediately left of the Alliance shield button, grounded centre (609, 713) in fullscreen) was tapped once with no change - it is not the working Help All entry on this screen; the Alliance panel route is the verified one. Help button in the Alliance menu carries a red dot while requests wait, grounded at (523, 507); Help All button grounded at (488, 778). (The 0451 bubble tile at (814, 688) cleared with one tap in its framing; the (609, 713) point in this fullscreen framing did not - the bubble tile point is framing-bound and must be re-grounded fresh, not reused across framings.)
- Session note: computer session cc-197 dropped mid-unit (observation unavailable); session cc-200 was started, LastWar re-selected, and no game state was lost. Commented onto Issue #282 by this run (device-channel family, distinct from the capture-failure form).
- No diamonds or money spent. No other unit's work touched. Assemble was not opened.
- Result stats: target 1, achieved 1, resources_gained none, costs about 4 minutes of unit time, no items spent, verified yes, points 0 (no increase claimed - in-session read only), helps_pressed 1 verified row cleared, device_takeovers 0.

## What the 2026-11-09 0419 unit added - Help All cleared one ally request, header 520/1,000 unchanged in-session

- Unit help-2026-11-09-0230 by ticker-0404, about 04:18 to 04:19 local, status done. Evidence in `_records_/2026-11-09/alliance-help/0419-queue-run.md` (commit 9fdcc4c9ee on records/2026-11-09). Computer session cc-219 on the owner Mac mini.
- Entry: Alliance button tapped at norm 916,715 from the panned base view. The Alliance panel read live: [AP3x] The Apex, Leader Jerry Apex, Power 13,532,886,654, Members 96/100. The Help button carried a red dot.
- Help page opened at norm 685,515. Header read live: "Today's points gained from Alliance Help: 520/1,000".
- Rows before Help All: three own requests, all already 30/30 - Bears Lair, Missile Mastery II research; Bears Lair, Defense Training VIII research; Bears Lair, building Lv.30 Aircraft Center - and one ally request: 꿀밤Bamie, Oil Output I research.
- Help All tapped at norm 495,765. The toast read live: "Allies are very grateful for your assistance!"
- Closing read: the ally row is gone; the three own rows now read reduced-time displays - Missile Mastery II "Time reduced: 18:00:22", Defense Training VIII "Time reduced: 10:02:00", Lv.30 Aircraft Center "Time reduced: 3d 23:58:04". The header still read 520/1,000 at the closing read, so no points increase is claimed - the single cleared ally request is the verified outcome. This matches the standing pattern across the 0836, 0308, 0710, 0837 and 0100 units (header unchanged in-session); the 2214 unit is the exception where the header moved 100 to 360. (1846 update: a sixth in-session-unchanged datapoint - header 140/1,000 after the bubble press plus Help All cleared two ally requests.)
- Help dialog closed with its X; back arrow returned the game to the base screen. The game was left on the base screen. No diamonds or money spent, no other unit's work touched, Assemble not opened.
- Result stats: target 1, achieved 1, resources_gained none, points 0, costs 2m_wall_no_stamina, verified yes, helps_cleared 1, device_takeovers 0.

## What the 2026-11-09 1019 unit added - Alliance button unresponsive to background clicks in fullscreen, Help All not reached, partial

- Unit help-2026-11-09-0630 by ticker-1004, about 10:06 to 10:19 local, status partial. Evidence in `_records_/2026-11-09/alliance-help/1019-queue-run.md` (commit 09e4f0863 on records/2026-11-09).
- Base screen at entry (fullscreen 1920x1080, window 642x951 zoomed via the green zoom button): power 149,217,331, coin 46.2M, food 544.5M, iron 871.8M. The bottom bar was clipped in the windowed view, so the pass went fullscreen for a full view.
- Green up-arrow menu button tapped once at (484,975): the side menu expanded (HEROES / WORLD labels, Alliance, Mail, Inventory buttons visible on the right). Background input reaches the game for this control.
- Alliance shield button carries a RED DOT (seen live in a cropped screenshot, top-right of the tile) - help requests are waiting. The Help page was never reached, so the points header was never read and no points figure is claimed.
- Alliance button tapped six times in four input variants, all at the freshly grounded centre (visual grounding bbox x 626-673, y 678-747; centre about (650,712); cursor seen on the shield in the cropped screenshot): (1) click at (715,701) on window 489932 - no change; (2) click at (650,712) on window 489932 - no change; (3) left_mouse_down / 1s hold / left_mouse_up at (641,694) on window 489932 - no change; (4) click at (650,712) on window 508052 - small press animation only (5% changed area), panel never opened; (5) left_press at (650,700) on window 508052, 3s wait - no change; (6) move + click at (654,700) on window 508052, 3s wait - no change.
- Two LastWar windows exist, both 1920x1080 at (0,0): window 489932 titled "Last War" and window 508052 with an empty title. The duplicate window is a new finding and may be part of the blocker.
- Blocker, queue rule R2: same-method taps ended after the second no-change tap; the variants above were the pivot attempts inside this unit. The Alliance button does not respond to background coordinate clicks in this fullscreen session, while the green menu arrow does. Changed method for the next unit: exit fullscreen to the native 642x951 window (menu View to Exit Full Screen) and retry the Alliance tap there, or find a click_element route if an Alliance label element appears in the observation. Do NOT repeat the fullscreen background-click sequence.
- The red dot means the objective is still pending, not absent: the next help unit must still press Help All.
- Result stats: target 1, achieved 0, resources_gained none, costs about 13 minutes of unit time, no items spent, verified no, blocker_category c, points 0.

## What the 2026-11-09 1846 unit added - bubble press plus Help All cleared two ally requests, header 140/1,000 unchanged in-session

- Unit help-2026-11-09-1430 by ticker-1822, about 18:43 to 18:46 local, status done. Evidence in `_records_/2026-11-09/alliance-help/1846-queue-run.md` (commit 6761c35d1 on records/2026-11-09).
- The base-screen help bubble (yellow tile left of the Alliance shield, lower right) was tapped once at 18:44 and the game answered "Allies are very grateful for your assistance!" - the bubble press works from the base screen.
- Help page opened afterwards to verify: header read "Today's points gained from Alliance Help: 140/1,000". Two ally requests were still waiting - PrincessEsra10xoxo (Lv.21 Crystal Factory) and AMD Commander (Lv.29 Oil Well) - plus this account's own two requests, both already 30/30 (Missile Mastery II research, Lv.30 Aircraft Center).
- Help All pressed at 18:46; the game answered "Allies are very grateful for your assistance!" again and both ally rows left the list. Only the two own 30/30 requests remain.
- The points header still read 140/1,000 after both presses - recorded as read; whether the counter lags or counts only some helps is an open question, not a conclusion. This is the sixth in-session-unchanged datapoint (see the updated pattern note in the 0419 section); the 2214 unit remains the only exception where the header moved in-session.
- No diamonds or money spent. No other unit's work touched.
- Result stats: target 2, achieved 2, resources_gained none counted (helps given, points header read 140/1,000 unchanged), costs about 3 minutes of unit time, no items spent, verified yes, points 0.

## What the 2026-11-09 2124 unit added - done through the base-screen bubble, header 420/1,000, only own requests remain

- Unit help-2026-11-09-1830 by ticker-2109, about 21:22 to 21:24 local, status done. Evidence in `_records_/2026-11-09/alliance-help/2124-queue-run.md` (commit 88c1abf8e on records/2026-11-09).
- Base screen: the yellow help bubble (hand holding a green missile) sat immediately left of the Alliance shield, at norm (833,724). One tap on its centre answered "Allies are very grateful for your assistance!" and the tile disappeared. Chat showed Buckeye16: "Thank you Mami" and Mistress Sam: "Got you Papi".
- Help page (opened after the bubble for the closing read): Today's points gained from Alliance Help 420/1,000. Only the account's own two requests remain - Bears Lair, Missile Mastery II research (Time reduced: 15:00:22) and Lv.30 Aircraft Center (Time reduced: 3d 23:58:04) - both already helped to the maximum, and a player cannot help their own requests. No ally request waited on the page, so Help All was not pressed again; the bubble press had already cleared the waiting set.
- The number of ally requests the bubble cleared is unread (the toast carries no count), so no per-request count is claimed for this unit. The points header read 410/1,000 in the garbled OCR of the Help-page open and 420/1,000 on the screenshot; the 10-point difference is not attributed to this unit.
- Header movement across the day: 140/1,000 at the 1846 unit (about 18:46) to 420/1,000 here (about 21:22) - the header moves between units as helps accumulate; the in-session-unchanged pattern from the 1846 unit stands for within-unit reads.
- No diamonds or money spent. No other unit's work touched.
- Result stats: target 1, achieved 1, resources_gained waiting ally help requests cleared via base bubble; Help page verified only own two requests remain, costs about 3 minutes of unit time, no items spent, verified yes, points 0.
