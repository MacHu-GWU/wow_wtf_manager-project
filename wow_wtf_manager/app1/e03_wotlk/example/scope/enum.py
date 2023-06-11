# -*- coding: utf-8 -*-

from pathlib_mate import Path

from wow_wtf_manager.api import (
    IS_WINDOWS,
    Client,
    Account,
    Realm,
    Character,
)
from wow_wtf_manager.paths import dir_tests_int


if IS_WINDOWS:  # pragma: no cover
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
    dir_wtf = dir_tests_int.joinpath("app1", "e03_wotlk_acore", "WTF-output")
    client = Client(locale="zhTW", dir_wtf=dir_wtf)


class AccountEnum:
    wtf1 = Account.new("wtfmanager1")
    wtf2 = Account.new("wtfmanager2")


class RealmEnum:
    wtf1_acore = Realm.new(AccountEnum.wtf1, "AzerothCore")
    wtf2_acore = Realm.new(AccountEnum.wtf2, "AzerothCore")


class CharacterEnum:
    wtfaa = Character.new(RealmEnum.wtf1_acore, "wtfaa")
    wtfab = Character.new(RealmEnum.wtf1_acore, "wtfab")
    wtfba = Character.new(RealmEnum.wtf2_acore, "wtfba")
    wtfbb = Character.new(RealmEnum.wtf2_acore, "wtfbb")
