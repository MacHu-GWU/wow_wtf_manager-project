# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e03_wotlk.macro import MacroTxt, Macro


class TestMacroTxt:
    def test_parse_header(self):
        macro_id, name, icon = MacroTxt._parse_header(
            'MACRO 123 "MyMacro" INV_Misc_QuestionMark'
        )
        assert macro_id == 123
        assert name == "MyMacro"
        assert icon == "INV_Misc_QuestionMark"

        macro_id, name, icon = MacroTxt._parse_header(
            'MACRO 456 "My Other Macro" INV_Misc_QuestionMark'
        )
        assert macro_id == 456
        assert name == "My Other Macro"
        assert icon == "INV_Misc_QuestionMark"

    def test_is_macro_header(self):
        assert MacroTxt._is_macro_header('MACRO 123 "MyMacro" INV_Misc_QuestionMark') is True
        assert MacroTxt._is_macro_header('MACRO abc "MyMacro" INV_Misc_QuestionMark') is False
        assert MacroTxt._is_macro_header('macro abc "MyMacro" INV_Misc_QuestionMark') is False

    def test_parse(self):
        macro_txt = MacroTxt.parse((dir_tests / "macro" / "account-macro.txt"))
        assert macro_txt.macros[0].id == 3
        assert macro_txt.macros[1].id == 1

        # print(macro_txt)


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
        "--cov=wow_wtf_manager.exp.e03_wotlk.macro",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
