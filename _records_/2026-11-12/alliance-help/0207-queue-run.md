---
title: Alliance help queue run 0207
created: 2026-11-12T10:07:00Z
modified: 2026-11-12T10:07:00Z
version: 1.0.0
description: Ticker-0204 help unit - device input blocked, control channel locked with outcome_unknown, no game input possible, unit failed
status: unverified
---

# Alliance help - ticker-0204, 02:06 to 02:07 PST

Unit help-2026-11-11-2230, executor ticker-0204. Status
failed: the Mac computer-control channel refused every game
input with outcome_unknown, so no help work was done and
nothing was claimed. Computer sessions cc-698 and cc-699.
No device dialog, no login demand, no Touch ID, no
password typed.

## What happened

- Token acquired about 02:06; unit claimed about 02:06
  (expires_at 2026-11-12T10:30:00Z, 02:30 PT).
- Input attempt 1 (cc-698): open_app LastWar -
  outcome_unknown, "An earlier action has an unresolved
  outcome. Stop sending input; read-only inspection is
  allowed. Report the uncertainty. A new local user
  submission is required before input can resume. The
  reconcile action cannot clear this state." Nothing was
  dispatched.
- Read-only inspection worked: computer.observe returned
  the live Last War window 676414 on the base screen
  (HEROES and WORLD buttons visible, no dialog, no
  "active on a different device" dialog). The OCR text
  was too garbled to claim any numeric HUD figure from
  this observation, so none is claimed here.
- Input attempt 2 (cc-699, fresh session after ending
  cc-698): activate Last War window 676414 - the same
  outcome_unknown.
- Input attempt 3 (cc-699): open_app LastWar - the same
  outcome_unknown.
- Three recovery attempts, the standard count, all failed
  with the identical error text. No further input was
  sent after the third attempt.

## Classification

- This is the same lock the ticker-0134 pass hit twice
  earlier this night and filed as Issue #689 (scout unit
  scout-scout-2026-11-10-006, sessions cc-693 and cc-694;
  radar unit radar-2026-11-11-2203, sessions cc-695, cc-696
  and cc-697; same window 676414, same error text). This
  pass is the third occurrence of the same lock.
- It is NOT the "lacks owner-authorized device access"
  error - the owner authorization stands and is not in
  question - and it is NOT a different-device dialog, NOT
  a login demand, and NOT the Issue #648 zoom state (the
  window was windowed 642x951 throughout, per the
  observe). New sessions do not clear it; only a local
  user submission on the Mac can, and the owner is asleep,
  so no local submission is available to a detached
  overnight pass.
- Per Issue #689 a pass meeting this state stops: no
  further unit was attempted this pass, and the
  zombie-invasion unit 024 stays in inbox for the next
  tick, which will hit the same wall unless the channel
  clears.
- A comment on Issue #689 records this third occurrence
  (sessions cc-698 and cc-699, help unit).

## Result stats

- target: 1 (Help All pressed, waiting ally helps checked)
- achieved: 0 helps - no game input was possible
- resources_gained: none
- points: 0
- costs: about 1 minute, no items spent
- verified: yes (the input block is observed on screen,
  not inferred; no closing figure is claimed)
- blocker_category: f (missing precondition - device input
  unavailable; control channel locked, Issue #689)
- follow_up: the next tick retries; if the channel is
  still locked, the next pass records its own access
  failure per Issue #689. The zombie-invasion unit 024
  stays queued.

Record-hygiene note: the file was first written as
  0215-queue-run.md with 02:14/8-minute claims, then renamed
  to 0207-queue-run.md and corrected to the true 02:06-02:07
  window and 1-minute cost before commit, with the unit
  evidence path and costs stat corrected to match.
