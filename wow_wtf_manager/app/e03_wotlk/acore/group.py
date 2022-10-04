# -*- coding: utf-8 -*-

"""
枚举我在 Acore 的各个服务器上拥有的所有 账号, 角色.
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
    fat06 = Account("Fat06")
    fat07 = Account("Fat07")
    fat08 = Account("Fat08")
    fat09 = Account("Fat09")
    fat10 = Account("Fat10")
    fat11 = Account("Fat11")
    fat12 = Account("Fat12")
    fat13 = Account("Fat13")
    fat14 = Account("Fat14")
    fat15 = Account("Fat15")
    fat16 = Account("Fat16")
    fat17 = Account("Fat17")
    fat18 = Account("Fat18")
    fat19 = Account("Fat19")
    fat20 = Account("Fat20")
    fat21 = Account("Fat21")
    fat22 = Account("Fat22")
    fat23 = Account("Fat23")
    fat24 = Account("Fat24")
    fat25 = Account("Fat25")

class CharacterEnum:
    fat01_acore_ra = Character.from_string("Fat01.AzerothCore.Ra")
    fat02_acore_rb = Character.from_string("Fat02.AzerothCore.Rb")
    fat03_acore_rc = Character.from_string("Fat03.AzerothCore.Rc")
    fat04_acore_rd = Character.from_string("Fat04.AzerothCore.Rd")
    fat05_acore_re = Character.from_string("Fat05.AzerothCore.Re")
    fat06_acore_rf = Character.from_string("Fat06.AzerothCore.Rf")
    fat07_acore_rg = Character.from_string("Fat07.AzerothCore.Rg")
    fat08_acore_rh = Character.from_string("Fat08.AzerothCore.Rh")
    fat09_acore_ri = Character.from_string("Fat09.AzerothCore.Ri")
    fat10_acore_rj = Character.from_string("Fat10.AzerothCore.Rj")
    fat11_acore_rk = Character.from_string("Fat11.AzerothCore.Rk")
    fat12_acore_rl = Character.from_string("Fat12.AzerothCore.Rl")
    fat13_acore_rm = Character.from_string("Fat13.AzerothCore.Rm")
    fat14_acore_rn = Character.from_string("Fat14.AzerothCore.Rn")
    fat15_acore_ro = Character.from_string("Fat15.AzerothCore.Ro")
    fat16_acore_rp = Character.from_string("Fat16.AzerothCore.Rp")
    fat17_acore_rq = Character.from_string("Fat17.AzerothCore.Rq")
    fat18_acore_rr = Character.from_string("Fat18.AzerothCore.Rr")
    fat19_acore_rs = Character.from_string("Fat19.AzerothCore.Rs")
    fat20_acore_rt = Character.from_string("Fat20.AzerothCore.Rt")
    fat21_acore_ru = Character.from_string("Fat21.AzerothCore.Ru")
    fat22_acore_rv = Character.from_string("Fat22.AzerothCore.Rv")
    fat23_acore_rw = Character.from_string("Fat23.AzerothCore.Rw")
    fat24_acore_rx = Character.from_string("Fat24.AzerothCore.Rx")
    fat25_acore_ry = Character.from_string("Fat25.AzerothCore.Ry")


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
        AccountEnum.fat06,
        AccountEnum.fat07,
        AccountEnum.fat08,
        AccountEnum.fat09,
        AccountEnum.fat10,
        AccountEnum.fat11,
        AccountEnum.fat12,
        AccountEnum.fat13,
        AccountEnum.fat14,
        AccountEnum.fat15,
        AccountEnum.fat16,
        AccountEnum.fat17,
        AccountEnum.fat18,
        AccountEnum.fat19,
        AccountEnum.fat20,
        AccountEnum.fat21,
        AccountEnum.fat22,
        AccountEnum.fat23,
        AccountEnum.fat24,
        AccountEnum.fat25,
    ])

    ag_fat_01_to_10 = OrderedSet([
        AccountEnum.fat01,
        AccountEnum.fat02,
        AccountEnum.fat03,
        AccountEnum.fat04,
        AccountEnum.fat05,
        AccountEnum.fat06,
        AccountEnum.fat07,
        AccountEnum.fat08,
        AccountEnum.fat09,
        AccountEnum.fat10,
    ])

    ag_fat_11_to_25 = OrderedSet([
        AccountEnum.fat11,
        AccountEnum.fat12,
        AccountEnum.fat13,
        AccountEnum.fat14,
        AccountEnum.fat15,
        AccountEnum.fat16,
        AccountEnum.fat17,
        AccountEnum.fat18,
        AccountEnum.fat19,
        AccountEnum.fat20,
        AccountEnum.fat21,
        AccountEnum.fat22,
        AccountEnum.fat23,
        AccountEnum.fat24,
        AccountEnum.fat25,
    ])



class CharacterGroup:
    """
    ``cg_`` stands for character group is the common prefix,
    can be used for search using PyCharm.
    """
    # --- Group by accounts
    cg_all_character = OrderedSet([
        CharacterEnum.fat01_acore_ra,
        CharacterEnum.fat02_acore_rb,
        CharacterEnum.fat03_acore_rc,
        CharacterEnum.fat04_acore_rd,
        CharacterEnum.fat05_acore_re,
        CharacterEnum.fat06_acore_rf,
        CharacterEnum.fat07_acore_rg,
        CharacterEnum.fat08_acore_rh,
        CharacterEnum.fat09_acore_ri,
        CharacterEnum.fat10_acore_rj,
        CharacterEnum.fat11_acore_rk,
        CharacterEnum.fat12_acore_rl,
        CharacterEnum.fat13_acore_rm,
        CharacterEnum.fat14_acore_rn,
        CharacterEnum.fat15_acore_ro,
        CharacterEnum.fat16_acore_rp,
        CharacterEnum.fat17_acore_rq,
        CharacterEnum.fat18_acore_rr,
        CharacterEnum.fat19_acore_rs,
        CharacterEnum.fat20_acore_rt,
        CharacterEnum.fat21_acore_ru,
        CharacterEnum.fat22_acore_rv,
        CharacterEnum.fat23_acore_rw,
        CharacterEnum.fat24_acore_rx,
        CharacterEnum.fat25_acore_ry,
    ])

    cg_ra_to_rj = OrderedSet([
        CharacterEnum.fat01_acore_ra,
        CharacterEnum.fat02_acore_rb,
        CharacterEnum.fat03_acore_rc,
        CharacterEnum.fat04_acore_rd,
        CharacterEnum.fat05_acore_re,
        CharacterEnum.fat06_acore_rf,
        CharacterEnum.fat07_acore_rg,
        CharacterEnum.fat08_acore_rh,
        CharacterEnum.fat09_acore_ri,
        CharacterEnum.fat10_acore_rj,
    ])

    cg_rk_to_ry = OrderedSet([
        CharacterEnum.fat11_acore_rk,
        CharacterEnum.fat12_acore_rl,
        CharacterEnum.fat13_acore_rm,
        CharacterEnum.fat14_acore_rn,
        CharacterEnum.fat15_acore_ro,
        CharacterEnum.fat16_acore_rp,
        CharacterEnum.fat17_acore_rq,
        CharacterEnum.fat18_acore_rr,
        CharacterEnum.fat19_acore_rs,
        CharacterEnum.fat20_acore_rt,
        CharacterEnum.fat21_acore_ru,
        CharacterEnum.fat22_acore_rv,
        CharacterEnum.fat23_acore_rw,
        CharacterEnum.fat24_acore_rx,
        CharacterEnum.fat25_acore_ry,
    ])

    cg_paladin_prot_pve_and_retri_pve = OrderedSet([
        CharacterEnum.fat01_acore_ra,
    ])

    cg_shaman_element_pve_and_restore_pve = OrderedSet([
        CharacterEnum.fat02_acore_rb,
    ])

    cg_druid_balance_pve_and_bear_pve = OrderedSet([
        CharacterEnum.fat03_acore_rc,
    ])

    cg_mage_arcane_pve_and_fire_pve = OrderedSet([
        CharacterEnum.fat04_acore_rd,
    ])

    cg_priest_shadow_pve_and_holy_pve = OrderedSet([
        CharacterEnum.fat05_acore_re,
        CharacterEnum.fat19_acore_rs,
        CharacterEnum.fat20_acore_rt,
        CharacterEnum.fat21_acore_ru,
        CharacterEnum.fat22_acore_rv,
    ])

    cg_priest_shadow_pve_and_disco_pve = OrderedSet([
        CharacterEnum.fat14_acore_rn,
        CharacterEnum.fat15_acore_ro,
        CharacterEnum.fat16_acore_rp,
        CharacterEnum.fat17_acore_rq,
        CharacterEnum.fat25_acore_ry,
    ])

    cg_warlock_demon_pve_and_destruct_pve = OrderedSet([
        CharacterEnum.fat06_acore_rf,
    ])

    cg_hunter_marksman_pve_and_beast_pve = OrderedSet([
        CharacterEnum.fat07_acore_rg,
    ])

    cg_druid_resto_pve_and_balance_pve = OrderedSet([
        CharacterEnum.fat08_acore_rh,
    ])

    cg_paladin_holy_pve_and_retri_pve = OrderedSet([
        CharacterEnum.fat09_acore_ri,
    ])

    cg_dk_blood_tank_pve_and_unholy_dps_pve = OrderedSet([
        CharacterEnum.fat10_acore_rj,
    ])

    cg_druid_balance_pve_and_resto_pve = OrderedSet([
        CharacterEnum.fat11_acore_rk,
        CharacterEnum.fat12_acore_rl,
        CharacterEnum.fat13_acore_rm,
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
