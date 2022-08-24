# -*- coding: utf-8 -*-

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
    account: str = attr.ib(converter=titleize)
    server: str = attr.ib(converter=titleize)
    name: str = attr.ib(converter=titleize)

    @classmethod
    def from_string(cls, s: str) -> 'Character':
        """
        A factory class that create object "Account.Server.Name"
        """
        return cls(*s.split("."))

    @property
    def sort_key(self) -> str:
        return f"{right_zfill(self.account)}.{right_zfill(self.server)}.{right_zfill(self.name)}"

    def __gt__(self, other: 'Character'):
        return self.sort_key > other.sort_key

    def __eq__(self, other: 'Character'):
        return self.sort_key == other.sort_key


@attr.s
class CharacterGroup(AttrsClass):
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
