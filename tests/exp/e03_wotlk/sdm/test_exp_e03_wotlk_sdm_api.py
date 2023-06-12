# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.sdm import api


def test():
    _ = api.SDMMacroTypeEnum
    _ = api.SDMCharacter
    _ = api.SDMMacro
    _ = api.SDMLua
    _ = api.SDMMacroFile
    _ = api.AccountSDMSetup
    _ = api.ClientSDMSetup
    _ = api.SDMMacroModuleGenerator


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.exp.e03_wotlk.sdm.api", preview=False)
