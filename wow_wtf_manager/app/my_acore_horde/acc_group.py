# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from wow_wtf.api import get_values
from .acc_enum import AccountEnum, CharacterEnum


# ==============================================================================
# START of manual editing
# ==============================================================================
class AccountGroupEnum:
    all_accounts = get_values(AccountEnum)


class CharacterGroupEnum:
    all_characters = get_values(CharacterEnum)
    multiboxer_master_paladin = [
        CharacterEnum.rab01_AzerothCore_sa,
    ]
    multiboxer_master_non_paladin = []
    multiboxer_slave_paladin = []
    multiboxer_slave_non_paladin = (
        get_values(CharacterEnum)
        .difference(multiboxer_master_paladin)
        .difference(multiboxer_slave_paladin)
        .difference(multiboxer_slave_paladin)
    )

    warrior_and_dk = []
    non_warrior_and_dk = get_values(CharacterEnum).difference(warrior_and_dk)


# ==============================================================================
# END of manual editing
# ==============================================================================
