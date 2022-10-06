# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_wotlk_acore_project
from wow_wtf_manager.app.e03_wotlk.acore.group import (
    AccountGroup, CharacterGroup, AccountSavedVariableGroup
)
from wow_wtf_manager.app.e03_wotlk.acore.form import (
    acore_wtf_form,
)


class TestCharacterGroup:
    def test(self):
        assert sum([
            len(CharacterGroup.cg_paladin),
            len(CharacterGroup.cg_non_paladin),
        ]) == len(CharacterGroup.cg_all_character)

        assert sum([
            len(CharacterGroup.cg_warrior_and_dk),
            len(CharacterGroup.cg_non_warrior_and_dk),
        ]) == len(CharacterGroup.cg_all_character)

        assert sum([
            len(CharacterGroup.cg_multibox_master_paladin),
            len(CharacterGroup.cg_multibox_master_non_paladin),
        ]) == 2

        assert sum([
            len(CharacterGroup.cg_multibox_master_paladin),
            len(CharacterGroup.cg_multibox_master_non_paladin),
            len(CharacterGroup.cg_multibox_slave_paladin),
            len(CharacterGroup.cg_multibox_slave_non_paladin),
        ]) == len(CharacterGroup.cg_all_character)


class TestWtfForm:
    def test(self):
        # 在单元测试里我们不希望将生成的 WTF 文件覆盖游戏客户端中的文件,
        # 所以我们将生成的 WTF 文件放在 本地的测试文件夹
        acore_wtf_form.dir_wow = dir_wotlk_acore_project / "world-of-warcraft"
        acore_wtf_form.__attrs_post_init__()
        acore_wtf_form.verbose = False
        acore_wtf_form.apply()

        acore_wtf_form.apply_account_saved_variables_config()

        acore_wtf_form.apply_character_addon_config()
        acore_wtf_form.apply_character_layout_config()
        acore_wtf_form.apply_character_saved_variables_config()


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=wow_wtf_manager.exp.e03_wotlk.form",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
