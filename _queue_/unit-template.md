---
unit: <regular-id>-<yyyy-mm-dd>-<hhmm>
regular: <regular-id from _tools_/regulars.json>
activity: <activity type folder name>
segment: <1, 2 or 3>
priority: <1 expiry-critical, 2 windowed, 3 standard>
created_at: <ISO 8601 UTC>
expires_at: <ISO 8601 UTC or empty>
planned_for: <cadence window this unit serves, ISO 8601 UTC>
not_before: <claim not allowed before this time, or empty>
window: <phase or posture constraint or empty>
est_minutes: <producer estimate, never above 15>
serves: <exactly one of: upkeep, snapshot, baseline, fill idle slot, or a plan item id that has a row in the forecast ledger (PL-nn, comma separated if more than one); free text fails the validate check>
chain_id: <continuation chain id or empty>
chain_seq: <position inside the chain or empty>
attempts: 0
max_attempts: 3
claimed_by: <empty until claimed>
claimed_at: <empty until claimed>
lease_until: <empty until claimed>
---

# <Regular name>

What to do, in the regular's own terms; read `_activities_/<activity>/`.

THE FORECAST REFUSAL IS LIVE: every unit minted or synced, chain follow-ups
included, is refused unless EACH comma or semicolon part of serves is a plan item id with a row in the forecast
ledger or an exempt word (upkeep, snapshot, baseline): 'PL-17' passes, 'PL-17 the Oil Well chain' does not.
Write the ledger row before the unit; emergency path `--no-require-forecast`.

A FALLBACK unit says 'DISPATCH ONLY WHEN NAMED', carries priority 9 and a not_before beyond any tick pick: retire a moot unit.

A BUILD UNIT'S PREVIEW STEP (Steer A 13:34Z): DRAG THE COST LIST until EVERY row (iron, food, coin, oil) is visible; check ALL floors against ALL rows and the table's three columns (2541) before the press; a row not seen: DO NOT press, write what was seen and STOP. HELMET (Steer A 14:04Z): after the press, a 6x crop above the building: press a white round green-helmet bubble ONCE (no other); end time before, +1, +10.

A brief that taps buildings or menus points at the route card `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`, writes a precondition first, records the tag text beside every number taken from a building panel, and stops with one named reason (capacity, owner on another device, cost, prerequisite, route or window).

Close DONE or PARTIAL by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do with ONE `state_read: <what was read, quoted> | <frame: step or file> | <HH:MM:SSZ>` line; PARTIAL when the state could not be read or the route not completed. Complete with `--state-change yes|no`: yes when the result changed the game state.

A brief that reads the Backpack names its PLAN REASON (a conversion, an open date, the HQ 31 start, a stock check): no forensic read without one; a stock claim needs two reads within the hour.

A NEW UNIT names its expected value against its cost (0.2 to 0.3 USD): below about 100K of resource-equivalent, a power gain, a duel row or a stated information value, fold it into an existing unit or do not stage it.

Every unit carries Steer A's standing line (2026-11-23), word for word: 'May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.'

At the start of every unit: if `lsappinfo front` is not LastWar, record it, run the standing front script ONCE, record again; still not LastWar: stop, release and tell the Coordinator. Standing rule (Steer A 14:16Z): run it only if the Mac's input idle is at least 300 s and the window is not a macOS consent or security window (never answered by us); touch nothing in the other app; back in front within 10 minutes: STOP and report; a person at the Mac: wait.

On completion the executor runs `_tools_/queue.py complete` (the result section, then `done`; the shape is in the [task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md)).
