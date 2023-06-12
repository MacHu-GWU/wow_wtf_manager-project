# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk.sdm.api import SDMMacroModuleGenerator
from wow_wtf_manager.app.e03_wotlk_example.paths import dir_sdm, path_sdm_macro

sdm_macro_module_generator = SDMMacroModuleGenerator(
    import_line="from .paths import dir_sdm",
    dir_root_var_name="dir_sdm",
    dir_root=dir_sdm,
    path_sdm_macro_py=path_sdm_macro,
)
sdm_macro_module_generator.generate()
