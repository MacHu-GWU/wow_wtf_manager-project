# -*- coding: utf-8 -*-

"""
为了能
该模块实现了用 Python 来操作 SDM 插件的 SavedVariables lua 文件. 从而允许我们在 Python
中指定我们需要用到哪些宏, 然后一键生成 ``WTF/Account/${AccountName}/SavedVariables/SuperDuperMacro.lua``
文件.
"""

import typing as T
from functools import cached_property

from yaml import load, Loader
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

from ..group import Account, Character

_dir_here = Path.dir_here(__file__)
_path_sdm_template = _dir_here / "sdm.tpl"
_sdm_template = Template(_path_sdm_template.read_text())


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

    def set_id(self, id: int) -> "SDMMacro":
        """
        Update it's attributes value.
        """
        self.id = id
        return self

    def set_char(self, name: str, realm: str) -> "SDMMacro":
        """
        Update it's attributes value.
        """
        if self.character is None:
            self.character = SDMCharacter(
                name=name,
                realm=realm,
            )
        else:
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
    def parse_yml(cls, content: str) -> "SDMMacro":
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
            lines.append(f"    }},")
        lines.append(f'    ["ID"] = {self.id},')
        lines.append(f'    ["icon"] = {self.icon},')
        lines.append(f'    ["text"] = "{self.encode_text()}",')
        lines.append(f"}},")
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
    return _sdm_template.render(macro_list=macro_list)


@attr.s
class AccountSDMSetup(AttrsClass):
    """
    代表着一个 WTF 文件夹下一个 魔兽世界账号中的 SuperDuperMacro 插件的 Lua 配置的对象.

    :param account: 是一个 Account 对象, 代表它输于哪一个 Account.
    :param macro_mapper: key = macro id, value = SDMMacro
    """

    account: Account = Account.ib_nested()
    macro_mapper: T.Dict[int, SDMMacro] = attr.ib(factory=dict)

    def add_macros(self, macros: T.Iterable[SDMMacro], overwrite: bool = False):
        for macro in macros:
            if macro in macros:
                if overwrite:
                    raise Exception
                else:
                    self.macro_mapper[macro.id] = macro
            else:
                self.macro_mapper[macro.id] = macro


@attr.s
class ClientSDMSetup(AttrsClass):
    """
    代表着一个魔兽世界客户端下所有的账号的 SuperDuperMacro 插件的配置.

    :param dir_wow:
    :param account_sdm_setup_mapper: key = account name, value = AccountSDMSetup
    """

    dir_wow: Path = attr.ib()
    account_sdm_setup_mapper: T.Dict[str, AccountSDMSetup] = attr.ib(factory=dict)

    def apply(self, plan=True):
        """
        将插件实际应用到 WTF 文件夹, 该操作会覆盖掉已有的 SuperDuperMacro 插件配置.
        """
        print("This")
        for account_sdm_setup in self.account_sdm_setup_mapper.values():
            print(f"working on account: {account_sdm_setup.account}")
            path = (
                self.dir_wow
                / "WTF"
                / "Account"
                / account_sdm_setup.account.account
                / "SavedVariables"
                / "SuperDuperMacro.lua"
            )
            content = render_sdm_lua(list(account_sdm_setup.macro_mapper.values()))
            if plan is False:
                path.write_text(content)

    def get_or_init_setup(self, account: Account) -> AccountSDMSetup:
        """
        获取或是初始化一个 :class`AccountSDMSetup` 并放到 :attr:`ClientSDMSetup.account_sdm_setup_mapper``
        属性中.
        """
        # 如果已经存在, 那么直接 get
        if account.account in self.account_sdm_setup_mapper:
            return self.account_sdm_setup_mapper[account.account]
        # 如果还不存在, 则先初始化然后再 get
        else:
            account_sdm_setup = AccountSDMSetup(account=account)
            self.account_sdm_setup_mapper[account.account] = account_sdm_setup
            return account_sdm_setup

    def add_macros_for_many_accounts(
        self,
        accounts: T.Iterable[Account],
        files: T.Iterable[SDMMacroFile],
    ):
        """
        为一批 Account 添加一堆一样的 SDMMacro 对象. 这些 Macro 将会成为 Global Macro.
        例如我们可以给所有账号添加一个接受邀请组队宏.

        我们不希望直接用 list.append 或是 dict.update 的方式来参加, 语义不是很明确.
        我们专门设计了这个方法, 用来提升代码可读性.
        """
        for account in accounts:
            account_sdm_setup = self.get_or_init_setup(account)
            macros = [file.macro for file in files]
            account_sdm_setup.add_macros(macros)

    def add_macros_for_many_chars(
        self,
        chars: T.Iterable[Character],
        files: T.Iterable[SDMMacroFile],
    ):
        """
        为一批 Character 添加一堆一样的 SDMMacro 对象. 这些 Macro 将会成为 Character Macro.
        例如我们可以给所有法师角色添加一个打断焦点的目标施法宏.

        我们不希望直接用 list.append 或是 dict.update 的方式来参加, 语义不是很明确.
        我们专门设计了这个方法, 用来提升代码可读性.
        """
        for character in chars:
            account_sdm_setup = self.get_or_init_setup(character.acc_obj)
            macros = [file.macro for file in files]
            for macro in macros:
                macro.set_char(
                    name=character.character,
                    realm=character.server,
                )
            account_sdm_setup.add_macros(macros)