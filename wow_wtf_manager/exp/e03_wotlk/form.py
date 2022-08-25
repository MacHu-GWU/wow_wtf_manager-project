# -*- coding: utf-8 -*-

"""
本模块实现了 WTF 配置 和 游戏角色 之间的关联.
"""

import typing as T
import functools

from ordered_set import OrderedSet
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

from ..e03_wotlk.macro import apply_macros_cache_txt

from .group import Account, Character
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

    evolve_from_account,
    evolve_from_character,
)


@attr.s
class WtfForm(AttrsClass):
    """
    一个具体的 WTF 表格, 定义了哪些角色使用哪些配置.
    """

    dir_wow: Path = attr.ib()

    game_client_config: GameClientConfig = attr.ib()

    account_user_interface_config: T.List[
        T.Tuple[AccountUserInterfaceConfig, OrderedSet[Account]]
    ] = attr.ib(factory=list)
    account_macro_config: T.List[
        T.Tuple[AccountMacroConfig, OrderedSet[Account]]
    ] = attr.ib(factory=list)
    account_saved_variables_config: T.List[
        T.Tuple[AccountSavedVariablesConfig, OrderedSet[Account]]
    ] = attr.ib(factory=list)
    account_keybinding_config: T.List[
        T.Tuple[AccountKeybindingConfig, OrderedSet[Account]]
    ] = attr.ib(factory=list)
    account_cache_config: T.List[
        T.Tuple[AccountCacheConfig, OrderedSet[Account]]
    ] = attr.ib(factory=list)

    character_user_interface_config: T.List[
        T.Tuple[CharacterUserInterfaceConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_chat_config: T.List[
        T.Tuple[CharacterChatConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_keybinding_config: T.List[
        T.Tuple[CharacterKeybindingConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_layout_config: T.List[
        T.Tuple[CharacterLayoutConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_addon_config: T.List[
        T.Tuple[CharacterAddonConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_macro_config: T.List[
        T.Tuple[CharacterMacroConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)
    character_saved_variables_config: T.List[
        T.Tuple[CharacterSavedVariablesConfig, OrderedSet[Character]]
    ] = attr.ib(factory=list)

    all_characters: OrderedSet[Character] = attr.ib(factory=OrderedSet)

    def __attrs_post_init__(self):
        self.game_client_config.dir_wow = self.dir_wow
        for key, value in attr.asdict(self, recurse=False).items():
            if key.startswith("account_") or key.startswith("character_"):
                for config, _ in value:
                    config.dir_wow = self.dir_wow

    def plan(self):
        pass

    def apply_game_client_config(self):
        game_client_config = self.game_client_config
        game_client_config.output_path.parent.mkdir_if_not_exists()
        game_client_config.output_path.write_text(
            game_client_config.input_path.read_text()
        )

    def apply_account_user_interface_config(self):
        for config, account_orderedset in self.account_user_interface_config:
            config_content = config.input_path.read_text()
            for account in account_orderedset:
                config = evolve_from_account(config, account)
                config.output_path.parent.mkdir_if_not_exists()
                config.output_path.write_text(config_content)

    def apply_account_macro_config(self):
        for config, account_orderedset in self.account_macro_config:
            for account in account_orderedset:
                config = evolve_from_account(config, account)
                config.output_path.parent.mkdir_if_not_exists()
                apply_macros_cache_txt(
                    macros_data_file=config.input_path.abspath,
                    game_client_file=config.output_path.abspath,
                )

    def apply_account_saved_variables_config(self):
        for config, account_orderedset in self.account_saved_variables_config:
            config_content_mapper: T.Dict[str, str] = dict()
            for p in config.lua_file_list:
                tpl = Template(p.read_text())
                content = tpl.render(all_characters=self._all_characters)
                config_content_mapper[p.basename] = content

            for account in account_orderedset:
                config = evolve_from_account(config, account)
                config.output_path.mkdir_if_not_exists()
                for p in config.lua_file_list:
                    (config.output_path / p.basename).write_text(
                        config_content_mapper[p.basename]
                    )

    def apply_account_keybinding_config(self):
        pass

    def apply_account_cache_config(self):
        pass

    def _apply_character_single_file_config(self, attr: str):
        for config, character_orderedset in getattr(self, attr):
            config_content = config.input_path.read_text()
            for character in character_orderedset:
                config = evolve_from_character(config, character)
                config.output_path.parent.mkdir_if_not_exists()
                config.output_path.write_text(config_content)

    def apply_character_user_interface_config(self):
        self._apply_character_single_file_config(
            attr="character_user_interface_config"
        )

    def apply_character_chat_config(self):
        self._apply_character_single_file_config(
            attr="character_chat_config"
        )

    def apply_character_keybinding_config(self):
        self._apply_character_single_file_config(
            attr="character_keybinding_config"
        )

    def apply_character_layout_config(self):
        self._apply_character_single_file_config(
            attr="character_layout_config"
        )

    def apply_character_addon_config(self):
        self._apply_character_single_file_config(
            attr="character_addon_config"
        )

    def apply_character_macro_config(self):
        for config, character_orderedset in self.character_macro_config:
            for character in character_orderedset:
                config = evolve_from_character(config, character)
                config.output_path.parent.mkdir_if_not_exists()
                apply_macros_cache_txt(
                    macros_data_file=config.input_path.abspath,
                    game_client_file=config.output_path.abspath,
                )

    def apply_character_saved_variables_config(self):
        for config, character_orderedset in self.character_saved_variables_config:
            config_content_mapper: T.Dict[str, str] = dict()
            for p in config.lua_file_list:
                tpl = Template(p.read_text())
                content = tpl.render(all_characters=self._all_characters)
                config_content_mapper[p.basename] = content

            for character in character_orderedset:
                config = evolve_from_character(config, character)
                config.output_path.mkdir_if_not_exists()
                for p in config.lua_file_list:
                    (config.output_path / p.basename).write_text(
                        config_content_mapper[p.basename]
                    )

    def apply(self):
        self.apply_game_client_config()
        self.apply_account_user_interface_config()
        self.apply_account_macro_config()
        self.apply_account_saved_variables_config()
        # self.apply_account_keybinding_config()
        # self.apply_account_cache_config()

        self.apply_character_user_interface_config()
        self.apply_character_chat_config()
        self.apply_character_keybinding_config()
        self.apply_character_layout_config()
        self.apply_character_addon_config()
        self.apply_character_macro_config()
        self.apply_character_saved_variables_config()

    @functools.cached_property
    def _all_characters(self) -> OrderedSet[Character]:
        """
        把所有在 WtfForm 中所有涉及到的 Character 收集起来, 去重后形成一个列表后返回.

        这是因为在 SavedVariables 里面插件的配置是用 Profile 来管理的. 然后你用不同的角色
        登录后就根据 Profile Name 选择已经定义好的或是默认值. 这就需要虽然我们只对一个
        """
        char_set_list = [self.all_characters, ]
        for key, value in attr.asdict(self, recurse=False).items():
            if key.startswith("character_"):
                for _, char_set in value:
                    char_set_list.append(char_set)
        char_set = OrderedSet.union(*char_set_list)
        char_list = list(char_set)
        char_list.sort()
        return OrderedSet(char_list)
