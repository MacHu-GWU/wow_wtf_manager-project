# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk import wtf
from wow_wtf_manager.paths import dir_project_root

dir_app = dir_project_root / "project" / "wotlk"
dir_wow = Path(r"C:\Games\World of Warcraft")
base_game_client_config = wtf.GameClientConfig(dir_wow=dir_wow)
