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
            CharacterEnum.fatbird,
            CharacterEnum.sa,
            CharacterEnum.sb,
            CharacterEnum.sc,
            CharacterEnum.sd,
            CharacterEnum.se,
        ]
    )

    master_pala = OrderedSet(
        [
            CharacterEnum.sa,
        ]
    )

    master_non_pala = OrderedSet(
        [
            CharacterEnum.shootingrab,
            CharacterEnum.fatbird,
        ]
    )

    slave_pala = OrderedSet([])

    slave_non_pala = OrderedSet(
        [
            CharacterEnum.sb,
            CharacterEnum.sc,
            CharacterEnum.sd,
            CharacterEnum.se,
        ]
    )
