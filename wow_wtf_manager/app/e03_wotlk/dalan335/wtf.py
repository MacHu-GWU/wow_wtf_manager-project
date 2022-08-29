# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk import wtf
from wow_wtf_manager.paths import dir_wotlk_dalan335_project

dir_01_game_client = dir_wotlk_dalan335_project / "01_game_client"
dir_11_account_user_interface = dir_wotlk_dalan335_project / "11_account_user_interface"
dir_12_account_macros = dir_wotlk_dalan335_project / "12_account_macros"
dir_13_account_saved_variables = dir_wotlk_dalan335_project / "13_account_saved_variables"
dir_21_character_user_interface = dir_wotlk_dalan335_project / "21_character_user_interface"
dir_22_character_chat = dir_wotlk_dalan335_project / "22_character_chat"
dir_23_character_keybindings = dir_wotlk_dalan335_project / "23_character_keybindings"
dir_24_character_layout = dir_wotlk_dalan335_project / "24_character_layout"
dir_25_character_addons = dir_wotlk_dalan335_project / "25_character_addons"
dir_26_character_macros = dir_wotlk_dalan335_project / "26_character_macros"
dir_27_character_saved_variables = dir_wotlk_dalan335_project / "27_character_saved_variables"


class WarmaneWTF:
    class GameClient:
        c01_1920_1080_max = wtf.GameClientConfig(
            input_path=dir_01_game_client / "1920-1080-max-graphic-sound.txt"
        )
        c2_1920_1080_minimal = wtf.GameClientConfig(
            input_path=dir_01_game_client / "1920-1080-minimal-graphic-sound.txt"
        )
        c3_1600_900_minimal = wtf.GameClientConfig(
            input_path=dir_01_game_client / "1600-900-minimal-graphic-sound.txt"
        )
        c4_1176_664_minimal = wtf.GameClientConfig(
            input_path=dir_01_game_client / "1176-664-minimal-graphic-sound.txt"
        )

    class AccountUserInterface:
        default = wtf.AccountUserInterfaceConfig(
            input_path=dir_11_account_user_interface / "default.txt"
        )

    class AccountMacros:
        default = wtf.AccountMacroConfig(
            input_path=dir_12_account_macros / "default.txt"
        )

    class AccountSavedVariables:
        account_saved_variables = wtf.AccountSavedVariablesConfig(
            input_path=dir_13_account_saved_variables
        )

    class CharacterUserInterface:
        default = wtf.CharacterUserInterfaceConfig(
            input_path=dir_21_character_user_interface / "default.txt"
        )

    class CharacterChat:
        default = wtf.CharacterChatConfig(
            input_path=dir_22_character_chat / "default.txt"
        )

    class CharacterKeybinding:
        default = wtf.CharacterKeybindingConfig(
            input_path=dir_23_character_keybindings / "default.txt"
        )
        warrior_and_dk = wtf.CharacterKeybindingConfig(
            input_path=dir_23_character_keybindings / "warrior-and-dk.txt"
        )

    class CharacterLayout:
        default = wtf.CharacterLayoutConfig(
            input_path=dir_24_character_layout / "default.txt"
        )

    class CharacterAddons:
        multibox_minimal = wtf.CharacterAddonConfig(
            input_path=dir_25_character_addons / "05-multibox-minimal.txt"
        )

    class CharacterMacros:
        paladin_prot_pve_and_retri_pve_lv80 = wtf.CharacterMacroConfig(
            input_path=dir_26_character_macros / "paladin-prot-pve-and-retri-pve-lv80.txt"
        )
        paladin_retri_pve_and_prot_pve_lv80 = wtf.CharacterMacroConfig(
            input_path=dir_26_character_macros / "paladin-bcd-retri-pve-and-prot-pve-lv80.txt"
        )
        paladin_holy_pve_and_retri_pve_lv80 = wtf.CharacterMacroConfig(
            input_path=dir_26_character_macros / "paladin-holy-pve-and-retri-pve-lv80.txt"
        )

    class CharacterSavedVariables:
        character_saved_variables = wtf.CharacterSavedVariablesConfig(
            input_path=dir_27_character_saved_variables
        )
