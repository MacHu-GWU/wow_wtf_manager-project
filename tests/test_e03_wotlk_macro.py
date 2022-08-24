# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e03_wotlk.macro import MacroTxt, Macro, apply_macros_cache_txt


class TestMacro:
    def test_dump(self):
        macro = Macro(
            id=1,
            name="Invite Team",
            icon="INV_Misc_QuestionMark",
            content=(
                "/inv char2\n"
                "/inv char3\n"
                "/inv char4\n"
                "/inv char5"
            )
        )
        assert len(macro.content_lines) == 4
        assert macro.dump() == (
            'MACRO 1 "Invite Team" INV_Misc_QuestionMark\n'
            '/inv char2\n'
            '/inv char3\n'
            '/inv char4\n'
            '/inv char5\n'
            'END'
        )


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
        macro_txt_file = dir_tests / "macro" / "account-macro.txt"
        macro_txt = MacroTxt.parse(macro_txt_file.abspath)

        assert macro_txt.macros[0].id == 3
        assert macro_txt.macros[0].content == (
            "/inv char2\n"
            "/inv char3\n"
            "/inv char4\n"
            "/inv char5"
        )
        assert macro_txt.macros[1].id == 1
        assert macro_txt.macros[1].content == "/y want to buy abc item!"
        assert macro_txt.dump() == (
            "MACRO 3 \"InviteTeam\" INV_Misc_QuestionMark\n"
            "/inv char2\n"
            "/inv char3\n"
            "/inv char4\n"
            "/inv char5\n"
            "END\n"
            "MACRO 1 \"BuyItem\" INV_Misc_QuestionMark\n"
            "/y want to buy abc item!\n"
            "END"
        )


def test_apply_macros_cache_txt():
    macros_data_file = dir_tests / "macro" / "macros_data_file.txt"
    game_client_file_backup = dir_tests / "macro" / "game_client_file_backup.txt"
    game_client_file = dir_tests / "macro" / "game_client_file.txt"
    game_client_file.write_text(game_client_file_backup.read_text())
    apply_macros_cache_txt(macros_data_file, game_client_file)


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
