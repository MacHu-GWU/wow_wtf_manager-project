# -*- coding: utf-8 -*-

from wow_wtf_manager.models.utils import right_zfill


def test_right_zfill():
    assert right_zfill("fat", 6) == "fat000"


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.models.utils", preview=False)
