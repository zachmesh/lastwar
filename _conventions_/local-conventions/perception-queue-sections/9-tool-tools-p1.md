---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 1
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 26
description: Implemented 2026-11-01 as _tools_/scout_diff.py (standard library only), to the design this section fixed in Phase 1.
---
## 9. Tool - _tools_/scout_diff.py (Phase 2, implemented)

Implemented 2026-11-01 as `_tools_/scout_diff.py` (standard library
only), to the design this section fixed in Phase 1. The tool is
the diff of section 5 as a program, so the step from observation
to queue stops depending on an executor remembering to do it.

**CLI usage**

```text
_tools_/scout_diff.py --observation FILE [--date YYYY-MM-DD]
                    [--out DIR] [--root POOL] [--repo DIR]
                    [--regulars FILE] [--ledger FILE]
                    [--now ISO] [--apply] [--format text|json]
```

