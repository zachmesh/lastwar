---
title: Perception scout queue run 2259
created: 2026-11-23T07:03:00Z
modified: 2026-11-23T07:03:00Z
version: 1.0.0
description: Scout unit scout-2026-11-22-1800, operator seat, read-only red-dot accounting of the base, Hero List, Alliance hub and Mail, 16 of 19 dots explained
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T065938Z-fd2683, 2026-11-23T06:59Z to 07:01Z
  - source: run screenshot step-0004.png read by the operator, the other readings are the run's own report, final frame saved as _tools_/state/cu_scout_2300.png
  - source: lsappinfo front reading before the start, 2026-11-23T06:59:38Z, and observation.py append and check on the day file
  - source: _tools_/ rule digest at /tmp/lw-ps-digest.md, read instead of the profile
---

# Perception scout queue run 2259

- Unit scout-2026-11-22-1800, operator seat, assignment A-20261123-0659-operator, attempt
  1. The pass is in [observation.md](observation.md), appended with `observation.py`
  (check clean). Rows are in the sidecar [2259-queue-run-detail.md](2259-queue-run-detail.md).
- Status: done, read-only. Nothing claimed, no message opened, no map pin, no Quick Dispatch.
- Run `20261123T065938Z-fd2683`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 8 steps. Actions done 10, refused 0. Model time 7.23 s per
  step. Cost 0.113182 USD. No takeover.
- Front precondition held. The first frame was the base, with no account dialog and no
  boarding banner.
- Route: Heroes, back, Alliance, back, Mail, back. One back tap on Mail missed, because
  its arrow sits near (113,935), and one extra tap fixed it, harmless.
- Red dots: seen 19, explained 16, unexplained 3. The unexplained are the Events badge 1,
  the wrench badge 1 and a hero card thumbs-up marker.
- Surfaces: Hero List has three card dots. The Alliance hub has five dots, on Help,
  Gifts, Store, Techs and Events. Mail has three tab dots. None was opened.
- Digest rules, measured: rules 1, 3 and 9 held, with chat 99+ as unread chat. Rule 6
  held in spirit, but this bridge uses pixel points, and after a fresh launch the first
  taps can be inert, so wait and retry once. Rule 10 did not apply, because this bridge
  launches with `osascript` and uses a consent flow.
- Closing state: the base screen.
- Red lines held: no purchase, no diamonds, no diplomacy, trophy bubble not tapped.
- Follow-up: the Events 1 and the wrench 1 are still unowned. The Alliance hub dots and
  the Mail dots point at the gifts, help, techs and mail regulars.
