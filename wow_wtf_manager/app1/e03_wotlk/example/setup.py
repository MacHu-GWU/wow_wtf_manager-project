# -*- coding: utf-8 -*-

import typing as T

from wow_wtf_manager.exp.e03_wotlk.api import Setup

from .config import api as config
from .scope import api as scope

game_client = config.ClientConfigEnum.r_1920_1080_max

account_user_interface = [
    (config.AccountUserInterfaceConfigEnum.default, account)
    for account in scope.AccountGroupEnum.all
]

account_saved_variables = []
for account_saved_variables_config in config.AccountSavedVariablesConfigGroup.all:
    for account in scope.AccountGroupEnum.all:
        account_saved_variables.append((account_saved_variables_config, account))

character_user_interface = [
    (config.CharacterUserInterfaceConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]

character_chat = [
    (config.CharacterChatConfigEnum.default, character)
    for character in scope.CharacterGroupEnum.all
]


setup = Setup(
    client=scope.client,
    game_client=game_client,
    account_user_interface=account_user_interface,
    account_saved_variables=account_saved_variables,
    character_user_interface=character_user_interface,
    character_chat=character_chat,
)
