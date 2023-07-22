# -*- coding: utf-8 -*-

import pytest
from wow_wtf_manager.config.base import BaseConfig


def test():
    with pytest.raises(NotImplementedError):
        BaseConfig().build()
    with pytest.raises(NotImplementedError):
        BaseConfig().apply()


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.config.base", preview=False)
