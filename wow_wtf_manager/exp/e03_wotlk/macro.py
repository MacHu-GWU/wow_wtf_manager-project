# -*- coding: utf-8 -*-

"""
Macro management.
"""

import typing as T

import attr
from attrs_mate import AttrsClass


@attr.s
class Macro(AttrsClass):
    id: int = attr.ib()
    name: str = attr.ib()
    icon: str = attr.ib()
    content: str = attr.ib()

    @property
    def content_lines(self) -> T.List[str]:
        return []


@attr.s
class MacroTxt(AttrsClass):
    path: str = attr.ib()
    macros: T.List[Macro] = attr.ib()

    @classmethod
    def parse(cls, path: str) -> 'MacroTxt':
        raise NotImplementedError
