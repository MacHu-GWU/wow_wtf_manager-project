# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk import wtf
from wow_wtf_manager.paths import dir_project_root

dir_app = dir_project_root / "project" / "mop"
dir_01_game_client = dir_app / "01_game_client"
dir_11_account_user_interface = dir_app / "11_account_user_interface"
dir_12_account_macros = dir_app / "12_account_macros"
dir_13_account_saved_variables = dir_app / "13_account_saved_variables"
dir_21_character_user_interface = dir_app / "21_character_user_interface"
dir_22_character_chat = dir_app / "22_character_chat"
dir_23_character_keybindings = dir_app / "23_character_keybindings"
dir_24_character_layout = dir_app / "24_character_layout"
dir_25_character_addons = dir_app / "25_character_addons"
dir_26_character_macros = dir_app / "26_character_macros"
dir_27_character_saved_variables = dir_app / "27_character_saved_variables"


class WarmaneWTF:
    class GameClient:
        c01_2560_1400_high_graphic_sound = wtf.GameClientConfig(
            input_path=dir_01_game_client / "2560-1440-high-graphic-sound.txt"
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
        pass

    class CharacterSavedVariables:
        character_saved_variables = wtf.CharacterSavedVariablesConfig(
            input_path=dir_27_character_saved_variables
        )
