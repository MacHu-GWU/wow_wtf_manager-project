# -*- coding: utf-8 -*-

from wow_wtf_manager.config import api


def test():
    _ = api.BaseConfig
    _ = api.FileConfig


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.config.api", preview=False)
