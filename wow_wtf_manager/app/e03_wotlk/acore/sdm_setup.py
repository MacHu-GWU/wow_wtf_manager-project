# -*- coding: utf-8 -*-

"""
这个脚本定义了你每个魔兽世界账号下的 SuperDupeMacro 插件的配置.
"""

import typing as T
from wow_wtf_manager.exp.e03_wotlk.sdm import AccountSDMSetup, ClientSDMSetup

from .group import AccountEnum, AccountGroup, CharacterGroup, CharacterEnum
from .sdm_macro import Macros
from .form import dir_wow

client_sdm_setup = ClientSDMSetup(
    dir_wow=dir_wow,
)

# ------------------------------------------------------------------------------
# Global Macro
# ------------------------------------------------------------------------------
def global_macro():
    client_sdm_setup.add_macros_for_many_accounts(
        accounts=AccountGroup.ag_all_account,
        files=[
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


# ------------------------------------------------------------------------------
# Character
# ------------------------------------------------------------------------------
def s_01_protect_retribution_paladin():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat01_acore_ra,
        ],
        files=[
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


def s_02_elemental_resto_shaman():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat02_acore_rb,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_00_common____2004_buff_healer,
            Macros.sdm_05_shaman____0_common____15101_consumable,
            Macros.sdm_05_shaman____0_common____15102_interrupt,
            Macros.sdm_05_shaman____1_elemental_resto____15311_buff_self_zhTW,
            # Act
            Macros.sdm_05_shaman____0_common____15111_elemental_rotation_zhTW,
            Macros.sdm_05_shaman____0_common____15112_resto_rotation_zhTW,
            Macros.sdm_05_shaman____0_common____15114_mb_resto_earth_shield_zhTW,
            Macros.sdm_05_shaman____1_elemental_resto____15312_burst_zhTW,
        ],
    )


def s_03_balance_resto_druid():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat03_acore_rc,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_07_druid____0_common____17101_consumable,
            Macros.sdm_07_druid____1_balance_resto____17301_buff_self_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17302_buff_raid_zhTW,
            # Act
            Macros.sdm_07_druid____1_balance_resto____17303_multibox_main_rotate_zhTW,
        ],
    )


def s_04_arcane_fire_mage():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat04_acore_rd,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_09_mage____0_common____19101_consumable,
            Macros.sdm_09_mage____0_common____19102_interrupt_zhTW,
            Macros.sdm_09_mage____0_common____19103_buff_self_zhTW,
            Macros.sdm_09_mage____0_common____19104_buff_team_zhTW,
            # Act
            Macros.sdm_09_mage____1_arcane_fire____19311_act1_zhTW,
            Macros.sdm_09_mage____1_arcane_fire____19312_act2_zhTW,
            Macros.sdm_09_mage____0_common____19105_act3_zhTW,
            Macros.sdm_09_mage____1_arcane_fire____19319_rotation_zhTW,
            Macros.sdm_09_mage____1_arcane_fire____19322_add_debuff_zhTW,
        ],
    )


def s_05_shadow_disco_priest():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat05_acore_re,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_10_priest____0_common____19101_consumable,
            Macros.sdm_10_priest____1_shadow_disco____19301_buff_self_zhTW,
            Macros.sdm_10_priest____0_common____19102_buff_raid_zhTW,
            # Act
            Macros.sdm_10_priest____1_shadow_disco____19302_act1_zhTW,
            Macros.sdm_10_priest____1_shadow_disco____19303_act2_zhTW,
            Macros.sdm_10_priest____1_shadow_disco____19306_multibox_main_rotate_zhTW,
        ],
    )


