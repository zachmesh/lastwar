---
title: Account Privacy
created: 2026-11-01T07:14:00Z
modified: 2026-11-23T08:00:00Z
level: L2
version: 2.0.0
description: Executors keep the owner's own in-game name and personal identifiers out of the public repository; other in-game names are allowed
status: active
grounded_in:
  - source: owner instruction 2026-11-01 to remove account identifiers holistically and prevent executors from recording them
  - source: owner decision 2026-11-22 22:2x PT (OD-20261123-04) narrowing the scope to the owner's own in-game name and personal identifiers
---

# Account privacy

This repository is public. Executors verify the correct account privately in
the game and refer to it in repository content as **the owner account**. Do
not publish an identifier merely to prove which account was checked.

## Narrowed scope (owner decision 2026-11-22, version 2.0.0)

The owner's own in-game name is the one name that must never appear. Other
in-game names are allowed as game facts, kept to what the record needs:
alliance names and tags (including the owner's alliance), rival alliances,
allies and other players. Version 1.0.0 listed alliance names and tags too;
that part is withdrawn.

## Information that stays out of repository content

- The owner's own in-game name and any alias of it.
- Numeric player UID, game user ID, account number, login identifier and
  platform account IDs linked to the owner account.
- Game Center nicknames, platform account labels, Apple or other account
  email addresses, real names and personal contact data.
- Account-linked profile URLs, invite or referral codes, login or recovery
  details, and equivalent identifiers in links, query strings and metadata;
  the server or warzone number and base coordinates when attributed to the
  owner account.
- Screenshots or attachments exposing any of the above, including text
  outside the main game panel and image metadata.

Do not substitute a hash or encoding for a removed identifier or infer one
from another field. NPC, quest, queue-unit and other non-account system IDs
are outside this scope. GitHub usernames and repository links remain permitted.

## Exception to C1 (records immutable), recorded 2026-11-23

By explicit owner decision the owner's own in-game name was redacted from the
current tree, including play records and logs. Every file is kept; only the
name was replaced by the phrase `owner account`; the originals remain in git
history, which is **not rewritten**; the repository stays public. This
exception covers that name only and is not a precedent for editing records.

## Executor writing rules

1. Before committing, inspect every changed file and attachment, including
   frontmatter, structured results, logs, transcribed screen text, filenames
   and link targets.
2. Use `owner account` when the account must be referenced. Never copy a
   prohibited value into a record, queue result, commit message or PR text.
3. Record gameplay actions, amounts, points, timings and outcomes. Anonymize
   attribution rather than removing unrelated game facts.
4. Inspect screenshots before adding them; omit any that cannot be masked.
5. A later observation that reveals a prohibited value does not authorize
   publication; keep the record nonidentifying.

## Enforcement

A local denylist inside `.git` (never committed) holds the owner-name pattern;
the commit gate blocks any added line or file name that matches it. Scans
report counts and paths only, never a matched value. The rule that no value
appears in any message applies to the owner's name.
