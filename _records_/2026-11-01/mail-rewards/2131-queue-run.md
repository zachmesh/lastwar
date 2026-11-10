---
title: Queue Run 2131 Mail Rewards Partial
created: 2026-11-01T21:31:00-08:00
modified: 2026-11-01T21:31:00-08:00
version: 1.0.0
description: Ticker unit mail-2026-11-01-1830 execution record, partial, Alliance panel back arrow stalled on background input, mail screen never reached
status: partial
---

# Mail rewards 2026-11-01 21:31

- Unit: mail-2026-11-01-1830, executor ticker-2104, fourth
  unit of the same pass (after training partial, gifts done,
  help done).
- The unit reached the Alliance panel (after closing the Help
  dialog from the previous unit with its X) but never reached
  the mail screen: the panel's bottom-left back arrow took
  three no-change taps in a row - norm 55,964, then 97,964
  twice, the last after a fresh activate - and the panel
  stayed open each time, confirmed by screenshots.
- Under queue rule R2 (foreground precondition, retro of
  2026-10-31) two no-change taps end the background-input
  method inside the unit, so tapping stopped instead of
  repeating: the game window stays covered by Chrome and
  background input stopped reaching this control. A
  click_foreground attempt was refused for missing
  element_number, and no Escape key was used (it has crashed
  this app before). No foreground route was available inside
  this unit.
- Outcome: partial. No mail category was opened, nothing was
  claimed, and Delete All was never touched. The tracker is
  left untouched, so the next tick re-produces the regular and
  the work resumes as a fresh unit.
- Note for the next mail unit: try the panel exit first with a
  fresh observation, and if the back arrow stalls again, treat
  it as the known foreground precondition rather than a dead
  entry route - earlier units the same day recovered from it.
