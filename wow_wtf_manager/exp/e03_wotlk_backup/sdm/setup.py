# -*- coding: utf-8 -*-

"""
:mod:`wow_wtf_manager.exp.e03_wotlk.sdm.model` 模块的实现了对单个账号下的
``SuperDuperMacro.lua`` 文件进行管理. 作为补充, 本模块实现了对一个魔兽世界客户端下, 多个账号,
多个服务器, 多个角色的 SuperDuperMacro 宏命令的批量管理.

SDM 这个插件设计上是让一个账号下所有服务器, 所有角色的数据都保存在一个
``Account/${AccountName}/SavedVariables/SuperDuperMacro.lua`` 文件中.
"""

import typing as T
import attr
from pathlib_mate import Path

from ....logger import logger
from ....compat import cached_property
from ....models.api import Account, Character

from .model import SDMMacro, SDMLua


@attr.define(slots=False)
class SDMMacroFile:
    """
    代表着一个 YAML 文件, 其内容是 :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.model.SDMMacro`
    对象的数据.

    .. note::

        这个类存在的意义是为了 Lazyload. 因为我们在对宏命令和账号角色的关系进行关联的时候, 需要
        枚举所有的宏命令, 而这些宏命令都是文件, 并不是每个文件都会被用到. 所以我们不需要一开始就
        将所有的文件都读到内存中来, 而是需要的时候再读取.

        例如在进行宏命令和账号角色的关联时引用的是 :class:`SDMMacroFile` 对象, 而最终调用
        :meth:`SDMMacroFile.macro` 这个带缓存的方法才会真正将文件中的数据读取到内存中.

    :param path: YAML 文件的路径.
    """

    path: Path = attr.field()

    @cached_property
    def content(self) -> str:
        """
        YAML 文件的具体内容.

        .. note::

            该属性要被缓存起来, 以避免重复的 IO.
        """
        return self.path.read_text()

    @property
    def macro(self) -> SDMMacro:
        """
        YAML 文件所对应的 :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.model.SDMMacro` 对象.

        .. note::

            该属性 **不能** 被缓存. 因为我们很可能生成了 ``SDMMacro`` 对象后要对其在内存中
            进行修改. 如果该宏在多个地方被引用, 那么就会产生很多奇奇怪怪的问题. 所以这个属性
            被设计成每次都返回一个新的对象.
        """
        return SDMMacro.parse_yml(self.content)


@attr.define
class AccountSDMSetup:
    """
    代表着一个 WTF 文件夹下的单个魔兽世界账号中的 ``SuperDuperMacro.lua`` 文件.

    :param account: 是一个 Account 对象, 代表它属于于哪一个 Account.
    :param macro_mapper: 根据 macro id 映射到
        :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.model.SDMMacro` 对象的字典.
        这个属性是为了实现对 macro id 进行去重管理, 以便于尽早发现错误, 而不要等到
        真正修改 ``SuperDuperMacro.lua`` 文件的时候才发现.

    Todo: 为了避免直接修改 macro_mapper 属性, 将其定义为一个私有属性.
    """

    account: Account = attr.field()
    macro_mapper: T.Dict[int, SDMMacro] = attr.field(factory=dict)

    def add_macro(
        self,
        macro: T.Union[SDMMacro, T.Iterable[SDMMacro]],
        overwrite: bool = False,
    ):
        """
        将一个或是一堆 :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.model.SDMMacro`
        对象添加到该账号下.

        .. important::

            请不要直接修改 :attr:`macro_mapper` 属性, 而是通过这个方法来添加.
        """
        if isinstance(macro, SDMMacro):  # pragma: no cover
            macros: T.Iterable[SDMMacro] = [macro]
        else:  # pragma: no cover
            macros: T.Iterable[SDMMacro] = macro

        for macro in macros:
            if macro.id in macros:  # pragma: no cover
                if overwrite:
                    raise KeyError(
                        f"macro id {macro.id} already exists in "
                        f"account {self.account.account}",
                    )
            self.macro_mapper[macro.id] = macro


