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
    BaseConfig,
    BaseGameClientConfig,
    BaseAccountConfig,
    BaseCharacterConfig,

    GameClientConfig,

    AccountUserInterfaceConfig,
    AccountMacroConfig,
    AccountSavedVariablesConfig,
    AccountKeybindingConfig,
    AccountCacheConfig,

    CharacterUserInterfaceConfig,
    CharacterChatConfig,
    CharacterKeybindingConfig,
    CharacterLayoutConfig,
    CharacterAddonConfig,
    CharacterMacroConfig,
    CharacterSavedVariablesConfig,
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

    def apply_game_client_config(self, associations: T.List[Asso]):
        for asso in associations:
            asso.config

    def apply_account_user_interface_config(self, associations: T.List[Asso]):
        pass

    def apply_account_macro_config(self, associations: T.List[Asso]):
        pass

    def apply_account_saved_variables_config(self, associations: T.List[Asso]):
        pass

    def apply_account_keybinding_config(self, associations: T.List[Asso]):
        pass

    def apply_account_cache_config(self, associations: T.List[Asso]):
        pass

    def apply_character_user_interface_config(self, associations: T.List[Asso]):
        pass

    def apply_character_chat_config(self, associations: T.List[Asso]):
        pass

    def apply_character_keybinding_config(self, associations: T.List[Asso]):
        pass

    def apply_character_layout_config(self, associations: T.List[Asso]):
        pass

    def apply_character_addon_config(self, associations: T.List[Asso]):
        pass

    def apply_character_macro_config(self, associations: T.List[Asso]):
        pass

    def apply_character_saved_variables_config(self, associations: T.List[Asso]):
        pass

    def apply(self):
        groups: T.Dict[str, dict] = {
            GameClientConfig.__name__: {
                "method": "apply_game_client_config",
                "associations": [],
            },
            AccountUserInterfaceConfig.__name__: {
                "method": "apply_account_user_interface_config",
                "associations": [],
            },
            AccountMacroConfig.__name__: {
                "method": "apply_account_macro_config",
                "associations": [],
            },
            AccountSavedVariablesConfig.__name__: {
                "method": "apply_account_saved_variables_config",
                "associations": [],
            },
            AccountKeybindingConfig.__name__: {
                "method": "apply_account_keybinding_config",
                "associations": [],
            },
            AccountCacheConfig.__name__: {
                "method": "apply_account_cache_config",
                "associations": [],
            },
            CharacterUserInterfaceConfig.__name__: {
                "method": "apply_character_user_interface_config",
                "associations": [],
            },
            CharacterChatConfig.__name__: {
                "method": "apply_character_chat_config",
                "associations": [],
            },
            CharacterKeybindingConfig.__name__: {
                "method": "apply_character_keybinding_config",
                "associations": [],
            },
            CharacterLayoutConfig.__name__: {
                "method": "apply_character_layout_config",
                "associations": [],
            },
            CharacterAddonConfig.__name__: {
                "method": "apply_character_addon_config",
                "associations": [],
            },
            CharacterMacroConfig.__name__: {
                "method": "apply_character_macro_config",
                "associations": [],
            },
            CharacterSavedVariablesConfig.__name__: {
                "method": "apply_character_saved_variables_config",
                "associations": [],
            },
        }
        for asso in self.associations:
            groups[asso.config.__class__.__name__]["associations"].append(asso)

        for key, value in groups.items():
            getattr(self, value["method"])(value["associations"])

    @functools.cached_property
    def all_characters(self) -> T.List[Character]:
        """
        把所有在 WtfForm 中所有涉及到的 Character 收集起来, 去重后形成一个列表后返回.

        这是因为在 SavedVariables 里面插件的配置是用 Profile 来管理的. 然后你用不同的角色
        登录后就根据 Profile Name 选择已经定义好的或是默认值. 这就需要虽然我们只对一个
        """
        char_set = set()
        for asso in self.associations:
            for char in asso.group.char_list:
                char_set.add(char)
        char_list = list(char_set)
        char_list.sort()
        return char_list
