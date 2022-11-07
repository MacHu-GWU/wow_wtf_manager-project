# -*- coding: utf-8 -*-

from wow_wtf_manager.paths import dir_wotlk_acore_project
from wow_wtf_manager.exp.e03_wotlk.sdm import SDMMacroFile

class Macros:
    sdm_00_common____01_respawn = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "01-respawn.yml"))
    sdm_00_common____02_feigh_death = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "02-feigh-death.yml"))
    sdm_00_common____03_reset_cooldown = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "03-reset-cooldown.yml"))
    sdm_00_common____04_ice_block = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "04-ice-block.yml"))
    sdm_00_common____05_resurrection = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "05-resurrection.yml"))
    sdm_00_common____06_invisibility = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "06-invisibility.yml"))
    sdm_00_common____07_unbind_instance = SDMMacroFile(path=dir_wotlk_acore_project.joinpath("SuperDuperMacro", "00-common", "07-unbind-instance.yml"))