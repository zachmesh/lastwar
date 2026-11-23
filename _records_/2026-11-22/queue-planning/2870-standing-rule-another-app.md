---
title: Queue Planning The Standing Rule On Opening Another App 2870 2026-11-23
created: 2026-11-23T07:38:00-08:00
modified: 2026-11-23T07:38:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying Steer A's standing rule after the T3 incident - one line in the unit template and in every live brief that can reach a banner, Go, Buy, link, web or share button, and the full rule in the route card
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0738-another-app-rule
trigger: coordinator message 15:28Z
started_at: 2026-11-23T07:27:00-08:00
finished_at: 2026-11-23T07:38:00-08:00
verified: the inbox searched for units already carrying the line and for those that can reach the named buttons; word counts under 450; validate exit 0
grounded_in:
  - source: coordinator message 15:28Z (Steer A's standing rule)
---

# The standing rule on opening another app, 2870

## The rule

Any test or action whose possible effect includes opening another app, a browser, a store or a payment surface needs Steer A's approval in advance, with the exit plan stated: what is pressed if it happens, and what is never pressed. A test whose failure mode leaves the game is never run on a guess. Never click Go on the check-in banner: it opens the web store. An unexpected foreground switch stops the run at once; the operator presses nothing, answers nothing, touches nothing in the other app and tells the Coordinator within minutes. Consent requests are human-only. Only the operator seat and the bridge touch the desktop; every other seat uses `lsappinfo front`, read-only, at most. I make no desktop call of any kind.

## What changed

The unit template tells a producer that a brief which can reach a banner, a Go, a Buy, a link, a web, a share or an external-app button carries one line: may open another app, needs Steer A's approval first, if it opens STOP. The route card (now 1.5.0, 341 body words) holds the full rule and a seventh stop reason, 'blocked by another app'. Forty-six live units carry the compact line: every passes, shop-read, events, mail, vip, daily-missions, treasures, radar, secrets, survivors, gifts, help, train, star-ceremony, duel-score, zero-sweep and midday scout unit, the Oil Depot units and the five store reads W1 and H1. None was claimed. The Researcher's T3 unit had already ended as skipped-needs-owner at 15:17:06Z. The store buy units, not yet staged, will reach Buy buttons: each must carry the line and a stated exit plan before it is minted.
