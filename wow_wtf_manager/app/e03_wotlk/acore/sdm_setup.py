# -*- coding: utf-8 -*-

import typing as T
from wow_wtf_manager.exp.e03_wotlk.sdm import AccountSDMSetup, ClientSDMSetup

from .group import AccountEnum, AccountGroup, CharacterGroup
from .sdm_macro import Macros
from .form import dir_wow

accounts: T.List[AccountSDMSetup] = list()

# ------------------------------------------------------------------------------
# Global
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Character
# ------------------------------------------------------------------------------
# Balance Druid
for account in [
    AccountEnum.fat11,
    # AccountEnum.fat12,
    # AccountEnum.fat13,
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            # Macros.sdm_00_common____01_respawn.macro
        ],
    )
    accounts.append(account_sdm_setup)

# for account in AccountGroup.ag_fat_01_to_25:
for account_sdm_setup in accounts:
    common_macros = [
        Macros.sdm_00_common____1001_respawn.macro,
        Macros.sdm_00_common____1002_feigh_death.macro,
        Macros.sdm_00_common____1003_reset_cooldown.macro,
        Macros.sdm_00_common____1004_ice_block.macro,
        Macros.sdm_00_common____1005_resurrection.macro,
        Macros.sdm_00_common____1006_invisibility.macro,
        Macros.sdm_00_common____1007_unbind_instance.macro,
        Macros.sdm_00_common____1008_fly_up.macro,
        Macros.sdm_00_common____1009_fly_down.macro,
        Macros.sdm_00_common____1010_x32_speed.macro,

        Macros.sdm_00_common____1101_target_party.macro,
        Macros.sdm_00_common____1102_target_raid.macro,
        Macros.sdm_00_common____1103_target_focus_target.macro,
        Macros.sdm_00_common____1104_target_focus_target_target.macro,
        Macros.sdm_00_common____1105_confirm.macro,
        Macros.sdm_00_common____1106_set_focus.macro,
        Macros.sdm_00_common____1107_clear_focus.macro,
        Macros.sdm_00_common____1108_set_high_fps.macro,
        Macros.sdm_00_common____1109_set_low_fps.macro,
        Macros.sdm_00_common____1110_follow_focus.macro,

        Macros.sdm_00_common____1131_target_window_01.macro,
        Macros.sdm_00_common____1132_target_window_10.macro,

        Macros.sdm_00_common____1151_invite_raid.macro,
        Macros.sdm_00_common____1152_leave_raid.macro,
        Macros.sdm_00_common____1153_summon.macro,

        Macros.sdm_00_common____1171_tele_darnassus.macro,
        Macros.sdm_00_common____1172_tele_ironforge.macro,
        Macros.sdm_00_common____1175_tele_shattrath.macro,
        Macros.sdm_00_common____1176_tele_dalaran.macro,
    ]
    account_sdm_setup.macros = common_macros + account_sdm_setup.macros

client_sdm_setup = ClientSDMSetup(
    dir_wow=dir_wow,
    accounts=accounts,
)
