# -*- coding: utf-8 -*-

"""
本模块定义了再 WOTLK 资料片下, 有哪些不同类型的配置文件. 以及针对不同类型的配置文件,
如何生成最终配置数据的逻辑.

.. note::

    开发者注意:

    1. 每种类型的配置文件类下面都有 apply() 方法, 用于将配置文件内容应用到目标文件中.
        里面看似有很多重复的逻辑, 但是请不要过度优化! 让这些逻辑清晰可见在这种情况下更重要.
    2. 每个 build() 和 apply() 方法 PyCharm 都会提示有问题, 这是因为我们定义了抽象方法
        而导致的, 请忽略这些警告.
"""

import attr

from ...models.api import Client, Account, Character
from ...scope.api import (
    ClientScope,
    AccountUserInterfaceScope,
    AccountAddonSavedVariablesScope,
    CharacterKeyBindingScope,
    CharacterChatScope,
    CharacterUserInterfaceScope,
    CharacterLayoutScope,
    CharacterAddonsScope,
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
            scope.apply(content, dry_run=dry_run)
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
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.s
class AccountSavedVariablesConfig(FileConfig):
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
            client=client,
            account=account,
            lua_file=self.path_input.basename,
        )
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.define
class CharacterUserInterfaceConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterUserInterfaceScope(client=client, character=character)
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.define
class CharacterChatConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterChatScope(client=client, character=character)
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.define
class CharacterKeybindingConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterKeyBindingScope(client=client, character=character)
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.s
class CharacterLayoutConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterLayoutScope(client=client, character=character)
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.s
class CharacterAddonsConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterAddonsScope(client=client, character=character)
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run


@attr.s
class CharacterSavedVariablesConfig(FileConfig):
    def apply(
        self,
        client: Client,
        character: Character,
        dry_run: bool = True,
    ) -> bool:
        content = self.build()
        scope = CharacterAddonSavedVariablesScope(
            client=client,
            character=character,
            lua_file=self.path_input.basename,
        )
        if dry_run is False:
            scope.apply(content, dry_run=dry_run)
        return not dry_run
