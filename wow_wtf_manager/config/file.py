# -*- coding: utf-8 -*-

"""
该模块实现了对单个配置文件的类型的管理. 所谓管理的本质就是:

1. 从数据中读取配置的模板
2. 然后输入参数生成最终的数据
3. 将数据文件写入到指定的位置
"""

import typing as T
import attr
import jinja2
from pathlib_mate import Path

from .base import BaseConfig


@attr.define
class FileConfig(BaseConfig):
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
