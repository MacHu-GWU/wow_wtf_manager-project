# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from .enum import client, AccountEnum, CharacterEnum


class AccountGroupEnum:
    all = OrderedSet(
        [
            AccountEnum.husanhe,
        ]
    )


class CharacterGroupEnum:
    all = OrderedSet(
        [
            CharacterEnum.shootingrab,
        ]
    )

    master_pala = OrderedSet([])

    master_non_pala = OrderedSet(
        [
            CharacterEnum.shootingrab,
        ]
    )

    slave_pala = OrderedSet([])

    slave_non_pala = OrderedSet([])
