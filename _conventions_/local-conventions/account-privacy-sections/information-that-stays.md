---
title: Information that stays out of repository content
created: 2026-11-23T09:06:18Z
modified: 2026-11-23T09:06:18Z
version: 0.1.0
sequence: 3
description: The owner's own in-game name and any alias of it.
---
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

