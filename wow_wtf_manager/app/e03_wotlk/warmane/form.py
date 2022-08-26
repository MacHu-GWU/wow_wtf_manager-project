# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk.form import WtfForm
from wow_wtf_manager.exp.e03_wotlk.macro import apply_macros_cache_txt

from .wtf import WarmaneWTF
from .group import AccountGroup, CharacterGroup

warmane_wtf_form = WtfForm(
    dir_wow=Path(r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-enUS-Warmane"),
    game_client_config=WarmaneWTF.GameClient.c3_1600_900_minimal,
    all_characters=CharacterGroup.cg_all_character,
    account_user_interface_config=[
        (
            WarmaneWTF.AccountUserInterface.default,
            AccountGroup.ag_fatmulti_1_to_5,
        )
    ],
    account_macro_config=[
        (
            WarmaneWTF.AccountMacros.default,
            AccountGroup.ag_fatmulti_1_to_5,
        )
    ],
    account_saved_variables_config=[
        (
            WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
                exclude_list=[
                ],
            ),
            AccountGroup.ag_fatmulti_1_to_5,
        )
    ],
    character_user_interface_config=[
        (
            WarmaneWTF.CharacterUserInterface.default,
            CharacterGroup.cg_test,
        )
    ],
    character_chat_config=[
        (
            WarmaneWTF.CharacterChat.default,
            CharacterGroup.cg_test,
        )
    ],
    character_keybinding_config=[
        (
            WarmaneWTF.CharacterKeybinding.default,
            CharacterGroup.cg_test,
        )
    ],
    character_layout_config=[
        (
            WarmaneWTF.CharacterLayout.default,
            CharacterGroup.cg_test,
        )
    ],
    character_addon_config=[
        (
            WarmaneWTF.CharacterAddons.multibox_minimal,
            CharacterGroup.cg_test,
        )
    ],
    character_macro_config=[
        (
            WarmaneWTF.CharacterMacros.paladin_prot_pve_and_retri_pve_lv80,
            CharacterGroup.cg_class_paladin_prot_pve_and_retri_pve,
        ),
        (
            WarmaneWTF.CharacterMacros.paladin_retri_pve_and_prot_pve_lv80,
            CharacterGroup.cg_class_paladin_retri_pve_and_prot_pve,
        ),
        (
            WarmaneWTF.CharacterMacros.paladin_holy_pve_and_retri_pve_lv80,
            CharacterGroup.cg_class_paladin_holy_pve_and_retri_pve,
        ),
    ],
    character_saved_variables_config=[
        (
            WarmaneWTF.CharacterSavedVariables.character_saved_variables.evolve(
                exclude_list=[
                ],
            ),
            CharacterGroup.cg_test,
        )
    ],
    apply_macros_cache_txt=apply_macros_cache_txt,
)
