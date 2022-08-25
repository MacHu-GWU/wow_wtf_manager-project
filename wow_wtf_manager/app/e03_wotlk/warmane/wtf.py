# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk import wtf
from wow_wtf_manager.paths import dir_project_root

dir_wow = Path(r"C:\Games\World of Warcraft")

dir_app = dir_project_root / "project" / "wotlk"
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

base_game_client_config = wtf.BaseGameClientConfig(dir_wow=dir_wow)


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
            input_path=dir_12_account_macros / "default.txt"
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

    class CharacterSavedVariables:
        character_saved_variables = wtf.CharacterSavedVariablesConfig(
            input_path=dir_27_character_saved_variables
        )
