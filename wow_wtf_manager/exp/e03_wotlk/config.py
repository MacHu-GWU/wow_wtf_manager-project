# -*- coding: utf-8 -*-

import attr
from ordered_set import OrderedSet

from ...config.api import FileConfig
from ...models.api import Account, Character


@attr.define
class GameClientConfig(FileConfig):
    pass


@attr.define
class AccountUserInterfaceConfig(FileConfig):
    pass


@attr.s
class AccountSavedVariablesConfig(FileConfig):
    def build(
        self,
        account: Account,
        account_group: OrderedSet[Account],
        character: Character,
        character_group: OrderedSet[Character],
    ) -> str:
        return self.template.render(
            account=account,
            account_group=account_group,
            character=character,
            character_group=character_group,
        )


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
        account: Account,
        account_group: OrderedSet[Account],
        character: Character,
        character_group: OrderedSet[Character],
    ) -> str:
        return self.template.render(
            account=account,
            account_group=account_group,
            character=character,
            character_group=character_group,
        )
