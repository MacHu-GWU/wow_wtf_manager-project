# -*- coding: utf-8 -*-

from wow_wtf_manager import api


def test():
    pass


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.api", preview=False)
