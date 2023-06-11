# -*- coding: utf-8 -*-

from wow_wtf_manager.scope import api


def test():
    _ = api.BaseScope
    _ = api.ClientScope
    _ = api.AccountKeyBindingScope
    _ = api.AccountUserInterfaceScope
    _ = api.AccountAddonSavedVariablesScope
    _ = api.CharacterUserInterfaceScope
    _ = api.CharacterChatScope
    _ = api.CharacterKeyBindingScope
    _ = api.CharacterLayoutScope
    _ = api.CharacterAddonsScope
    _ = api.CharacterAddonSavedVariablesScope


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.scope.api", preview=False)
