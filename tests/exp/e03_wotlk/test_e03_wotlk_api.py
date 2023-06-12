# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk import api


def test():
    _ = api.AppData
    _ = api.GameClientConfig
    _ = api.AccountUserInterfaceConfig
    _ = api.AccountSavedVariablesConfig
    _ = api.CharacterUserInterfaceConfig
    _ = api.CharacterChatConfig
    _ = api.CharacterKeybindingConfig
    _ = api.CharacterAddonsConfig
    _ = api.CharacterLayoutConfig
    _ = api.CharacterSavedVariablesConfig
    _ = api.Setup


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.exp.e03_wotlk.api", preview=False)
