# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass


#------------------------------------------------------------------------------
# 为各种具体的配置进行数据建模
#------------------------------------------------------------------------------
@attr.s
class Config(AttrsClass):
    """
    各种具体配置的基类.

    配置有很多种, 例如:

    - 游戏客户端启动配置
    - 插件配置
    - 快捷键配置
    - 宏命令
    - 插件的 SavedVariables
    """
    pass


@attr.s
class GameClientConfig(Config):
    """
    客户端设定, 图像质量, 声音等. 对应 ``WTF/config.wtf``
    """
    pass


@attr.s
class KeybindingConfig(Config):
    """
    快捷键绑定设置. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/bindings-cache.wtf``
    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/bindings-cache.wtf``
    """


@attr.s
class AccountMacroConfig(Config):
    """
    账号下所有服务器所有角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/macros-cache.txt``
    """


@attr.s
class CharacterMacroConfig(Config):
    """
    单个角色的宏命令设置. 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/macros-cache.txt``
    """


@attr.s
class GameInterfaceConfig(Config):
    """
    用户界面设置, 例如自动拾取, 显示血量百分比等. 对应:

    - 账户下所有角色: ``WTF/Account/${AccountName}/config-cache.txt``
    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/config-cache.txt``
    """


@attr.s
class LayoutConfig(Config):
    """
    用户界面窗口布局. 例如人物窗口, 背包窗口, 天赋窗口, 动作条的位置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/layout-local.txt``
    """


@attr.s
class ChatConfig(Config):
    """
    聊天窗口的配置. 对应:

    - 单个角色: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/chat-cache.txt``
    """


@attr.s
class AccountSavedVariablesConfig(Config):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/SavedVariables/``
    """


@attr.s
class CharacterSavedVariablesConfig(Config):
    """
    全账号级别的插件配置: 对应: ``WTF/Account/${AccountName}/${ServerName}/${CharName}/SavedVariables/``
    """