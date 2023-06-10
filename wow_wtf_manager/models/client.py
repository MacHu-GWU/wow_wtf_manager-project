# -*- coding: utf-8 -*-

import typing as T

import attr
from pathlib_mate import Path


@attr.define
class Client:
    """
    代表着一个具体魔兽世界客户端.

    :param locale: 客户端语种
    :param dir_wtf: 客户端的 WTF 目录, 根据此目录可以定位其他的目录.
    """

    locale: str = attr.field()
    dir_wtf: Path = attr.field()

    @classmethod
    def new(
        cls,
        locale: str,
        dir_wtf: T.Union[str, Path],
    ) -> "Client":
        obj = cls(
            locale=locale,
            dir_wtf=Path(dir_wtf).absolute(),
        )
        return obj
