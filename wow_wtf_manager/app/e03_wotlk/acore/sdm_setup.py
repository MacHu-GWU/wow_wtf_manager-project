# -*- coding: utf-8 -*-

import typing as T
from wow_wtf_manager.exp.e03_wotlk.sdm import AccountSDMSetup, ClientSDMSetup

from .group import AccountEnum, AccountGroup, CharacterGroup
from .sdm_macro import Macros
from .form import dir_wow

accounts: T.List[AccountSDMSetup] = list()

# ------------------------------------------------------------------------------
# Global
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Character
# ------------------------------------------------------------------------------
# Balance Druid
for account in [
    AccountEnum.fat11,
    # AccountEnum.fat12,
    # AccountEnum.fat13,
]:
    account_sdm_setup = AccountSDMSetup(
        account=account,
        macros=[
            # Macros.sdm_00_common____01_respawn.macro
        ],
    )
    accounts.append(account_sdm_setup)

# for account in AccountGroup.ag_fat_01_to_25:
for account_sdm_setup in accounts:
    common_macros = [
        Macros.sdm_00_common____01_respawn.macro,
        Macros.sdm_00_common____02_feigh_death.macro,
        Macros.sdm_00_common____03_reset_cooldown.macro,
        Macros.sdm_00_common____04_ice_block.macro,
        Macros.sdm_00_common____05_resurrection.macro,
        Macros.sdm_00_common____06_invisibility.macro,
        Macros.sdm_00_common____07_reset.macro,
    ]
    account_sdm_setup.macros = common_macros + account_sdm_setup.macros

client_sdm_setup = ClientSDMSetup(
    dir_wow=dir_wow,
    accounts=accounts,
)
