# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e03_wotlk.group import Character, CharacterGroup


class TestCharacter:
    def test(self):
        char1 = Character.from_string("acc1.serv.char2")
        char2 = Character.from_string("acc2.serv.char1")
        assert char1 < char2
        assert char2.sort_key > char1.sort_key
        assert len({char1, char1}) == 1
        assert len({char1, char2}) == 2

        l = [char2, char1]
        l.sort()
        assert l[0].account == "Acc1"


class TestCharacterGroup:
    def test(self):
        char1 = Character.from_string("acc1.serv.char1")
        char2 = Character.from_string("acc1.serv.char2")
        char3 = Character.from_string("acc1.serv.char3")
        char4 = Character.from_string("acc1.serv.char4")
        char5 = Character.from_string("acc1.serv.char5")
        char6 = Character.from_string("acc1.serv.char6")

        cg_1 = CharacterGroup(
            char_or_group_list=[char1, char2],
        )
        cg_2 = CharacterGroup(
            char_or_group_list=[char3, char4],
        )
        cg_3 = CharacterGroup(
            char_or_group_list=[cg_1, cg_2, char5, char6],
        )
        assert len(cg_1.char_list) == 2
        assert len(cg_2.char_list) == 2
        assert len(cg_3.char_list) == 6

        cg_a = CharacterGroup([char1, char2])
        cg_b = CharacterGroup([char2, char3])

        cg = CharacterGroup.union(cg_a, cg_b)
        assert len(cg.char_list) == 3
        assert cg.char_list[2].name == "Char3"

        cg = CharacterGroup.intersect(cg_a, cg_b)
        assert len(cg.char_list) == 1
        assert cg.char_list[0].name == "Char2"

        cg = CharacterGroup.difference(cg_a, cg_b)
        assert len(cg.char_list) == 1
        assert cg.char_list[0].name == "Char1"


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
        "--cov=wow_wtf_manager.exp.e03_wotlk.group",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
