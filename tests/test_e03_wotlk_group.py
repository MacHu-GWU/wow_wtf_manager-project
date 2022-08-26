# -*- coding: utf-8 -*-

import os

from ordered_set import OrderedSet
from wow_wtf_manager.exp.e03_wotlk.group import Account, Character


class TestAccount:
    def test(self):
        acc1 = Account("acc1")
        acc2 = Account("acc2")
        acc3 = Account("acc3")

        assert acc1 < acc2
        assert acc2 > acc1
        assert acc1 <= acc1
        assert acc1 >= acc1
        assert acc1 == acc1
        assert acc1 != acc2

        assert len(OrderedSet([acc1, acc1])) == 1
        assert len(OrderedSet([acc1, acc2])) == 2

        s1 = OrderedSet([acc1, acc2])
        s2 = OrderedSet([acc2, acc3])
        assert len(s1.union(s2)) == 3
        assert len(s1.intersection(s2)) == 1
        assert s1.difference(s2)[0] == acc1

        l = [acc2, acc1]
        l.sort()
        assert l[0].account == "acc1"


class TestCharacter:
    def test(self):
        char1 = Character.from_string("acc1.serv.char2")
        char2 = Character.from_string("acc2.serv.char1")
        char3 = Character.from_string("acc3.serv.char3")

        assert char1 < char2
        assert char2 > char1
        assert char1 <= char1
        assert char1 >= char1
        assert char1 == char1
        assert char1 != char2

        assert len(OrderedSet([char1, char1])) == 1
        assert len(OrderedSet([char1, char2])) == 2

        s1 = OrderedSet([char1, char2])
        s2 = OrderedSet([char2, char3])
        assert len(s1.union(s2)) == 3
        assert len(s1.intersection(s2)) == 1
        assert s1.difference(s2)[0] == char1

        l = [char2, char1]
        l.sort()
        assert l[0].account == "acc1"


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
