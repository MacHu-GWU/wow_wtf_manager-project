# -*- coding: utf-8 -*-

import typing as T
import attr

from ...logger import logger
from ...models.api import (
    Client,
    Account,
    Character,
)

from .config import (
    GameClientConfig,
    AccountUserInterfaceConfig,
    AccountSavedVariablesConfig,
    CharacterUserInterfaceConfig,
    CharacterChatConfig,
    CharacterKeybindingConfig,
    CharacterLayoutConfig,
    CharacterAddonsConfig,
    CharacterSavedVariablesConfig,
)


@attr.define
class Setup:
    client: Client = attr.ib()

    game_client: GameClientConfig = attr.ib()

    account_user_interface: T.List[T.Tuple[AccountUserInterfaceConfig, Account]] = attr.ib(factory=list)
    account_saved_variables: T.List[T.Tuple[AccountSavedVariablesConfig, Account]] = attr.ib(factory=list)

    character_user_interface: T.List[T.Tuple[CharacterUserInterfaceConfig, Character]] = attr.ib(factory=list)
    character_chat: T.List[T.Tuple[CharacterChatConfig, Character]] = attr.ib(factory=list)
    character_keybinding: T.List[T.Tuple[CharacterKeybindingConfig, Character]] = attr.ib(factory=list)
    character_layout: T.List[T.Tuple[CharacterLayoutConfig, Character]] = attr.ib(factory=list)
    character_addons: T.List[T.Tuple[CharacterAddonsConfig, Character]] = attr.ib(factory=list)
    character_saved_variables: T.List[T.Tuple[CharacterSavedVariablesConfig, Character]] = attr.ib(factory=list)

    @logger.start_and_end(msg="{func_name}", pipe="💻")
    def show_game_client(self):
        logger.info(f"Working on {self.client.dir_wtf}")

    @logger.start_and_end(msg="{func_name}", pipe="💻")
    def apply_game_client(self, dry_run: bool = True):
        self.game_client.apply(client=self.client, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🏷")
    def apply_account_user_interface(self, dry_run: bool = True):
        for config, account in self.account_user_interface:
            config.apply(client=self.client, account=account, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🏷")
    def apply_account_saved_variables(self, dry_run: bool = True):
        for config, account in self.account_saved_variables:
            config.apply(client=self.client, account=account, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_user_interface(self, dry_run: bool = True):
        for config, character in self.character_user_interface:
            config.apply(client=self.client, character=character, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_chat(self, dry_run: bool = True):
        for config, character in self.character_chat:
            config.apply(client=self.client, character=character, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_keybinding(self, dry_run: bool = True):
        for config, character in self.character_keybinding:
            config.apply(client=self.client, character=character, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_layout(self, dry_run: bool = True):
        for config, character in self.character_layout:
            config.apply(client=self.client, character=character, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_addons(self, dry_run: bool = True):
        for config, character in self.character_addons:
            config.apply(client=self.client, character=character, dry_run=dry_run)

    @logger.start_and_end(msg="{func_name}", pipe="🐮")
    def apply_character_saved_variables(self, dry_run: bool = True):
        for config, character in self.character_saved_variables:
            config.apply(client=self.client, character=character, dry_run=dry_run)
