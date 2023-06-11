# -*- coding: utf-8 -*-

from wow_wtf_manager.logger import logger
from wow_wtf_manager.app1.e03_wotlk.example.setup import setup

# dry_run = True # for testing
dry_run = False # *** THIS WILL APPLY CHANGES TO YOUR WTF FILEs ***


def _test():
    setup.client.dir_wtf.remove_if_exists()

    setup.show_game_client()
    setup.apply_game_client(dry_run=dry_run)
    setup.apply_account_user_interface(dry_run=dry_run)
    setup.apply_account_saved_variables(dry_run=dry_run)
    setup.apply_character_user_interface(dry_run=dry_run)
    setup.apply_character_chat(dry_run=dry_run)


def test():
    with logger.disabled(
        # disable=True,
        disable=False,
    ):
        print("")
        _test()


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test
    run_cov_test(__file__, "wow_wtf_manager.app1.e03_wotlk.example", is_folder=True, preview=False)

