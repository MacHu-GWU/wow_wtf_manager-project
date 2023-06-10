# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.models.client import Client

dir_here = Path.dir_here(__file__)
dir_wtf = dir_here.joinpath("WTF")


class TestClient:
    def test(self):
        client = Client.new(
            locale="enUS",
            dir_wtf=dir_wtf.abspath,
        )
        assert isinstance(client.dir_wtf, Path)


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.models.client", preview=False)
