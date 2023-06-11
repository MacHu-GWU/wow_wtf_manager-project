# -*- coding: utf-8 -*-

from wow_wtf_manager import api


def test():
    _ = api.IS_WINDOWS
    _ = api.IS_MACOS
    _ = api.IS_LINUX
    _ = api.OS_NAME
    _ = api.OSEnum

    _ = api.Client
    _ = api.Account
    _ = api.Realm
    _ = api.Character

    _ = api.BaseConfig
    _ = api.FileConfig

    _ = api.BaseScope
    _ = api.ClientScope
    _ = api.AccountKeyBindingScope
    _ = api.AccountUserInterfaceScope
    _ = api.AccountAddonSavedVariablesScope
    _ = api.CharacterKeyBindingScope
    _ = api.CharacterChatScope
    _ = api.CharacterUserInterfaceScope
    _ = api.CharacterLayoutScope
    _ = api.CharacterAddonSavedVariablesScope

    _ = api.models
    _ = api.config
    _ = api.scope
    _ = api.wotlk


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.api", preview=False)
