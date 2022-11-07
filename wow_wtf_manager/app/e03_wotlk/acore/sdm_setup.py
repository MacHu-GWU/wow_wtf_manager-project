# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.sdm import AccountSDMSetup, ClientSDMSetup

from .group import AccountEnum
from .sdm_macro import Macros
from .form import dir_wow

client_sdm_setup = ClientSDMSetup(
    dir_wow=dir_wow,
)
