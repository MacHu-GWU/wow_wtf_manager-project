# -*- coding: utf-8 -*-

import pytest
from pathlib_mate import Path

from wow_wtf_manager.exp.e03_wotlk.sdm.setup import (
    Account,
    Character,
    SDMMacroFile,
    AccountSDMSetup,
    ClientSDMSetup,
)

dir_here = Path.dir_here(__file__)

global_macro = SDMMacroFile(dir_here / "parser" / "sample-global.yml")
character_macro = SDMMacroFile(dir_here / "parser" / "sample-character.yml")


class TestClientSDMSetup:
    def test(self):
        client_setup = ClientSDMSetup(dir_wow=dir_here)

        account1 = Account("acc1")
        account2 = Account("acc2")
        char1 = Character("acc1", "acore", "mage1")
        char2 = Character("acc2", "acore", "mage2")

        client_setup.add_macros_for_many_accounts(
            accounts=[account1, account2],
            files=[global_macro],
        )
        client_setup.add_macros_for_many_chars(
            chars=[char1, char2],
            files=[character_macro],
        )

        client_setup.apply(plan=True)


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(
        __file__,
        "wow_wtf_manager.exp.e03_wotlk.sdm.setup",
        preview=False,
    )
