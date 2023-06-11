# -*- coding: utf-8 -*-

"""
该模块用于更方便的枚举 WTF config 数据文件.
"""

import attr
from pathlib_mate import Path


@attr.define
class AppData:
    """
    一个命名空间对象. 可以方便的访问那些用于存放 WTF app data 的重要文件夹. 它是根据
    WOTLK 版本的客户端设计的.

    假设你用 ``${dir_root}`` 保存你的 WTF 配置数据. 那么你喜欢的配置文件就应该保存在这个目录
    下的各个子目录中. 这些子目录包括:

    - ``${dir_root}/01_game_client``
    - ``${dir_root}/11_account_user_interface``
    - ``${dir_root}/12_account_macros``
    - ``${dir_root}/13_account_saved_variables``
    - ``${dir_root}/21_character_user_interface``
    - ``${dir_root}/22_character_chat``
    - ``${dir_root}/23_character_keybindings``
    - ``${dir_root}/24_character_layout``
    - ``${dir_root}/25_character_addons``
    - ``${dir_root}/26_character_macros``
    - ``${dir_root}/27_character_saved_variables``
    """

    dir_root: Path = attr.field()

    @property
    def dir_01_game_client(self) -> Path:
        return self.dir_root.joinpath("01_game_client")

    @property
    def dir_11_account_user_interface(self) -> Path:
        return self.dir_root.joinpath("11_account_user_interface")

    @property
    def dir_12_account_macros(self) -> Path:
        return self.dir_root.joinpath("12_account_macros")

    @property
    def dir_13_account_saved_variables(self) -> Path:
        return self.dir_root.joinpath("13_account_saved_variables")

    @property
    def dir_21_character_user_interface(self) -> Path:
        return self.dir_root.joinpath("21_character_user_interface")

    @property
    def dir_22_character_chat(self) -> Path:
        return self.dir_root.joinpath("22_character_chat")

    @property
    def dir_23_character_keybindings(self) -> Path:
        return self.dir_root.joinpath("23_character_keybindings")

    @property
    def dir_24_character_layout(self) -> Path:
        return self.dir_root.joinpath("24_character_layout")

    @property
    def dir_25_character_addons(self) -> Path:
        return self.dir_root.joinpath("25_character_addons")

    @property
    def dir_26_character_macros(self) -> Path:
        return self.dir_root.joinpath("26_character_macros")

    @property
    def dir_27_character_saved_variables(self) -> Path:
        return self.dir_root.joinpath("27_character_saved_variables")
