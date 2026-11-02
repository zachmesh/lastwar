---
title: Alliance Duel
created: 2026-10-25T20:46:00Z
modified: 2026-11-02T03:47:03Z
version: 1.8.0
description: The weekly Alliance Duel event and its Alliance Star Ceremony - themed days, points, reward chests and the weekly ceremony claim
grounded_in:
  - source: task intaken at the owner direction on 2026-10-25, details to be confirmed in game the same day
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner correction on 2026-10-25 - the task names the Star Ceremony, taught step by step in session
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1324 star-ceremony unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1745 star-ceremony unit)
  - source: radar execution record 2026-11-01 1904 queue run (duel delta test still owed after 25 release-day claims)
  - source: queue-planning execution record 2026-11-01 1840 run (duel-score staging gap: live pool tree predates the PR 137 merge)
---


# Alliance duel

## What this activity is

The weekly Alliance Duel event, where this alliance faces one rival
alliance across themed days and members earn points from matching
activities. This folder accumulates duel knowledge - the day themes,
how points are earned, and which chests can be claimed passively.
Grinding points by spending resources or speedups is a decision for
the owner, not part of a claim check.
Executions are recorded in `_records_/<date>/alliance-duel/`, one file per execution.

The weekly claim of this cycle is the Alliance Star Ceremony. The
owner named this task "weekly alliance dual ceremony" and corrected
the first reading on 2026-10-25 - the claim is the ceremony, not
anything on the VS duel screens. Never close a duel check without
looking for the ceremony trophy icon on the base screen.

## How to enter

Measured on 2026-10-25.

- Duel screens — tap the gold VS medallion on the right side of the
  base screen, below the Events icon. ALLIANCE DUEL opens with two
  tabs - the duel week tab and Infinite Roulette.
- Star Ceremony — tap the trophy icon on the right side of the base
  screen, beside the Alliance icon. It opens an alliance ALLIANCE STAR
  CEREMONY (EVENT 38). The icon is present only while a ceremony is
  waiting; it disappears once the ceremony has been played and
  claimed.

## The Star Ceremony — how it runs

Measured on Event 38, 2026-10-25, under the owner procedure.

- The ceremony is a staged awards show. A progress track along the
  bottom walks 13 award steps and ends in an MVP finale. Each step
  honours one member for the week — S2 Big Shot, Little Sun, Ice
  Sculptor, 3v3 Brawl Star, Alliance Champion, Star of Desert Storm,
  Guardian Defender, Divine Healer, Devil Trainer, Doom Elite
  Slayer and more.
- Procedure set by the owner — keep tapping the forward button at
  bottom right and do not wait for the presenter. When actionable
  icons appear, act on them, then keep forwarding. The emote
  reaction bar is actionable — the emotes are the mechanic, and
  the owner asks for love (the heart emote) to at least 3 winners.
- Measured caution — forwarding too fast can skip an award detail
  card entirely (two cards were skipped in Event 38). When a winner
  card is up with the emote bar visible, send the emote first, then
  forward.
- The chest icon at top right shows emotes sent against the tier
  target (6 of 3 at the end of Event 38) and opens the Ceremony
  Rewards panel. Rewards unlock at 1, 2 and 3 emotes sent — gift
  boxes, rubies and badges per tier.
- The finale puts a golden chest on the podium. Tapping it pays
  every alliance member extra rewards scaled by the stars awarded
  (14 stars in Event 38), and a separate Participation Prize
  follows (ruby times 500 in Event 38). The Details overview shows
  the star winners themselves receive Diamonds in Grand, 1st and
  2nd Prize tiers.

## Cadence

- Weekly league cycle. At the first check (Sunday 2026-10-25) the
  duel tab read Starting Soon for Alliance Duel League S38 - the
  week had not opened.
- The Star Ceremony for the settled week is claimable on the
  weekend — Event 38 was played and claimed on Sunday 2026-10-25,
  while League S38 showed as calculating promotions and demotions.
- Infinite Roulette spins and points reset every Sunday at 24:00 as
  displayed; the countdown matched the 19:00 local daily reset.

## Scope and availability

- This alliance sits at Gold Tier 38 - 7 in League S38. The rewards
  strip showed member rewards for the alliances ranked No.4 to 16.
- Infinite Roulette needs spin tokens - balance 0 at the check,
  wheel progress 2 of 10. Spinning without tokens would mean buying
  them, which is out of scope without owner approval.
- The ceremony itself is free to play and claim — emotes and the
  finale chest cost nothing. Skipping it leaves the week rewards
  unclaimed, which is what the 1359 check did before the owner
  correction.

