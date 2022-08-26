# -*- coding: utf-8 -*-

"""
该模块主要实现了对 WTF 中的各种配置文件的抽象.

``BaseConfig`` 是所有配置文件对象的基类. 每一个具体的配置文件就是一个 ``BaseConfig`` 子类
的的实例. 这个实例是除了包含具体的配置文件引用自哪个文本文件, 同时也包含了 Wow dir,
Account, Server, Character 的信息. 有了这些信息, 程序就知道将这些配置应用拷贝到哪个客户端
文件的位置.
"""

import typing as T

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

if T.TYPE_CHECKING:  # pragma: no cover
    from .group import Account, Character


# ------------------------------------------------------------------------------
# 为各种具体的配置进行数据建模
# ------------------------------------------------------------------------------
# --- Per GameClient Level
@attr.s
class BaseConfig(AttrsClass):
    """
    各种具体配置的基类.

    配置有很多种, 例如:

    - 游戏客户端启动配置
    - 插件配置
    - 快捷键配置
    - 宏命令
    - 插件的 SavedVariables
    """


@attr.s
class BaseGameClientConfig(BaseConfig):
    """
    游戏客户端级的配置的基类
    """
    dir_wow: Path = attr.ib(default=None)

    @property
    def dir_wtf(self) -> Path:
        return self.dir_wow / "WTF"


@attr.s
class GameClientConfig(BaseGameClientConfig):
    """
    客户端设定, 图像质量, 声音等. 对应 ``WTF/Config.wtf``
    """
    input_path: Path = attr.ib(default=None)

    _file = "Config.wtf"

    @property
    def output_path(self) -> Path:
        return self.dir_wtf / self._file


# --- Per Account Level
@attr.s
class BaseAccountConfig(BaseGameClientConfig):
    account: str = attr.ib(default=None)

    @property
    def dir_account(self) -> Path:
        return self.dir_wtf / "Account" / uppercase(self.account)


@attr.s
class AccountKeybindingConfig(BaseAccountConfig):
    """
    快捷键绑定设置. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/bindings-cache.wtf``
    """
    input_path: Path = attr.ib(default=None)

    _file = "bindings-cache.wtf"

    @property
    def output_path(self) -> Path:
        return self.dir_account / self._file


@attr.s
class AccountMacroConfig(BaseAccountConfig):
    """
    账号下所有服务器所有角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/macros-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "macros-cache.txt"

    @property
    def output_path(self) -> Path:
        return self.dir_account / self._file


@attr.s
class AccountUserInterfaceConfig(BaseAccountConfig):
    """
    用户界面设置, 例如自动拾取, 显示血量百分比等. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/config-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "config-cache.wtf"

    @property
    def output_path(self) -> Path:
        return self.dir_account / self._file


@attr.s
class AccountCacheConfig(BaseAccountConfig):
    """
    所有缓存文件的 MD5 指纹, 如果跟服务器端的不一样则重新读取.

    - 账户下所有角色: ``WTF/Account/${AccountName}/cache.md5``
    """
    input_path: Path = attr.ib(default=None)

    _file = "cache.md5"

    @property
    def output_path(self) -> Path:
        return self.dir_account / self._file


@attr.s
class AccountSavedVariablesConfig(BaseAccountConfig):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/SavedVariables/``
    """
    input_path: Path = attr.ib(default=None)
    include_list: T.List[str] = attr.ib(factory=list)
    exclude_list: T.List[str] = attr.ib(factory=list)

    _file = "SavedVariables"

    @property
    def output_path(self) -> Path:
        return self.dir_account / self._file

    def evolve(
        self,
        include_list: T.Optional[T.List[str]] = None,
        exclude_list: T.Optional[T.List[str]] = None,
    ):
        config = attr.evolve(self)
        if include_list:
            config.include_list = include_list
        if exclude_list:
            config.exclude_list = exclude_list
        return config

    @property
    def lua_file_list(self) -> T.List[Path]:
        if self.include_list:
            include_list = list(self.include_list)
        else:
            include_list = [
                p.fname
                for p in self.input_path.select_by_ext(".lua")
            ]
        for addon in self.exclude_list:
            try:
                include_list.remove(addon)
            except ValueError:
                pass
        return [
            self.input_path / f"{addon}.lua"
            for addon in include_list
        ]


# --- Per Character Level
@attr.s
class BaseCharacterConfig(BaseAccountConfig):
    server: str = attr.ib(default=None)
    character: str = attr.ib(default=None)

    @property
    def dir_char(self) -> Path:
        return self.dir_account / self.server / self.character


@attr.s
class CharacterKeybindingConfig(BaseCharacterConfig):
    """
    单个角色的快捷键设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/binding-cache.wtf``
    """
    input_path: Path = attr.ib(default=None)

    _file = "bindings-cache.wtf"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterAddonConfig(BaseCharacterConfig):
    """
    单个角色的插件设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/AddOns.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "AddOns.txt"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterMacroConfig(BaseCharacterConfig):
    """
    单个角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/macros-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "macros-cache.txt"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterUserInterfaceConfig(BaseCharacterConfig):
    """
    用户界面设置, 例如自动拾取, 显示血量百分比等. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/config-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "config-cache.wtf"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterLayoutConfig(BaseCharacterConfig):
    """
    用户界面窗口布局. 例如人物窗口, 背包窗口, 天赋窗口, 动作条的位置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/layout-local.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "layout-local.txt"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterChatConfig(BaseCharacterConfig):
    """
    聊天窗口的配置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/chat-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    _file = "chat-cache.txt"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file


@attr.s
class CharacterSavedVariablesConfig(BaseCharacterConfig):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/SavedVariables/``
    """
    input_path: Path = attr.ib(default=None)
    include_list: T.List[str] = attr.ib(factory=list)
    exclude_list: T.List[str] = attr.ib(factory=list)

    _file = "SavedVariables"

    @property
    def output_path(self) -> Path:
        return self.dir_char / self._file

    def evolve(
        self,
        include_list: T.Optional[T.List[str]] = None,
        exclude_list: T.Optional[T.List[str]] = None,
    ):
        config = attr.evolve(self)
        if include_list:
            config.include_list = include_list
        if exclude_list:
            config.exclude_list = exclude_list
        return config

    @property
    def lua_file_list(self) -> T.List[Path]:
        if self.include_list:
            include_list = list(self.include_list)
        else:
            include_list = [
                p.fname
                for p in self.input_path.select_by_ext(".lua")
            ]
        for addon in self.exclude_list:
            try:
                include_list.remove(addon)
            except ValueError:
                pass
        return [
            self.input_path / f"{addon}.lua"
            for addon in include_list
        ]


def uppercase(s: str) -> str:
    return s.upper()


def titleize(s: str) -> str:
    return s[0].upper() + s[1:].lower()


def evolve_from_account(config: BaseAccountConfig, account: 'Account') -> BaseAccountConfig:
    """
    从 Account 对象中获得 账号 信息, 并对 Config 对象进行更新.
    """
    config = attr.evolve(config)
    config.account = account.account
    return config


def evolve_from_character(config: BaseCharacterConfig, character: 'Character') -> BaseCharacterConfig:
    """
    从 Character 对象中获得 账号, 服务器, 角色名 等信息, 并对 Config 对象进行更新.
    """
    config = attr.evolve(config)
    config.account = character.account
    config.server = character.server
    config.character = character.character
    return config
