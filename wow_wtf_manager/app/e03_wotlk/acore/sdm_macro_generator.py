# -*- coding: utf-8 -*-

"""
sdm_macro.py 是用来枚举所有的 MacroFile txt 文件的模块. 这个模块是跟 SuperDuperMacro
文件夹下众多的 txt 文件对应的. 本模块自动化了根据 SuperDuperMacro 里的文件自动生成
sdm_macro.py 代码的逻辑, 以便于人类进行编辑后自动更新这个模块.
"""

from pathlib_mate import Path
from wow_wtf_manager.paths import dir_wotlk_acore_project

lines = [
    "# -*- coding: utf-8 -*-",
    "",
    "from wow_wtf_manager.paths import dir_wotlk_acore_project",
    "from wow_wtf_manager.exp.e03_wotlk.sdm import SDMMacroFile",
    "",
    "class Macros:",
]

dir_sdm = dir_wotlk_acore_project / "SuperDuperMacro"
for dir in dir_sdm.select_dir(recursive=False):
    for p in Path.sort_by_fname(dir.select_by_ext(ext=".yml")):
        relpath = p.relative_to(dir_sdm)
        key = "sdm_" + (
            str(relpath)[:-4]
                .replace("-", "_")
                .replace("/", "____")
        )
        value = "dir_wotlk_acore_project.joinpath({}, {})".format(
            '"SuperDuperMacro"',
            ", ".join([
                f"\"{part}\""
                for part in relpath.parts
            ])
        )
        line = (
            f"    {key} = SDMMacroFile(path={value})"
        )
        lines.append(line)

dir_here = Path.dir_here(__file__)
path_sdm_macro_py = dir_here / "sdm_macro.py"
path_sdm_macro_py.write_text("\n".join(lines))
