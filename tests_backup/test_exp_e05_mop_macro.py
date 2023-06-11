# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e05_mop.macro import MacroTxt, Macro, apply_macros_cache_txt

dir_root = dir_tests / "e05_mop" / "macro"


class TestMacro:
    def test_dump(self):
        macro = Macro(
            revision=3,
            macro_id="000000000015331D",
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
            'VER 3 000000000015331D "Invite Team" "INV_Misc_QuestionMark"\n'
            '/inv char2\n'
            '/inv char3\n'
            '/inv char4\n'
            '/inv char5\n'
            'END'
        )


class TestMacroTxt:
    def test_parse_header(self):
        revision, macro_id, name, icon = MacroTxt._parse_header(
            'VER 3 000000000015331D "Invite Team" "INV_Misc_QuestionMark"'
        )
        assert revision == 3
        assert macro_id == "000000000015331D"
        assert name == "Invite Team"
        assert icon == "INV_Misc_QuestionMark"

    def test_is_macro_header(self):
        assert MacroTxt._is_macro_header('VER 3 000000000015331D "Invite Team" "INV_Misc_QuestionMark"') is True
        assert MacroTxt._is_macro_header('VER abc 000000000015331D "Invite Team" "INV_Misc_QuestionMark"') is False
        assert MacroTxt._is_macro_header('ver 3 000000000015331D "Invite Team" INV_Misc_QuestionMark') is False

    def test_parse(self):
        macro_txt_file = dir_root / "account-macro.txt"
        macro_txt = MacroTxt.parse(macro_txt_file.abspath)
        assert macro_txt.macros[0].revision == 3
        assert macro_txt.macros[0].content == (
            "/inv char2\n"
            "/inv char3\n"
            "/inv char4\n"
            "/inv char5"
        )
        assert macro_txt.macros[1].macro_id == "0000000000625EE2"
        assert macro_txt.macros[1].content == "/s alice"
        assert macro_txt.dump() == (
            "VER 3 000000000015331D \"InvT1\" \"Spell_Shadow_Twilight\"\n"
            "/inv char2\n"
            "/inv char3\n"
            "/inv char4\n"
            "/inv char5\n"
            "END\n"
            "VER 3 0000000000625EE2 \"InvT2\" \"Spell_Shadow_Twilight\"\n"
            "/s alice\n"
            "END"
        )


def test_apply_macros_cache_txt():
    macros_data_file = dir_root / "macros_data_file.txt"
    game_client_file_backup = dir_root / "game_client_file_backup.txt"
    game_client_file = dir_root / "game_client_file.txt"
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
        "--cov=wow_wtf_manager.exp.e05_mop.macro",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
