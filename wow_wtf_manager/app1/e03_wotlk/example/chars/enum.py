# -*- coding: utf-8 -*-

"""
枚举所有的:

- 客户端
- 账户
- 服务器
- 角色
"""

from pathlib_mate import Path

from wow_wtf_manager.api import (
    IS_WINDOWS,
    Client,
    Account,
    Realm,
    Character,
)
from wow_wtf_manager.paths import dir_tests_int


if IS_WINDOWS:
    dir_wtf = Path.home().joinpath(
        "Documents",
        "Games",
        "WoW-Root",
        "Client",
        "World-of-Warcraft-3.3.5-zhTW",
        "WTF",
    )
    client = Client(locale="zhTW", dir_wtf=dir_wtf)
else:
    dir_wtf = dir_tests_int.joinpath("app1", "e03_wotlk_acore", "WTF")
    client = Client(locale="zhTW", dir_wtf=dir_wtf)


class AccountEnum:
    wft1 = Account.new("wftmanager1")
    wft2 = Account.new("wftmanager2")


class RealmEnum:
    wft1_acore = Realm.new(AccountEnum.wft1, "AzerothCore")
    wft2_acore = Realm.new(AccountEnum.wft2, "AzerothCore")


class CharacterEnum:
    wftaa = Character.new(RealmEnum.wft1_acore, "wftaa")
    wftab = Character.new(RealmEnum.wft1_acore, "wftab")
    wftba = Character.new(RealmEnum.wft2_acore, "wftba")
    wftbb = Character.new(RealmEnum.wft2_acore, "wftbb")
