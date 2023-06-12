# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf_manager.exp.e03_wotlk.sdm.model import (
    SDMMacroTypeEnum,
    SDMMacro,
    SDMLua,
)

dir_here = Path.dir_here(__file__)

path_global_yml = dir_here / "parser" / "sample-global.yml"
path_character_yml = dir_here / "parser" / "sample-character.yml"
path_lua = dir_here / "SuperDuperMacro.lua"


class TestSDMMacro:
    def test_init(self):
        macro = SDMMacro(name="test")
        assert macro.character is None

    def test_parser(self):
        global_macro = SDMMacro.from_yaml_file(path_global_yml)
        assert global_macro.name == "interrupt"
        assert global_macro.character.name is None
        assert global_macro.id == 1
        assert global_macro.type == SDMMacroTypeEnum.button
        assert global_macro.icon == 1
        assert global_macro.text == (
            "#showtooltip\n" "/stopcasting\n" "/cast Counterspell"
        )
        assert global_macro.is_global() is True
        lua_code = global_macro.render()
        _ = lua_code
        # print(lua_code)

        character_macro = SDMMacro.from_yaml_file(path_character_yml)
        assert character_macro.name == "interrupt"
        assert character_macro.character.name == "Admin"
        assert character_macro.character.realm == "Azerothcore"
        assert character_macro.id == 2
        assert character_macro.type == SDMMacroTypeEnum.button
        assert character_macro.icon == 1
        assert character_macro.text == (
            "#showtooltip\n" "/stopcasting\n" "/cast Counterspell"
        )
        assert character_macro.is_global() is False
        lua_code = global_macro.render()
        _ = lua_code
        # print(lua_code)


class TestSDMLua:
    def test(self):
        sdm_lua = SDMLua(
            path_lua=path_lua,
            macros=[
                SDMMacro.from_yaml_file(path_global_yml),
                SDMMacro.from_yaml_file(path_character_yml),
            ],
        )
        lua_code = sdm_lua.render()
        _ = lua_code
        # print(lua_code)


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.exp.e03_wotlk.sdm.model", preview=False)
