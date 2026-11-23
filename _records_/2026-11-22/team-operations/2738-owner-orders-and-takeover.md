---
title: Owner takeover of the game session and three new orders - 2026-11-23 12:32 to 12:44Z
created: 2026-11-23T04:46:00-08:00
modified: 2026-11-23T04:50:00-08:00
level: L3
version: 0.1.0
description: Steer B confirmed the TIPS dialog on the owner's order, the base came back live, the operator resumes at 12:49:13Z under conditions, and the owner's three play orders (Base Expansion for strategy and research, trade truck plunder) were recorded as decisions 17 to 21
status: done
activity: team-operations
run_id: team-operations-2026-11-23-1238-owner-takeover
trigger: owner order at 12:32Z relayed by Steer B; owner orders at 12:36Z relayed by Steer A at 12:37Z; Steer B's note at 12:44Z
started_at: 2026-11-23T04:38:00-08:00
finished_at: 2026-11-23T04:50:00-08:00
verified: Steer B's timeline and frames (UTC, his date -u) read through his message; device-token.md shows claimed_by steer-b, lease_until 12:49:13Z; the run-lock reads free; the HID log shows no Mac input between 12:35Z and the read at 12:42Z
---

# Owner takeover and new orders

## Takeover (Steer B)

- 12:34:13Z Steer B took the device token (lease to 12:49:13Z). 12:34:47Z one Confirm on the TIPS dialog 'Your account is currently active on a different device!' (run 20261123T123447Z-e72a5d, one tap). 12:35:20Z relaunch of the app by bundle id; 12:36:25Z read-only run: base view, no dialog.
- This was the second Confirm in 23 minutes (the first, the operator's, at about 12:11:50Z); the owner's explicit order overrides the 30-minute guard for this press. If the dialog returns, nobody presses Confirm again without the owner.
- Frames 12:12Z and 12:36Z: coin 9.8M to 55.9K, energy 195 to 79, Total Power 150,215,709 to 150,413,046: spent on another device while the operator was stood down. Whether that was the owner is the OPEN decision OD-20261123-21.

## Collision of two Steer notes

My 12:42Z Confirm one-shot was deleted (no second Confirm). Steer B and I agreed on a resume at 12:49:13Z with two conditions: a returning dialog stops the operator at once, and nothing spends coin, energy or diamonds beyond the standing rules while coin is near zero.

## Orders recorded (owner decisions)

OD-20261123-17 take ownership of the session; -18 strategy prioritizes Base Expansion (retires the 'HQ 31 and Age of Oil off the plan' line); -19 research prioritizes Base Expansion (speed-up rule amended by Steer A); -20 trade truck plunder re-enabled with a casualty guard; -21 OPEN: was the second device the owner.

## Routing

Planner: the Age of Oil survey unit, the withdrawn Special Forces fill, plunder units. Strategist: re-rank and the first node. Scribe: the truck-plunder profile. Toolsmith: the cu team's question (answered: the bridge runs the whole MCP server from the pinned checkout).
