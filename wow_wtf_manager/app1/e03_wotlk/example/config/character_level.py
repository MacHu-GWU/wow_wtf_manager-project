# -*- coding: utf-8 -*-

from wow_wtf_manager.config.file_config import AccountUserInterfaceConfig
from wow_wtf_manager.paths import dir_project_root

dir_root = dir_project_root.joinpath("e03_wotlk_acore")
dir_account_user_interface = dir_root.joinpath("11_account_user_interface")


class AccountUserInterfaceConfigEnum:
    default = AccountUserInterfaceConfig(dir_account_user_interface.joinpath("default"))


if __name__ == "__main__":
    print(AccountUserInterfaceConfigEnum.default.build())
    pass