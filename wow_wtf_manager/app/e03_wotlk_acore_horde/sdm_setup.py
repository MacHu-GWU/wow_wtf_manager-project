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
            Macros.sdm_00_common____1173_tele_orgrimmar,
            Macros.sdm_00_common____1174_tele_undercity,
            Macros.sdm_00_common____1175_tele_shattrath,
            Macros.sdm_00_common____1176_tele_dalaran,
        ],
    )


def s_01_protect_retribution_paladin():
    sdm_setup.add_macros_to_character(
        character=[
            CharacterEnum.sa,
        ],
        sdm_files=[
            # Buff
            Macros.sdm_00_common____2003_buff_tank,
            Macros.sdm_00_common____2001_buff_physics_dps,
            Macros.sdm_02_paladin____0_common____11101_consumable,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhCN,
            Macros.sdm_02_paladin____1_protect_retri____11311_buff_self_alliance_zhCN,
            # Act
            Macros.sdm_02_paladin____1_protect_retri____11301_act1_zhCN,
            Macros.sdm_02_paladin____1_protect_retri____11302_act2_zhCN,
            Macros.sdm_02_paladin____1_protect_retri____11303_act3_zhCN,
            Macros.sdm_02_paladin____1_protect_retri____11304_act4_zhCN,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhCN,
            Macros.sdm_02_paladin____0_common____11132_retribution_rotation_zhCN,
        ],
    )


def s_02_elemental_resto_shaman():
    sdm_setup.add_macros_to_character(
        character=[
            CharacterEnum.sb,
            CharacterEnum.sc,
            CharacterEnum.sd,
            CharacterEnum.se,
        ],
        sdm_files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_00_common____2004_buff_healer,
            Macros.sdm_05_shaman____0_common____15101_consumable,
            Macros.sdm_05_shaman____0_common____15102_interrupt_zhCN,
            Macros.sdm_05_shaman____1_elemental_resto____15311_buff_self_zhCN,
            # Act
            Macros.sdm_05_shaman____0_common____15111_elemental_rotation_zhCN,
            Macros.sdm_05_shaman____0_common____15112_resto_rotation_zhCN,
            Macros.sdm_05_shaman____0_common____15114_mb_resto_earth_shield_zhCN,
            Macros.sdm_05_shaman____1_elemental_resto____15312_burst_zhCN,
        ],
    )


def s_03_balance_resto_druid():
    sdm_setup.add_macros_to_character(
        character=[
            CharacterEnum.fatbird,
        ],
        sdm_files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_07_druid____0_common____17101_consumable,
            Macros.sdm_07_druid____1_balance_resto____17301_buff_self_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17302_buff_raid_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17303_rotation_zhTW,
            # Act
            Macros.sdm_07_druid____1_balance_resto____17303_rotation_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17304_multibox_slow_heal_zhTW,
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
            Macros.sdm_04_hunter____0_common____14102_misdirect_zhCN,
            Macros.sdm_04_hunter____0_common____14103_tranquil_zhCN,
            Macros.sdm_04_hunter____0_common____14104_pack_aspect_zhCN,
            Macros.sdm_04_hunter____0_common____14105_viper_aspect_zhCN,
            Macros.sdm_04_hunter____0_common____14106_burst_zhCN,
            Macros.sdm_04_hunter____1_marksmanship_survival____14301_buff_self_zhCN,
            Macros.sdm_04_hunter____0_common____14111_act1_zhCN,
            Macros.sdm_04_hunter____1_marksmanship_survival____14312_act2_zhCN,
            Macros.sdm_04_hunter____1_marksmanship_survival____14313_act3_zhCN,
            Macros.sdm_04_hunter____1_marksmanship_survival____14314_act4_zhCN,
            Macros.sdm_04_hunter____0_common____14121_marksmanship_rotation_zhCN,
            Macros.sdm_04_hunter____0_common____14122_survival_rotation_zhCN,
            Macros.sdm_04_hunter____1_marksmanship_survival____14321_add_debuff_zhCN,
        ],
    )


global_macro()

s_01_protect_retribution_paladin()
s_02_elemental_resto_shaman()
s_03_balance_resto_druid()
s04_hunter()
