# -*- coding: utf-8 -*-

from pathlib_mate import Path

from wow_wtf_manager.config.file import (
    FileConfig,
)


class TestFileConfig:
    def test(self):
        path = Path(__file__)
        file_config = FileConfig.new(path_input=path)
        assert file_config.build() == path.read_text()


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.config.file", preview=False)