def s_06_demonology_affiliation_warlock():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat06_acore_rf,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_08_warlock____0_common____18101_consumable,
            # Act
            Macros.sdm_08_warlock____0_common____18102_elemental_curse_zhTW,
            Macros.sdm_08_warlock____0_common____18103_tongue_curse_zhTW,
            Macros.sdm_08_warlock____0_common____18104_corruption_zhTW,
            Macros.sdm_08_warlock____0_common____18111_demonology_rotation_zhTW,
            Macros.sdm_08_warlock____0_common____18112_affiliation_rotation_zhTW,
            Macros.sdm_08_warlock____0_common____18114_spell_stone_zhTW,
            Macros.sdm_08_warlock____1_demonology_affiliation____18311_burst_zhTW,
            Macros.sdm_08_warlock____1_demonology_affiliation____18321_add_debuff_zhTW,
        ],
    )


def s_07_marksmanship_survival_hunter():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat07_acore_rg,
        ],
        files=[
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


def s_08_balance_resto_druid():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat08_acore_rh,
        ],
        files=[
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_07_druid____0_common____17101_consumable,
            Macros.sdm_07_druid____1_balance_resto____17301_buff_self_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17302_buff_raid_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17303_multibox_main_rotate_zhTW,
        ],
    )


def s_09_holy_protect_paladin():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat09_acore_ri,
            CharacterEnum.fat24_acore_rx,
        ],
        files=[
            Macros.sdm_00_common____2003_buff_tank,
            Macros.sdm_00_common____2004_buff_healer,
            Macros.sdm_02_paladin____0_common____11101_consumable,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW,
            Macros.sdm_02_paladin____0_common____11151_high_int_heal_rotation_zhTW,
            Macros.sdm_02_paladin____0_common____11152_high_crt_heal_rotation_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11751_mb_periodical_beacon_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11752_mb_periodical_judgement_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11711_act1_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11712_act2_zhTW,
            Macros.sdm_02_paladin____0_common____11133_holy_rotation_zhTW,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11731_buff_self_alliance_zhTW,
        ],
    )


def s_10_blood_unholy_dk():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat10_acore_rj,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2003_buff_tank,
            Macros.sdm_00_common____2001_buff_physics_dps,
            Macros.sdm_03_dk____0_common____13101_consumable,
            Macros.sdm_03_dk____0_common____13123_frost_buff_self_zhTW,
            Macros.sdm_03_dk____0_common____13122_unholy_buff_self_zhTW,
            # Act
            Macros.sdm_03_dk____0_common____13111_act1_zhTW,
            Macros.sdm_03_dk____0_common____13112_act2_zhTW,
            Macros.sdm_03_dk____0_common____13113_act3_zhTW,
            Macros.sdm_03_dk____0_common____13114_act4_zhTW,
            Macros.sdm_03_dk____0_common____13131_tank_rotation_zhTW,
            Macros.sdm_03_dk____0_common____13132_tank_survival_rotation_zhTW,
        ],
    )


def s_11_to_13_balance_resto_druid():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat11_acore_rk,
            CharacterEnum.fat12_acore_rl,
            CharacterEnum.fat13_acore_rm,
        ],
        files=[
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_07_druid____0_common____17101_consumable,
            Macros.sdm_07_druid____1_balance_resto____17301_buff_self_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17302_buff_raid_zhTW,
            Macros.sdm_07_druid____1_balance_resto____17303_multibox_main_rotate_zhTW,
        ],
    )


def s_14_to_22_shadow_disco_priest():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat14_acore_rn,
            CharacterEnum.fat15_acore_ro,
            CharacterEnum.fat16_acore_rp,
            CharacterEnum.fat17_acore_rq,
            CharacterEnum.fat18_acore_rr,
            CharacterEnum.fat19_acore_rs,
            CharacterEnum.fat20_acore_rt,
            CharacterEnum.fat21_acore_ru,
            CharacterEnum.fat22_acore_rv,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_10_priest____0_common____19101_consumable,
            Macros.sdm_10_priest____1_shadow_disco____19301_buff_self_zhTW,
            Macros.sdm_10_priest____0_common____19102_buff_raid_zhTW,
            # Act
            Macros.sdm_10_priest____1_shadow_disco____19302_act1_zhTW,
            Macros.sdm_10_priest____1_shadow_disco____19303_act2_zhTW,
            Macros.sdm_10_priest____1_shadow_disco____19306_multibox_main_rotate_zhTW,
        ],
    )


