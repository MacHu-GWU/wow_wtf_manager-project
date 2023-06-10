# -*- coding: utf-8 -*-

import typing as T

import attr
from pathlib_mate import Path

from ..models.api import (
    Account,
    Realm,
    Character,
)


@attr.define
class Client:
    """
    代表着一个具体账号. 是可哈希, 可排序的.
    """

    locale: str = attr.field()
    dir_wtf: Path = attr.field()

    @classmethod
    def new(
        cls,
        locale: str,
        dir_wtf: T.Union[str, Path],
    ) -> "Client":
        obj = cls(
            locale=locale,
            dir_wtf=Path(dir_wtf).absolute(),
        )
        return obj


@attr.define
class ClientConfig:
    client: Client = attr.field()

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath("Config.wtf")


# ------------------------------------------------------------------------------
# Account Level
# ------------------------------------------------------------------------------
@attr.define
class BaseAccountLevelConfig:
    client: Client = attr.field()
    account: Account = attr.field()

    @property
    def filename(self) -> str:
        raise NotImplementedError

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath(
            "Account",
            self.account.account.upper(),
            self.filename,
        )


@attr.define
class AccountKeyBindingConfig(BaseAccountLevelConfig):
    @property
    def filename(self) -> str:
        raise "bindings-cache.wtf"


@attr.define
class AccountUserInterfaceConfig(BaseAccountLevelConfig):
    @property
    def filename(self) -> str:
        raise "config-cache.wtf"


@attr.define
class AccountAddonSavedVariablesConfig:
    client: Client = attr.field()
    account: Account = attr.field()
    addon: str = attr.field()

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath(
            "Account",
            self.account.account.upper(),
            "SavedVariables",
            f"{self.addon}.lua",
        )


# ------------------------------------------------------------------------------
# Character Level
# ------------------------------------------------------------------------------
@attr.define
class BaseCharacterLevelConfig:
    client: Client = attr.field()
    character: Character = attr.field()

    @property
    def filename(self) -> str:
        raise NotImplementedError

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath(
            "Account",
            self.character.account_name.upper(),
            self.character.realm_name,
            self.character.character[0].upper() + self.character.character[1:],
        )


@attr.define
class CharacterKeyBindingConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        raise "bindings-cache.wtf"


@attr.define
class CharacterChatConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        raise "chat-cache.txt"


@attr.define
class CharacterUserInterfaceConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        raise "config-cache.wtf"


@attr.define
class CharacterLayoutConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        raise "layout-local.txt"


@attr.define
class CharacterAddonSavedVariablesConfig:
    client: Client = attr.field()
    character: Character = attr.field()
    addon: str = attr.field()

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath(
            "Account",
            self.character.account_name.upper(),
            self.character.realm_name,
            self.character.character[0].upper() + self.character.character[1:],
            "SavedVariables",
            f"{self.addon}.lua",
        )


@attr.define
class CharacterLayoutConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        raise "layout-local.txt"
