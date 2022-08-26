# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent
assert dir_project_root.basename == "wow_wtf_manager-project"

dir_python_lib = dir_project_root / "wow_wtf_manager"
dir_tests = dir_project_root / "tests"

_dir_project = dir_project_root / "project"

dir_wotlk_project = _dir_project / "e03_wotlk"
dir_mop_project = _dir_project / "e05_mop"
