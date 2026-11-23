---
title: 3. The fixes, and where each one landed part 2
created: 2026-11-23T08:36:59Z
modified: 2026-11-23T08:36:59Z
version: 0.1.0
sequence: 5
description: H - by-design partials counted as failure noise, 11 units R8 - chain continuation and stack
---
| H - by-design partials counted as failure noise, 11 units | R8 - chain continuation and stack posture get their own label in reporting, split from misses, so the daily miss count only counts units that failed their own objective | task-unit-queue-design.md section 11 |
| I - owner-named task with no escalation, crystal, 6 days, 0 units | R5 - an owner-named task incomplete after 24 hours rises to priority 1 and is named in every round summary until it closes. Crystal itself is now modelled and queued - see section 4 | task-unit-queue-design.md section 11; _activities_/crystal-shop/INDEX.md; queue unit crystal-shop-2026-11-01-0503 |
| Checklist item 4 - daily missions never scheduled | daily-missions added to _tools_/regulars.json as a daily-reset regular on the VIP pattern, so the planner and the ticker sync produce its units. Validated by a scratch-root planner run before commit - see section 5 | _tools_/regulars.json |
| Unmodelled item, same class - the Glittering Market, named 2026-10-31 | Known only by its residue - a Glittering Market Unclaimed mail claimed through Event Claim All on 2026-10-27, 2026-10-29 and 2026-10-30 - while the market itself was never opened, located or worked on any day. Modelled as its own activity type, entered on the ledger with a closing standard that mail residue can never satisfy, and queued at priority 1 to be located - the daily-missions and crystal pattern applied from its first day instead of its sixth | _activities_/glittering-market/INDEX.md; daily-collection-ledger.md line 23; queue unit glittering-market-2026-11-01-0501 |
| Checklist item 5 - duel daily total never read | The alliance-duel metadata now requires a live personal daily total read per duel day against the owner target of 3.6M, the gap recorded, an unread total reported as unread, and a re-read enqueued - a fragment score never substitutes | _activities_/alliance-duel/INDEX.md |
| Checklist umbrella - whole lines invisible | The master daily collection ledger lists every daily line with its closing read, and two pre-reset zero sweep units walk it item by item before each 19:00 reset. The pair for 2026-11-01 is enqueued - see section 4 | daily-collection-ledger.md; task-unit-queue-design.md section 12; queue chain pre-reset-sweep-2026-11-01 |
| Owner-named gap - alliance donations not completed | The donations metadata now states the daily target as the full 30 of 30, the closing count as a same-unit live read of the remaining count, the timer-hidden fallback, and early-day scheduling under the R3 checkpoints | _activities_/alliance-donations/INDEX.md |

