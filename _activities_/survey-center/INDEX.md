---
title: Survey Center
created: 2026-11-09T19:17:00Z
modified: 2026-11-09T19:32:17Z
level: L1
version: 1.0.0
description: In-game Survey Center - read-only survey exploration and reward claim after the owner completes a survey; one live Season 11 Polar World Experience Survey, reward unmeasured (owner-gated)
status: unverified
grounded_in:
  - source: ticker-1104 scout discovery unit 012 execution record 2026-11-09 1117 queue run (done, Survey Center explored read-only - one live Season 11 Polar World Experience Survey, Instructions read in full, Proceed opens a SurveyMonkey link in the owner's Chrome, tab left open, nothing answered; record commit 46d7110f on records/2026-11-09)
  - source: ticker-1104 scout discovery unit 013 execution record 2026-11-09 1120 queue run (done, duplicate of unit 012 - the survey-center-tab candidate is the same Events hub tab; record commit 46d7110f on records/2026-11-09)
---


# Survey Center

## What this activity is

Feedback surveys in the Events hub Survey Center tab (the tab also
appears in Special Ops when surveys exist). A survey card lists the
survey; Proceed opens an external link, the owner completes the survey
there, and the reward is claimed back in the Survey Center - or mailed
if it is not claimed before the survey disappears. This is not a
scoring event: it pays a completion reward, not points. Executions are
recorded in `_records_/<date>/survey-center/`, one file per execution.
The candidate is tracked in GitHub Issue #506.

## How it is done

- Enter from the Events hub, Survey Center tab (red-dot badge 1 while
  a survey is open); the tab sits at the right end of the tab bar.
- Read the survey card: title, Proceed button, countdown if the survey
  is timed. Read the Instructions (i button) for the survey's rules.
- Proceed opens an external SurveyMonkey link in the owner's Chrome.
  Completing the survey is the owner's own opinion - no agent answers
  or submits anything.
- Return to the Survey Center to claim the reward. Exiting midway is
  fine - return and click "Continue" to resume. Each survey can only
  be submitted once; a revisit shows as completed.
- Timed surveys disappear when the countdown ends. Surveys without a
  countdown disappear 3 hours after completion. A completed survey
  whose reward is not claimed before it disappears has its reward sent
  via mail.

## What is known from 2026-11-09 1117

- One live survey card, read live about 11:11 PT: "Season 11: Polar
  World / Experience Survey", blue Proceed button, red dot, no
  countdown on the card. No other survey is open.
- Instructions, read in full: 1. When surveys are available the
  Survey Center appears in Special Ops. 2. Click to proceed and fill
  out the survey through the provided link, then return to the Survey
  Center to claim rewards. 3. Exiting midway is fine - return and
  click "Continue" to resume. 4. Each survey can only be submitted
  once; a revisit shows as completed. 5. Timed surveys disappear when
  the countdown ends. 6. Surveys without a countdown disappear 3 hours
  after completion. 7. A completed survey whose reward is not claimed
  before it disappears has its reward sent via mail.
- Proceed opens an external SurveyMonkey link in the owner's Chrome,
  tab "Season II: Polar World Experience Survey":
  surveymonkey.com/r/LW260921S2, with openid, sid 2110, vip 13, lang
  en parameters. Intro: "Dear Commanders, Season II: Polar World has
  ended. How was your experience?" Q1 (required): rate the Season
  gameplay 1-5 plus "I had limited participation, I can't give a
  proper assessment". Q2: likelihood to recommend Last War:Survival,
  0-10. Nothing answered, nothing submitted - answering is the owner's
  own opinion. The Chrome tab was left open for the owner.
- Rewards: UNMEASURED - no reward is named on the card, in the
  Instructions, or on the survey first page; it is revealed only by
  completing the survey. This is the one profile field left open.
- Cost: free. No diamonds, no money, no priced button anywhere on
  this path.
- Cycle and deadline: this card carries no countdown, so rule 6
  applies - it disappears 3 hours after completion; timed surveys
  disappear at their countdown end.
- Scoring: none - a feedback survey, not a scoring event; it pays a
  completion reward, not points.
- Base screen on return: coin 46.2M, power 149,217,331 - unchanged.
- Method note (input route): two background clicks on Proceed at its
  freshly grounded centre (782, 752) in the windowed 642x951 layout
  and one click_element on the Proceed OCR element all reported no
  change - yet the first tap HAD worked: it opened the Chrome survey
  tab. A click whose effect lands in another window is invisible to
  the LastWar observation, so "no change observed" on the game window
  does not prove a tap missed; check the window list before re-tapping
  a link button.

## Open questions

- Reward contents and the claim step: only measurable after the owner
  completes the Season 11 survey (his own opinions) and claims the
  reward in the Survey Center; the next survey-center unit measures
  the reward and the claim step. Follow-up is on Issue #506.
- Whether the claim button appears in the Survey Center after
  completion, and what the reward pays in practice.

## What the 2026-11-09 1117 scout-discovery unit added - Survey Center learned read-only, 6 of 7 fields, reward unmeasured

- Unit scout-scout-discovery-2026-11-09-012 by ticker-1104, about
  11:09 to 11:17 local, status done. Evidence in
  `_records_/2026-11-09/survey-center/1117-queue-run.md` (commit
  46d7110f on records/2026-11-09). Read-only exploration: opened the
  Survey Center, read the Instructions in full, opened the survey link
  only to read its first page, left the Chrome tab open for the owner,
  and returned the game to the base screen. No answers given, nothing
  submitted, nothing claimed, nothing spent.
- Events hub tab bar, scrolled end to end: The Age of Oil, Arms Race,
  Winter Battlefield, Desert Battlefield, Wanted Boss (red dot),
  Survey Center (red dot badge 1), Community. No Zombie Invasion tab
  - event still ended, no chain seeded.
- The provisional profile was NOT written into `_activities_/` by the
  unit (tier 2, left for the knowledge PR flow); this profile is that
  write, by the knowledge organizer.
- Unit 013 in the same pass (record
  `_records_/2026-11-09/survey-center-tab/1120-queue-run.md`) is a
  duplicate of this unit: the scout diff filed the Survey Center
  twice, once as the unmatched label "Survey Center" (unit 012) and
  once as the events-surface tab "Survey Center tab" (unit 013). They
  are the same entity - the Events hub tab at the right end of the tab
  bar, badge 1, whose page unit 012 opened and read in full. No
  separate "tab" profile exists; no game session was opened for unit
  013.
- Result stats: target learn-survey-center-profile-fields, achieved 6
  of 7 (rewards unmeasured, owner-gated), resources_gained none, costs
  about 8 minutes of unit time, no items spent, verified yes,
  blocker_category none, points 0, surfaces_walked
  events-hub-survey-center-instructions-survey-link, items_observed 1
  survey card, red_dots_seen 1, red_dots_explained 1,
  unexplained_red_dots 0, unknown_items 0.
