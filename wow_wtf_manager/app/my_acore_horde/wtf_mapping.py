# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf.api import get_values, concat_lists, exp03_wotlk
from .acc_enum import (
    AccountEnum as AccEnum,
    CharacterEnum as CharEnum,
)
from .acc_group import (
    AccountGroupEnum as AccGrpEnum,
    CharacterGroupEnum as CharGrpEnum,
)
from .wtf_enum import (
    ClientConfigEnum,
    AccountUserInterfaceEnum as AuiEnum,
    AccountSavedVariablesEnum as AsvEnum,
    CharacterUserInterfaceEnum as CuiEnum,
    CharacterChatEnum as CcEnum,
    CharacterKeybindingsEnum as CkEnum,
    CharacterLayoutEnum as ClEnum,
    CharacterAddonsEnum as CaEnum,
    CharacterSavedVariablesEnum as CsvEnum,
)
from .wtf_group import (
    AsvGroupEnum,
    CsvGroupEnum,
)

Client = exp03_wotlk.Client
AccMap = exp03_wotlk.AccLvlMapping
CharMap = exp03_wotlk.CharLvlMapping
WtfMapping = exp03_wotlk.WtfMapping

dir_here = Path.dir_here(__file__)
dir_game_client = dir_here.joinpath("tmp", "world_of_warcraft_zhCN")  # Test
# dir_game_client = dir_here.joinpath("tmp", "world_of_warcraft_zhCN") # Real

client = exp03_wotlk.Client(
    locale="zhCN",
    dir=dir_game_client,
)
all_accounts = AccGrpEnum.all_accounts
all_characters = CharGrpEnum.all_characters


# ==============================================================================
# START of manual editing
# ==============================================================================
# ------------------------------------------------------------------------------
# client_config
# ------------------------------------------------------------------------------
# client_config = ClientConfigEnum.f_1176_664_minimal_graphic_sound
# client_config = ClientConfigEnum.f_1600_900_minimal_graphic_sound
client_config = ClientConfigEnum.f_1920_1080_max_graphic_sound
# client_config = ClientConfigEnum.f_1920_1080_minimal_graphic_sound
# client_config = ClientConfigEnum.f_3840_2160_max_graphic_sound

# ------------------------------------------------------------------------------
# acc_user_interface
# ------------------------------------------------------------------------------
acc_user_interface = AccMap.make_many(all_accounts, AuiEnum.default)

# ------------------------------------------------------------------------------
# acc_saved_variables
# ------------------------------------------------------------------------------
acc_saved_variables = AccMap.make_many(all_accounts, AsvGroupEnum.common)

# ------------------------------------------------------------------------------
# char_user_interface
# ------------------------------------------------------------------------------
char_user_interface = CharMap.make_many(all_characters, CuiEnum.default)

# ------------------------------------------------------------------------------
# char_chat
# ------------------------------------------------------------------------------
char_chat = CharMap.make_many(all_characters, CcEnum.default)

# ------------------------------------------------------------------------------
# char_keybinding
# ------------------------------------------------------------------------------
char_keybinding = concat_lists(
    CharMap.make_many(
        all_characters.difference(CharGrpEnum.warrior_and_dk), CkEnum.warrior_and_dk
    ),
    CharMap.make_many(
        all_characters.difference(CharGrpEnum.non_warrior_and_dk), CkEnum.default
    ),
)

# ------------------------------------------------------------------------------
# char_layout
# ------------------------------------------------------------------------------
char_layout = CharMap.make_many(all_characters, ClEnum.default)

# ------------------------------------------------------------------------------
# char_addons
# ------------------------------------------------------------------------------
char_addons = concat_lists(
    CharMap.make_many(
        CharGrpEnum.multiboxer_master_paladin,
        CaEnum.f_01_multiboxer_master_paladin,
    ),
    CharMap.make_many(
        CharGrpEnum.multiboxer_master_non_paladin,
        CaEnum.f_02_multiboxer_master_non_paladin,
    ),
    CharMap.make_many(
        CharGrpEnum.multiboxer_slave_paladin,
        CaEnum.f_03_multiboxer_slave_paladin,
    ),
    CharMap.make_many(
        CharGrpEnum.multiboxer_slave_non_paladin,
        CaEnum.f_04_multiboxer_slave_non_paladin,
    ),
)

# ------------------------------------------------------------------------------
# char_saved_variables
# ------------------------------------------------------------------------------
char_saved_variables = concat_lists(
    CharMap.make_many(
        all_characters,
        CsvGroupEnum.common,
    ),
)

# ==============================================================================
# END of manual editing
# ==============================================================================
# ------------------------------------------------------------------------------
# wtf_mapping
# ------------------------------------------------------------------------------
wtf_mapping = exp03_wotlk.WtfMapping(
    client=client,
    all_accounts=all_accounts,
    all_characters=all_characters,
    client_config=client_config,
    acc_user_interface=acc_user_interface,
    # acc_macros=acc_macros,
    acc_saved_variables=acc_saved_variables,
    char_user_interface=char_user_interface,
    char_chat=char_chat,
    char_keybinding=char_keybinding,
    char_layout=char_layout,
    char_addons=char_addons,
    # char_macros=char_macros,
    char_saved_variables=char_saved_variables,
)
