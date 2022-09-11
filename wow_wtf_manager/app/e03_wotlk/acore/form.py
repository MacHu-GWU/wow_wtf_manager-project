# -*- coding: utf-8 -*-

from pathlib_mate import Path
from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.form import WtfForm
from wow_wtf_manager.exp.e03_wotlk.macro import apply_macros_cache_txt

from .wtf import WarmaneWTF
from .group import (
    AccountEnum,
    CharacterEnum,
    AccountGroup,
    CharacterGroup,
    AccountSavedVariableGroup,
)

warmane_wtf_form = WtfForm(
    dir_wow=Path(r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-zhCN"),
    game_client_config=WarmaneWTF.GameClient.c01_1920_1080_max,
    # game_client_config=WarmaneWTF.GameClient.c2_1920_1080_minimal,
    all_characters=CharacterGroup.cg_all_character,
    account_user_interface_config=[
        (
            WarmaneWTF.AccountUserInterface.default,
            AccountGroup.ag_all_account,
        )
    ],
    account_macro_config=[
        (
            WarmaneWTF.AccountMacros.default,
            AccountGroup.ag_all_account,
        )
    ],
    account_saved_variables_config=[
        (
            WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
                include_list=AccountSavedVariableGroup.common_include_list + [
                    # "SuperDuperMacro_paladin_holy_pve_and_retri_pve"
                ]
            ),
            AccountGroup.ag_all_account,
        )
        # (
        #     WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
        #         include_list=AccountSavedVariableGroup.common_include_list + [
        #             # "SuperDuperMacro_paladin_prot_pve_and_retri_pve"
        #         ]
        #     ),
        #     OrderedSet([
        #         AccountEnum.fat01,
        #     ])
        # ),
        # (
        #     WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
        #         include_list=AccountSavedVariableGroup.common_include_list + [
        #             # "SuperDuperMacro_paladin_retri_pve_and_prot_pve"
        #         ]
        #     ),
        #     OrderedSet([
        #         AccountEnum.fat02,
        #         AccountEnum.fat03,
        #         AccountEnum.fat04,
        #     ])
        # ),
        # (
        #     WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
        #         include_list=AccountSavedVariableGroup.common_include_list + [
        #             # "SuperDuperMacro_paladin_holy_pve_and_retri_pve"
        #         ]
        #     ),
        #     OrderedSet([
        #         AccountEnum.fat05,
        #     ])
        # )
    ],
    character_user_interface_config=[
        (
            WarmaneWTF.CharacterUserInterface.default,
            CharacterGroup.cg_all_character,
        )
    ],
    character_chat_config=[
        (
            WarmaneWTF.CharacterChat.default,
            CharacterGroup.cg_all_character,
        )
    ],
    character_keybinding_config=[
        (
            WarmaneWTF.CharacterKeybinding.default,
            CharacterGroup.cg_all_character,
        )
    ],
    character_layout_config=[
        (
            WarmaneWTF.CharacterLayout.default,
            CharacterGroup.cg_all_character,
        )
    ],
    character_addon_config=[
        (
            WarmaneWTF.CharacterAddons.multibox_minimal,
            CharacterGroup.cg_all_character,
        )
    ],
    character_macro_config=[
        (
            WarmaneWTF.CharacterMacros.paladin_prot_pve_and_retri_pve_lv80,
            CharacterGroup.cg_paladin_prot_pve_and_retri_pve,
        ),
    ],
    character_saved_variables_config=[
        (
            WarmaneWTF.CharacterSavedVariables.character_saved_variables.evolve(
                exclude_list=[
                ],
            ),
            CharacterGroup.cg_all_character,
        )
    ],
    apply_macros_cache_txt=apply_macros_cache_txt,
)
