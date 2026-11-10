---
title: Perception Scout Queue Run
created: 2026-11-05T09:52:00-08:00
modified: 2026-11-05T09:52:00-08:00
version: 1.0.0
description: Scout-midday unit scout-midday-scout-mid-2026-10-31-005 executed by ticker-0941, failed on Mac device invoke channel stall, forty-first consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 09:44 to 09:52 local
---

# Perception scout 2026-11-05, ticker-0941

Unit scout-midday-scout-mid-2026-10-31-005, failed. No game
screen was ever read and no game input was dispatched: every
device invoke timed out with zero responses, so the alliance
remainder this unit owns (station panel, loot box) is unwalked
and no observation was produced. This is a stale-chain unit
(chain scout-mid-2026-10-31, seq 5, staged 2026-11-03); per the
stale-scout precedent its observation would have been filed
under 2026-11-05 as a read of the current game state, but no
read exists to file.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd reported
  online by device.list, but last_seen 2026-11-05T15:36:52Z
  (07:36 local), stale about 2 hours 5 minutes at pass time;
  the recovery device shows the same stale timestamp.
- Attempt 1: computer.session start - node_invoke_timeout
  after 120000ms, zero response.
- Attempt 2: connection.health - node_invoke_timeout after
  25000ms, zero response.
- Attempt 3: computer.session start - node_invoke_timeout
  after 120000ms, zero response.
- Three attempts, zero responses. This meets the standing
  at-least-3-attempts retry rule, and it is the worsened form
  the ticker-0904 pass first recorded: the invoke channel
  itself is stalled, not just the LastWar window stream.
- The in-tree probe _tools_/mac_capture_probe.py 1.0.0
  answers this evidence UNKNOWN (low confidence, exit 1):
  it has no invoke-timeout field and asks for the checklist
  (list_windows, View-menu inspect, one observe attempt),
  each step of which would burn another 120s timeout. The
  CHANNEL_STALL diagnosis that classifies exactly this
  evidence (invoke_timeouts with invoke_responses 0, high
  confidence, stop_pass yes) lives in PR #321, still open
  and unmerged, so this pass classifies by that design and
  stops here rather than re-running the checklist.
- No blind taps were dispatched: without a session or an
  observation, any tap could land on the wrong control, so
  the unit stops here under the check-first rule. No
  different-device dialog was observed (no screen was ever
  captured) and no device takeover was needed.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the forty-first consecutive ticker
  pass with a Mac device-access blocker (fortieth was
  ticker-0904, which first recorded this zero-response
  form; thirty-seventh was ticker-0734 on the capture
  failure form).
- No surface walked, no items observed, no red dots seen
  or explained, no unknown items filed. The station panel
  and loot box remainder stays unwalked and stays with
  the chain; no successor unit is enqueued from this
  unit - the chain's remainder is unchanged by a pass
  that read nothing, and a successor would hit the same
  stalled channel.
- Tracker untouched. No zombie check was possible (Events
  hub unwalked); no zombie chain is seeded, per the
  standing rule that the event ended 2026-10-30 and no
  live return sighting exists in this pass.
- Recovery still needs the owner-side step, now at the
  gateway level: the Mac-side agent gateway likely needs
  a restart before re-probing (per the PR #321 design);
  the Dock-icon step addresses the window-stream fault,
  not a stalled invoke channel.
- Issue 284 commented with this pass's failure; no new
  issue filed (same blocker, same issue).
