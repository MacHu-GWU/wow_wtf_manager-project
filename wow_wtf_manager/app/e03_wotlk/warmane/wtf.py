# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk import wtf
from wow_wtf_manager.paths import dir_project_root

dir_wow = Path(r"C:\Games\World of Warcraft")

dir_app = dir_project_root / "project" / "wotlk"
dir_01_game_client = dir_app / "01_game_client"

base_game_client_config = wtf.BaseGameClientConfig(dir_wow=dir_wow)


class WTF:
    class GameClient:
        c01_1920_1080_max = base_game_client_config.to_game_client_config(
            dir_01_game_client / "1920-1080-max-graphic-sound.txt"
        )
        c2_1920_1080_minimal = base_game_client_config.to_game_client_config(
            dir_01_game_client / "1920-1080-minimal-graphic-sound.txt"
        )
        c3_1600_900_minimal = base_game_client_config.to_game_client_config(
            dir_01_game_client / "1600-900-minimal-graphic-sound.txt"
        )
        c4_1176_664_minimal = base_game_client_config.to_game_client_config(
            dir_01_game_client / "1176-664-minimal-graphic-sound.txt"
        )
