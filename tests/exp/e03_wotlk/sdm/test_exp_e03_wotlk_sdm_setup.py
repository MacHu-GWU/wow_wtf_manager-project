# -*- coding: utf-8 -*-

from pathlib_mate import Path

from wow_wtf_manager.logger import logger
from wow_wtf_manager.models.api import (
    Account,
    Realm,
    Character,
)
from wow_wtf_manager.exp.e03_wotlk.sdm.setup import (
    SDMMacroFile,
    AccountSDMSetup,
    ClientSDMSetup,
)

dir_here = Path.dir_here(__file__)

global_macro = SDMMacroFile(dir_here / "parser" / "sample-global.yml")
character_macro = SDMMacroFile(dir_here / "parser" / "sample-character.yml")


class TestClientSDMSetup:
    def _test(self):
        client_setup = ClientSDMSetup(dir_wtf=dir_here)

        account1 = Account.new("acc1")
        account2 = Account.new("acc2")

        char1 = Character.new(Realm.new(account1, "acore"), "mage1")
        char2 = Character.new(Realm.new(account1, "acore"), "mage2")

        client_setup.add_macros_to_account(
            account=[account1, account2],
            sdm_files=[global_macro],
        )
        client_setup.add_macros_to_character(
            character=[char1, char2],
            sdm_files=[character_macro],
        )
        client_setup.apply(dry_run=True)
        pass

    def test(self):
        with logger.disabled(
            disable=True, # DON'T show log
            # disable=False,  # show log
        ):
            print("")
            self._test()


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.exp.e03_wotlk.sdm.setup", preview=False)
