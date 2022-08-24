# -*- coding: utf-8 -*-

"""
这个模块是主要是实现了对 游戏角色的 抽象.
"""

import typing as T
import functools

import attr
from attrs_mate import AttrsClass
from ordered_set import OrderedSet


def titleize(s: str) -> str:
    return s[0].upper() + s[1:].lower()


def right_zfill(s: str) -> str:
    return s + "0" * (20 - len(s))


@functools.total_ordering
@attr.s(frozen=True, order=False)
class Character(AttrsClass):
    """
    代表着一个具体的游戏角色. 一个角色是唯一的, 也是可排序的. 一个角色的 Key 在
    ``sort_key`` 的方法中被定义. 同时我们也提供了一个工厂函数, 方便开发者从形如
    ``account.server.character`` 的字符串创建对象.
    """
    account: str = attr.ib(converter=titleize)
    server: str = attr.ib(converter=titleize)
    character: str = attr.ib(converter=titleize)

    @classmethod
    def from_string(cls, s: str) -> 'Character':
        """
        A factory class that create object "Account.Server.Name"
        """
        return cls(*s.split("."))

    @property
    def sort_key(self) -> str:
        return f"{right_zfill(self.account)}.{right_zfill(self.server)}.{right_zfill(self.character)}"

    def __gt__(self, other: 'Character'):
        return self.sort_key > other.sort_key

    def __eq__(self, other: 'Character'):
        return self.sort_key == other.sort_key


@attr.s
class CharacterGroup(AttrsClass):
    """
    代表着多个游戏角色的集合. 成员可以是 "游戏角色", 也可以是 "游戏角色组" 本身.
    由 ``char_list`` 方法来对里面的 "游戏角色" 成员进行遍历. 它本身支持集合中的
    交, 并, 补 操作.
    """
    char_or_group_list: T.List[T.Union[Character, 'CharacterGroup']] = attr.ib(factory=list)

    @property
    def char_list(self) -> T.List[Character]:
        char_set = OrderedSet()
        for item in self.char_or_group_list:
            if isinstance(item, Character):
                char_set.add(item)
            else:
                for char in item.char_list:
                    char_set.add(char)
        char_list = list(char_set)
        char_list.sort()
        return char_list

    @classmethod
    def union(cls, *groups: 'CharacterGroup') -> 'CharacterGroup':
        l = list(OrderedSet.union(*[group.char_list for group in groups]))
        l.sort()
        return cls(char_or_group_list=l)

    @classmethod
    def intersect(cls, *groups: 'CharacterGroup') -> 'CharacterGroup':
        l = list(OrderedSet.intersection(*[group.char_list for group in groups]))
        l.sort()
        return cls(char_or_group_list=l)

    @classmethod
    def difference(cls, *groups: 'CharacterGroup') -> 'CharacterGroup':
        l = list(OrderedSet.difference(*[group.char_list for group in groups]))
        l.sort()
        return cls(char_or_group_list=l)
