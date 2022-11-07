# -*- coding: utf-8 -*-

import typing as T
from functools import cached_property

from rich import print as rprint
import yaml
from yaml import load, dump, Loader, Dumper
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

from ..group import Account

dir_here = Path.dir_here(__file__)
path_sdm_template = dir_here / "sdm.tpl"

sdm_template = Template(path_sdm_template.read_text())


@attr.s
class SDMCharacter(AttrsClass):
    name: str = attr.ib(default="")
    realm: str = attr.ib(default="")


class SDMMacroTypeEnum:
    button = "b"
    floating = "f"
    script = "s"


_DEFAULT_TYPE = SDMMacroTypeEnum.button
_DEFAULT_ID = 0
_DEFAULT_ICON = 1


@attr.s
class SDMMacro(AttrsClass):
    """
    定义了一个魔兽世界中的 SDM 宏命令的抽象, 目前只支持 Button + Global 这一种模式.
    """
    name: str = attr.ib()
    character: SDMCharacter = AttrsClass.ib_nested()
    type: str = attr.ib(default=_DEFAULT_TYPE)
    id: int = attr.ib(default=_DEFAULT_ID)  # SDM macro ID starts from 0
    icon: int = attr.ib(default=_DEFAULT_ICON)  # 1 is the Question Mark Icon
    text: str = attr.ib(default="")

    def set_id(self, id: int) -> 'SDMMacro':
        self.id = id
        return self

    def set_char(self, name: str, realm: str) -> 'SDMMacro':
        self.character.name = name
        self.character.realm = realm
        return self

    def is_global(self) -> bool:
        """
        Is this SDM macro a global macro or character macro
        """
        if self.character is None:
            return True
        elif (self.character.name is None) or (self.character.realm is None):
            return True
        else:
            return False

    def encode_text(self) -> str:
        """
        Encode macro text to single-ling Lua string.
        """
        return self.text.replace("\n", "\\n")

    @classmethod
    def parse_yml(cls, content: str) -> 'SDMMacro':
        data = load(content, Loader)
        return cls(
            name=data["name"],
            character=SDMCharacter(**data["character"]),
            type=data["type"] if data["type"] else _DEFAULT_TYPE,
            id=data["id"] if data["id"] else _DEFAULT_ID,
            icon=data["icon"] if data["icon"] else _DEFAULT_ICON,
            text=data["text"].strip(),
        )

    def render(self) -> str:
        """
        Render the corresponding SuperDupeMacro.lua code
        """
        lines: T.List[str] = list()
        lines.append(f"[{self.id}] = {{")
        lines.append(f'    ["type"] = "{self.type}",')
        lines.append(f'    ["name"] = "{self.name}",')
        if self.is_global() is False:
            lines.append(f'    ["character"] = {{')
            lines.append(f'        ["name"] = "{self.character.name}",')
            lines.append(f'        ["realm"] = "{self.character.realm}",')
            lines.append(f'    }},')
        lines.append(f'    ["ID"] = {self.id},')
        lines.append(f'    ["icon"] = {self.icon},')
        lines.append(f'    ["text"] = "{self.encode_text()}",')
        lines.append(f'}},')
        return "\n".join(lines)


@attr.s
class SDMMacroFile(AttrsClass):
    """
    以 YAML 文件形式存在的一个 SDM 宏.
    """
    path: Path = attr.ib()

    @cached_property
    def content(self) -> str:
        return self.path.read_text()

    @property
    def macro(self) -> SDMMacro:
        return SDMMacro.parse_yml(self.content)


def render_sdm_lua(macro_list: T.List[SDMMacro]) -> str:
    id_set = {macro.id for macro in macro_list}
    if len(id_set) != len(macro_list):
        macro_id_list = [macro.id for macro in macro_list]
        raise ValueError(
            "Cannot render SDM lua! Found duplicate id in 'macro_list'."
            f"macro id list: {macro_id_list}"
        )
    return sdm_template.render(macro_list=macro_list)


@attr.s
class AccountSDMSetup(AttrsClass):
    account: Account = Account.ib_nested()
    macros: T.List[SDMMacro] = SDMMacro.ib_list_of_nested()


@attr.s
class ClientSDMSetup(AttrsClass):
    dir_wow: Path = attr.ib()
    accounts: T.List[AccountSDMSetup] = AccountSDMSetup.ib_list_of_nested()

    def apply(self, plan=True):
        for account in self.accounts:
            print(f"working on account: {account.account}")
            path = self.dir_wow / "WTF" / "Account" / account.account.account / "SavedVariables" / "SuperDuperMacro.lua"
            content = render_sdm_lua(account.macros)
            if plan is False:
                path.write_text(content)