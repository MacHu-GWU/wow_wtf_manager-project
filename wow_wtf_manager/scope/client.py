# -*- coding: utf-8 -*-

"""
该模块实现了以魔兽世界客户端根目录为跟, 延伸到各个账号, 各个服务器, 各个角色, 各个插件的配置作用域.
"""

import attr
from pathlib_mate import Path

from ..logger import logger
from ..models.api import (
    Client,
    Account,
    Character,
)
from .base import BaseScope


class FileScope(BaseScope):
    """
    作用域为单个文件的基类. 魔兽世界配置大多数都可以用单个文件的排列组合来完成.
    """

    @property
    def path_output(self) -> Path:
        """
        作用域的目标文件路径. 该函数必须被子类实现.
        """
        raise NotImplementedError

    @property
    def relpath(self) -> Path:
        """
        从 WTF/ 文件夹开始的相对路径, 用于在 log 中显式.
        """
        for ind, part in enumerate(self.path_output.parts):
            if part in ["WTF", "WTF-output"]:
                return Path(*self.path_output.parts[ind + 1 :])
        raise ValueError(f"Cannot locate WTF or WTF-output in {self.path_output}")

    def apply(
        self,
        content: str,
        dry_run: bool = True,
    ):
        """
        将配置文件内容应用到目标文件中.
        """
        logger.info(f"Write to {self.relpath}")
        if dry_run is False:
            self.path_output.parent.mkdir_if_not_exists()
            self.path_output.write_text(content)


@attr.define
class ClientScope(FileScope):
    """
    作用域为客户端配置的文件.
    """

    client: Client = attr.field()

    @property
    def path_output(self) -> Path:
        """
        Example: ``C:\...\WTF\Config.wtf``
        """
        return self.client.dir_wtf.joinpath("Config.wtf")


# ------------------------------------------------------------------------------
# Account Level
# ------------------------------------------------------------------------------
@attr.define
class BaseAccountLevelScope(FileScope):
    """
    作用域为单个账号的基类.

    :param client: 制定了客户端的路径.
    :param account: 指定了账号的信息.
    """

    client: Client = attr.field()
    account: Account = attr.field()

    @property
    def filename(self) -> str:
        raise NotImplementedError

    @property
    def path_output(self) -> Path:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\*.*``
        """
        return self.client.dir_wtf.joinpath(
            "Account",
            self.account.account.upper(),
            self.filename,
        )


@attr.define
class AccountUserInterfaceScope(BaseAccountLevelScope):
    """
    作用域为指定 Account 的客户端配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\config-cache.wtf``
        """
        return "config-cache.wtf"


@attr.define
class AccountKeyBindingScope(BaseAccountLevelScope):
    """
    作用域为指定 Account 的按键绑定配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\bindings-cache.wtf``
        """
        return "bindings-cache.wtf"


@attr.define
class AccountAddonSavedVariablesScope(FileScope):
    """
    作用域为指定 Account 的每个插件的 Lua 数据文件.

    :param lua_file: 在 SavedVariables 文件夹中的文件名.
    """

    client: Client = attr.field()
    account: Account = attr.field()
    lua_file: str = attr.field()

    @property
    def path_output(self) -> Path:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\SavedVariables\*.lua``
        """
        return self.client.dir_wtf.joinpath(
            "Account",
            self.account.account.upper(),
            "SavedVariables",
            self.lua_file,
        )


# ------------------------------------------------------------------------------
# Character Level
# ------------------------------------------------------------------------------
@attr.define
class BaseCharacterLevelScope(FileScope):
    """
    作用域为单个角色的基类.

    :param client: 制定了客户端的路径.
    :param character: 指定了角色的信息.
    """

    client: Client = attr.field()
    character: Character = attr.field()

    @property
    def filename(self) -> str:
        raise NotImplementedError

    @property
    def path_output(self) -> Path:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\*.*``
        """
        return self.client.dir_wtf.joinpath(
            "Account",
            self.character.account_name.upper(),
            self.character.realm_name,
            self.character.character[0].upper() + self.character.character[1:],
            self.filename,
        )


@attr.define
class CharacterUserInterfaceScope(BaseCharacterLevelScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character 的客户端配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\config-cache.wtf``
        """
        return "config-cache.wtf"


@attr.define
class CharacterChatScope(BaseCharacterLevelScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character 的聊天配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\chat-cache.txt``
        """
        return "chat-cache.txt"


@attr.define
class CharacterKeyBindingScope(BaseCharacterLevelScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character 的快捷键绑定配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\bindings-cache.wtf``
        """
        return "bindings-cache.wtf"


@attr.define
class CharacterLayoutScope(BaseCharacterLevelScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character 的界面布局配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\layout-local.txt``
        """
        return "layout-local.txt"


@attr.define
class CharacterAddonsScope(BaseCharacterLevelScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character 所启用的插件列表配置文件.
    """

    @property
    def filename(self) -> str:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\AddOns.txt``
        """
        return "AddOns.txt"


@attr.define
class CharacterAddonSavedVariablesScope(FileScope):
    """
    作用域为指定 Account 下, 指定 Realm 下, 指定 Character, 指定插件的 Lua 数据文件.

    :param lua_file: 在 SavedVariables 文件夹中的文件名.
    """

    client: Client = attr.field()
    character: Character = attr.field()
    lua_file: str = attr.field()

    @property
    def path_output(self) -> Path:
        """
        Example: ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\SavedVariables\*.lua``
        """
        return self.client.dir_wtf.joinpath(
            "Account",
            self.character.account_name.upper(),
            self.character.realm_name,
            self.character.character[0].upper() + self.character.character[1:],
            "SavedVariables",
            self.lua_file,
        )
