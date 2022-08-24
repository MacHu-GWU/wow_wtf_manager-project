# -*- coding: utf-8 -*-

"""
本模块实现了 WTF 配置 和 游戏角色 之间的关联.
"""

import typing as T
import functools

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

from .group import Character, CharacterGroup
from .wtf import (
    BaseConfig, BaseGameClientConfig, BaseAccountConfig, BaseCharacterConfig,
    AccountSavedVariablesConfig, CharacterSavedVariablesConfig,
)


@attr.s
class Asso(AttrsClass):
    """
    WTF 配置 和 游戏角色 之间的关联.

    这里的 config 对象无需给 dir_wow, account, server, character 这些属性赋值.
    config 只要定义了 input_path, 知道从哪里读配置数据即可. 而 group 中的 Character
    对象会补充这些信息.
    """
    config: BaseConfig = attr.ib()
    group: CharacterGroup = attr.ib()


@attr.s
class WtfForm(AttrsClass):
    """
    一个具体的 WTF 表格, 定义了哪些角色使用哪些配置.
    """
    dir_wow: Path = attr.ib()
    associations: T.List[Asso] = attr.ib(factory=list)

    def __attrs_post_init__(self):
        for asso in self.associations:
            asso.config.dir_wow = self.dir_wow

    def plan(self):
        pass

    def apply(self):
        for asso in self.associations:
            asso.config.apply(
                asso.group,
                context={
                    "all_characters": self.all_characters
                }
            )

    @functools.cached_property
    def all_characters(self) -> T.List[Character]:
        char_set = set()
        for asso in self.associations:
            for char in asso.group.char_list:
                char_set.add(char)
        char_list = list(char_set)
        char_list.sort()
        return char_list
