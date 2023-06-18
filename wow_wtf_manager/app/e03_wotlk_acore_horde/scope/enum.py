# -*- coding: utf-8 -*-

from pathlib_mate import Path

from wow_wtf_manager.api import (
    IS_WINDOWS,
    Client,
    Account,
    Realm,
    Character,
)
from wow_wtf_manager.paths import dir_tests


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
    dir_wtf = dir_tests.joinpath("app", "e03_wotlk_acore_horde", "WTF-output")
    client = Client(locale="zhTW", dir_wtf=dir_wtf)


class AccountEnum:
    husanhe = Account.new("husanhe")


class RealmEnum:
    husanhe_acore = Realm.new(AccountEnum.husanhe, "AzerothCore")


class CharacterEnum:
    shootingrab = Character.new(RealmEnum.husanhe_acore, "shootingrab")
    fatbird = Character.new(RealmEnum.husanhe_acore, "fatbird")
