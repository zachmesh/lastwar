---
title: Mail rewards queue run 0138
created: 2026-11-09T09:38:00Z
modified: 2026-11-09T09:38:00Z
version: 1.0.0
description: Mail check partial - Alliance and Event Claim All both returned no rewards available, System Regular Battle Report not walked
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 01:20-01:38 PT
---

# Mail rewards queue run 0138 (ticker-0113)

Unit: mail-2026-11-08-2230. Status: partial.
Activity: mail-rewards.

## Live reads

- Mail home: red dots on Alliance, Event and In-app Purchases.
  Note under the list - mails older than 30 days are deleted
  automatically.
- Alliance list: Leadership Transfer Notice (red, 2h ago) -
  "Jerry Apex has become the new Alliance..." (full text not
  opened); Daily Donation Rankings (7h ago); Weekly Donation
  Ranking (7h ago); 3v3 Brawl Major's Gift x3 (7h ago).
  Claim All pressed - toast "No rewards available.", nothing
  claimed.
- Event list: "[AP3x] DCna8ive's train has arrived" (train
  arrival); "[AP3x] Missile Apex's Mega Ex..." (3h ago);
  "[AP3x] DCna8ive's train has departed" (3h ago); "Weekly
  Pass Unclaimed Rewards" (6h ago); "Unclaimed VIP Daily Level
  Rewards" (7h ago). Claim All pressed - toast "No rewards
  available.", nothing claimed. The two "Unclaimed" mails read
  as notifications, not claimable attachments - their rewards
  are claimed on the VIP and pass screens, not from mail.
- Base screen: food 513.8M, iron 838.3M, coin 25.2M, power
  149,209,253, diamonds 6,027.

## What was done

- Alliance and Event categories walked; Claim All pressed in
  both; both returned no claimable attachments.
- Alliance page opened once as a navigation check (right rail
  tap at the grounded point works - it opened the Alliance
  page: [AP3x] The Apex, 96/100 members, leader row Jerry Apex,
  the same name as the transfer notice). The Mail button itself
  did not respond to five background taps at two grounded
  points ((707, 792) twice, (650, 791) single and double,
  manual mouse press) and only opened on a later tap at
  (652, 793) after the Alliance page had been visited - the
  entry point is flaky and the next mail unit should re-ground
  it fresh rather than reuse a stale point.
- Noted for the VIP regular: the "Unclaimed VIP Daily Level
  Rewards" mail (7h ago) suggests the VIP daily freebie may
  still be unclaimed - the vip unit in the inbox should check
  the VIP screen, not the mail.

## What was not done

- System, Regular and Battle Report categories were not walked
  in this unit (unit cap reached at the Event Claim All). Per
  queue rule R7 they are the first action of the next mail
  unit. In-app Purchases was not opened (receipts only, nothing
  to claim, per the activity metadata).
- The Leadership Transfer Notice was not opened in full - the
  leadership change (Jerry Apex named as the new Alliance
  leader, previously Texan Apex per the repo) is recorded here
  from its preview line and flagged in the pass report; the
  next alliance-facing unit should confirm the leader row live.

## Red lines

- No diamonds or money spent. Delete All never pressed. No
  mail deleted. No login or verification was demanded, and no
  different-device dialog appeared.

## Stats

- target: 5
- achieved: 2
- resources_gained: none
- costs: about 15 minutes of unit time, no items spent
- verified: yes
- blocker_category: c
