"""Tests for home_glob_check.py: what it flags (a wildcard directly under the home folder, a listing of the home folder or of a protected folder in it,
in Python, shell and Node), what it lets through (named roots, docstrings, comments, an allow marker) and the guard over our own tree: no Python, shell or
Node file under _tools_ globs, lists or walks from the home folder.

Run: python3 -m unittest discover -s _tools_/home-glob-check
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "home_glob_check.py"
ROOT = HERE.parent.parent

sys.path.insert(0, str(HERE))
import home_glob_check as hg  # noqa: E402


def findings(text: str, kind: str = "python"):
    return [why for _n, why in hg.scan_text("x", text, kind)]


class PythonFlagged(unittest.TestCase):
    def flagged(self, source: str):
        self.assertTrue(findings(source), source)

    def test_the_shape_that_caused_it_a_wildcard_first_below_the_home_folder(self):
        self.flagged('import glob\nfrom pathlib import Path\nKNOWN = (str(Path.home() / "*" / "*" / "TEAM.yaml"),)\n')
        self.flagged('import glob, os\nglob.glob(os.path.expanduser("~/*/*/TEAM.yaml"))\n')
        self.flagged('import glob\nglob.glob("$HOME/*/x")\n')
        self.flagged('from pathlib import Path\nlist(Path.home().glob("*/TEAM.yaml"))\n')
        self.flagged('from pathlib import Path\nlist(Path.home().rglob("TEAM.yaml"))\n')

    def test_a_listing_or_walk_of_the_home_folder_or_a_protected_folder_in_it(self):
        self.flagged('import os\nos.listdir(os.path.expanduser("~"))\n')
        self.flagged('import os\nos.listdir(os.environ["HOME"])\n')
        self.flagged('import os\nos.listdir(os.environ.get("HOME"))\n')
        self.flagged('import os\nfor _ in os.walk(os.path.expanduser("~/Documents")): pass\n')
        self.flagged('from pathlib import Path\nlist(Path.home().iterdir())\n')
        self.flagged('from pathlib import Path\nlist((Path.home() / "Desktop").iterdir())\n')
        self.flagged('import os\nos.scandir(os.path.join(os.path.expanduser("~"), "Music"))\n')
        self.flagged('from pathlib import Path\nPath("~").expanduser().glob("*")\n')
        self.flagged('import os\nos.listdir("/Users/someone")\n')

    def test_a_name_set_from_the_home_folder_is_followed(self):
        self.flagged('from pathlib import Path\nhome = Path.home()\nlist(home.glob("*"))\n')
        self.flagged('import os\nbase = os.path.expanduser("~")\nos.listdir(base)\n')
        self.flagged('import os\nh = os.path.expanduser("~")\nimport glob\nglob.glob(h + "/*/x")\n')

    def test_an_f_string_pattern_with_a_wildcard_first(self):
        self.flagged('import glob, os\nglob.glob(f"{os.path.expanduser(\'~\')}/*")\nx = "~/*"\n')


class PythonPasses(unittest.TestCase):
    def clean(self, source: str):
        self.assertEqual(findings(source), [], source)

    def test_named_roots_under_the_home_folder(self):
        self.clean('import glob, os\nglob.glob(os.path.expanduser("~/.dsh/sessions/*/x/session.jsonl"))\n')
        self.clean('from pathlib import Path\nlist((Path.home() / ".computer-use" / "runs").iterdir())\n')
        self.clean('from pathlib import Path\nPath.home().joinpath(".dsh", "sessions").glob("*")\n')
        self.clean('import os\nos.listdir(os.path.expanduser("~/dtadpole/reflection/_tools_"))\n')
        self.clean('from pathlib import Path\nhome = Path.home()\nlist((home / ".dsh" / "sessions").glob("*/x"))\n')

    def test_a_message_built_from_the_home_folder_is_not_a_path_pattern(self):
        self.clean('from pathlib import Path\nhome = Path.home()\ndef shown(path):\n    return "~/" + Path(path).relative_to(home).as_posix()\n')
        self.clean('import os\nname = "x"\nprint(os.path.expanduser("~") + "/" + name)\n')

    def test_a_parameter_named_home_shadows_a_module_level_home(self):
        self.clean('from pathlib import Path\nhome = Path.home()\ndef scan(home):\n    return list(home.iterdir())\n')

    def test_a_parameter_whose_default_is_the_home_folder_is_the_home_folder(self):
        self.assertTrue(findings('from pathlib import Path\ndef scan(home=Path.home()):\n    return list(home.iterdir())\n'))
        self.assertTrue(findings('from pathlib import Path\ndef scan(home=None):\n    home = home or Path.home()\n    return list(home.iterdir())\n'))

    def test_a_function_local_home_is_followed_inside_that_function_only(self):
        self.assertTrue(findings('from pathlib import Path\ndef scan():\n    home = Path.home()\n    return list(home.glob("*"))\n'))
        self.clean('from pathlib import Path\ndef a():\n    home = Path.home()\n    return home / ".x"\ndef b(path):\n    home = path\n    return list(home.glob("*"))\n')

    def test_library_itself_and_its_protected_children_count_but_launchagents_does_not(self):
        self.assertTrue(findings('import os\nos.listdir(os.path.expanduser("~/Library"))\n'))
        self.assertTrue(findings('from pathlib import Path\nlist((Path.home() / "Library" / "Mail").iterdir())\n'))
        self.assertTrue(findings('from pathlib import Path\nlist((Path.home() / "Library" / "*").iterdir())\n'))
        self.clean('from pathlib import Path\nlist((Path.home() / "Library" / "LaunchAgents").glob("*.plist"))\n')

    def test_a_local_function_called_home_is_not_the_home_folder(self):
        self.clean('def home():\n    return "/var/inbox"\nimport glob\nglob.glob(str(home()) + "/*/x")\nlist((home() / "*").iterdir())\n')

    def test_pathlib_qualified_home_still_counts(self):
        self.assertTrue(findings('import pathlib\nlist(pathlib.Path.home().iterdir())\n'))

    def test_other_roots_and_plain_reads(self):
        self.clean('import glob, os\nglob.glob("/tmp/*.cj")\nos.listdir("/tmp")\nos.walk("/var/x")\n')
        self.clean('import os\nos.listdir(folder)\nos.listdir(os.path.join(root, "_queue_"))\n')
        self.clean('from pathlib import Path\nPath(__file__).parent.glob("*.py")\nopen(Path.home() / ".reflection" / "x.json")\n')
        self.clean('import os\nopen(os.path.expanduser("~/.heddle/keys/k"))\n')

    def test_docstrings_and_comments_are_text_not_paths(self):
        self.clean('"""globs ~/*/*/TEAM.yaml to find rosters"""\n# glob.glob("~/*")\nx = 1\n')
        self.clean('def f():\n    """Walks Path.home() / "*" in the old design."""\n    return 1\n')

    def test_an_allow_marker_on_the_line_or_the_line_above(self):
        self.assertEqual(findings('import os\nos.listdir(os.path.expanduser("~"))  # home-glob: ok the owner asked for this listing\n'), [])
        self.assertEqual(findings('import os\n# home-glob: ok one-off\nos.listdir(os.path.expanduser("~"))\n'), [])
        self.assertTrue(findings('import os\n# home-glob: ok\n\nos.listdir(os.path.expanduser("~"))\n'))          # two lines away is not the line above

    def test_unreadable_python_is_reported_not_passed_silently(self):
        self.assertEqual(findings("def broken(:\n"), ["unreadable Python (syntax error): not checked"])


class ShellAndNode(unittest.TestCase):
    def test_shell_commands_over_the_home_folder(self):
        for line in ("ls ~", "ls ~/", "find ~ -name TEAM.yaml", "ls ~/Desktop", "du -sh $HOME", 'ls "$HOME"', "for f in ~/*; do echo $f; done",
                     "grep -r x ${HOME}/Documents", "ls ~/*/TEAM.yaml"):
            self.assertTrue(findings(line + "\n", "shell"), line)

    def test_shell_named_roots_and_other_commands_pass(self):
        for line in ("ls /tmp", "ls ~/.dsh/sessions", "cd ~/dtadpole/reflection", "echo ~", "cat ~/.reflection/x.json", "ls ~/dtadpole/reflection/_tools_",
                     "# ls ~", "git -C ~/workspace/lastwar status", "ls ~/.computer-use/runs"):
            self.assertEqual(findings(line + "\n", "shell"), [], line)

    def test_shell_allow_marker(self):
        self.assertEqual(findings("ls ~  # home-glob: ok interactive helper\n", "shell"), [])

    def test_node_listings_over_the_home_folder(self):
        for line in ("fs.readdirSync(os.homedir())", "fs.readdir(os.homedir(), cb)", "glob('~/*/x')", "globSync(`${os.homedir()}/*`)",
                     "fs.opendirSync(process.env.HOME)"):
            self.assertTrue(findings(line + "\n", "node"), line)

    def test_node_named_roots_pass(self):
        for line in ("fs.readdirSync(path.join(os.homedir(), '.computer-use', 'runs'))", "fs.readdirSync('/tmp')", "fs.readFileSync(path.join(os.homedir(), '.x'))"):
            self.assertEqual(findings(line + "\n", "node"), [], line)


class CommandLine(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run([sys.executable, "-B", str(TOOL), *args], capture_output=True, text=True)

    def test_exit_codes_and_the_finding_line_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.py"
            bad.write_text('import os\nos.listdir(os.path.expanduser("~"))\n')
            good = Path(tmp) / "good.py"
            good.write_text("x = 1\n")
            r = self.run_tool("--root", tmp, str(bad))
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertRegex(r.stdout, r"bad\.py:2: listdir\(\) over the home folder itself")
            self.assertIn("1 finding(s) in 1 file(s)", r.stdout)
            self.assertEqual(self.run_tool("--root", tmp, str(good)).returncode, 0)

    def test_staged_blobs_are_what_is_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = lambda *a: subprocess.run(["git", "-C", tmp, *a], capture_output=True, text=True, check=True)
            run("init", "-q")
            (Path(tmp) / "t.py").write_text('import os\nos.listdir(os.path.expanduser("~"))\n')
            run("add", "t.py")
            (Path(tmp) / "t.py").write_text("x = 1\n")                                       # the working copy is clean, the staged blob is not
            r = self.run_tool("--root", tmp, "--staged")
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn("t.py:2:", r.stdout)

    def test_the_default_scan_is_the_tools_folder_of_the_root(self):
        r = self.run_tool("--root", str(ROOT))
        self.assertIn("file(s)", r.stdout)


class OurOwnTree(unittest.TestCase):
    def test_no_tool_under_tools_globs_lists_or_walks_from_the_home_folder(self):
        """The guard (2026-11-26): a wildcard first below ~, or a listing of ~ or of Desktop, Documents, Downloads, Music, Movies, Pictures, Library,
        Public, in any Python, shell or Node file here. Named roots are fine; `home-glob: ok <reason>` allows one line."""
        bad = []
        for f in hg.files_under([ROOT / "_tools_"]):
            if "test_home_glob_check" in f.name:
                continue                                                                      # its own fixtures are strings, not code that runs
            for number, why in hg.scan_text(str(f), f.read_text(encoding="utf-8", errors="replace"), hg.EXTENSIONS[f.suffix]):
                bad.append(f"{f.relative_to(ROOT)}:{number}: {why}")
        self.assertEqual(bad, [], "a tool that globs or lists from the home folder is the same breach as `ls ~` (~/.dsh/AGENTS.md): name the root")


if __name__ == "__main__":
    unittest.main()
