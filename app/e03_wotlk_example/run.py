# -*- coding: utf-8 -*-

from wow_wtf_manager.logger import logger
from wow_wtf_manager.app.e03_wotlk_example.setup import setup

# dry_run = True # for testing
dry_run = False  # *** THIS WILL APPLY CHANGES TO YOUR WTF FILEs ***

with logger.disabled(
    # disable=True, # DON't show log
    disable=False, # show log
):
    setup.show_game_client()
    setup.apply_game_client(dry_run=dry_run)
    setup.apply_account_user_interface(dry_run=dry_run)
    setup.apply_account_saved_variables(dry_run=dry_run)
    setup.apply_character_user_interface(dry_run=dry_run)
    setup.apply_character_chat(dry_run=dry_run)
    setup.apply_character_keybinding(dry_run=dry_run)
    setup.apply_character_layout(dry_run=dry_run)
    setup.apply_character_addons(dry_run=dry_run)
    setup.apply_character_saved_variables(dry_run=dry_run)
