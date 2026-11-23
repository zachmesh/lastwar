"""Fixture tests for the log_append.py gate. Made-up JSONL files in a temporary folder only.

Run: python3 -m unittest discover -s _tools_/log-append-tests
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "log_append.py"


def objects(path: Path) -> list:
    return [json.loads(line) for line in path.read_text().split("\n") if line.strip()]


class Gate(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="log-gate-"))
        self.addCleanup(lambda: __import__("shutil").rmtree(self.tmp, True))

    def run_gate(self, *files, extra=()):
        args = [sys.executable, "-B", str(TOOL), "gate"]
        for f in files:
            args += ["--file", str(f)]
        return subprocess.run(args + list(extra), capture_output=True, text=True)

    def write(self, name, lines):
        path = self.tmp / name
        path.write_text("\n".join(lines) + "\n")
        return path

    def test_the_stale_tail_of_issue_422_is_repaired_and_no_object_is_lost(self):
        head = [json.dumps({"n": i}) for i in range(3)]
        pairs = [json.dumps({"n": 10 + i}) + json.dumps({"n": 20 + i}) for i in range(4)]
        path = self.write("tail.jsonl", head + pairs + [""] + [json.dumps({"n": 99})])
        before = [json.loads(p) for line in path.read_text().split("\n") for p in
                  ([line] if line.count("}{") == 0 else line.replace("}{", "}\n{").split("\n")) if p.strip()]
        r = self.run_gate(path)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("repaired 4 line(s), dropped 1 blank line(s); 12 lines now, all valid JSON", r.stdout)
        after = objects(path)
        self.assertEqual(after, before)                                          # same objects, same order
        self.assertEqual(len(path.read_text().rstrip("\n").split("\n")), 12)     # one object per line, no blank
        again = self.run_gate(path)
        self.assertEqual(again.returncode, 0)
        self.assertIn("all valid JSON", again.stdout)
        self.assertNotIn("repaired", again.stdout)

    def test_a_clean_file_is_left_byte_identical(self):
        path = self.write("clean.jsonl", [json.dumps({"n": i}) for i in range(5)])
        before = path.read_bytes()
        r = self.run_gate(path)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(path.read_bytes(), before)

    def test_an_unrepairable_line_blocks_with_exit_1_and_changes_nothing(self):
        path = self.write("bad.jsonl", [json.dumps({"n": 1}), "this is not json", json.dumps({"n": 2}) + json.dumps({"n": 3})])
        before = path.read_bytes()
        r = self.run_gate(path)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("unrepairable, gate blocked", r.stdout)
        self.assertEqual(path.read_bytes(), before)                              # nothing is written when anything is unrepairable

    def test_an_unreadable_file_exits_2(self):
        r = self.run_gate(self.tmp / "missing.jsonl")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("cannot read", r.stderr)

    def test_several_files_and_json_output(self):
        a = self.tmp / "a.jsonl"
        a.write_text(json.dumps({"n": 1}) + json.dumps({"n": 2}) + "\n")
        b = self.write("b.jsonl", [json.dumps({"n": 3})])
        r = self.run_gate(a, b, extra=["--format", "json"])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        data = json.loads(r.stdout)
        self.assertTrue(data["gate_passed"])
        self.assertEqual([f["status"] for f in data["files"]], ["repaired", "clean"])
        self.assertEqual(objects(a), [{"n": 1}, {"n": 2}])

    def test_one_bad_file_among_several_fails_the_gate(self):
        good = self.write("good.jsonl", [json.dumps({"n": 1})])
        bad = self.write("bad.jsonl", ["not json"])
        r = self.run_gate(good, bad)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)

    def test_the_older_repair_refused_a_blank_line_and_the_gate_does_not(self):
        path = self.write("blank.jsonl", [json.dumps({"n": 1}), "", json.dumps({"n": 2})])
        r = subprocess.run([sys.executable, "-B", str(TOOL), "repair", "--file", str(path), "--write"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)                    # repair itself now drops blank lines
        self.assertEqual(objects(path), [{"n": 1}, {"n": 2}])


if __name__ == "__main__":
    unittest.main()
