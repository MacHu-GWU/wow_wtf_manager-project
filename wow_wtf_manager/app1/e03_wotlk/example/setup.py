# -*- coding: utf-8 -*-

import typing as T
import attr
from ordered_set import OrderedSet

# from wow_wtf_manager.api import BaseConfig, BaseScope
# from wow_wtf_manager.paths import dir_project_root
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


setup = Setup(
    client=scope.client,
    game_client=game_client,
    account_user_interface=account_user_interface,
    account_saved_variables=account_saved_variables,
)
