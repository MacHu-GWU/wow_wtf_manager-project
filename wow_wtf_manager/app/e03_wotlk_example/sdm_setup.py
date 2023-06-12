# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.sdm.api import ClientSDMSetup

from .scope.api import (
    client,
    AccountEnum,
    AccountGroupEnum,
    CharacterEnum,
    CharacterGroupEnum,
)
from .sdm_macro import Macros


sdm_setup = ClientSDMSetup(dir_wtf=client.dir_wtf)


def global_macro():
    sdm_setup.add_macros_to_account(
        account=AccountGroupEnum.all,
        sdm_files=[
            # GM command
            Macros.sdm_00_common____1001_respawn,
            Macros.sdm_00_common____1002_feigh_death,
            Macros.sdm_00_common____1003_reset_cooldown,
            Macros.sdm_00_common____1004_ice_block,
            Macros.sdm_00_common____1005_resurrection,
            Macros.sdm_00_common____1006_invisibility,
            Macros.sdm_00_common____1007_unbind_instance,
            Macros.sdm_00_common____1008_fly_up,
            Macros.sdm_00_common____1009_fly_down,
            Macros.sdm_00_common____1010_x32_speed,
            # Mount
            Macros.sdm_00_common____1011_MountUp_zhTW,
            Macros.sdm_00_common____1012_MountDown_zhTW,
            # Multi-box
            Macros.sdm_00_common____1101_target_party,
            Macros.sdm_00_common____1102_target_raid,
            Macros.sdm_00_common____1103_target_focus_target,
            Macros.sdm_00_common____1104_target_focus_target_target,
            Macros.sdm_00_common____1105_confirm,
            Macros.sdm_00_common____1106_set_focus,
            Macros.sdm_00_common____1107_clear_focus,
            Macros.sdm_00_common____1108_set_high_fps,
            Macros.sdm_00_common____1109_set_low_fps,
            Macros.sdm_00_common____1110_follow_focus,
            # Target specific character
            Macros.sdm_00_common____1131_target_window_01,
            Macros.sdm_00_common____1132_target_window_10,
            # Party and Raid
            Macros.sdm_00_common____1151_invite_raid,
            Macros.sdm_00_common____1152_leave_raid,
            Macros.sdm_00_common____1153_summon,
            # Teleport
            Macros.sdm_00_common____1171_tele_darnassus,
            Macros.sdm_00_common____1172_tele_ironforge,
            Macros.sdm_00_common____1175_tele_shattrath,
            Macros.sdm_00_common____1176_tele_dalaran,
        ],
    )


def s02_paladin():
    sdm_setup.add_macros_to_character(
        character=[
            CharacterEnum.wtfaa,
        ],
        sdm_files=[
            # Buff
            Macros.sdm_00_common____2003_buff_tank,
            Macros.sdm_00_common____2001_buff_physics_dps,
            Macros.sdm_02_paladin____0_common____11101_consumable,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW,
            Macros.sdm_02_paladin____1_protect_retri____11311_buff_self_alliance_zhTW,
            # Act
            Macros.sdm_02_paladin____1_protect_retri____11301_act1_zhTW,
            Macros.sdm_02_paladin____1_protect_retri____11302_act2_zhTW,
            Macros.sdm_02_paladin____1_protect_retri____11303_act3_zhTW,
            Macros.sdm_02_paladin____1_protect_retri____11304_act4_zhTW,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW,
            Macros.sdm_02_paladin____0_common____11132_retribution_rotation_zhTW,
        ],
    )


global_macro()
s02_paladin()
