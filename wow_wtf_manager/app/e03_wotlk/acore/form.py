# -*- coding: utf-8 -*-

"""
Acore 客户端的 WTF 配置的具体定义.
"""

from pathlib_mate import Path
from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.form import WtfForm

from .wtf import WarmaneWTF
from .group import (
    AccountEnum,
    CharacterEnum,
    AccountGroup,
    CharacterGroup,
    SavedVariableEnum,
    AccountSavedVariableGroup,
)

# 之所以用台服客户端是因为国服客户端不支持 PGR BOT 程序
dir_wow = Path(r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-zhTW")

acore_wtf_form = WtfForm(
    dir_wow=dir_wow,
    game_client_config=WarmaneWTF.GameClient.c5_3840_2160_max,
    all_characters=CharacterGroup.cg_all_character,
)

__account_user_interface = None
acore_wtf_form.account_user_interface_config = [
    (
        WarmaneWTF.AccountUserInterface.default,
        AccountGroup.ag_all_account,
    )
]

__account_macro = None
acore_wtf_form.account_macro_config = [
    (
        WarmaneWTF.AccountMacros.default,
        AccountGroup.ag_all_account,
    )
]

__account_saved_variables = None
acore_wtf_form.account_saved_variables_config = [
    (
        WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
            include_list=OrderedSet.union(
                AccountSavedVariableGroup.common_include_list,
            )
        ),
        # AccountGroup.ag_all_account,
        # AccountGroup.ag_fat_11_to_25,
        AccountGroup.ag_rab_01_to_05,
    )
]

__character_user_interface = None
acore_wtf_form.character_user_interface_config = [
    (
        WarmaneWTF.CharacterUserInterface.default,
        CharacterGroup.cg_all_character,
    )
]

__character_chat = None
acore_wtf_form.character_chat_config = [
    (
        WarmaneWTF.CharacterChat.default,
        CharacterGroup.cg_all_character,
    )
]

__character_keybinding = None
acore_wtf_form.character_keybinding_config = [
    (
        WarmaneWTF.CharacterKeybinding.default,
        CharacterGroup.cg_non_warrior_and_dk,
    ),
    (
        WarmaneWTF.CharacterKeybinding.warrior_and_dk,
        CharacterGroup.cg_warrior_and_dk,
    )
]

__character_addon = None
acore_wtf_form.character_addon_config = [
    (
        WarmaneWTF.CharacterAddons.multiboxer_master_paladin,
        CharacterGroup.cg_multibox_master_paladin,
    ),
    (
        WarmaneWTF.CharacterAddons.multiboxer_master_non_paladin,
        CharacterGroup.cg_multibox_master_non_paladin,
    ),
    (
        WarmaneWTF.CharacterAddons.multiboxer_slave_paladin,
        CharacterGroup.cg_multibox_slave_paladin,
    ),
    (
        WarmaneWTF.CharacterAddons.multiboxer_slave_non_paladin,
        CharacterGroup.cg_multibox_slave_non_paladin,
    ),
]

__character_layout = None
acore_wtf_form.character_layout_config = [
    (
        WarmaneWTF.CharacterLayout.default,
        CharacterGroup.cg_all_character,
    ),
]

__character_macro = None
acore_wtf_form.character_macro_config = [
    (
        WarmaneWTF.CharacterMacros.paladin_prot_pve_and_retri_pve_lv80,
        CharacterGroup.cg_paladin_prot_pve_and_retri_pve,
    ),
]

__character_saved_variables = None
acore_wtf_form.character_saved_variables_config = [
    (
        WarmaneWTF.CharacterSavedVariables.character_saved_variables.evolve(
            exclude_list=[
            ],
        ),
        # CharacterGroup.cg_all_character,
        # CharacterGroup.cg_rk_to_ry,
        CharacterGroup.cg_sa_to_se,
    )
]

acore_wtf_form.__attrs_post_init__()
