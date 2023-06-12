# -*- coding: utf-8 -*-

from wow_wtf_manager.app.e03_wotlk_example.sdm_setup import sdm_setup

# dry_run = True  # for testing
dry_run = False  # *** THIS WILL APPLY CHANGES TO YOUR WTF FILEs ***

sdm_setup.apply(dry_run=dry_run)
