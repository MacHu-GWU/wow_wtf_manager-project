# -*- coding: utf-8 -*-

import typing as T
import attr
from ordered_set import OrderedSet

from ...logger import logger
from ...models.api import Client, Account, Character
from ...scope.api import (
    ClientScope,
    AccountKeyBindingScope,
    AccountUserInterfaceScope,
    AccountAddonSavedVariablesScope,
    CharacterKeyBindingScope,
    CharacterChatScope,
    CharacterUserInterfaceScope,
    CharacterLayoutScope,
    CharacterAddonSavedVariablesScope,
)
from ...config.api import FileConfig


@attr.define
class GameClientConfig(FileConfig):
    def apply(
        self,
        client: Client,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = ClientScope(client=client)
        if dry_run is False:
            scope.path_output.write_text(content)
        return not dry_run


@attr.define
class AccountUserInterfaceConfig(FileConfig):
    def build(self, account: Account) -> str:
        return self.template.render(account=account)

    def apply(
        self,
        client: Client,
        account: Account,
        dry_run: bool = True,
    ) -> bool:
        content = self.build(account=account)
        scope = AccountUserInterfaceScope(client=client, account=account)
        if dry_run is False:
            scope.path_output.write_text(content)
        return not dry_run


@attr.s
class AccountSavedVariablesConfig(FileConfig):
    @property
    def addon(self) -> str:
        basename = self.path_input.basename
        if basename.endswith(".lua"):
            basename = basename[:-4]
        return basename

    def build(self, account: Account) -> str:
        return self.template.render(account=account)

    def apply(
        self,
        client: Client,
        account: Account,
        dry_run: bool = True,
    ) -> bool:
        content = self.build(account=account)
        scope = AccountAddonSavedVariablesScope(
            client=client, account=account, addon=self.addon
        )
        if dry_run is False:
            scope.path_output.write_text(content)
        return not dry_run


@attr.define
class CharacterUserInterfaceConfig(FileConfig):
    pass


@attr.define
class CharacterKeybindingConfig(FileConfig):
    pass


@attr.s
class CharacterAddonConfig(FileConfig):
    pass


@attr.s
class CharacterLayoutConfig(FileConfig):
    pass


@attr.s
class CharacterSavedVariablesConfig(FileConfig):
    def build(
        self,
        client: T.Optional[Client] = None,
        account: T.Optional[Account] = None,
        account_group: T.Optional[OrderedSet[Account]] = None,
        character: T.Optional[Character] = None,
        character_group: T.Optional[OrderedSet[Character]] = None,
    ) -> str:
        return self.template.render(
            account=account,
            account_group=account_group,
            character=character,
            character_group=character_group,
        )