## Daily total read - the 3.6M target (2026-10-31 fix)

The owner target is **3,600,000 personal Alliance Duel points per
duel day**. The miss audit of 2026-10-31 found that no record on
either audited day ever read a personal daily total - this folder
held only Star Ceremony checks, and fragment scores (an Arms Race
phase score, a radar points figure) are not a duel total and never
substitute for one.

- The star-ceremony unit - the alliance-duel regular - reads the
  personal daily total live on the duel panel (the gold VS
  medallion) on its runs, and the read of the last run before the
  19:00 reset is the day closing figure.
- Superseded in part by the owner decision of 2026-11-01 on
  Issue #132 - the daily total read moves to a dedicated
  duel-score regular (Issue #136), because in practice the read
  was skipped whenever no ceremony was waiting (for example
  star-ceremony-2026-11-01-1030 closed with no total read). The
  star-ceremony unit keeps the ceremony claim only.

## Duel score tracking - the duel-score regular (2026-11-01)

Owner decision on Issue #132 - add duel-score tracking only;
building and research queues were left untouched by that
decision (deferred, not ruled non-goals).

- The duel-score regular runs every 4 hour cycle (segment 2,
  activity alliance-duel) and is staged by the queue planner
  like every other regular.
- Each unit is read-only - open the duel panel from the gold VS
  medallion, read the personal daily total, and close with the
  unit result stats target 3600000, achieved set to the total
  read live, and the gap target minus achieved. Fragment scores
  never substitute, and the Duel Progress mail is a cross-check
  only.
- The last unit executed before the 19:00 reset carries the
  day closing figure, recorded in the day alliance-duel record.
- A tracking unit never grinds, spends or buys to chase the
  target - scoring actions stay with the themed-day regulars
  under the duel day gates in _tools_/duel_schedule.json.
- If the total cannot be read, the unit closes that line as
  unverified and a re-read is enqueued before the reset (rule
  R1 of the task unit queue design), as already stated above.
- The closing figure is recorded in the day alliance-duel record
  and in the unit result stats as the total and its gap against
  3,600,000. The Duel Progress mail is a cross-check only, never
  the source.
- If the total cannot be read, the unit closes that line as
  unverified and a re-read is enqueued before the reset (rule R1
  of the task unit queue design). A duel day with no total read
  is reported in the round summary as **total unread** - never
  passed over in silence, and never estimated from fragments.
- This read is part of the alliance-duel type, alongside the
  ceremony. It does not merge the ceremony claim into a duel
  result or the other way round - one unit still reports one
  type, and the total read is that type own work.

## What is known from 2026-11-01

Measured in the 0108 star-ceremony unit (ticker-0104, window mode
642x951, no different-device dialog).

- No Star Ceremony waiting: the base screen showed no gold trophy
  icon beside the Alliance button on the right rail. No ceremony
  panel was opened, no hearts sent, no rewards claimed. The right
  rail read Halloween Check-In, Events, Faction Duel, VS, Season
  II, Alliance, Mail, Inventory.
- Duel panel read live in the inter-week calculating state:
  Infinite Roulette shows 0 spin tokens, wheel 0/10, spins and
  points reset Sunday at 24:00. Duel League S38 shows Gold Tier
  38-7, AP3x rank 3, Week 1 Win, Week 2 Win, Week 3 crossed out,
  Week 4 sleeping, and the banner "Calculating the number of
  Alliances promoted and demoted..." with 13d 18:53 left. Match
  Record Week 2 shows [AP3x]The Apex vs [Sync] IMPERIUM 7-6.
  Weekly Ranking shows [AP3x]Bears Lair rank 190 with 17,240,439
  points - a weekly cumulative figure, NOT a daily total, and
  never to be reported as one.
- Daily total line closed as unverified, per the 2026-10-31 fix:
  no themed duel-day panel with a personal daily total was found
  on the duel screens in this calculating state, the Achievements
  pill (8/16 Completed) did not open a panel, and the Your
  Alliance control on the Ranking panel produced no change on
  two taps, so that route was dropped under the pivot rule. No
  fragment score was substituted for the daily total. Later
  star-ceremony units already staged for today (0230, 0630,
  1030) are the re-reads before the 19:00 reset; no extra unit
  was enqueued.



## What the 2026-11-01 1324 unit added

- Unit star-ceremony-2026-11-01-1030 by ticker-1304,
  session about 13:21 to 13:22, status done as checked
  only.
- Base screen inspected in the wide view: right rail
  showed Alliance, Mail, Inventory and WORLD, with
  Events, Faction Duel, VS and Season icons at top
  right. No trophy icon beside the Alliance icon, so no
  Star Ceremony is waiting, matching the checked-only
  units of 2026-10-31.
- No ceremony was opened, no emotes sent, no rewards
  claimed, no other task type touched.
- Incidental live read confirming the mail unit's
  claims landed: food 308.2M (was 289.2M), iron 496.2M
  (was 477.2M), coins 22.7M (was 10.6M) on the base
  resource bar - deltas matching the 1306 mail popup
  exactly (see mail-rewards 1.3.0).

## What the 2026-11-01 1745 unit added

- Unit star-ceremony-2026-11-01-1430 by ticker-1738,
  session cc-72, window mode 642x951, no
  different-device dialog. The game was left on the Mail
  screen by the previous pass (mail unit partial); the back
  arrow returned it to the base screen.
- No Star Ceremony waiting: the base screen showed no gold
  trophy icon beside the Alliance button on the right rail.
  The right rail read Halloween Check-In, Events, Faction
  Duel, VS, Season II, Alliance, Mail, Inventory. No
  ceremony panel was opened, no hearts sent, no rewards
  claimed.
- Duel panel read live in the inter-week calculating state:
  Infinite Roulette shows 0 spin tokens, wheel 0/10, spins
  and points reset Sunday at 24:00. Duel League S38 shows
  Gold Tier 38-7, AP3x rank 3, Week 1 Win, Week 2 Win, Week
  3 crossed out, Week 4 sleeping, and the banner
  "Calculating the number of Alliances promoted and
  demoted..." with 13d 02:16 left, down from 13d 18:53 at
  the 0108 read, consistent with the time elapsed. Match
  Record Week 2 shows [AP3x]The Apex vs [Sync] IMPERIUM
  7-6. Weekly Ranking shows [AP3x]Bears Lair rank 190
  with 17,240,439 points, unchanged from the 0108 read -
  a weekly cumulative figure, NOT a daily total, and never
  to be reported as one.
- Daily total line closed as unverified, matching the 0108
  unit: no themed duel-day panel with a personal daily
  total was found on the duel screens in this calculating
  state, and no fragment score was substituted. Note on
  ownership: this unit was staged before the duel-score
  split merged (PR 137 merged in the 1745 integrator
  pass), so it still carried the daily-total line in its
  unit stats (daily_total_unverified, target 3600000,
  verified no). Ceremony-only units after the split do not
  carry it; the duel-score regular owns the total read.
  The 1757 zero sweep named a star-ceremony re-read for
  the total line (star-ceremony-2026-11-01-1830); under
  the split that read belongs to the duel-score regular,
  and the 1830 unit result will show which type carried
  it.


## What the 2026-11-01 1904 radar unit and 1840 planner run added for duel tracking

- Duel delta test still owed after the 1904 release unit:
  the VS panel was not opened in that unit, so no duel
  score before and after its 25 release-day radar claims
  was read. The 10,000 versus 30,000 versus another figure
  question stands, and the 25-claim batch is the batch the
  test should measure against on the next release day.
  The radar points figure (66 to 91) is not a duel total
  and never substitutes for one.
- Duel-score staging gap at the 1840 plan: the live pool
  tree still ran pre-merge tools/regulars.json (PR 137
  merged to main at 16:51 local, after that tree's sync),
  so the 1840 plan staged no duel-score unit and none was
  in the pool. The daily total against the 3,600,000
  target therefore had no staged read from that plan. The
  next planner or ticker pass after the live tree syncs
  to main stages duel-score units automatically under its
  every-run cadence; no unit was hand-enqueued by the
  planner, because the local activity metadata predated
  the regular and a hand-built unit would carry no
  task-specific instructions. This is a sync gap, not a
  profile gap - if the sync still has not landed by the
  next duel-score slot, it becomes a retro item.
- Confirmed again at the 1940 plan, the first planner pass
  after the reset: the live pool tools/regulars.json still
  carries no duel-score regular, so that plan also staged
  no duel-score unit. Two consecutive planner passes
  (1840, 1940) now show the gap; the next run checks
  whether the sync has landed, and the gap goes to the
  retro if a third plan still stages none.
- New duel day context from the 1904 record: duel day 1,
  Radar Training, radar posture release, day ends
  2026-11-02 19:00 local. The last duel-score unit
  executed before that reset carries the new day's closing
  figure.


## Open questions

- The day themes and scoring once League S38 opens, and the current
  opponent.
- How spin tokens are earned inside the duel week.
- How long the ceremony trophy icon waits if unplayed, and whether
  a skipped award card can be revisited (Event 38 suggests not).
- Who the MVP finale honours and how the winners list is ordered.
