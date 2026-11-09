---
title: Mail rewards queue run 2313
created: 2026-11-02T23:13:00Z
modified: 2026-11-02T23:19:00Z
version: 1.0.0
description: Queue unit mail-2026-11-02-2230 executed by ticker-2304
status: done
grounded_in:
  - source: game screen reads live in this unit on the owner Mac mini
---

# Mail rewards - queue run 2313

Executor: ticker-2304. Unit: mail-2026-11-02-2230. Status: done.
Session window: about 23:13 to 23:19 local, inside the 15 minute
unit cap.

## What was done

- Mail category list at entry carried red dots on Battle Report,
  Alliance, Event, Regular and In-app Purchases. Season and System
  carried none.
- Claim All pressed in every category except In-app Purchases
  (receipts only, nothing to claim, per the activity metadata):
  - Alliance: "No rewards available." List held Voting Results
    (unread, 2h ago, "Do you read the Announcements?"), Daily
    Donation Rankings, Zombie Siege Reports and a Defense Success
    Reward, all 5h or older.
  - Event: "No rewards available." List held train departure
    notices, a Competition Item Expired notice, a Daily
    Participation Reward and a Race Ranking Reward row.
  - Regular: "No rewards available." List held Victory reports
    (Lv.60 Doom Elite, Lv.160 Doom Walker, Lv.55 Doom Elite).
  - Battle Report: "No rewards available." List held attack
    Victory reports (Lv.20 Zombie Raider, Lv.19 to Lv.16 Zombie
    Horde).
  - Season: "No rewards available." List held Ice Breaking
    Reports only.
  - System: Claim All pressed twice, no toast captured either
    time and the list unchanged (President Mails, Season
    Conclusion). Per queue rule R2 the method ended there; the
    honest read is no claimable attachment observed in System,
    not a captured "No rewards" toast.
- Delete All was never pressed in any category.
- The Alliance Voting Results mail was left unread: it is a results
  announcement, not a claimable reward, and opening it was not
  needed to close this unit. Its unread state is why the Alliance
  category dot may persist.
- In-app Purchases was not opened: receipts only, nothing to claim.

## Mid-unit incident

- Leaving the Alliance panel for the base, a tap grounded by visual
  grounding at (162,935) quit LastWar outright (app-exited
  evidence). The tap was not repeated. The game was relaunched
  with open_app plus activate, recovered with state intact at the
  base screen (power 149,940,141), and the mail unit continued from
  the base Mail button. Background input worked while Chrome
  stayed frontmost for the rest of the unit.
- On returning to the base at the end of the unit, a notification
  permission dialog appeared ("Enable notifications and never miss
  important messages again."). Cancel was tapped; Enable Now was
  not touched and no system setting was changed.

## Totals

- Rewards claimed in this unit: 0. Every claimable category
  answered no rewards available (System: no toast, list unchanged).
- Mails deleted: 0.

## Red lines

- No diamonds or money spent, no Delete All pressed, no system
  setting changed.
