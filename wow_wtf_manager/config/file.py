# -*- coding: utf-8 -*-

"""
该模块实现了对单个配置文件的类型的管理. 所谓管理的本质就是:

1. 从数据中读取配置的模板
2. 然后输入参数生成最终的数据文件
3. 将数据文件写入到指定的位置
"""

import typing as T
import attr
import jinja2
from pathlib_mate import Path

from .base import BaseConfig

from ..models.api import (
    Client,
    Account,
    Character,
)
from ..scope.api import (
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

# T_FILE_SCOPE = T.Union[
#     ClientConfig,
#     AccountKeyBindingConfig,
#     AccountUserInterfaceConfig,
#     AccountAddonSavedVariablesConfig,
#     CharacterKeyBindingConfig,
#     CharacterChatConfig,
#     CharacterUserInterfaceConfig,
#     CharacterLayoutConfig,
#     CharacterAddonSavedVariablesConfig,
# ]


@attr.define
class FileConfig(BaseConfig):
    path_input: Path = attr.field(converter=Path)
    template: T.Optional[jinja2.Template] = attr.field()

    @classmethod
    def new(
        cls,
        path_input: T.Union[str, Path],
    ):
        path_input = Path(path_input)
        template = jinja2.Template(source=path_input.read_text())
        return cls(path_input=path_input, template=template)


@attr.define
class AccountUserInterfaceConfig(FileConfig):
    def build(self) -> str:
        return self.template.render()


@attr.define
class CharacterUserInterfaceConfig(FileConfig):
    def build(self) -> str:
        return self.template.render()


# account_keybinding_config = AccountKeybindingConfiguration(path_input=Path(__file__))
# account_keybinding_config.apply(scope=)
