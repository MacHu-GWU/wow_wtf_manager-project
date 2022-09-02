# -*- coding: utf-8 -*-

"""
枚举我在 Maocore 的各个服务器上拥有的所有 账号, 角色.
然后将其分组, 以便于我在 WtfForm 的设置中将其排列组合, 应用不同的设置.
"""

from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.group import Account, Character


# ==============================================================================
# Define Individual Account / Character
# ==============================================================================
class AccountEnum:
    fat01 = Account("Fat01")
    fat02 = Account("Fat02")
    fat03 = Account("Fat03")
    fat04 = Account("Fat04")
    fat05 = Account("Fat05")


class CharacterEnum:
    fat01_maocore_qsa = Character.from_string("Fat01.AzerothCore.Qsa")
    fat02_maocore_qsb = Character.from_string("Fat02.AzerothCore.Qsb")
    fat03_maocore_qsc = Character.from_string("Fat03.AzerothCore.Qsc")
    fat04_maocore_qsd = Character.from_string("Fat04.AzerothCore.Qsd")
    fat05_maocore_qse = Character.from_string("Fat05.AzerothCore.Qse")


# ==============================================================================
# Define Account / Character Groups
# ==============================================================================
class AccountGroup:
    """
    ``ag_`` stands for account group is the common prefix,
    can be used for search using PyCharm.
    """
    ag_all_account = OrderedSet([
        AccountEnum.fat01,
        AccountEnum.fat02,
        AccountEnum.fat03,
        AccountEnum.fat04,
        AccountEnum.fat05,
    ])


class CharacterGroup:
    """
    ``cg_`` stands for character group is the common prefix,
    can be used for search using PyCharm.
    """
    # --- Group by accounts
    cg_all_character = OrderedSet([
        CharacterEnum.fat01_maocore_qsa,
        CharacterEnum.fat02_maocore_qsb,
        CharacterEnum.fat03_maocore_qsc,
        CharacterEnum.fat04_maocore_qsd,
        CharacterEnum.fat05_maocore_qse,
    ])

    cg_paladin_prot_pve_and_retri_pve = OrderedSet([
        CharacterEnum.fat01_maocore_qsa,
    ])

    cg_paladin_retri_pve_and_prot_pve = OrderedSet([
        CharacterEnum.fat02_maocore_qsb,
        CharacterEnum.fat03_maocore_qsc,
        CharacterEnum.fat04_maocore_qsd,
    ])

    cg_paladin_holy_pve_and_retri_pve = OrderedSet([
        CharacterEnum.fat05_maocore_qse,
    ])


class AccountSavedVariableGroup:
    common_include_list = [
        "AtlasLoot",
        "Combuctor",
        "Dominos",
        "HealBot",
        "Mappy",
        "MobInfo2",
        "oCC",
        "Omen",
        "PallyPower",
        "Parrot",
        "Postal",
        "Quartz",
        "RatingBuster",
        "Skada",
        "SlideBar",
    ]
