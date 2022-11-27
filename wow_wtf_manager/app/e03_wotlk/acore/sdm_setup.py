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
# Global
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Character
# ------------------------------------------------------------------------------
def s_01_protect_retribution_paladin():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat01_acore_ra,
        ],
        macros=[
            Macros.sdm_00_common____2003_buff_tank.macro,
            Macros.sdm_00_common____2001_buff_physics_dps.macro,
            Macros.sdm_02_paladin____0_common____11101_consumable.macro,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11311_buff_self_alliance_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11301_act1_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11302_act2_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11303_act3_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11304_act4_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11132_retribution_rotation_zhTW.macro,
        ],
    )


s_01_protect_retribution_paladin()


def s_02_elemental_resto_shaman():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat02_acore_rb,
        ],
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_00_common____2004_buff_healer.macro,
            Macros.sdm_05_shaman____0_common____15101_consumable.macro,
            Macros.sdm_05_shaman____0_common____15102_interrupt.macro,
            Macros.sdm_05_shaman____1_elemental_resto____15311_buff_self_zhTW.macro,
            Macros.sdm_05_shaman____0_common____15111_elemental_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____15112_resto_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____15114_mb_resto_earth_shield_zhTW.macro,
            Macros.sdm_05_shaman____1_elemental_resto____15312_burst_zhTW.macro,
        ],
    )


s_02_elemental_resto_shaman()
# # --- Feral / Balance Druid
# # for account, character in [
# #     (AccountEnum.fat03, CharacterEnum.fat03_acore_rc),
# # ]:
# #     account_sdm_setup = AccountSDMSetup(
# #         account=account,
# #         macros=[
# #             Macros.sdm_00_common____2002_buff_caster_dps.macro,
# #             Macros.sdm_07_druid____0_common____17101_consumable.macro,
# #             Macros.sdm_07_druid____3_feral_and_balance____17701_buff_self_zhTW.macro,
# #             Macros.sdm_07_druid____3_feral_and_balance____17702_buff_raid_zhTW.macro,
# #             Macros.sdm_07_druid____3_feral_and_balance____17703_multibox_main_rotate_zhTW.macro,
# #
# #             # Macros.sdm_00_common____6001_mb_special1.macro,
# #             # Macros.sdm_00_common____6002_mb_special2.macro,
# #             # Macros.sdm_00_common____6003_mb_special3.macro,
# #         ],
# #     )
# #     for macro in account_sdm_setup.macros:
# #         macro.set_char(name=character.character, realm=character.server)
# #     accounts.append(account_sdm_setup)


def s_04_arcane_fire_mage():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat04_acore_rd,
        ],
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_09_mage____0_common____19101_consumable.macro,
            Macros.sdm_09_mage____0_common____19102_interrupt.macro,
            Macros.sdm_09_mage____0_common____19103_buff_self_zhTW.macro,
            Macros.sdm_09_mage____0_common____19104_buff_team_zhTW.macro,
            Macros.sdm_09_mage____1_arcane_fire____19311_act1_zhTW.macro,
            Macros.sdm_09_mage____1_arcane_fire____19312_act2_zhTW.macro,
            Macros.sdm_09_mage____0_common____19105_act3_zhTW.macro,
            Macros.sdm_09_mage____1_arcane_fire____19319_rotation_zhTW.macro,
            Macros.sdm_09_mage____1_arcane_fire____19322_add_debuff_zhTW.macro,
        ],
    )


s_04_arcane_fire_mage()


def s_05_and_14_to_22_shadow_disco_priest():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat05_acore_re,
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
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_10_priest____0_common____19101_consumable.macro,
            Macros.sdm_10_priest____1_shadow_disco____19301_buff_self_zhTW.macro,
            Macros.sdm_10_priest____0_common____19102_buff_raid_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19302_act1_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19303_act2_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19306_multibox_main_rotate_zhTW.macro,
        ],
    )


s_05_and_14_to_22_shadow_disco_priest()


