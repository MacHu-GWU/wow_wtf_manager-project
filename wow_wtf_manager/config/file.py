# -*- coding: utf-8 -*-

"""
该模块实现了对单个配置文件的抽象, 以便于进行管理.
"""

import typing as T
import attr
import jinja2
from pathlib_mate import Path

from .base import BaseConfig


@attr.define
class FileConfig(BaseConfig):
    """
    单个配置文件的抽象.

    例如, 游戏的按键绑定 bindings-cache.wtf 文件就是单个配置文件的实例. 而对多个账号的这个的
    文件进行管理的本质就是:

    1. 从数据中读取配置的模板.
    2. 根据输入参数 (包括账号名, 服务器名, 角色名) 生成最终的数据.
    3. 将最终数据文件写入到指定的位置.
    """
    path_input: Path = attr.field(converter=Path)
    template: T.Optional[jinja2.Template] = attr.field()

    @classmethod
    def new(
        cls,
        path_input: T.Union[str, Path],
    ):
        """
        :param path_input: 配置文件模板的路径
        """
        path_input = Path(path_input)
        template = jinja2.Template(source=path_input.read_text())
        return cls(path_input=path_input, template=template)

    def build(self) -> str:
        """
        单个文件的配置文件情况下生成最终的数据的默认实现就是原封不动的拷贝.
        """
        return self.path_input.read_text()
