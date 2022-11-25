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
            Macros.sdm_02_paladin____1_protect_retri____11305_rotation_zhTW.macro,
            Macros.sdm_02_paladin____1_protect_retri____11311_buff_self_alliance_zhTW.macro,
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
