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
        # "World-of-Warcraft-3.3.5-zhTW",
        "World-of-Warcraft-3.3.5-zhCN", # 之所以选用 CN 是因为 azerothcore 的 CN 任务文本壁 TW 丰富, 有更好的游戏体验
        "WTF",
    )
    client = Client(locale="zhTW", dir_wtf=dir_wtf)
else:
    dir_wtf = dir_tests.joinpath("app", "e03_wotlk_acore_horde", "WTF-output")
    client = Client(locale="zhTW", dir_wtf=dir_wtf)


class AccountEnum:
    husanhe = Account.new("husanhe")
    rab01 = Account.new("rab01")
    rab02 = Account.new("rab02")
    rab03 = Account.new("rab03")
    rab04 = Account.new("rab04")
    rab05 = Account.new("rab05")


class RealmEnum:
    husanhe_acore = Realm.new(AccountEnum.husanhe, "AzerothCore")
    husanhe_rab01 = Realm.new(AccountEnum.rab01, "AzerothCore")
    husanhe_rab02 = Realm.new(AccountEnum.rab02, "AzerothCore")
    husanhe_rab03 = Realm.new(AccountEnum.rab03, "AzerothCore")
    husanhe_rab04 = Realm.new(AccountEnum.rab04, "AzerothCore")
    husanhe_rab05 = Realm.new(AccountEnum.rab05, "AzerothCore")


class CharacterEnum:
    shootingrab = Character.new(RealmEnum.husanhe_acore, "shootingrab")
    fatbird = Character.new(RealmEnum.husanhe_acore, "fatbird")

    sa = Character.new(RealmEnum.husanhe_rab01, "sa")
    sb = Character.new(RealmEnum.husanhe_rab02, "sb")
    sc = Character.new(RealmEnum.husanhe_rab03, "sc")
    sd = Character.new(RealmEnum.husanhe_rab04, "sd")
    se = Character.new(RealmEnum.husanhe_rab05, "se")
