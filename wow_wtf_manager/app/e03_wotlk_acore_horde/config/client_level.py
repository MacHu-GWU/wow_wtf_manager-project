# -*- coding: utf-8 -*-

from wow_wtf_manager.exp.e03_wotlk import api as wotlk

from .app_data import app_data


def _new(filename: str) -> wotlk.GameClientConfig:
    return wotlk.GameClientConfig.new(app_data.dir_01_game_client.joinpath(filename))


class ClientConfigEnum:
    """
    对客户端的配置文件进行枚举. 其中 min 表示图像声音配置都很低, max 表示图像声音配置都很高.
    """

    r_1176_664_min = _new("1176-664-minimal-graphic-sound.txt")
    r_1600_900_min = _new("1600-900-minimal-graphic-sound.txt")
    r_1920_1080_min = _new("1920-1080-minimal-graphic-sound.txt")
    r_1920_1080_max = _new("1920-1080-max-graphic-sound.txt")
    r_3840_2160_max = _new("3840-2160-max-graphic-sound.txt")
