# -*- coding: utf-8 -*-

import typing as T
import attr
from ordered_set import OrderedSet

from .config import (
    GameClientConfig,
    AccountUserInterfaceConfig,
    AccountSavedVariablesConfig,
    # CharacterUserInterfaceConfig,
    # CharacterKeybindingConfig,
    # CharacterAddonConfig,
    # CharacterLayoutConfig,
    # CharacterSavedVariablesConfig,
)
from ...models.api import (
    Client,
    Account,
    Character,
)


@attr.define
class Setup:
    client: Client = attr.ib()

    game_client: GameClientConfig = attr.ib()

    account_user_interface: T.List[
        T.Tuple[AccountUserInterfaceConfig, Account]
    ] = attr.ib(factory=list)

    account_saved_variables_config: T.List[
        T.Tuple[AccountSavedVariablesConfig, Account]
    ] = attr.ib(factory=list)

    def apply_game_client(self, dry_run: bool = True):
        self.game_client.apply(client=self.client, dry_run=dry_run)

    def apply_account_user_interface(self, dry_run: bool = True):
        for config, account in self.account_user_interface:
            config.apply(client=self.client, account=account, dry_run=dry_run)

    def apply_saved_variables_config(self, dry_run: bool = True):
        for config, account in self.account_saved_variables_config:
            config.apply(client=self.client, account=account, dry_run=dry_run)
