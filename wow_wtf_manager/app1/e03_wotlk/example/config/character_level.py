# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk import api as wotlk
from .app_data import app_data


class CharacterUserInterfaceConfigEnum:
    default = wotlk.CharacterUserInterfaceConfig.new(
        app_data.dir_21_character_user_interface.joinpath("default.txt")
    )


class CharacterChatConfigEnum:
    default = wotlk.CharacterChatConfig.new(
        app_data.dir_22_character_chat.joinpath("default.txt")
    )


class CharacterKeybindingConfigEnum:
    default = wotlk.CharacterKeybindingConfig.new(
        app_data.dir_23_character_keybindings.joinpath("default.txt")
    )
    warrior_and_dk = wotlk.CharacterKeybindingConfig.new(
        app_data.dir_23_character_keybindings.joinpath("warrior-and-dk.txt")
    )


class CharacterLayoutConfigEnum:
    default = wotlk.CharacterLayoutConfig.new(
        app_data.dir_24_character_layout.joinpath("default.txt")
    )


class CharacterAddonsConfigEnum:
    mb_master_pala = wotlk.CharacterAddonConfig.new(
        app_data.dir_25_character_addons.joinpath("01-multiboxer-master-paladin.txt"),
    )
    mb_master_non_pala = wotlk.CharacterAddonConfig.new(
        app_data.dir_25_character_addons.joinpath(
            "02-multiboxer-master-non-paladin.txt"
        ),
    )
    mb_slave_pala = wotlk.CharacterAddonConfig.new(
        app_data.dir_25_character_addons.joinpath("03-multiboxer-slave-paladin.txt"),
    )
    mb_slave_non_pala = wotlk.CharacterAddonConfig.new(
        app_data.dir_25_character_addons.joinpath(
            "04-multiboxer-slave-non-paladin.txt"
        ),
    )


class CharacterSavedVariablesConfigGroup:
    all = [
        wotlk.CharacterSavedVariablesConfig.new(path)
        for path in app_data.dir_27_character_saved_variables.select_by_ext(".lua")
    ]
