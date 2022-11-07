# -*- coding: utf-8 -*-

import pytest
from wow_wtf_manager.app.e03_wotlk.acore.sdm_setup import client_sdm_setup
from wow_wtf_manager.paths import dir_wotlk_acore_project


def test():
    client_sdm_setup.dir_wow = dir_wotlk_acore_project / "world-of-warcraft"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
