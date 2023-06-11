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
