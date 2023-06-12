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


def s04_hunter():
    sdm_setup.add_macros_to_character(
        character=[
            CharacterEnum.shootingrab,
        ],
        sdm_files=[
            # Buff
            Macros.sdm_00_common____2001_buff_physics_dps,
            Macros.sdm_04_hunter____0_common____14101_consumable,
            # Act
            Macros.sdm_04_hunter____0_common____14102_misdirect_zhTW,
            Macros.sdm_04_hunter____0_common____14103_tranquil_zhTW,
            Macros.sdm_04_hunter____0_common____14104_pack_aspect_zhTW,
            Macros.sdm_04_hunter____0_common____14105_viper_aspect_zhTW,
            Macros.sdm_04_hunter____0_common____14106_burst_zhTW,
            Macros.sdm_04_hunter____1_marksmanship_survival____14301_buff_self_zhTW,
            Macros.sdm_04_hunter____0_common____14111_act1_zhTW,
            Macros.sdm_04_hunter____1_marksmanship_survival____14312_act2_zhTW,
            Macros.sdm_04_hunter____1_marksmanship_survival____14313_act3_zhTW,
            Macros.sdm_04_hunter____1_marksmanship_survival____14314_act4_zhTW,
            Macros.sdm_04_hunter____0_common____14121_marksmanship_rotation_zhTW,
            Macros.sdm_04_hunter____0_common____14122_survival_rotation_zhTW,
            Macros.sdm_04_hunter____1_marksmanship_survival____14321_add_debuff_zhTW,
        ],
    )


global_macro()
s04_hunter()
