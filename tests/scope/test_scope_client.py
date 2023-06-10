# -*- coding: utf-8 -*-

from pathlib_mate import Path

from wow_wtf_manager.scope.client import (
    BaseScope,
    Client,
    Account,
    Realm,
    Character,
    ClientConfig,
    AccountKeyBindingConfig,
    AccountUserInterfaceConfig,
    AccountAddonSavedVariablesConfig,
    CharacterKeyBindingConfig,
    CharacterChatConfig,
    CharacterUserInterfaceConfig,
    CharacterLayoutConfig,
    CharacterAddonSavedVariablesConfig,
)

dir_here = Path.dir_here(__file__)
dir_wtf = dir_here.joinpath("WTF")


class TestClientConfig:
    def test(self):
        # variables
        client = Client.new(locale="enUS", dir_wtf=dir_wtf.abspath)
        acc1 = Account.new(account="acc1")
        realm1 = Realm.new(acc1, realm="realm1")
        char1 = Character.new(realm1, character="char1")

        # scope enum
        client_config = ClientConfig(
            client=Client.new(
                locale="enUS",
                dir_wtf=dir_wtf.abspath,
            )
        )

        account_key_binding_config = AccountKeyBindingConfig(
            client=client, account=acc1
        )
        account_user_interface_config = AccountUserInterfaceConfig(
            client=client, account=acc1
        )
        account_addon_saved_variables_config = AccountAddonSavedVariablesConfig(
            client=client, account=acc1, addon="Atlas"
        )

        character_key_binding_config = CharacterKeyBindingConfig(
            client=client, character=char1
        )
        character_chat_config = CharacterChatConfig(client=client, character=char1)
        character_user_interface_config = CharacterUserInterfaceConfig(
            client=client, character=char1
        )
        character_layout_config = CharacterLayoutConfig(client=client, character=char1)
        character_addon_saved_variables_config = CharacterAddonSavedVariablesConfig(
            client=client, character=char1, addon="Atlas"
        )

        # test def path_output(self)
        assert client_config.path_output.abspath.endswith("WTF/Config.wtf")
        assert account_key_binding_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/bindings-cache.wtf"
        )
        assert account_user_interface_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/config-cache.wtf"
        )
        assert account_addon_saved_variables_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/SavedVariables/Atlas.lua"
        )
        assert character_key_binding_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/realm1/Char1/bindings-cache.wtf"
        )
        assert character_chat_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/realm1/Char1/chat-cache.txt"
        )
        assert character_user_interface_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/realm1/Char1/config-cache.wtf"
        )
        assert character_layout_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/realm1/Char1/layout-local.txt"
        )
        assert character_addon_saved_variables_config.path_output.abspath.endswith(
            "WTF/Account/ACC1/realm1/Char1/SavedVariables/Atlas.lua"
        )

        # type typing
        for scope in [
            client_config,
            account_key_binding_config,
            account_user_interface_config,
            account_addon_saved_variables_config,
            character_key_binding_config,
            character_chat_config,
            character_user_interface_config,
            character_layout_config,
            character_addon_saved_variables_config,
        ]:
            assert isinstance(scope, BaseScope)


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.scope.client", preview=False)
