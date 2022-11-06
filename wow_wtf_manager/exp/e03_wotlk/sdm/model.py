# -*- coding: utf-8 -*-

import typing as T
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

dir_here = Path.dir_here(__file__)
path_sdm_template = dir_here / "sdm.tpl"

sdm_template = Template(path_sdm_template.read_text())


@attr.s
class Macro:
    """
    定义了一个魔兽世界中的 SDM 宏命令的抽象, 目前只支持 Button + Global 这一种模式.
    """
    name: str = attr.ib()
    content: str = attr.ib()

    def encode_content(self) -> str:
        return self.content.replace("\n", "\\n")


def render_sdm(macro_list: T.List[Macro]) -> str:
    return sdm_template.render(macro_list=macro_list)


@attr.s
class MacroFile:
    """
    以文件形式存在的一个宏.
    """
    path: Path

    @property
    def macro(self) -> Macro:
        return Macro(
            name=self.path.basename,
            content=self.path.read_text(encoding="utf-8").strip()
        )
