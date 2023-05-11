# -*- coding: utf-8 -*-

import os
from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk.sdm.model import (
    SDMMacroTypeEnum,
    SDMMacro,
    SDMMacroFile,
    render_sdm_lua,
)

dir_here = Path.dir_here(__file__)


class TestSDMMacroFile:
    def test_init(self):
        macro = SDMMacro(name="test")
        assert macro.character is None

    def test_parser(self):
        macro_list = list()
        # --- sample-global.yml
        path = dir_here / "parser" / "sample-global.yml"
        content = path.read_text()

        # test parser
        macro = SDMMacro.parse_yml(content)
        assert macro.name == "interrupt"
        assert macro.character.name is None
        assert macro.id == 0
        assert macro.type == SDMMacroTypeEnum.button
        assert macro.icon == 1
        assert macro.text == ("#showtooltip\n" "/stopcasting\n" "/cast Counterspell")
        lua_code = macro.render()
        _ = lua_code
        macro_list.append(macro)

        # --- sample-character.yml
        path = dir_here / "parser" / "sample-character.yml"
        content = path.read_text()

        # test parser
        macro = SDMMacro.parse_yml(content)
        assert macro.name == "interrupt"
        assert macro.character.name == "Admin"
        assert macro.character.realm == "Azerothcore"
        assert macro.id == 0
        assert macro.type == SDMMacroTypeEnum.button
        assert macro.icon == 1
        assert macro.text == ("#showtooltip\n" "/stopcasting\n" "/cast Counterspell")
        lua_code = macro.render()
        _ = lua_code

        macro.id = 1
        macro_list.append(macro)

        lua_code = render_sdm_lua(macro_list)
        # print(lua_code)


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.exp.e03_wotlk.sdm", preview=False)