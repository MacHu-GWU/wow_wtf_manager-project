# -*- coding: utf-8 -*-

from pathlib_mate import Path
from ...paths import dir_app

dir_here = Path.dir_here(__file__)
path_sdm_macro = dir_here / "sdm_macro.py"
dir_root = dir_app / "e03_wotlk_example"
dir_sdm = dir_root / "32_SuperDuperMacro"
