---
title: Operator run recipe and hazards 0054
created: 2026-11-23T16:12:00Z
modified: 2026-11-24T13:08:00Z
version: 1.8.0
description: Operator sidecar page - the run recipe and hazards moved verbatim from handover 0.9.0, plus the run-shape and never-press lines from the route tables
status: handover
grounded_in:
  - source: handover 0.9.0 section Run recipe and hazards, moved 2026-11-23T15:12Z into the sidecar detail page and split out 2026-11-23T16:12Z
  - source: sidecar rows Run shape (records alliance-donations 1441, resource-collection 1445) and Never (shop-claims 1528-t3-focus-incident.md)
---

# Run recipe and hazards

Part of [the sidecar](0054-operator-handover-detail.md); the current short form is in `_seats_/operator/handover.md`.

- Run recipe (current form in the handover): claim BY NAME (stale read receipt: `queue.py read --record PATH --executor operator`), `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front` names LastWar, `cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5`; turn 1 a NO-CLICK frame, last turn a report.
- Safe point for menus: the bare spot (310,660) after WORLD then BASE (never (400,640) after a camera shift, never (200,610), a Gold Mine); no bubble taps (a Farmland tap collected food).
- Backpack Resources opens with the 5,000 Diamonds tile SELECTED and a live Use: never press Use.
- A `local_input` pause: stop, retry once, record the time to the millisecond. Desktop gate: `cu_bridge.py lock` (free, held or waiter); on a refusal wait and log a waits row (note OTHER for the cu-integrator). Owner-idle wait: restored 20:04Z (OD-23), 0 from the restart after 21:25Z (OD-27), 300 s again from 2026-11-24T08:36:10Z when the bridge moved to the computer-use worktree (CU-720's carry): owner-idle waits are 0 s on every run since; the cost is the cu gate runs holding the lock about 2.4 min.
- Hazards seen: cu gate runs hold the lock 2.4 min (a nightly near 11:28Z; PR gate runs after cu merges, unpredictable); a macOS alert (UserNotificationCenter) at 02:34:19Z and 09:05:46Z, no tap before the second: only the standing killall on the coordinator's word; "Google Chrome for Testing" from the owner's ai-sync job 10:00:05Z to 10:01:01Z, left by itself (hold, no killall); the cu "CU Fixture" 11:09:32Z to 11:09:48Z, a cu dry run. The start hint no longer prints "Approve the app (first use only)" (PR 955); com.lastwar.ios has an approval.
- TIPS "active on a different device": STOP, press nothing, release the token, report; never Confirm.

## Run shape and never

An 8-step cap gives 7 effective actions; three harvest panels need two runs. The Go button on the check-in banner opens the web store in Chrome ([1528-t3-focus-incident.md](../shop-claims/1528-t3-focus-incident.md)); a consent request is human-only.

## Finished upgrades and drags (02:28Z)

A finished upgrade shows a wrapped gift box; one tap on its body is the Complete (Oil Well +4,200 power, 0218; +4,900, 0808). One drag per turn: two in one turn lost two runs.

## Clipped page pan (13:08Z)

On a clipped page start from the blank right margin, in ONE message: mouse_move to the start, left_mouse_down, wait 1 s, ONE move of 175 px, wait 1 s, left_mouse_up, then the screenshot after the up; a malformed or missing wait refuses the whole batch and nothing runs. Then tap the claim once only if it is a plain Claim. A single drag event moved nothing at 70 and 135 px and flung at 250 px. Evidence: [shop-claims 1301](../shop-claims/1301-queue-run.md) (150 px moved, S1 Claim y 915 to 765, Drone Parts x15); [1158](../shop-claims/1158-queue-run.md), [1211](../shop-claims/1211-queue-run.md), [1150](../shop-claims/1150-queue-run.md), [1248](../shop-claims/1248-queue-run.md). A drag that starts on a card moves nothing; Page Down did nothing.
