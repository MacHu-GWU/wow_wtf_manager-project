# -*- coding: utf-8 -*-

from .acc_dataset import ds


# fmt: off
class AccountEnum:
    husanhe = ds.accounts["husanhe"]
    rab01 = ds.accounts["rab01"]
    rab02 = ds.accounts["rab02"]
    rab03 = ds.accounts["rab03"]
    rab04 = ds.accounts["rab04"]
    rab05 = ds.accounts["rab05"]


class RealmEnum:
    husanhe_AzerothCore = ds.accounts["husanhe"].realms_mapper["AzerothCore"]
    rab01_AzerothCore = ds.accounts["rab01"].realms_mapper["AzerothCore"]
    rab02_AzerothCore = ds.accounts["rab02"].realms_mapper["AzerothCore"]
    rab03_AzerothCore = ds.accounts["rab03"].realms_mapper["AzerothCore"]
    rab04_AzerothCore = ds.accounts["rab04"].realms_mapper["AzerothCore"]
    rab05_AzerothCore = ds.accounts["rab05"].realms_mapper["AzerothCore"]


class CharacterEnum:
    husanhe_AzerothCore_shootingrab = ds.accounts["husanhe"].realms_mapper["AzerothCore"].characters_mapper["shootingrab"]
    husanhe_AzerothCore_fatbird = ds.accounts["husanhe"].realms_mapper["AzerothCore"].characters_mapper["fatbird"]
    rab01_AzerothCore_sa = ds.accounts["rab01"].realms_mapper["AzerothCore"].characters_mapper["sa"]
    rab02_AzerothCore_sb = ds.accounts["rab02"].realms_mapper["AzerothCore"].characters_mapper["sb"]
    rab03_AzerothCore_sc = ds.accounts["rab03"].realms_mapper["AzerothCore"].characters_mapper["sc"]
    rab04_AzerothCore_sd = ds.accounts["rab04"].realms_mapper["AzerothCore"].characters_mapper["sd"]
    rab05_AzerothCore_se = ds.accounts["rab05"].realms_mapper["AzerothCore"].characters_mapper["se"]
# fmt: on