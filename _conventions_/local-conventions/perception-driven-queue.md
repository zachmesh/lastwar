---
title: Perception-Driven Queue
created: 2026-11-01T05:10:00Z
modified: 2026-11-23T09:03:33Z
level: L2
version: 1.5.0
description: The scout layer - daily work is determined by what the game screen actually offers, perceived first and scheduled by observation triggers rather than fixed slots, with the regulars kept as a capability profile library and new tasks discovered, profiled and scheduled automatically
status: phase-2-landed
grounded_in:
  - source: owner direction of 2026-10-31 - daily tasks shall be determined by what is observed on screen, perceive the game first, see what is available to do, and place it into the queue dynamically
  - source: owner refinement of 2026-10-31 - no fixed schedule; check and perceive where tasks are needed and schedule them automatically; discover potentially new tasks, learn about them, create their task profile and metadata, and start scheduling executions for them
  - source: miss audit of 2026-10-31 - whole classes of work had no execution channel because no static model named them
  - source: reflection of 2026-10-31 in this folder
  - source: "organizer 0432 run 2026-11-07 (Refs #147, #247) - the two standing 19:00 reset anchors rewritten to the absolute reset instant 02:00 UTC"
---

# Perception-Driven Queue

The scout layer - daily work is determined by what the game screen actually offers, perceived first and scheduled by observation triggers rather than fixed... This register stays at this path as an entry page; its text was split verbatim into 40 articles in [perception-queue-sections](perception-queue-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `perception-queue-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](perception-queue-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Changelog

- 1.4.0, 2026-11-23 - Split verbatim by split_doc.py into 29 articles plus 1 catalog page; --check EQUAL, sha256 74f10c1c2c7b; the unsplit 1.3.0 file is commit 6d019ade.
- 1.5.0, 2026-11-23 - Re-split verbatim into articles of 300 words or fewer (split_doc.py with a 300-word limit); --check EQUAL, sha256 74f10c1c2c7b; the 1.4.0 split is in git history.

## Articles

- [Catalog 01](perception-queue-sections/catalog-01.md) - Perception-driven queue - the scout layer to 7-perception-points
- [Catalog 02](perception-queue-sections/catalog-02.md) - 7-perception-points to 12-standing-rules
