---
title: VIP rewards queue run 2234 detail
created: 2026-11-23T06:40:00Z
modified: 2026-11-23T06:40:00Z
version: 1.0.0
description: Sidecar with the timeline rows of the blocked VIP attempt in run 2234
status: run-failure
grounded_in:
  - source: run 20261123T063411Z-49accf events.jsonl and screenshots, read by the operator, 2026-11-23T06:34Z to 06:38Z
---

# Detail for VIP run 2234

Companion to [2234-queue-run.md](2234-queue-run.md). All times 2026-11-23, UTC.

## Timeline

- 06:34:11 claim passed after the read receipt, run started, front app named the game.
- 06:34:13 first frame, a TIPS dialog about an account active on a different device,
  with a red Confirm button and an X at about (569,371).
- 06:34:19.9 first model turn: click (569,371), wait, click (110,100).
- 06:34:20.0 click (569,371) delivered to the game, decision allow.
- 06:34:22.3 click (110,100) blocked, rule excluded:terminal, front app Terminal.
- 06:34:22.4 second frame, fully black.
- 06:34:25.6 second model turn, a wait. Consent requested: class new_app, rule
  app:not_approved, app Google Chrome. Status awaiting_consent for the rest of the run.
- about 06:37:42 the run ended without a result; the run was gone from the server.
- 06:37:54 front app Google Chrome.
- 06:38:26 unit released to the inbox (attempts 1), token released, front app still
  Google Chrome.

## Counters

- Steps 2. Clicks delivered 1, blocked 1. Actions refused by the operator 0.
