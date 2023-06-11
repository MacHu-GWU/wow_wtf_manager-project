# -*- coding: utf-8 -*-

from wow_wtf_manager.app1.e03_wotlk.example.setup import setup

# dry_run = True # for testing
dry_run = False # *** THIS WILL APPLY CHANGES TO YOUR WTF FILEs ***

setup.apply_game_client(dry_run=dry_run)
