# -*- coding: utf-8 -*-

"""
为了能实现用 Python 来操作 SDM 插件的 ``SavedVariables/SuperDuperMacro.lua`` 文件,
我们要对 .lua 文件中的代码块进行数据建模, 定义一些 Python 类来代表这些代码块, 然后实现将
Python 对象转化为 .lua 代码块的逻辑.
"""

import typing as T

import attr
from jinja2 import Template
from pathlib_mate import Path
from yaml import load, Loader

_dir_here = Path.dir_here(__file__)
_path_sdm_template = _dir_here / "sdm.tpl"
_sdm_template = Template(_path_sdm_template.read_text())


@attr.define
class SDMCharacter:
    """
    代表 Character Macro 专有宏命令中关于角色信息的部分. 对应着如下代码块:

    .. code-block:: lua

        ["character"] = {
            ["name"] = "charname",
            ["realm"] = "realmname",
        },
    """

    name: str = attr.field()
    realm: str = attr.field()


class SDMMacroTypeEnum:
    """
    枚举 SDM 宏命令的三种类型.
    """

    button = "b"
    floating = "f"
    script = "s"


_DEFAULT_TYPE = SDMMacroTypeEnum.button  # 默认的宏命令类型
_DEFAULT_ID = 0  # 默认的起始 ID
_DEFAULT_ICON = 1  # 默认的宏命令图标


@attr.define
class SDMMacro:
    """
    定义了一个魔兽世界中的 SDM 宏命令的抽象, 目前只支持 Button + Global 这一种模式.

    代表着如下代码块:

    .. code-block:: lua

        {
            ["type"] = "f",
            ["name"] = "macroname",
            ["character"] = {
                ["name"] = "charname",
                ["realm"] = "realmname",
            },
            ["ID"] = 1,
            ["text"] = "/s hello",
            ["icon"] = 1,
        }, -- [1]
    """

    name: str = attr.field()
    character: T.Optional[SDMCharacter] = attr.field(default=None)
    type: str = attr.ib(default=_DEFAULT_TYPE)
    id: int = attr.ib(default=_DEFAULT_ID)  # SDM macro ID starts from 0
    icon: int = attr.ib(default=_DEFAULT_ICON)  # 1 is the Question Mark Icon
    text: str = attr.ib(default="")

    def set_id(self, id: int) -> "SDMMacro":  # pragma: no cover
        """
        Update it's attributes value.
        """
        self.id = id
        return self

    def set_char(self, name: str, realm: str) -> "SDMMacro":  # pragma: no cover
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
        Encode macro text to single-ling Lua string. The final string of the
        macro body in lua has to have only one line.
        """
        return self.text.replace("\n", "\\n")

    @classmethod
    def parse_yml(cls, content: str) -> "SDMMacro":
        """
        从人类可读写的 yaml 文件中读取数据, 创建 :class:`SDMMacro` 对象.

        下面是一个示例的 yaml 文件.

        .. code-block:: yaml

            name: interrupt
            character:
              name:
              realm:
            type: b
            id:
            # you can find icon id on https://wotlk.evowow.com/?icons
            icon:
            description: |
              cancel casting spell, interrupt enemy casting immediately!
            text: |
              #showtooltip
              /stopcasting
              /cast Counterspell
        """
        data = load(content, Loader)
        return cls(
            name=data["name"],
            character=SDMCharacter(**data["character"]),
            type=data["type"] if data["type"] else _DEFAULT_TYPE,
            id=data["id"] if data["id"] else _DEFAULT_ID,
            icon=data["icon"] if data["icon"] else _DEFAULT_ICON,
            text=data["text"].strip(),
        )

    @classmethod
    def from_yaml_file(cls, path: Path) -> "SDMMacro":
        """
        从 yaml 文件中读取数据, 创建 :class:`SDMMacro` 对象.
        """
        return cls.parse_yml(path.read_text())

    def render(self) -> str:
        """
        Render the corresponding SuperDupeMacro.lua code. See example at
        :class:`SDMMacro`.
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


@attr.define
class SDMLua:
    """
    代表了 SuperDupeMacro.lua 文件的抽象. 该类只能用于将数据写入到 SuperDupeMacro.lua,
    而不能从 SuperDupeMacro.lua 中读取数据.

    :param path_lua: SuperDupeMacro.lua 文件路径.
    :param macros: :class:`SDMMacro` 对象的列表.
    """

    path_lua: Path = attr.field()
    macros: T.List[SDMMacro] = attr.field(factory=list)

    @path_lua.validator
    def check_path_lua(self, attribute, value):  # pragma: no cover
        if value.basename != "SuperDuperMacro.lua":
            raise ValueError(f"the SDMLua.path_lua has to end with SuperDupeMacro.lua!")

    def validate_macros(self):  # pragma: no cover
        """
        Todo: add doc string
        """
        id_set = {macro.id for macro in self.macros}
        if len(id_set) != len(self.macros):
            macro_id_list = [macro.id for macro in self.macros]
            raise ValueError(
                f"Cannot render SDM lua! Found duplicate id in 'macro_list': {macro_id_list}"
            )

    def render(self) -> str:
        """
        将一堆 :class:`SDMMacro` 对象渲染成 SuperDupeMacro.lua 文件的内容 (只是生成内容
        而不将内容写入文件). 这里面会检查 macro_list 中的 macro id 是否有重复, 如果有重复,
        则会抛出异常.
        """
        self.validate_macros()
        return _sdm_template.render(macros=self.macros)

    def write(self, dry_run: bool = True) -> str:  # pragma: no cover
        content = self.render()
        if dry_run is False:
            self.path_lua.parent.mkdir_if_not_exists()
            self.path_lua.write_text(content)
        return content
