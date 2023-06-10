# -*- coding: utf-8 -*-

import typing as T

import attr
from pathlib_mate import Path

from ..models.api import (
    Client,
    Account,
    Realm,
    Character,
)
from .base import BaseScope


@attr.define
class ClientConfig(BaseScope):
    client: Client = attr.field()

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath("Config.wtf")


# ------------------------------------------------------------------------------
# Account Level
# ------------------------------------------------------------------------------
@attr.define
class BaseAccountLevelConfig(BaseScope):
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
        return "bindings-cache.wtf"


@attr.define
class AccountUserInterfaceConfig(BaseAccountLevelConfig):
    @property
    def filename(self) -> str:
        return "config-cache.wtf"


@attr.define
class AccountAddonSavedVariablesConfig(BaseScope):
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
class BaseCharacterLevelConfig(BaseScope):
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
            self.filename,
        )


@attr.define
class CharacterKeyBindingConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        return "bindings-cache.wtf"


@attr.define
class CharacterChatConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        return "chat-cache.txt"


@attr.define
class CharacterUserInterfaceConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        return "config-cache.wtf"


@attr.define
class CharacterLayoutConfig(BaseCharacterLevelConfig):
    @property
    def filename(self) -> str:
        return "layout-local.txt"


@attr.define
class CharacterAddonSavedVariablesConfig(BaseScope):
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
