# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.api import Setup

from .config import api as config
from .scope import api as scope

# ------------------------------------------------------------------------------
# game_client
# ------------------------------------------------------------------------------
game_client = config.ClientConfigEnum.r_3840_2160_max


# ------------------------------------------------------------------------------
# account_user_interface
# ------------------------------------------------------------------------------
account_user_interface = [
    (config.AccountUserInterfaceConfigEnum.default, account)
    for account in scope.AccountGroupEnum.all
]

# ------------------------------------------------------------------------------
# account_saved_variables
# ------------------------------------------------------------------------------
account_saved_variables = []
for account in scope.AccountGroupEnum.all:
    for account_saved_variables_config in config.AccountSavedVariablesConfigGroup.all:
        account_saved_variables.append((account_saved_variables_config, account))

# ------------------------------------------------------------------------------
# character_user_interface
# ------------------------------------------------------------------------------
character_user_interface = [
    (config.CharacterUserInterfaceConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]

# ------------------------------------------------------------------------------
# character_chat
# ------------------------------------------------------------------------------
character_chat = [
    (config.CharacterChatConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]

# ------------------------------------------------------------------------------
# character_keybinding
# ------------------------------------------------------------------------------
character_keybinding = [
    (config.CharacterKeybindingConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]

# ------------------------------------------------------------------------------
# character_layout
# ------------------------------------------------------------------------------
character_layout = [
    (config.CharacterLayoutConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]

# ------------------------------------------------------------------------------
# character_addons
# ------------------------------------------------------------------------------
character_addons = []
character_addons.extend(
    [
        (config.CharacterAddonsConfigEnum.mb_master_pala, character)
        for character in scope.CharacterGroupEnum.master_pala
    ]
)
character_addons.extend(
    [
        (config.CharacterAddonsConfigEnum.mb_master_non_pala, character)
        for character in scope.CharacterGroupEnum.master_non_pala
    ]
)
character_addons.extend(
    [
        (config.CharacterAddonsConfigEnum.mb_slave_pala, character)
        for character in scope.CharacterGroupEnum.slave_pala
    ]
)
character_addons.extend(
    [
        (config.CharacterAddonsConfigEnum.mb_slave_non_pala, character)
        for character in scope.CharacterGroupEnum.slave_non_pala
    ]
)

# ------------------------------------------------------------------------------
# character_saved_variables
# ------------------------------------------------------------------------------
character_saved_variables = []
for character in scope.CharacterGroupEnum.all:
    for (
        character_saved_variables_config
    ) in config.CharacterSavedVariablesConfigGroup.all:
        character_saved_variables.append((character_saved_variables_config, character))

# ------------------------------------------------------------------------------
# setup
# ------------------------------------------------------------------------------
setup = Setup(
    client=scope.client,
    game_client=game_client,
    account_user_interface=account_user_interface,
    account_saved_variables=account_saved_variables,
    character_user_interface=character_user_interface,
    character_chat=character_chat,
    character_keybinding=character_keybinding,
    character_layout=character_layout,
    character_addons=character_addons,
    character_saved_variables=character_saved_variables,
)
