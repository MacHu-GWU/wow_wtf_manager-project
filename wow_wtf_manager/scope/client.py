# -*- coding: utf-8 -*-

import typing as T

import attr
from pathlib_mate import Path

from ..logger import logger
from ..models.api import (
    Client,
    Account,
    Realm,
    Character,
)
from .base import BaseScope


class FileScope(BaseScope):
    """
    A mixin class for that the scope is a file.
    """

    @property
    def path_output(self) -> Path:
        raise NotImplementedError

    @property
    def relpath(self) -> Path:
        for ind, part in enumerate(self.path_output.parts):
            if part in ["WTF", "WTF-output"]:
                return Path(*self.path_output.parts[ind + 1 :])
        raise ValueError(f"Cannot locate WTF or WTF-output in {self.path_output}")

    def apply(
        self,
        content: str,
        dry_run: bool = True,
    ):
        logger.info(f"Write to {self.relpath}")
        if dry_run is False:
            self.path_output.parent.mkdir_if_not_exists()
            self.path_output.write_text(content)


@attr.define
class ClientScope(FileScope):
    client: Client = attr.field()

    @property
    def path_output(self) -> Path:
        return self.client.dir_wtf.joinpath("Config.wtf")


# ------------------------------------------------------------------------------
# Account Level
# ------------------------------------------------------------------------------
@attr.define
class BaseAccountLevelScope(FileScope):
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
class AccountKeyBindingScope(BaseAccountLevelScope):
    @property
    def filename(self) -> str:
        return "bindings-cache.wtf"


@attr.define
class AccountUserInterfaceScope(BaseAccountLevelScope):
    @property
    def filename(self) -> str:
        return "config-cache.wtf"


@attr.define
class AccountAddonSavedVariablesScope(FileScope):
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
class BaseCharacterLevelScope(FileScope):
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
class CharacterUserInterfaceScope(BaseCharacterLevelScope):
    @property
    def filename(self) -> str:
        return "config-cache.wtf"


@attr.define
class CharacterChatScope(BaseCharacterLevelScope):
    @property
    def filename(self) -> str:
        return "chat-cache.txt"


@attr.define
class CharacterKeyBindingScope(BaseCharacterLevelScope):
    @property
    def filename(self) -> str:
        return "bindings-cache.wtf"


@attr.define
class CharacterLayoutScope(BaseCharacterLevelScope):
    @property
    def filename(self) -> str:
        return "layout-local.txt"


@attr.define
class CharacterAddonsScope(BaseCharacterLevelScope):
    @property
    def filename(self) -> str:
        return "AddOns.txt"


@attr.define
class CharacterAddonSavedVariablesScope(FileScope):
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
