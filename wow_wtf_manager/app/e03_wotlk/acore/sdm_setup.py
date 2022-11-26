# -*- coding: utf-8 -*-

import typing as T
from wow_wtf_manager.exp.e03_wotlk.sdm import AccountSDMSetup, ClientSDMSetup

from .group import AccountEnum, AccountGroup, CharacterGroup, CharacterEnum
from .sdm_macro import Macros
from .form import dir_wow

accounts: T.List[AccountSDMSetup] = list()

# ------------------------------------------------------------------------------
# Global
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Character
# ------------------------------------------------------------------------------
# --- Protect / Retribution Paladin
for account, character in [
    (AccountEnum.fat01, CharacterEnum.fat01_acore_ra),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            Macros.sdm_00_common____2003_buff_tank.macro,
            Macros.sdm_00_common____2001_buff_physics_dps.macro,
            Macros.sdm_02_paladin____0_common____11101_consumable.macro,
            Macros.sdm_02_paladin____0_common____11111_clear_debuff_zhTW.macro,

            Macros.sdm_02_paladin____1_protect_retri____11301_act1_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11302_act2_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11303_act3_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11304_act4_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11311_buff_self_alliance_zhTW.macro,

            Macros.sdm_02_paladin____0_common____11131_protect_rotation_zhTW.macro,
            Macros.sdm_02_paladin____0_common____11132_retribution_rotation_zhTW.macro,
        ],
    )
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Elemental / Resto Shaman
for account, character in [
    (AccountEnum.fat02, CharacterEnum.fat02_acore_rb),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_00_common____2004_buff_healer.macro,
            Macros.sdm_05_shaman____0_common____14101_consumable.macro,
            Macros.sdm_05_shaman____0_common____14102_interrupt.macro,

            Macros.sdm_05_shaman____0_common____14111_elemental_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____14112_resto_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____14114_mb_resto_earth_shield_zhTW.macro,

            Macros.sdm_05_shaman____1_elemental_resto____14311_buff_self_zhTW.macro,
            Macros.sdm_05_shaman____1_elemental_resto____14312_burst_zhTW.macro,
        ],
    )
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Arcane / Fire Mage
for account, character in [
    (AccountEnum.fat04, CharacterEnum.fat04_acore_rd),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
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
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Demonology / Affiliation Warlock
for account, character in [
    (AccountEnum.fat06, CharacterEnum.fat06_acore_rf),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
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
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Holy / Protect Paladin
for account, character in [
    (AccountEnum.fat09, CharacterEnum.fat09_acore_ri),
    (AccountEnum.fat24, CharacterEnum.fat24_acore_rx),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
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
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Balance Druid
for account, character in [
    (AccountEnum.fat11, CharacterEnum.fat11_acore_rk),
    # (AccountEnum.fat12, CharacterEnum.fat12_acore_rl),
    # (AccountEnum.fat13, CharacterEnum.fat13_acore_rm),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_07_druid____0_common____16101_consumable.macro,
            Macros.sdm_07_druid____1_balance_resto____16301_buff_self_zhTW.macro,
            Macros.sdm_07_druid____1_balance_resto____16302_buff_raid_zhTW.macro,
            Macros.sdm_07_druid____1_balance_resto____16303_multibox_main_rotate_zhTW.macro,

            Macros.sdm_00_common____6001_mb_special1.macro,
            Macros.sdm_00_common____6002_mb_special2.macro,
            Macros.sdm_00_common____6003_mb_special3.macro,
        ],
    )
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)

# --- Shadow Priest
for account, character in [
    (AccountEnum.fat14, CharacterEnum.fat14_acore_rn),
    (AccountEnum.fat15, CharacterEnum.fat15_acore_ro),
    # (AccountEnum.fat16, CharacterEnum.fat16_acore_rp),
    # (AccountEnum.fat17, CharacterEnum.fat17_acore_rq),
    # (AccountEnum.fat18, CharacterEnum.fat18_acore_rr),
    # (AccountEnum.fat19, CharacterEnum.fat19_acore_rs),
    # (AccountEnum.fat20, CharacterEnum.fat20_acore_rt),
    # (AccountEnum.fat21, CharacterEnum.fat21_acore_ru),
    # (AccountEnum.fat22, CharacterEnum.fat22_acore_rv),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            Macros.sdm_00_common____2002_buff_caster_dps.macro,
            Macros.sdm_10_priest____0_common____19101_consumable.macro,
            Macros.sdm_10_priest____1_shadow_disco____19301_buff_self_zhTW.macro,
            Macros.sdm_10_priest____0_common____19102_buff_raid_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19302_act1_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19303_act2_zhTW.macro,
            Macros.sdm_10_priest____1_shadow_disco____19306_multibox_main_rotate_zhTW.macro,

            Macros.sdm_00_common____6001_mb_special1.macro,
            Macros.sdm_00_common____6002_mb_special2.macro,
            Macros.sdm_00_common____6003_mb_special3.macro,
        ],
    )
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
    accounts.append(account_sdm_setup)


# --- Resto / Enhancement Shaman
for account, character in [
    (AccountEnum.fat23, CharacterEnum.fat23_acore_rw),
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            Macros.sdm_00_common____2004_buff_healer.macro,
            Macros.sdm_00_common____2001_buff_physics_dps.macro,
            Macros.sdm_05_shaman____0_common____14101_consumable.macro,
            Macros.sdm_05_shaman____0_common____14102_interrupt.macro,

            Macros.sdm_05_shaman____0_common____14112_resto_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____14113_enhancement_rotation_zhTW.macro,
            Macros.sdm_05_shaman____0_common____14114_mb_resto_earth_shield_zhTW.macro,

            Macros.sdm_05_shaman____1_elemental_resto____14311_buff_self_zhTW.macro,
            Macros.sdm_05_shaman____1_elemental_resto____14312_burst_zhTW.macro,
        ],
    )
    for macro in account_sdm_setup.macros:
        macro.set_char(name=character.character, realm=character.server)
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
        Macros.sdm_00_common____1011_MountUp_zhTW.macro,
        Macros.sdm_00_common____1012_MountDown_zhTW.macro,

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