@attr.define
class ClientSDMSetup:
    """
    代表着一个魔兽世界客户端下所有的账号的 ``SuperDuperMacro.lua`` 文件, 从而实现了多账号
    的批量管理.

    :param dir_wtf: ``World of Warcraft/WTF``  文件夹的绝对路径.
    :param account_sdm_setup_mapper: 根据 account name 映射到
        :class:`AccountSDMSetup` 对象的字典. 这个属性是为了实现对 account name 进行去重
        管理, 以便于尽早发现错误, 而不要等到真正修改 ``SuperDuperMacro.lua`` 文件的时候才发现.

    .. important::

        请不要直接修改 :attr:`account_sdm_setup_mapper` 属性, 而是通过
        :meth:`add_macros_to_account`, :meth:`add_macros_to_character`
        方法来进行添加. 因为我们不希望直接用 list.append 或是 dict.update 的方式来参加,
        它们的语义不是很明确. 我们专门设计了这些方法, 用来避免错误.

    Todo: 为了避免直接修改 account_sdm_setup_mapper 属性, 将其定义为一个私有属性.
    """

    dir_wtf: Path = attr.field()
    account_sdm_setup_mapper: T.Dict[str, AccountSDMSetup] = attr.field(factory=dict)

    @logger.pretty_log()
    def apply(
        self,
        dry_run: bool = True,
    ):
        """
        将插件实际应用到 WTF 文件夹, 该操作会覆盖掉已有的 SuperDuperMacro 插件配置.
        """
        for account_sdm_setup in self.account_sdm_setup_mapper.values():
            logger.info(f"working on account: {account_sdm_setup.account.account}")
            path_lua = self.dir_wtf.joinpath(
                "Account",
                account_sdm_setup.account.capitalized_account_name,
                "SavedVariables",
                "SuperDuperMacro.lua",
            )
            sdm_lua = SDMLua(
                path_lua=path_lua,
                macros=list(account_sdm_setup.macro_mapper.values()),
            )
            logger.info(f"write to: {sdm_lua.path_lua}", 1)
            sdm_lua.write(dry_run=dry_run)

    # 注: 以下的方法都是为了方便开发者给 account_sdm_setup_mapper 属性添加数据而存在的
    def _get_or_init_setup(self, account: Account) -> AccountSDMSetup:
        """
        获取或是初始化一个 :class`AccountSDMSetup` 对象, 并放到
        :attr:`ClientSDMSetup.account_sdm_setup_mapper`` 属性中并返回. 如果已经存在,
        那么直接返回.
        """
        # 如果已经存在, 那么直接 get 并返回
        if account.account in self.account_sdm_setup_mapper:
            return self.account_sdm_setup_mapper[account.account]
        # 如果还不存在, 则先初始化然后再 get
        else:
            account_sdm_setup = AccountSDMSetup(account=account)
            self.account_sdm_setup_mapper[account.account] = account_sdm_setup
            return account_sdm_setup

    def add_macros_to_account(
        self,
        account: T.Union[Account, T.Iterable[Account]],
        sdm_files: T.Iterable[SDMMacroFile],
    ):
        """
        为一个或是多个 Account 添加一批 SDMMacro 对象. 这些 Macro 将会成为 Global Macro.
        例如我们可以给所有账号添加一个接受邀请组队宏.
        """
        if isinstance(account, Account):  # pragma: no cover
            accounts = [account]
        else:  # pragma: no cover
            accounts = account
        for account in accounts:
            account_sdm_setup = self._get_or_init_setup(account)
            account_sdm_setup.add_macro(
                macro=[file.macro for file in sdm_files],
                overwrite=False,
            )

    def add_macros_to_character(
        self,
        character: T.Union[Character, T.Iterable[Character]],
        sdm_files: T.Iterable[SDMMacroFile],
    ):
        """
        为一批 Character 添加一堆一样的 :class:`~wow_wtf_manager.exp.e03_wotlk.sdm.model.SDMMacro`
        对象. 这些 Macro 将会成为 Character Macro. 例如我们可以给所有法师角色添加一个打断焦点
        的目标施法宏.

        我们不希望直接用 list.append 或是 dict.update 的方式来参加, 语义不是很明确.
        我们专门设计了这个方法, 用来提升代码可读性.
        """
        if isinstance(character, Character):  # pragma: no cover
            characters = [character]
        else:  # pragma: no cover
            characters = character
        for character in characters:
            account_sdm_setup = self._get_or_init_setup(character.account)
            macros = [file.macro for file in sdm_files]
            for macro in macros:
                macro.set_char(
                    name=character.titled_character_name,
                    realm=character.realm_name,
                )
            account_sdm_setup.add_macro(
                macro=macros,
                overwrite=False,
            )
