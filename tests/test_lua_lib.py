# -*- coding: utf-8 -*-

import os
import lupa

from wow_wtf_manager.lua_lib import (
    is_lua_table,
    lua_table_to_dict,
)

lua = lupa.LuaRuntime()


class TestBaseConfig:
    def test(self):
        data = {
            "a": 1,
            "b": [1, 2, 3],
            "c": {"x": 1, "y": 2, "z": 3},
            "d": [{"m": 1}, {"n": 2}]
        }
        t = lua.table_from(data)
        assert lua_table_to_dict(t) == data


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
        "--cov=wow_wtf_manager.lua_lib",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
