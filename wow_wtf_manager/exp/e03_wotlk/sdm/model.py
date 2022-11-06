# -*- coding: utf-8 -*-

import typing as T
from functools import cached_property

from yaml import load, Loader
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
from jinja2 import Template

dir_here = Path.dir_here(__file__)
path_sdm_template = dir_here / "sdm.tpl"

sdm_template = Template(path_sdm_template.read_text())


@attr.s
class SDMMacro(AttrsClass):
    """
    定义了一个魔兽世界中的 SDM 宏命令的抽象, 目前只支持 Button + Global 这一种模式.
    """
    name: str = attr.ib()
    content: str = attr.ib()

    def encode_text(self) -> str:
        return self.content.replace("\n", "\\n")

    @classmethod
    def parse_file(cls, path: Path) -> 'SDMMacro':
        content = path.read_text()
        data = load(content, Loader)
        return cls(
            name=data["name"],
            content=data["content"]
        )


@attr.s
class SDMMacroFile(AttrsClass):
    """
    以 YAML 文件形式存在的一个 SDM 宏.
    """
    path: Path = attr.ib()

    @cached_property
    def macro(self) -> SDMMacro:
        return SDMMacro.parse_file(self.path)


def render_sdm_lua(macro_list: T.List[SDMMacro]) -> str:
    return sdm_template.render(macro_list=macro_list)


def parse_sdm_lua(content: str):
    pass
