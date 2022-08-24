# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

Pathlike = T.Union[str, Path]


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
    pass


@attr.s
class BaseGameClientConfig(BaseConfig):
    """
    游戏客户端级的配置的基类
    """
    dir_wow: Path = attr.ib(default=None)

    @property
    def dir_wtf(self) -> Path:
        return self.dir_wow / "WTF"

    def make_base_account_config(self, account: str) -> 'BaseAccountConfig':
        return BaseAccountConfig(
            dir_wow=self.dir_wow,
            account=account,
        )


@attr.s
class GameClientConfig(BaseGameClientConfig):
    """
    客户端设定, 图像质量, 声音等. 对应 ``WTF/Config.wtf``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> str:
        return self.dir_wtf / "Config.wtf"


# --- Per Account Level
@attr.s
class BaseAccountConfig(BaseGameClientConfig):
    account: str = attr.ib(default=None)

    @property
    def dir_account(self) -> Path:
        return self.dir_wtf / "Account" / self.account

    def make_base_character_config(self, server: str, character: str) -> 'BaseCharacterConfig':
        return BaseCharacterConfig(
            dir_wow=self.dir_wow,
            account=self.account,
            server=server,
            character=character,
        )

    def to_keybinding_config(self) -> 'AccountKeybindingConfig':
        return AccountKeybindingConfig(**self.to_dict())

    def to_cache_config(self) -> 'AccountCacheConfig':
        return AccountCacheConfig(**self.to_dict())

    def to_macro_config(self) -> 'AccountMacroConfig':
        return AccountMacroConfig(**self.to_dict())

    def to_saved_variables_config(self) -> 'AccountSavedVariablesConfig':
        return AccountSavedVariablesConfig(**self.to_dict())

    def to_user_interface_config(self) -> 'AccountUserInterfaceConfig':
        return AccountUserInterfaceConfig(**self.to_dict())


@attr.s
class AccountKeybindingConfig(BaseAccountConfig):
    """
    快捷键绑定设置. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/bindings-cache.wtf``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> str:
        return self.dir_account / "bindings-cache.wtf"


@attr.s
class AccountMacroConfig(BaseAccountConfig):
    """
    账号下所有服务器所有角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/macros-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> str:
        return self.dir_account / "macro-cache.txt"


@attr.s
class AccountUserInterfaceConfig(BaseAccountConfig):
    """
    用户界面设置, 例如自动拾取, 显示血量百分比等. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/config-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_account / "config-cache.txt"


@attr.s
class AccountCacheConfig(BaseAccountConfig):
    """
    所有缓存文件的 MD5 指纹, 如果跟服务器端的不一样则重新读取.

    - 账户下所有角色: ``WTF/Account/${AccountName}/cache.md5``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_account / "cache.md5"


@attr.s
class AccountSavedVariablesConfig(BaseAccountConfig):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/SavedVariables/``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_account / "SavedVariables"


# --- Per Character Level
@attr.s
class BaseCharacterConfig(BaseAccountConfig):
    server: str = attr.ib(default=None)
    character: str = attr.ib(default=None)

    @property
    def dir_char(self) -> Path:
        return self.dir_account / self.server / self.character

    def to_keybinding_config(self) -> 'CharacterKeybindingConfig':
        return CharacterKeybindingConfig(**self.to_dict())

    def to_addon_config(self) -> 'CharacterAddonConfig':
        return CharacterAddonConfig(**self.to_dict())

    def to_chat_config(self) -> 'CharacterChatConfig':
        return CharacterChatConfig(**self.to_dict())

    def to_layout_config(self) -> 'CharacterLayoutConfig':
        return CharacterLayoutConfig(**self.to_dict())

    def to_macro_config(self) -> 'CharacterMacroConfig':
        return CharacterMacroConfig(**self.to_dict())

    def to_saved_variables_config(self) -> 'CharacterSavedVariablesConfig':
        return CharacterSavedVariablesConfig(**self.to_dict())

    def to_user_interface_config(self) -> 'CharacterUserInterfaceConfig':
        return CharacterUserInterfaceConfig(**self.to_dict())


@attr.s
class CharacterKeybindingConfig(BaseCharacterConfig):
    """
    单个角色的快捷键设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/binding-cache.wtf``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "binding-cache.wtf"


@attr.s
class CharacterAddonConfig(BaseCharacterConfig):
    """
    单个角色的插件设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/AddOns.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "AddOns.txt"


@attr.s
class CharacterMacroConfig(BaseCharacterConfig):
    """
    单个角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/macros-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "macros-cache.txt"


@attr.s
class CharacterUserInterfaceConfig(BaseCharacterConfig):
    """
    用户界面设置, 例如自动拾取, 显示血量百分比等. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/config-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "config-cache.txt"


@attr.s
class CharacterLayoutConfig(BaseCharacterConfig):
    """
    用户界面窗口布局. 例如人物窗口, 背包窗口, 天赋窗口, 动作条的位置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/layout-local.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "layout-local.txt"


@attr.s
class CharacterChatConfig(BaseCharacterConfig):
    """
    聊天窗口的配置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/chat-cache.txt``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "chat-cache.txt"


@attr.s
class CharacterSavedVariablesConfig(BaseCharacterConfig):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/SavedVariables/``
    """
    input_path: Path = attr.ib(default=None)

    @property
    def path(self) -> Path:
        return self.dir_char / "SavedVariables"
