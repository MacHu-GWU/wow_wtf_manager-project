# -*- coding: utf-8 -*-

from pathlib_mate import Path
from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.form import WtfForm
from wow_wtf_manager.app.e03_wotlk.warmane.wtf import WarmaneWTF
from wow_wtf_manager.app.e03_wotlk.warmane.group import AccountGroup, CharacterGroup

warmane_wtf_form = WtfForm(
    dir_wow=Path(r"/Users/sanhehu/Documents/GitHub/wow_wtf_manager-project/project/wotlk/world-of-warcraft"),
    game_client_config=WarmaneWTF.GameClient.c3_1600_900_minimal,
    account_user_interface_config=[
        (
            WarmaneWTF.AccountUserInterface.default,
            AccountGroup.ag_fatmulti_1_to_5,
        )
    ],
    account_macro_config=[
        (
            WarmaneWTF.AccountMacros.default,
            CharacterGroup.cg_test,
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
)
# warmane_wtf_form.plan()
warmane_wtf_form.apply()