def s_06_demonology_affiliation_warlock():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat06_acore_rf,
        ],
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_08_warlock____0_common____18101_consumable.macro,
            Macros.sdm_08_warlock____0_common____18102_elemental_curse.macro,
            Macros.sdm_08_warlock____0_common____18103_tongue_curse.macro,
            Macros.sdm_08_warlock____0_common____18104_corruption.macro,
            Macros.sdm_08_warlock____0_common____18111_demonology_rotation_zhTW.macro,
            Macros.sdm_08_warlock____0_common____18112_affiliation_rotation_zhTW.macro,
            Macros.sdm_08_warlock____0_common____18114_spell_stone_zhTW.macro,
            Macros.sdm_08_warlock____1_demonology_affiliation____18311_burst_zhTW.macro,
            Macros.sdm_08_warlock____1_demonology_affiliation____18321_add_debuff_zhTW.macro,
        ],
    )


s_06_demonology_affiliation_warlock()


def s_07_marksmanship_survival_hunter():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat07_acore_rg,
        ],
        macros=[
            Macros.sdm_00_common____2001_buff_physics_dps.macro,
            Macros.sdm_04_hunter____0_common____14101_consumable.macro,
            Macros.sdm_04_hunter____0_common____14102_misdirect_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14103_tranquil_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14104_pack_aspect_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14105_viper_aspect_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14106_burst_zhTW.macro,
            Macros.sdm_04_hunter____1_marksmanship_survival____14301_buff_self_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14111_act1_zhTW.macro,
            Macros.sdm_04_hunter____1_marksmanship_survival____14312_act2_zhTW.macro,
            Macros.sdm_04_hunter____1_marksmanship_survival____14313_act3_zhTW.macro,
            Macros.sdm_04_hunter____1_marksmanship_survival____14314_act4_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14121_marksmanship_rotation_zhTW.macro,
            Macros.sdm_04_hunter____0_common____14122_survival_rotation_zhTW.macro,
            Macros.sdm_04_hunter____1_marksmanship_survival____14321_add_debuff_zhTW.macro,
        ],
    )


s_07_marksmanship_survival_hunter()


def s_09_holy_protect_paladin():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat09_acore_ri,
            CharacterEnum.fat24_acore_rx,
        ],
        macros=[
            Macros.sdm_00_common____2003_buff_tank.macro,
            Macros.sdm_00_common____2004_buff_healer.macro,
            Macros.sdm_02_paladin____0_common____11101_consumable.macro,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11151_high_int_heal_rotation_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11152_high_crt_heal_rotation_zhTW.macro,
            Macros.sdm_02_paladin____3_holy_protect____11751_mb_periodical_beacon_zhTW.macro,
            Macros.sdm_02_paladin____3_holy_protect____11752_mb_periodical_judgement_zhTW.macro,
            Macros.sdm_02_paladin____3_holy_protect____11711_act1_zhTW.macro,
            Macros.sdm_02_paladin____3_holy_protect____11712_act2_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11133_holy_rotation_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW.macro,
            Macros.sdm_02_paladin____3_holy_protect____11731_buff_self_alliance_zhTW.macro,
        ],
    )


s_09_holy_protect_paladin()


def s_11_to_13_balance_resto_druid():
    client_sdm_setup.add_macros_for_many_chars(
        chars=[
            CharacterEnum.fat11_acore_rk,
            CharacterEnum.fat12_acore_rl,
            CharacterEnum.fat13_acore_rm,
        ],
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_07_druid____0_common____17101_consumable.macro,
            Macros.sdm_07_druid____1_balance_resto____17301_buff_self_zhTW.macro,
            Macros.sdm_07_druid____1_balance_resto____17302_buff_raid_zhTW.macro,
            Macros.sdm_07_druid____1_balance_resto____17303_multibox_main_rotate_zhTW.macro,
        ],
    )


s_11_to_13_balance_resto_druid()


# ------------------------------------------------------------------------------
# Normal
# ------------------------------------------------------------------------------
def normal():
    pass
    # for character in CharacterGroup.cg_all_character:
    #     for macro in account_sdm_setup.macros:
    #         macro.set_char(name=character.character, realm=character.server)
    #     account_sdm_setup.macros.extend([
    #         Macros.sdm_00_common____6001_mb_special1.macro,
    #         Macros.sdm_00_common____6002_mb_special2.macro,
    #         Macros.sdm_00_common____6003_mb_special3.macro,
    #     ])
