# -*- coding: utf-8 -*-

"""
``sdm_macro.py`` 是用来枚举所有的 ``${SDMMacro}.yml`` 文件的模块. 人类通常是专注于编辑
YAML 文件. 我们希望免除人类编辑 ``sdm_macro.py`` 并保证它和 YAML 文件一一对应的麻烦, 所以
开发了这个工具, 能自动扫描指定文件夹, 定位到那些 YAML 文件, 并自动生成 ``sdm_macro.py`` 的
内容.
"""

import attr
from pathlib_mate import Path


@attr.define
class SDMMacroYamlFile:
    """
    代表一个 SDMMacro Yaml 文件, 每一个文件都会变成 enum 里面的一行代码.
    """

    dir_root_var_name: str
    dir_root: Path
    path: Path

    def render(self) -> str:
        relpath = self.path.relative_to(self.dir_root)
        key = "sdm_" + (
            str(relpath)[:-4]  # remove ".yml"
            .replace("-", "_")  # replace "-" with "_"
            .replace("/", "____")  # replace "/" with "____" for MacOS / Linux
            .replace("\\", "____")  # replace "\\" with "____" for windows
        )
        join_args = ", ".join([f'"{part}"' for part in relpath.parts])
        sdm_file_path = f"{self.dir_root_var_name}.joinpath({join_args})"
        value = f"SDMMacroFile(path={sdm_file_path})"
        return f"{key} = {value}"


@attr.define
class SDMMacroModuleGenerator:
    """
    :param import_line: something like ``from wow_wtf_manager.paths import dir_wotlk_example_sdm``
    :param dir_root_var_name: the imported path variable name form the ``import_line``
    :param dir_root: the root directory of all SDMMacro Yaml files.
    :param path_sdm_macro_py: the path of ``sdm_macro.py`` file.
    """

    import_line: str
    dir_root_var_name: str
    dir_root: Path
    path_sdm_macro_py: Path

    def render(self):
        lines = [
            "# -*- coding: utf-8 -*-",
            "",
            self.import_line,
            "from wow_wtf_manager.exp.e03_wotlk.sdm.api import SDMMacroFile",
            "",
            "class Macros:",
        ]
        for path in Path.sort_by_abspath(
            self.dir_root.select_by_ext(".yml")
        ):
            line = SDMMacroYamlFile(
                dir_root_var_name=self.dir_root_var_name,
                dir_root=self.dir_root,
                path=path,
            ).render()
            lines.append(" " * 4 + line)
        return "\n".join(lines)

    def generate(self):
        self.path_sdm_macro_py.write_text(self.render())
