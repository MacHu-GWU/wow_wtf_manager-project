# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_python_lib = Path.dir_here(__file__)
PACKAGE_NAME = dir_python_lib.basename

dir_project_root = dir_python_lib.parent
assert dir_project_root.basename == "wow_wtf_manager-project"

# --- Tests
# unit test
dir_tests = dir_project_root / "tests"
# integration test
dir_tests_int = dir_project_root / "tests_int"

# --- App
dir_app = dir_project_root / "app"
