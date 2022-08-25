# -*- coding: utf-8 -*-

"""
这个模块是主要是实现了对 游戏角色的 抽象.
"""

import functools

import attr
from attrs_mate import AttrsClass


def titleize(s: str) -> str:
    return s[0].upper() + s[1:].lower()


def right_zfill(s: str) -> str:
    return s + "0" * (20 - len(s))


@functools.total_ordering
@attr.s(frozen=True, order=False)
class Account(AttrsClass):
    """
    代表着一个具体账号. 也是可哈希, 可排序的.
    """
    account: str = attr.ib(converter=titleize)

    def __gt__(self, other: 'Account'):
        return self.account > other.account


@functools.total_ordering
@attr.s(frozen=True, order=False)
class Character(AttrsClass):
    """
    代表着一个具体的游戏角色. 一个角色是唯一的, 可哈希的, 也是可排序的.
    一个角色的用于排序的 Key 在 ``sort_key`` 的方法中被定义.
    同时我们也提供了一个工厂函数, 方便开发者从形如 ``account.server.character``
    的字符串创建对象.
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
