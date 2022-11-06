# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e03_wotlk.sdm.model import (
    SDMMacro, SDMMacroFile,
    render_sdm_lua,
)

dir_sdm = dir_tests / "e03_wotlk" / "sdm"


class TestSDMMacroFile:
    def test(self):
        path = dir_sdm / "sample.yml"
        macro = SDMMacro.parse_file(path)
        assert macro.name == "interrupt"
        assert macro.content == (
            "#showtooltip\n"
            "/stopcasting\n"
            "/cast Counterspell"
        )
        print(render_sdm_lua([macro,]))





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
        "--cov=wow_wtf_manager.exp.e03_wotlk.sdm.model",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
