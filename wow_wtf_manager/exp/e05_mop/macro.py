# -*- coding: utf-8 -*-

"""
Macro management.
"""

import typing as T
import random

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path


@attr.s
class Macro(AttrsClass):
    """
    Represent a WoW Macro, example::

        VER 3 000000000015331D "Invite Team" "INV_Misc_QuestionMark"
        /inv char2
        /inv char3
        /inv char4
        /inv char5
        END
    """
    revision: int = attr.ib()
    macro_id: str = attr.ib()
    name: str = attr.ib()
    icon: str = attr.ib(default="INV_Misc_QuestionMark")
    content: str = attr.ib(default="")

    @property
    def header(self) -> str:
        return f"VER {self.revision} {self.macro_id} \"{self.name}\" \"{self.icon}\""

    @property
    def footer(self) -> str:
        return "END"

    @property
    def content_lines(self) -> T.List[str]:
        return self.content.split("\n")

    def dump(self) -> str:
        return "\n".join([self.header, self.content, self.footer])

    @staticmethod
    def rand_id() -> str:
        return "000000000{}{}".format(
            str(random.randint(1, 999_999)).zfill(6),
            random.choice("A,B,C,D,E,F".split(","))
        )


@attr.s
class MacroTxt(AttrsClass):
    """
    Represent a ``macro-cache.txt`` file.
    """
    path: str = attr.ib()
    macros: T.List[Macro] = attr.ib()
    macros_id_mapper: T.Dict[int, Macro] = attr.ib(factory=dict)
    macros_name_mapper: T.Dict[str, Macro] = attr.ib(factory=dict)

    @staticmethod
    def _parse_header(header: str) -> T.Tuple[int, str, str, str]:
        parts = header.split(" ")
        revision = int(parts[1])
        macro_id = parts[2]
        name = " ".join(parts[3:-1])[1:-1]
        icon = parts[-1][1:-1]
        return revision, macro_id, name, icon

    @staticmethod
    def _is_macro_header(line: str) -> bool:
        try:
            if line.startswith("VER"):
                _ = int(line.split(" ")[1])
                return True
            return False
        except:
            return False

    @staticmethod
    def _is_macro_footer(line: str) -> bool:
        return line == "END"

    @classmethod
    def parse(cls, path: str) -> 'MacroTxt':
        """
        :param path: a ``macros-cache.txt`` file
        """
        content = Path(path).read_text()
        headers: T.List[str] = list()
        footers: T.List[str] = list()
        macros = list()

        is_in_macro_context = False
        for line in content.split("\n"):
            if cls._is_macro_header(line):
                headers.append(line)
                revision, macro_id, name, icon = cls._parse_header(line)
                macro_lines = list()
                is_in_macro_context = True
                continue

            if cls._is_macro_footer(line):
                footers.append(line)
                macro = Macro(
                    revision=revision,
                    macro_id=macro_id,
                    name=name,
                    icon=icon,
                    content="\n".join(macro_lines),
                )
                macros.append(macro)
                is_in_macro_context = False
                continue

            if is_in_macro_context:
                macro_lines.append(line)

        if not (len(macros) == len(headers) == len(footers)):  # pragma: no cover
            raise ValueError(f"{path!r} is not a valid macro.txt file!")

        return cls(path=path, macros=macros)

    def dump(self) -> str:
        return "\n".join([
            macro.dump()
            for macro in self.macros
        ])

    def to_file(self, path: str = None):  # pragma: no cover
        """
        Dump to macro.txt file

        :param path: optional file path.
        """
        if path is None:
            path = self.path
        Path(path).write_text(self.dump())

    def has_duplicate_id(self) -> bool:
        return len({macro.macro_id for macro in self.macros}) < len(self.macros)

    def has_duplicate_name(self) -> bool:
        return len({macro.name for macro in self.macros}) < len(self.macros)

    def ensure_no_duplicate_id(self):
        if self.has_duplicate_id():  # pragma: no cover
            raise ValueError
        else:
            self.macros_id_mapper = {
                macro.macro_id: macro
                for macro in self.macros
            }

    def ensure_no_duplicate_name(self):
        if self.has_duplicate_name():  # pragma: no cover
            raise ValueError
        else:
            self.macros_name_mapper = {
                macro.name: macro
                for macro in self.macros
            }

    def rand_new_id(self) -> int:
        for _ in range(10):
            id = Macro.rand_id()
            if id not in self.macros_id_mapper:
                return id


def apply_macros_cache_txt(
    macros_data_file: str,
    game_client_file: str,
    plan: bool = False,
):
    """
    把一个自定义的 macros-cache.txt 中的宏定义合并到游戏客户端中的 macros-cache.txt
    中去.

    这里要非常注意. 游戏客户端中的宏都是有 ID 的, 这些 ID 是服务器端给自动指定的. 动作条
    上的按钮需要靠这些 ID 来找到到底使用哪个宏命令. 如果你有一个宏的内容改了, 名字不变, 但是
    你在本地编辑的时候的 ID 和客户端中的 ID 不一致, 那么会出现宏的内容确实更新了, 但是 ID
    也变了, 导致动作条上已经放好的按钮消失了. 我们希望避免这一情况.

    所以我们在合并的时候, 要根据宏的名字来定位, 如果对已经存在的宏进行修改, 我们不能修改 ID.
    """
    macro_txt_data = MacroTxt.parse(macros_data_file)
    if Path(game_client_file).exists():
        macro_txt_game_client = MacroTxt.parse(game_client_file)
    else:
        macro_txt_game_client = MacroTxt(
            path=game_client_file,
            macros=[],
        )

    macro_txt_data.ensure_no_duplicate_id()
    macro_txt_data.ensure_no_duplicate_name()
    macro_txt_game_client.ensure_no_duplicate_id()
    macro_txt_game_client.ensure_no_duplicate_name()

    for macro1 in macro_txt_data.macros:
        if macro1.name in macro_txt_game_client.macros_name_mapper:
            macro2 = macro_txt_game_client.macros_name_mapper[macro1.name]
            macro2.icon = macro1.icon
            macro2.content = macro1.content
        else:
            new_macro_id = macro_txt_game_client.rand_new_id()
            macro1.revision = 1
            macro1.macro_id = new_macro_id
            macro_txt_game_client.macros.append(macro1)

    if plan is False:
        macro_txt_game_client.to_file()
