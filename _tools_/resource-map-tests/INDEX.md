---
title: Resource Map Tests
created: 2026-11-23T07:57:32Z
modified: 2026-11-23T07:57:32Z
version: 1.0.0
description: Tests for resource_map.py amounts with K, M, G and B suffixes and the power breakdown keys
---

# Resource map tests

Tests for `_tools_/resource_map.py`. `snap` crashed with a ValueError on a G suffix (1.1G), because `parse_amount`
knew only K and M.

They cover: 1.1G, 1.0G, 638.0M, commas, a bare number, B for billion, any case; exact Decimal arithmetic (float lands
one short on 32.3K and about 300 other one-decimal values); a message and exit 2 for text that is no amount; `snap` on a temporary copy storing the integer;
the six `power_*` keys defined in `resources.json`, so `snap` stops flagging them unknown and `show` prints their
labels; history rows only appended, and every recorded row still an integer map.

Run: `python3 -m unittest discover -s _tools_/resource-map-tests`.
