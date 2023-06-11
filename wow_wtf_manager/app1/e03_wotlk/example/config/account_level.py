# -*- coding: utf-8 -*-

from wow_wtf_manager.config.file_config import AccountUserInterfaceConfig

from .app_data import app_data


class AccountUserInterfaceConfigEnum:
    default = AccountUserInterfaceConfig.new(app_data.dir_11_account_user_interface.joinpath("default"))
