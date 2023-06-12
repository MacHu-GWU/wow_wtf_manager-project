# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk import api as wotlk
from .app_data import app_data


class AccountUserInterfaceConfigEnum:
    default = wotlk.AccountUserInterfaceConfig.new(
        app_data.dir_11_account_user_interface.joinpath("default.txt")
    )


class AccountSavedVariablesConfigGroup:
    all = [
        wotlk.AccountSavedVariablesConfig.new(path)
        for path in app_data.dir_13_account_saved_variables.select_by_ext(".lua")
    ]