def s_23_elemental_resto_shaman():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat23_acore_rw,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_00_common____2004_buff_healer,
            Macros.sdm_05_shaman____0_common____15101_consumable,
            Macros.sdm_05_shaman____0_common____15102_interrupt,
            Macros.sdm_05_shaman____1_elemental_resto____15311_buff_self_zhTW,
            # Act
            Macros.sdm_05_shaman____0_common____15111_elemental_rotation_zhTW,
            Macros.sdm_05_shaman____0_common____15112_resto_rotation_zhTW,
            Macros.sdm_05_shaman____0_common____15114_mb_resto_earth_shield_zhTW,
            Macros.sdm_05_shaman____1_elemental_resto____15312_burst_zhTW,
        ],
    )


def s_24_holy_protect_paladin():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat24_acore_rx,
        ],
        files=[
            Macros.sdm_00_common____2003_buff_tank,
            Macros.sdm_00_common____2004_buff_healer,
            Macros.sdm_02_paladin____0_common____11101_consumable,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW,
            Macros.sdm_02_paladin____0_common____11151_high_int_heal_rotation_zhTW,
            Macros.sdm_02_paladin____0_common____11152_high_crt_heal_rotation_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11751_mb_periodical_beacon_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11752_mb_periodical_judgement_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11711_act1_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11712_act2_zhTW,
            Macros.sdm_02_paladin____0_common____11133_holy_rotation_zhTW,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW,
            Macros.sdm_02_paladin____3_holy_protect____11731_buff_self_alliance_zhTW,
        ],
    )


def s_25_disco_holy_priest():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat25_acore_ry,
        ],
        files=[
            # Buff
            Macros.sdm_00_common____2002_buff_caster_dps,
            Macros.sdm_10_priest____0_common____19101_consumable,
            Macros.sdm_10_priest____2_disco_holy____19501_buff_self_zhTW,
            # Act
            Macros.sdm_10_priest____2_disco_holy____19521_heal_rotate_zhTW,
            Macros.sdm_10_priest____2_disco_holy____19522_mb_periodical_prayer_of_mending_zhTW,
        ],
    )


# ------------------------------------------------------------------------------
# Normal
# ------------------------------------------------------------------------------
def special_act_placeholder():
    client_sdm_setup.add_macros_for_many_chars(
        chars=CharacterGroup.cg_all_character,
        files=[
            Macros.sdm_00_common____6001_mb_special1,
            Macros.sdm_00_common____6002_mb_special2,
            Macros.sdm_00_common____6003_mb_special3,
        ],
    )


def special_act_ICC_1():
    client_sdm_setup.add_macros_for_many_chars(
        chars=CharacterGroup.cg_all_character,
        files=[
            Macros.sdm_00_common____6001_mb_special1,
            Macros.sdm_00_common____6002_mb_special2,
            Macros.sdm_00_common____6003_mb_special3,
        ],
    )


# --- global
global_macro()

# --- charactor
s_01_protect_retribution_paladin()
s_02_elemental_resto_shaman()
s_03_balance_resto_druid()
s_04_arcane_fire_mage()
s_05_shadow_disco_priest()
s_06_demonology_affiliation_warlock()
s_07_marksmanship_survival_hunter()
s_08_balance_resto_druid()
s_09_holy_protect_paladin()
s_10_blood_unholy_dk()

s_11_to_13_balance_resto_druid()
s_14_to_22_shadow_disco_priest()

s_23_elemental_resto_shaman()
s_24_holy_protect_paladin()
s_25_disco_holy_priest()

# --- special
special_act_placeholder()
# special_act_ICC_1()
