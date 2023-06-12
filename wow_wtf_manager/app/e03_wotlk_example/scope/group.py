# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from .enum import client, AccountEnum, CharacterEnum


class AccountGroupEnum:
    all = OrderedSet(
        [
            AccountEnum.wtf1,
            AccountEnum.wtf2,
        ]
    )


class CharacterGroupEnum:
    all = OrderedSet(
        [
            CharacterEnum.wtfaa,
            CharacterEnum.wtfab,
            CharacterEnum.wtfba,
            CharacterEnum.wtfbb,
        ]
    )

    master_pala = OrderedSet(
        [
            CharacterEnum.wtfaa,
        ]
    )

    master_non_pala = OrderedSet([])

    slave_pala = OrderedSet([])

    slave_non_pala = OrderedSet(
        [
            CharacterEnum.wtfab,
            CharacterEnum.wtfba,
            CharacterEnum.wtfbb,
        ]
    )
