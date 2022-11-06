# -*- coding: utf-8 -*-

import typing as T

from functools import cached_property
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

import lupa
from lupa import LuaRuntime

from wow_wtf_manager.lua_lib import lua_table_to_dict

lua = LuaRuntime(
    # unpack_returned_tuples=True
)


@attr.s
class SDMLua(AttrsClass):
    path: Path = attr.ib()

    # derived attributes
    sdm_version: str = attr.ib(default="1.8.3")
    sdm_listFilters: T.Dict[str, bool] = attr.ib(default=None)
    sdm_iconSize: int = attr.ib(default=36)
    sdm_mainContents: T.Dict[int, int] = attr.ib(default=None)
    sdm_macros: T.Dict[int, T.Dict[str, T.Any]] = attr.ib(default=None)

    def __attrs_post_init__(self):
        lua_code = self.path.read_text()
        lua.execute(lua_code)
        g = lua.globals()
        self.sdm_version = g.sdm_version
        self.sdm_listFilters = lua_table_to_dict(g.sdm_listFilters)
        self.sdm_iconSize = g.sdm_iconSize
        self.sdm_mainContents = lua_table_to_dict(g.sdm_mainContents)
        self.sdm_macros = lua_table_to_dict(g.sdm_macros)


# t = lua.eval(lua_code)
# print(t)
from rich import print as rprint

sdm_lua = SDMLua(path=Path("sdm.lua"))
rprint(sdm_lua)
