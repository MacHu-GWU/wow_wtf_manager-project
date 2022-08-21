# -*- coding: utf-8 -*-

"""
Macro management.
"""

import typing as T

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path


@attr.s
class Macro(AttrsClass):
    """
    Represent a WoW Macro, example::

        MACRO 3 "InviteTeam" INV_Misc_QuestionMark
        /inv char2
        /inv char3
        /inv char4
        /inv char5
        END
    """
    id: int = attr.ib()
    name: str = attr.ib()
    icon: str = attr.ib()
    content: str = attr.ib()

    @property
    def header(self) -> str:
        return f"MACRO {self.id} \"{self.name}\" {self.icon}"

    @property
    def footer(self) -> str:
        return "END"

    @property
    def content_lines(self) -> T.List[str]:
        return self.content.split("\n")

    def dump(self) -> str:
        return "\n".join([self.header, self.content, self.footer])


@attr.s
class MacroTxt(AttrsClass):
    """
    Represent a ``macro-cache.txt`` file.
    """
    path: str = attr.ib()
    macros: T.List[Macro] = attr.ib()

    @staticmethod
    def _parse_header(header: str) -> T.Tuple[int, str, str]:
        parts = header.split(" ")
        macro_id = int(parts[1])
        name = " ".join(parts[2:-1])[1:-1]
        icon = parts[-1]
        return macro_id, name, icon

    @staticmethod
    def _is_macro_header(line: str) -> bool:
        try:
            if line.startswith("MACRO"):
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
        content = Path(path).read_text()
        headers: T.List[str] = list()
        footers: T.List[str] = list()
        macros = list()

        is_in_macro_context = False
        for line in content.split("\n"):
            if cls._is_macro_header(line):
                headers.append(line)
                macro_id, name, icon = cls._parse_header(line)
                macro_lines = list()
                is_in_macro_context = True
                continue

            if cls._is_macro_footer(line):
                footers.append(line)
                macro = Macro(
                    id=macro_id,
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
