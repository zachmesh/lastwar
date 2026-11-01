---
title: Daily Collection Ledger
created: 2026-11-01T05:00:00Z
modified: 2026-11-01T05:00:00Z
level: L2
version: 1.0.0
description: The master list of everything collectible or due in one reset day, each line with the live read that closes it
status: active
grounded_in:
  - source: miss audit of 2026-10-31, section 4 umbrella rule
  - source: owner expanded collection checklist of 2026-10-31
  - source: owner direction of 2026-10-31 to reflect and fix
---

# Daily collection ledger

The master collection list for one reset day - the day runs from
the 19:00 local reset to the next 19:00 local reset. It exists
because of the finding at the head of the 2026-10-31 miss audit -
the routine ran task types, but no list anywhere said what a
complete day of collection looks like, so whole lines were
invisible in every per-unit count.

## The closing standard

- Every line closes on a live read from that day - a counter, a
  balance, a panel state seen on screen in the unit that closes
  it. Silence is not a close. A line that cannot be read closes
  as unverified and is named in the round summary, under rule R1
  of the [task unit queue design](task-unit-queue-design.md).
- A line with no producing unit is flagged unscheduled in the
  round summary, never silently absent (audit rule 4).
- The pre-reset zero sweep (queue design section 12) walks this
  ledger item by item twice before each reset, at about 17:30
  and about 18:30 local. A line not at zero gets a priority 1
  unit of its own type enqueued before the sweep closes, named
  in the sweep record.

## The lines

### Base and harvest

1. **Food bubbles** - producing unit, harvest. Closes when the
   final full-base sweep of the unit shows no food bubble
   standing, the farmland tap taken or farmland read empty.
2. **Iron bubbles** - harvest. Same standard, the iron line read
   collected or absent on its own, never merged into a general
   bubbles note.
3. **Coin bubbles** - harvest. Same standard, with the coin total
   read live after collection.
4. **EXP bubbles** - harvest. Read as their own line - collected
   or none standing. Hero EXP arriving inside a reward popup is
   a different source and does not close this line.
5. **Titanium bubbles** - harvest. The titanium cluster bubbles
   over the Titanium Alloy Factory, read collected or absent.
   Resource totals are reported under the name the HUD shows -
   the 2026-10-30 and 2026-10-31 records contradict each other
   on one second-row total, and that contradiction is why this
   line names its source building.
6. **Armed Truck** - harvest. Claimed when the fully loaded
   notice shows; when not full, closes on a live timer read. A
   fully loaded notice seen by any unit is claimed by that unit
   or handed to a harvest unit the same pass - in the audited
   days it was claimed 0 times in two days while other units saw
   the notice and left it.

### Shop, passes and VIP

7. **Drone components** - passes and shop checks. Read live each
   day as claimed, absent or offer-only. The S2 Drone Components
   Weekly Pass at a purchase price is an offer, not a pickup, and
   is recorded as offer-only. Drone components are never merged
   with drone data from radar popups - they are different items.
8. **Upgrade ore** - radar, shop and event units. Every reward
   popup is transcribed item by item, ore named with its amount
   as displayed.
9. **Screws** - same units, same transcription. A day whose
   records hold no screw line is reported in the round summary
   as no screw claim recorded - in the audited days the word
   screw appears in no record at all.
10. **Shop Daily Pickup and Free Supply** - passes. Each pickup
    read claimed or absent on the shop screen that day.
11. **Pass daily pickups** - passes. The weekly and monthly pass
    daily gifts, each read claimed or absent.
12. **VIP Daily Freebie** - vip. Attempted on its own, with the
    VIP points read live before and after.
13. **VIP login chest** - vip. Attempted independently of the
    Freebie - one unresponsive button never skips the other item
    (the 2026-10-31 failure, where both closed unclaimed because
    the chest was gated behind the Freebie attempt). A failed
    claim re-enters this ledger for the pre-reset sweep instead
    of waiting a full day.

### Missions, mail and alliance

14. **Daily activity chests** - daily-missions. The Mission
    panel is opened, the activity points total and every chest
    state are read live, completed tasks are claimed one by one
    with a re-check after each, and every reached chest is
    claimed. This line was unscheduled on both audited days -
    the type had metadata but no regular - and is a regular
    since the 2026-10-31 fix.
15. **Mail, six categories** - mail. Claim All per category; a
    category closes on its claimed list or on the live
    no-rewards answer. Mail that evidences an unworked source -
    the Glittering Market Unclaimed mail above all - is flagged
    to that source line, never counted as the source worked.
16. **Alliance gifts** - gifts. Claim All on the Regular and
    Premium tabs, closing counts read live.
17. **Alliance donations, 30 of 30** - donations. The daily
    target is the full 30 coin donations. Closes only on a live
    Donation Count read in the closing unit - the count is a
    remaining count, so done reads 0 remaining. The full rule,
    including the timer-hidden fallback, is in the
    alliance-donations metadata. Checkpoints under rule R3 of
    the queue design at six and two hours before the reset.

### Trucks, train, radar, duel

18. **Trucks - dispatch 5 of 5, plunder 4 of 4** - trucks. Both
    counts read live on the trade counter screen in the closing
    unit - never presumed, never by battle result. Returned
    trucks are settled first, then dispatch is filled, then
    plunder, under the quality rules in the truck-plunder
    metadata. Checkpoints under rule R3.
19. **Alliance train, per service** - train. The day services -
    1 ordinary train and 2 Mega Express trains, owner-stated -
    are each logged by name as boarded (carriage 2, the
    3-contract ticket), no train in preparation (station panel
    read - a banner-only check does not close this line), or
    missed. Arrival mail is claimed under the mail line and is
    not a boarding record.
20. **Radar, by duel posture** - radar. On stack days the line
    closes on tasks completed with rewards deliberately
    unclaimed and map pins untapped, recorded as stack, not as
    a miss. On release days it closes on Claim All done and the
    special map pins attempted individually - pins were the
    starved subtask of the audited release day (rule R7).
21. **Alliance Duel daily total against 3.6M** - the
    star-ceremony unit, the alliance-duel regular, reads the
    personal daily total live on its runs and the pre-reset run
    read is the day closing figure, recorded with its gap
    against the owner target of 3,600,000 in the alliance-duel
    record. The full rule is in the alliance-duel metadata. A
    day with no total read is reported as total unread.
22. **Crystal** - crystal-shop. Until the mechanism is located
    (see the crystal-shop metadata), this line closes on a daily
    named status - located or not located, with its age in days
    from 2026-10-25 - and is named in every round summary under
    rule R5. Once located, it closes on the live claim read of
    the day.
23. **Glittering Market** - glittering-market. Once located,
    closes on a live read of the market itself showing the day
    claimable and exchangeable items processed. The mail titled
    Glittering Market Unclaimed never closes this line - it is
    residue of a market not worked, and a day whose only
    glittering record is that mail is reported as market not
    worked. Until located, this line closes like the crystal
    line - a daily named status under rule R5, age counted from
    2026-10-31.
