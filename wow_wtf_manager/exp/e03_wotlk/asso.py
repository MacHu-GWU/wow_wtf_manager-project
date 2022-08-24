# -*- coding: utf-8 -*-

import typing as T
import attr
from attrs_mate import AttrsClass

from .group import CharacterGroup
from .wtf import BaseConfig


@attr.s
class Asso(AttrsClass):
    """
    Association of WTF Config and Character Groups.
    """
    config: BaseConfig = attr.ib()
    group: CharacterGroup = attr.ib()


@attr.s
class WtfForm(AttrsClass):
    """
    A WTF config definition.
    """
    associations: T.List[Asso] = attr.ib(factory=list)

    def plan(self):
        pass

    def apply(self):
        for asso in self.associations:
            asso.config.apply(asso.group)
