# -*- coding: utf-8 -*-

import pytest
from pathlib_mate import Path

from wow_wtf_manager.exp.e03_wotlk.sdm.saved_variable import (
    SDMMacroTypeEnum,
    SDMMacro,
    SDMMacroFile,
    render_sdm_lua,
)

dir_here = Path.dir_here(__file__)
path_global_yml = dir_here / "parser" / "sample-global.yml"
path_character_yml = dir_here / "parser" / "sample-character.yml"


class TestSDMMacro:
    def test_init(self):
        macro = SDMMacro(name="test")
        assert macro.character is None
        assert macro.is_global() is True

        macro.set_id(10)
        assert macro.id == 10

        macro.set_char(name="Admin", realm="Azerothcore")
        assert macro.character.name == "Admin"
        assert macro.character.realm == "Azerothcore"
        assert macro.is_global() is False

        macro.set_char(name="Player", realm="Azerothcore")
        assert macro.character.name == "Player"
        assert macro.character.realm == "Azerothcore"

    def test_parser(self):
        macro_list = list()
        content = path_global_yml.read_text()

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
        content = path_character_yml.read_text()

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

        # render sdm lua
        lua_code = render_sdm_lua(macro_list)
        # print(lua_code)

        # test error handling
        with pytest.raises(Exception):
            render_sdm_lua([macro, macro])


class TestSDMMacroFile:
    def test(self):
        _ = SDMMacroFile(path_global_yml).macro


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(
        __file__,
        "wow_wtf_manager.exp.e03_wotlk.sdm.saved_variable",
        preview=False,
    )
