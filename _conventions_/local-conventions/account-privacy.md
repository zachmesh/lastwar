---
title: Account Privacy
created: 2026-11-01T07:14:00Z
modified: 2026-11-01T07:14:00Z
level: L2
version: 1.0.0
description: Executors preserve useful gameplay evidence without publishing personal game-account identifiers or identifying combinations
status: active
grounded_in:
  - source: owner instruction 2026-11-01 to remove account identifiers holistically and prevent executors from recording them
---

# Account privacy

This repository is public. Executors verify the correct account privately
in the game and refer to it in repository content as **the owner account**.
Do not publish an identifier merely to prove which account was checked.

## Information that stays out of repository content

- Numeric player UID, game user ID, account number, login identifier, and
  platform account IDs linked to the owner account.
- In-game character/user names and aliases, Game Center nicknames, Apple
  or other account email addresses, real names and personal contact data.
- Account-linked profile URLs, invite or referral codes, login/recovery
  details, or equivalent identifiers in links, query strings and metadata.
- Alliance names/tags, server or warzone membership, base coordinates,
  rankings or other profile details when attributed to the owner account
  or combined so that the account can be recognized. Retain general game
  mechanics without preserving that account association.
- Screenshots or attachments exposing any of the above, including text
  outside the main game panel, image metadata and identifying filenames.

Numeric player IDs are included in this prohibition. Do not substitute
them for removed names, publish a hash or encoding of an identifier, or
infer a missing identifier from another field. NPC, quest, queue-unit and
other non-account system IDs are outside this personal-account scope.

GitHub usernames and repository links remain permitted under the owner's
explicit scope. This does not extend to personal game-account identifiers
embedded in a URL or in linked account-profile data.

## Executor writing rules

1. Before committing, inspect every changed file and attachment for
   identifiers, aliases and identifying combinations, not only a numeric
   UID. Check frontmatter, structured results, logs, transcribed screen
   text, filenames and link targets as well as prose.
2. Use the neutral phrase `owner account` or an existing redaction marker
   when the account must be referenced. Never copy a prohibited value
   into an execution record, queue result, commit message or PR text.
3. Record gameplay actions, amounts, points, timings and outcomes when
   they are needed as evidence and do not identify the account. Anonymize
   attribution rather than removing unrelated game facts or ordinary
   numeric measurements indiscriminately.
4. Inspect screenshots and exports before adding them. If identifying
   regions cannot be safely masked, omit the attachment and write the
   nonidentifying observation instead. Do not put an unmasked copy in the
   repository as supporting evidence.
5. A later observation that reveals an identifier does not authorize
   publication. Keep the public record nonidentifying; do not reconstruct
   previously removed values from older records or Git history.

This convention changes what executors may publish. It does not require
logging a UID, introduce a new account-ID field, change game actions or
authorize account/settings changes.
