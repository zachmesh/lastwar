---
title: Survey Center queue run 1117
created: 2026-11-09T19:17:00Z
modified: 2026-11-09T19:17:00Z
version: 1.0.0
description: Ticker-1104 scout discovery unit 012, Survey Center read-only exploration - mechanism learned, reward unmeasured pending the owner's survey completion
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 11:09-11:17 PT
---

# Survey Center queue run 1117 (ticker-1104)

Unit: scout-scout-discovery-2026-11-09-012. Status: done.
Activity: survey-center (candidate exploration, read-only learning).
Chain: scout-discovery-2026-11-09, seq 12.

## Live reads

- Events hub tab bar, scrolled end to end: The Age of Oil, Arms
  Race, Winter Battlefield, Desert Battlefield, Wanted Boss (red
  dot), Survey Center (red dot badge 1), Community. No Zombie
  Invasion tab - event still ended, no chain seeded.
- Survey Center page, read live about 11:11 PT: title "Survey
  Center", subtitle "We'd love to hear from you!". One survey
  card, red dot: "Season 11: Polar World / Experience Survey",
  with a blue Proceed button. No countdown timer on the card.
- Instructions (i button, read in full): 1. When surveys are
  available the Survey Center appears in Special Ops. 2. Click to
  proceed and fill out the survey through the provided link, then
  return to the Survey Center to claim rewards. 3. Exiting midway
  is fine - return and click "Continue" to resume. 4. Each survey
  can only be submitted once; a revisit shows as completed.
  5. Timed surveys disappear when the countdown ends. 6. Surveys
  without a countdown disappear 3 hours after completion.
  7. A completed survey whose reward is not claimed before it
  disappears has its reward sent via mail.
- Proceed opens an external SurveyMonkey link in the owner's
  Chrome (Zhen profile), tab "Season II: Polar World Experience
  Survey": surveymonkey.com/r/LW260921S2, with openid, sid 2110,
  vip 13, lang en parameters. Intro: "Dear Commanders, Season II:
  Polar World has ended. How was your experience?" Q1 (required):
  rate the Season gameplay 1-5 plus "I had limited participation,
  I can't give a proper assessment". Q2: likelihood to recommend
  Last War:Survival, 0-10. Nothing answered, nothing submitted -
  answering is the owner's own opinion.
- Base screen on return: coin 46.2M, power 149,217,331 - unchanged.

## What was learned (profile fields)

- Entry: Events hub, Survey Center tab (badge 1 while a survey
  is open); also appears in Special Ops when surveys exist.
- Mechanism: in-game card lists the survey; Proceed opens an
  external SurveyMonkey link in Chrome; complete it, return to
  the Survey Center to claim the reward, or the reward is mailed
  if unclaimed before expiry.
- Rewards: UNMEASURED - no reward is named on the card, the
  Instructions, or the survey first page; it is revealed only by
  completing the survey. This is the one profile field left open.
- Cost: free. No diamonds, no money, no priced button anywhere
  on this path.
- Cycle and deadline: this card carries no countdown, so rule 6
  applies - it disappears 3 hours after completion; timed
  surveys disappear at their countdown end.
- Scoring: none - a feedback survey, not a scoring event; it
  pays a completion reward, not points.

## What was done

- Opened the Survey Center, read the Instructions in full,
  opened the survey link only to read its first page, left the
  Chrome tab open for the owner, and returned the game to the
  base screen. No answers given, nothing submitted, nothing
  claimed, nothing spent.

## Not done in this unit

- The reward contents and the claim step: only the owner can
  complete the survey (his own opinions), so the reward stays
  unmeasured until he does. Follow-up: owner completes the
  Season 11 survey in the Chrome tab left open, then claims the
  reward in the Survey Center; the next survey-center unit
  measures the reward and the claim step.
- The provisional profile was NOT written into _activities_/
  (tier 2, left for the knowledge PR flow). The candidate is
  tracked in Issue #506, commented with this unit's findings.

## Method note (input route)

- Two background clicks on Proceed at its freshly grounded
  centre (782, 752) and one click_element on the Proceed OCR
  element all reported no change - yet the first tap HAD worked:
  it opened the Chrome survey tab. A click whose effect lands
  in another window is invisible to the LastWar observation, so
  "no change observed" on the game window does not prove a tap
  missed; check the window list before re-tapping a link button.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  survey question answered or submitted. No other unit's work
  touched.

## Stats

- target: learn-survey-center-profile-fields
- achieved: 6 of 7 fields (rewards unmeasured, owner-gated)
- resources_gained: none
- costs: about 8 minutes of unit time, no items spent
- verified: yes
- blocker_category: none
- points: 0
- surfaces_walked: events-hub, survey-center-page, instructions-popup, survey-link-first-page
- items_observed: 1 survey card (Season 11 Polar World Experience Survey)
- red_dots_seen: 1
- red_dots_explained: 1
- unexplained_red_dots: 0
- unknown_items: 0
