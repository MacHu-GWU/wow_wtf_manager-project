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
    """
    对角色进行分组, 通常会有以下五个分组:

    - all: 所有角色
    - master_pala: 多开中带队的司机圣骑士角色. 之所以要区别对待是因为多开中司机和非司机角色需要
        开启的插件区别很大.
    - master_non_pala: 多开中带队的司机角色, 但不是圣骑士, 通常是坦克, 也可能是皮糙肉厚的角色, 例如术士.
    - slave_pala: 多开中的跟随者圣骑士角色. 之所以要区别对待是因为圣骑士有专用插件.
    - slave_non_pala: 多开中的跟随者非圣骑士角色.
    """
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
