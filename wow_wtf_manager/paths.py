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

_dir_app = dir_project_root / "app"

dir_wotlk_warmane_project = _dir_app / "e03_wotlk_warmane"
dir_wotlk_acore_project = _dir_app / "e03_wotlk_acore"
dir_mop_project = _dir_app / "e05_mop"
