# -*- coding: utf-8 -*-

import os

from wow_wtf_manager.paths import dir_wotlk_warmane_project
from wow_wtf_manager.app.e03_wotlk.warmane.form import warmane_wtf_form


class TestWtfForm:
    def test(self):
        warmane_wtf_form.dir_wow = dir_wotlk_warmane_project / "world-of-warcraft"
        warmane_wtf_form.__attrs_post_init__()
        warmane_wtf_form.verbose = False
        warmane_wtf_form.apply()


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
