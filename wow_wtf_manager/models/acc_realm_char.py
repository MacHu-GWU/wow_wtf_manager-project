# -*- coding: utf-8 -*-

"""
本模块定义了 :class:`Account`, :class:`Realm`, :class:`Character` 三个配置应用场景类.

.. note::

    注意, 这里的类都带有一个 ``def new()`` 的工厂函数, 请不要直接用构造器, 而用这个工厂函数.
    里面会自动把新建的对象加入到父对象的映射中去.
"""

import typing as T

import attr

from .utils import right_zfill
from .base import BaseMixin


@attr.define(frozen=True, eq=True, order=True)
class Account(BaseMixin):
    """
    代表着一个具体账号. 是可哈希, 可排序的.

    :param account: 账号名
    :param realms_mapper: 该账号下的所有服务器从名字到对象的映射
    """

    account: str = attr.field()
    realms_mapper: T.Dict[str, "Realm"] = attr.field(factory=dict)

    @classmethod
    def new(
        cls,
        account: str,
    ) -> "Account":
        obj = cls(account=account)
        return obj

    @property
    def sort_key(self) -> str:
        """
        创建账号的排序键. 本质是左对齐并在尾部添加 "0" 的字符串.
        """
        return right_zfill(self.account, 20)

    def __hash__(self):
        """
        判断账号是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def realms(self) -> T.List["Realm"]:
        """
        返回该账号下的所有服务器.
        """
        return list(self.realms_mapper.values())

    @property
    def characters(self) -> T.List["Character"]:
        """
        返回该账号下所有服务器上的所有角色.
        """
        chars = list()
        for realm in self.realms:
            for character in realm.characters:
                chars.append(character)
        return chars

    @property
    def capitalized_account_name(self) -> str:
        r"""
        返回账号名的全部大写形式. 用于 WTF 文件夹中的路径名. 例如:

        ``C:\...\WTF\Account\MYACCOUNT\...``
        """
        return self.account.upper()


@attr.define(frozen=True, eq=True, order=True)
class Realm(BaseMixin):
    """
    代表着一个具体账号下的具体的服务器. 是可哈希, 可排序的.

    :param account: 该服务器所属的账号.
    :param realm: 服务器名.
    :param characters_mapper: 该服务器下的所有角色从名字到对象的映射.
    """

    account: Account = attr.ib()
    realm: str = attr.ib()
    characters_mapper: T.Dict[str, "Character"] = attr.ib(factory=dict)

    @classmethod
    def new(
        cls,
        account: Account,
        realm: str,
    ) -> "Realm":
        obj = cls(account=account, realm=realm)
        account.realms_mapper[obj.realm] = obj
        return obj

    @property
    def sort_key(self) -> str:
        """
        服务器名排序键. 本质是先对账号排序, 再对服务器名排序. 和账号的排序键一样, 也是左对齐
        并在尾部添加 "0" 的字符串.
        """
        return ".".join(
            [
                self.account.sort_key,
                right_zfill(self.realm, 20),
            ]
        )

    def __hash__(self):
        """
        判断服务器是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def account_name(self) -> str:
        """
        该服务器所属的账号名.
        """
        return self.account.account

    @property
    def characters(self) -> T.List["Character"]:
        return list(self.characters_mapper.values())


@attr.define(frozen=True, eq=True, order=True)
class Character(BaseMixin):
    """
    代表着一个具体账号下的具体的服务器上的具体游戏角色. 是可哈希, 可排序的.

    :param realm: 该角色所属的服务器对象.
    :param character: 角色名.
    """

    realm: Realm = attr.define()
    character: str = attr.define()

    @classmethod
    def new(
        cls,
        realm: Realm,
        character: str,
    ) -> "Character":
        obj = cls(realm=realm, character=character)
        realm.characters_mapper[obj.character] = obj
        return obj

    @property
    def sort_key(self) -> str:
        """
        角色名排序键. 本质是先对服务器排序, 再对角色名排序. 和服务器的排序键一样, 也是左对齐
        并在尾部添加 "0" 的字符串.
        """
        return ".".join(
            [
                self.realm.sort_key,
                right_zfill(self.character, 20),
            ]
        )

    def __hash__(self):
        """
        判断角色是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def realm_name(self) -> str:
        """
        该角色所属的服务器名.
        """
        return self.realm.realm

    @property
    def account(self) -> Account:
        return self.realm.account

    @property
    def account_name(self) -> str:
        """
        该角色所属的账号名.
        """
        return self.account.account

    @property
    def titled_character_name(self) -> str:
        r"""
        角色名的首字母大写形式. 例如 "mycharacter" -> "Mycharacter". 用于
        WTF 文件夹中的路径名. 例如:

        ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\...``
        """
        return self.character[0].upper() + self.character[1:].lower()
