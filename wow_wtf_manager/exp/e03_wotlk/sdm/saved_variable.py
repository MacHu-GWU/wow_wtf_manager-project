# -*- coding: utf-8 -*-

"""
该模块实现了用 Python 来操作 SDM 插件的 SavedVariables lua 文件. 从而允许我们在 Python
中用更自动化的方式指定我们需要用到哪些宏, 然后一键生成它, 免除了在游戏中打开插件界面编辑的麻烦.
该文件位于 ``WTF/Account/${AccountName}/SavedVariables/SuperDuperMacro.lua``.
"""

import typing as T
from functools import cached_property

from rich import print as rprint
from yaml import load, Loader
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

from ..group import Account, Character

# ------------------------------------------------------------------------------
# SDM SavedVariables 文件中最小的组成单位是 SDMMacro
# 这一段代码定义了 SDM Macro 的数据模型.
# ------------------------------------------------------------------------------

_dir_here = Path.dir_here(__file__)
_path_sdm_template = _dir_here / "sdm.tpl"
_sdm_template = Template(_path_sdm_template.read_text())


@attr.s
class SDMCharacter(AttrsClass):
    """
    :class`SDMCharacter` 是 :class:`SDMMacro` 的一个属性, 用来指定宏属于哪个角色.
    """

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
    character: T.Optional[SDMCharacter] = AttrsClass.ib_nested()
    type: str = attr.ib(default=_DEFAULT_TYPE)
    id: int = attr.ib(default=_DEFAULT_ID)  # SDM macro ID starts from 0
    icon: int = attr.ib(default=_DEFAULT_ICON)  # 1 is the Question Mark Icon
    text: str = attr.ib(default="")

    def set_id(self, id: int) -> "SDMMacro":
        """
        将该宏的 ID 设置为指定的 ID.
        """
        self.id = id
        return self

    def set_char(self, name: str, realm: str) -> "SDMMacro":
        """
        将该宏的角色信息设置为指定的角色.
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
        判断它是否是一个 Global 宏 (当前账号下所有角色通用), 还是一个 Character 专用宏.
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
        """
        我们将 SDM lua 文件中一个个的宏定义拆分成了一个个的宏, 并且改成了 Yaml 文件以便编辑.
        这样就可以一单个宏为单位进行排列组合, 批量管理很多账号很多角色的宏命令了.

        该方法能将 Yaml 文件中的一个宏定义解析成 :class:`SDMMacro` 对象. 下面是一个例子:

        .. code-block:: yml

            name: Follow-Focus
            character:
              name:
              realm:
            type: b
            id: 1110
            icon: 138
            description: |
              跟随焦点
            text: |
              /follow focus
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

    def render(self) -> str:
        """
        将该对象渲染成 SDM lua 文件中的一段代码. 例如:

        .. code-block:: lua

            [0] = {
                ["type"] = "b",
                ["name"] = "火球",
                ["ID"] = 0,
                ["text"] = "#showtooltip\n/cast 火球术",
                ["icon"] = 1,
            },
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
    对应着一个 :class:`SDMMacro` 对象的 YAML 文件. 本质上他是一个工厂函数, 自己本身是
     immutable 的, 但能生成 mutable 的 :class:`SDMMacro` 对象.

    Example::

        >>> sdm_file = SDMMacroFile(path=Path("test.yml"))
        >>> sdm_file.macro.render()
    """

    path: Path = attr.ib()

    @cached_property
    def content(self) -> str:
        return self.path.read_text()

    @property
    def macro(self) -> SDMMacro:
        return SDMMacro.parse_yml(self.content)


def render_sdm_lua(macro_list: T.List[SDMMacro]) -> str:
    """
    以一堆 :class:`SDMMacro` 为输入, 输出一个 SDM lua 文件的内容. 一个 SDM lua 文件
    本质上就是一堆 :class:`SDMMacro`.
    """
    # 确保没有重复的 id
    id_set = {macro.id for macro in macro_list}
    if len(id_set) != len(macro_list):
        macro_id_list = [macro.id for macro in macro_list]
        raise ValueError(
            "Cannot render SDM lua! Found duplicate id in 'macro_list'."
            f"macro id list: {macro_id_list}"
        )
    return _sdm_template.render(macro_list=macro_list)


# ------------------------------------------------------------------------------
# Todo: 添加从 SDM lua 文件中解析出一堆 SDMMacro 的方法.
# ------------------------------------------------------------------------------
