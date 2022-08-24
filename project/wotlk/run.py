# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.asso import Asso, WtfForm
from wow_wtf_manager.app.e03_wotlk.warmane.wtf import WarmaneWTF
from wow_wtf_manager.app.e03_wotlk.warmane.group import WarmaneGroup

warmane_wtf_form = WtfForm([
    # Asso(
    #     WarmaneWTF.GameClient.c3_1600_900_minimal,
    #     WarmaneGroup.cg_all_character,
    # )

    WarmaneWTF.CharacterUserInterface.default, WarmaneGroup.cg_all_character
])
# warmane_wtf_form.plan()
warmane_wtf_form.apply()
