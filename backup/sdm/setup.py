# -*- coding: utf-8 -*-

import typing as T

from collections import OrderedDict

import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

from ....logger import logger
from ..group import Account, Character
from .saved_variable import SDMMacro, SDMMacroFile, render_sdm_lua


@attr.s
class AccountSDMSetup(AttrsClass):
    """
    代表着一个 WTF 文件夹下一个 魔兽世界账号中的 SuperDuperMacro 插件的 Lua 配置的对象.

    :param account: 是一个 :class:`~wow_wtf_manager.exp.e03_wotlk.group.Account` 对象.
        由于 SuperDuperMacro 的 saved variable lua 是保存在 Account 下的, 所以这里
        需要 Account 信息来定位到 lua 文件路径.
    :param macro_mapper: key = macro id, value = SDMMacro, 使用字典数据结构是用来
        快速的发现是否有重复的 Macro.
    """

    account: Account = Account.ib_nested()
    macro_mapper: T.OrderedDict[int, SDMMacro] = attr.ib(factory=OrderedDict)

    def add_macros(
        self,
        macros: T.Iterable[T.Union[SDMMacro, SDMMacroFile]],
        overwrite: bool = False,
    ):
        """
        添加一组 Macro 到当前的 AccountSDMSetup 对象中. 比起直接用 dict.update 操作,
        增加了对于重复的判断, 能尽早的抛出异常提示.
        """
        for macro in macros:
            if isinstance(macro, SDMMacroFile):  # pragma: no cover
                macro = macro.macro
            if macro.id in self.macro_mapper:
                if overwrite:
                    self.macro_mapper[macro.id] = macro
                else:
                    raise Exception
            else:
                self.macro_mapper[macro.id] = macro


@attr.s
class ClientSDMSetup(AttrsClass):
    """
    代表着一个魔兽世界客户端下所有的账号的 SuperDuperMacro 插件的配置.

    :param dir_wow: 魔兽世界客户端的根目录, 用来定位到 WTF 文件夹.
    :param account_sdm_setup_mapper: key = account name, value = :class:`AccountSDMSetup`
    """

    dir_wow: Path = attr.ib()
    account_sdm_setup_mapper: T.Dict[str, AccountSDMSetup] = attr.ib(factory=dict)

    def apply_one_account(self, account_sdm_setup: AccountSDMSetup, plan=True):
        logger.info(f"working on account: {account_sdm_setup.account}")
        path = (
            self.dir_wow
            / "WTF"
            / "Account"
            / account_sdm_setup.account.account
            / "SavedVariables"
            / "SuperDuperMacro.lua"
        )
        macro_list = list(account_sdm_setup.macro_mapper.values())
        content = render_sdm_lua(macro_list=macro_list)
        if plan is False:  # pragma: no cover
            path.write_text(content)

    def apply(self, plan=True):
        """
        将插件实际应用到 WTF 文件夹, 该操作会覆盖掉已有的 SuperDuperMacro 插件配置.
        """
        for account_sdm_setup in self.account_sdm_setup_mapper.values():
            self.apply_one_account(account_sdm_setup=account_sdm_setup, plan=plan)

    def get_or_init_setup(self, account: Account) -> AccountSDMSetup:
        """
        获取或是初始化一个 :class`AccountSDMSetup` 并放到 :attr:`ClientSDMSetup.account_sdm_setup_mapper``
        属性中.
        """
        # 如果已经存在, 那么直接 get
        if account.account in self.account_sdm_setup_mapper:
            return self.account_sdm_setup_mapper[account.account]
        # 如果还不存在, 则先初始化然后再 get
        else:
            account_sdm_setup = AccountSDMSetup(account=account)
            self.account_sdm_setup_mapper[account.account] = account_sdm_setup
            return account_sdm_setup

    def add_macros_for_many_accounts(
        self,
        accounts: T.Iterable[Account],
        files: T.Iterable[SDMMacroFile],
    ):
        """
        为一批 Account 添加一堆一样的 SDMMacro 对象. 这些 Macro 将会成为 Global Macro.
        例如我们可以给所有账号添加一个接受邀请组队宏.

        我们不希望直接用 list.append 或是 dict.update 的方式来参加, 语义不是很明确.
        我们专门设计了这个方法, 用来提升代码可读性.

        :param accounts: 一批账号
        :param files: 一堆代表 Macro 的 YAML 文件, 是
            :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.saved_variable.SDMMacroFile` 对象.
        """
        for account in accounts:
            account_sdm_setup = self.get_or_init_setup(account)
            macros = [file.macro for file in files]  # 从 file 变成 macro 对象
            account_sdm_setup.add_macros(macros)

    def add_macros_for_many_chars(
        self,
        chars: T.Iterable[Character],
        files: T.Iterable[SDMMacroFile],
    ):
        """
        为一批 Character 添加一堆一样的 SDMMacro 对象. 这些 Macro 将会成为 Character Macro.
        例如我们可以给所有法师角色添加一个打断焦点的目标施法宏.

        我们不希望直接用 list.append 或是 dict.update 的方式来参加, 语义不是很明确.
        我们专门设计了这个方法, 用来提升代码可读性.
        """
        for character in chars:
            account_sdm_setup = self.get_or_init_setup(character.acc_obj)
            macros = [file.macro for file in files]  # 从 file 变成 macro 对象
            for macro in macros:
                macro.set_char(
                    name=character.character,
                    realm=character.server,
                )
            account_sdm_setup.add_macros(macros)
