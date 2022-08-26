# -*- coding: utf-8 -*-

"""
枚举我在 Tauri 的各个服务器上拥有的所有 账号, 角色.
然后将其分组, 以便于我在 WtfForm 的设置中将其排列组合, 应用不同的设置.
"""

from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.group import Account, Character

# ==============================================================================
# Define Individual Account / Character
# ==============================================================================
# All Account
fatmulti1 = Account("fatmulti1")
fatmulti2 = Account("fatmulti2")
fatmulti3 = Account("fatmulti3")
fatmulti4 = Account("fatmulti4")
fatmulti5 = Account("fatmulti5")

# All Characters
# ------------------------------------------------------------------------------
# Icecrown Server
# ------------------------------------------------------------------------------
Fatmulti1_Evermoon_Carrotflower = Character.from_string("Fatmulti1.[EN] Evermoon.Carrotflower")
Fatmulti2_Evermoon_Carrotroot = Character.from_string("Fatmulti2.[EN] Evermoon.Carrotroot")
Fatmulti3_Evermoon_Carrotstem = Character.from_string("Famulti3.[EN] Evermoon.Carrotstem")
Fatmulti4_Evermoon_Carrotleaf = Character.from_string("Fatmulti4.[EN] Evermoon.Carrotleaf")
Fatmulti5_Evermoon_Carrotseed = Character.from_string("Fatmulti5.[EN] Evermoon.Carrotseed")


# ==============================================================================
# Define Account / Character Groups
# ==============================================================================
class AccountGroup:
    """
    ``ag_`` stands for account group is the common prefix,
    can be used for search using PyCharm.
    """
    ag_all_account = OrderedSet([
        fatmulti1,
        fatmulti2,
        fatmulti3,
        fatmulti4,
        fatmulti5,
    ])


class CharacterGroup:
    """
    ``cg_`` stands for character group is the common prefix,
    can be used for search using PyCharm.
    """
    # --- Group by accounts
    cg_account_fatmulti_1_to_5 = OrderedSet([
        Fatmulti1_Evermoon_Carrotflower,
        Fatmulti2_Evermoon_Carrotroot,
        Fatmulti3_Evermoon_Carrotstem,
        Fatmulti4_Evermoon_Carrotleaf,
        Fatmulti5_Evermoon_Carrotseed,
    ])
