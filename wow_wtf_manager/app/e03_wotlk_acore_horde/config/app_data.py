# -*- coding: utf-8 -*-

from wow_wtf_manager.paths import dir_project_root
from wow_wtf_manager.exp.e03_wotlk.api import AppData

app_data = AppData(
    dir_root=dir_project_root.joinpath("app", "e03_wotlk_acore_horde")
)
