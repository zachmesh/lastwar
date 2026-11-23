---
title: Queue Planning Shop Findings And The Two Donation Hypotheses Applied 2820 2026-11-23
created: 2026-11-23T07:08:00-08:00
modified: 2026-11-23T07:08:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying the Coach's two-hypothesis pre-registration to the donation passes and the passes run findings to the shop units, with the dated facts the scribe needs for the shop-claims digest
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0708-shop-and-hypotheses
trigger: coordinator message 15:01Z and the Coach's refill check 0701
started_at: 2026-11-23T07:00:00-08:00
finished_at: 2026-11-23T07:08:00-08:00
verified: the three donation units and the four passes units read back after editing; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/coach/0701-refill-check.md and refill-test-prereg.csv
  - source: _records_/2026-11-22/shop-claims/1457-queue-run.md (as relayed by the coordinator)
---

# Shop findings and the two donation hypotheses, 2820

## 1. Donations

The Coach pre-registered two hypotheses at 15:02Z: H35 (one refill per 2,100 s) and H20 (1,200 s, the old rate, which fits 85 of 89 recorded timers but not today's entry count of 8). Their predictions at entry differ by 4 (5 against 9 at 17:45Z), so one pass separates them. `donations-pass-2026-11-23-001` carries both sets of predictions, the first timer's expected end (17:52:57 for H35, 17:57:57 for H20) and a rule that NO hand tap may precede the pass; `-002` and `donations-2026-11-23-1630` ask for both predictions to be written beside the actual count with the hypothesis it fits (H35, H20 or neither). The optional tail stays in `-001`.

## 2. The shop (passes run 1457, 2026-11-23 about 14:57Z)

For the scribe, as dated facts: the shop's tab row reads Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond and a cut-off G tab, with no Hot Sale Packs tab (the digest's name is stale or the tab moved). Both weekly cards (S2 Drone Components, S1 Drone Parts) read owned with 'Already claimed today', Renew $4.99 and 6d 11:07:32 remaining (to 2026-11-30 02:00Z), which contradicts digest rule 3 (read as offers on 2026-11-22); who bought them is unknown (the other device). Free Supply read Claimed, not by us. The Weekly Deal tab shows three priced packs only. The digest rules 3 and 1 and its tab names need a dated note.

## 3. Units

Staged: `passes-shop-tabs-read-2026-11-23-001` (read only, 15:05Z to 17:00Z, serves snapshot: drag the tab bar, read the G tab and any Hot Sale Packs or Hot Deals tab, never a price, Renew or Extension) and `passes-daily-pickup-2026-11-24-001` (02:05Z to 06:00Z, claim the two Daily Pickups if a green Claim shows, free items only). The two passes units still to run (`-0657`, `-1630`) carry the update, and the Researcher's T3 test unit no longer names the Hot Deals tab: it opens the tab that shows the check-in page, with at most three tab taps and a stop 'blocked by route'.
