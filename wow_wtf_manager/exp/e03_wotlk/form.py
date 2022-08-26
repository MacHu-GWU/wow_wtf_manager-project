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
from rich import print

from ..e03_wotlk.macro import apply_macros_cache_txt

from .group import Account, Character
from .wtf import (
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

    :param apply_macros_cache_txt: 对于不同的资料片, 宏命令的格式是有所不同的.
        这里我们没办法把这个做成一个基类, 所以只能把这个逻辑做成一个属性了. TODO: 把
        这个函数解耦, 作为工厂函数传入.
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
    verbose: bool = attr.ib(default=True)
    apply_macros_cache_txt: callable = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.game_client_config.dir_wow = self.dir_wow
        for key, value in attr.asdict(self, recurse=False).items():
            if key.startswith("account_") or key.startswith("character_"):
                for config, _ in value:
                    config.dir_wow = self.dir_wow

    def _print_header(self, msg: str):
        msg = f" {msg} "
        print(f"{msg:=^80}")

    def apply_game_client_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Game Client Config '{GameClientConfig._file}'")
        game_client_config = self.game_client_config
        if self.verbose:
            print(f"copy from {game_client_config.input_path.abspath}")
            print(f"  to {game_client_config.output_path.abspath}")
        if plan is False:
            game_client_config.output_path.parent.mkdir_if_not_exists()
            game_client_config.output_path.write_text(
                game_client_config.input_path.read_text()
            )

    def apply_account_user_interface_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Account User Interface Config '{AccountUserInterfaceConfig._file}'")
        for config, account_orderedset in self.account_user_interface_config:
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")
            config_content = config.input_path.read_text()
            for account in account_orderedset:
                config = evolve_from_account(config, account)
                if self.verbose:
                    print(f"  to {config.output_path.abspath}")
                if plan is False:
                    config.output_path.parent.mkdir_if_not_exists()
                    config.output_path.write_text(config_content)

    def apply_account_macro_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Account Macro Config '{AccountMacroConfig._file}'")
        for config, account_orderedset in self.account_macro_config:
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")
            for account in account_orderedset:
                config = evolve_from_account(config, account)
                if self.verbose:
                    print(f"  to {config.output_path.abspath}")
                if plan is False:
                    config.output_path.parent.mkdir_if_not_exists()
                    self.apply_macros_cache_txt(
                        macros_data_file=config.input_path.abspath,
                        game_client_file=config.output_path.abspath,
                        plan=plan,
                    )

    def apply_account_saved_variables_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Account SavedVariable Config '{AccountSavedVariablesConfig._file}'")
        for config, account_orderedset in self.account_saved_variables_config:
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")

            config_content_mapper: T.Dict[str, str] = dict()
            for p in config.lua_file_list:
                tpl = Template(p.read_text())
                content = tpl.render(all_characters=self._all_characters)
                config_content_mapper[p.basename] = content

            for account in account_orderedset:
                config = evolve_from_account(config, account)
                if plan is False:
                    config.output_path.mkdir_if_not_exists()
                for p in config.lua_file_list:
                    if self.verbose:
                        print(f"  to {(config.output_path / p.basename).abspath}")
                    if plan is False:
                        (config.output_path / p.basename).write_text(
                            config_content_mapper[p.basename]
                        )

    def apply_account_keybinding_config(self, plan=False):
        pass

    def apply_account_cache_config(self, plan=False):
        pass

    def _apply_character_single_file_config(self, attr: str, plan=False):
        for config, character_orderedset in getattr(self, attr):
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")
            config_content = config.input_path.read_text()
            for character in character_orderedset:
                config = evolve_from_character(config, character)
                if self.verbose:
                    print(f"  to {config.output_path.abspath}")
                if plan is False:
                    config.output_path.parent.mkdir_if_not_exists()
                    config.output_path.write_text(config_content)

    def apply_character_user_interface_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character User Interface Config '{CharacterUserInterfaceConfig._file}'")
        self._apply_character_single_file_config(
            attr="character_user_interface_config",
            plan=plan,
        )

    def apply_character_chat_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character Chat Config '{CharacterChatConfig._file}'")
        self._apply_character_single_file_config(
            attr="character_chat_config",
            plan=plan,
        )

    def apply_character_keybinding_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character Keybinding Config '{CharacterKeybindingConfig._file}'")
        self._apply_character_single_file_config(
            attr="character_keybinding_config",
            plan=plan,
        )

    def apply_character_layout_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character Layout Config '{CharacterLayoutConfig._file}'")
        self._apply_character_single_file_config(
            attr="character_layout_config",
            plan=plan,
        )

    def apply_character_addon_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character Addon Config '{CharacterAddonConfig._file}'")
        self._apply_character_single_file_config(
            attr="character_addon_config",
            plan=plan,
        )

    def apply_character_macro_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character Macro Config '{CharacterMacroConfig._file}'")
        for config, character_orderedset in self.character_macro_config:
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")
            for character in character_orderedset:
                config = evolve_from_character(config, character)
                if self.verbose:
                    print(f"  to {config.output_path.abspath}")
                if plan is False:
                    config.output_path.parent.mkdir_if_not_exists()
                    self.apply_macros_cache_txt(
                        macros_data_file=config.input_path.abspath,
                        game_client_file=config.output_path.abspath,
                        plan=plan,
                    )

    def apply_character_saved_variables_config(self, plan=False):
        if self.verbose:
            self._print_header(f"apply Character SavedVariable Config '{CharacterSavedVariablesConfig._file}'")
        for config, character_orderedset in self.character_saved_variables_config:
            if self.verbose:
                print(f"copy from {config.input_path.abspath}")
            config_content_mapper: T.Dict[str, str] = dict()
            for p in config.lua_file_list:
                tpl = Template(p.read_text())
                content = tpl.render(all_characters=self._all_characters)
                config_content_mapper[p.basename] = content

            for character in character_orderedset:
                config = evolve_from_character(config, character)
                if plan is False:
                    config.output_path.mkdir_if_not_exists()
                for p in config.lua_file_list:
                    if self.verbose:
                        print(f"  to {(config.output_path / p.basename).abspath}")
                    if plan is False:
                        (config.output_path / p.basename).write_text(
                            config_content_mapper[p.basename]
                        )

    def apply(self, plan=False):
        self.apply_game_client_config(plan=plan)
        self.apply_account_user_interface_config(plan=plan)
        self.apply_account_macro_config(plan=plan)
        self.apply_account_saved_variables_config(plan=plan)
        # self.apply_account_keybinding_config()
        # self.apply_account_cache_config()

        self.apply_character_user_interface_config(plan=plan)
        self.apply_character_chat_config(plan=plan)
        self.apply_character_keybinding_config(plan=plan)
        self.apply_character_layout_config(plan=plan)
        self.apply_character_addon_config(plan=plan)
        self.apply_character_macro_config(plan=plan)
        self.apply_character_saved_variables_config(plan=plan)

    def plan(self):
        return self.apply(plan=True)

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
