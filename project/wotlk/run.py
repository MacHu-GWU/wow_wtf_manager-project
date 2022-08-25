# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk.asso import Asso, WtfForm
from wow_wtf_manager.app.e03_wotlk.warmane.wtf import WarmaneWTF
from wow_wtf_manager.app.e03_wotlk.warmane.group import WarmaneGroup

warmane_wtf_form = WtfForm(
    dir_wow=Path(r"/Users/sanhehu/Documents/GitHub/wow_wtf_manager-project/project/wotlk/world-of-warcraft"),
    associations=[
        # ----------------------------------------------------------------------
        # Game Client
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.GameClient.c3_1600_900_minimal,
            WarmaneGroup.cg_all_character,
        ),

        # ----------------------------------------------------------------------
        # Account User Interface
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.AccountUserInterface.default,
            WarmaneGroup.cg_all_character,
        ),
        # ----------------------------------------------------------------------
        # Account Macros
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.AccountMacros.default,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Account SavedVariables
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.AccountSavedVariables.account_saved_variables.evolve(
                exclude_list=[

                ],
            ),
            WarmaneGroup.cg_test,
        ),

        # ----------------------------------------------------------------------
        # Character User Interface
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterUserInterface.default,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Character Chat
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterChat.default,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Character Keybinding
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterKeybinding.default,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Character Layout
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterLayout.default,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Character Addons
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterAddons.multibox_minimal,
            WarmaneGroup.cg_test,
        ),
        # ----------------------------------------------------------------------
        # Character Macros
        # ----------------------------------------------------------------------
        # ----------------------------------------------------------------------
        # Character Saved Variables
        # ----------------------------------------------------------------------
        Asso(
            WarmaneWTF.CharacterSavedVariables.character_saved_variables.evolve(
            ),
            WarmaneGroup.cg_test,
        ),
    ]
)
# warmane_wtf_form.plan()
warmane_wtf_form.apply()
