# -*- coding: utf-8 -*-

import typing as T
import os
import enum
import subprocess

import lupa
from lupa import LuaRuntime

import attr
from attrs_mate import AttrsClass
import yaml
from pathlib_mate import Path

from ..runtime import IS_WINDOWS, IS_MACOS

dir_here = Path.dir_here(__file__)
dir_home = Path.home()

path_humbase64_encode_lua = dir_here / "humbase64-encode.lua"
path_humbase64_encode_exec_lua = dir_home / "humbase64-encode-exec.lua"

path_humbase64_decode_lua = dir_here / "humbase64-decode.lua"
path_humbase64_decode_exec_lua = dir_home / "humbase64-decode-exec.lua"

lua = LuaRuntime(unpack_returned_tuples=True)

if IS_WINDOWS:
    lua_executable = None
elif IS_MACOS:
    lua_executable = "/opt/homebrew/bin/lua"
else:  # pragma: no cover
    raise NotImplementedError


def huffman_encode(
    encode_input_file: str,
    encode_output_file: str,
):
    """
    使用 lua 实现的 huffman 编码器进行编码
    """
    path_encode_input_file = Path(encode_input_file)
    path_encode_output_file = Path(encode_output_file)
    path_humbase64_encode_exec_lua.write_text(
        path_humbase64_encode_lua.read_text()
        .replace("{{ encode_input_file }}", path_encode_input_file.abspath)
        .replace("{{ encode_output_file }}", path_encode_output_file.abspath)
    )
    subprocess.run([
        lua_executable, f"{path_humbase64_encode_exec_lua}"
    ])


def huffman_decode(
    decode_input_file: str,
    decode_output_file: str,
):
    """
    使用 lua 实现的 huffman 解码器进行解码
    """
    path_decode_input_file = Path(decode_input_file)
    path_decode_output_file = Path(decode_output_file)
    path_humbase64_decode_exec_lua.write_text(
        path_humbase64_decode_lua.read_text()
        .replace("{{ decode_input_file }}", path_decode_input_file.abspath)
        .replace("{{ decode_output_file }}", path_decode_output_file.abspath)
    )
    subprocess.run([
        lua_executable, f"{path_humbase64_decode_exec_lua}"
    ])



def is_lua_table(obj) -> bool:
    """
    判断一个对象是不是 LuaTable 对象.
    """
    return type(obj).__name__ == "_LuaTable"


def lua_table_to_dict(lua_table) -> dict:
    """
    将 Lua Table 转化成 Python dict. Lua Table 中的列表都将转化成字典.
    """
    data = dict()
    for key, value in lua_table.items():
        if is_lua_table(value):
            data[key] = lua_table_to_dict(value)
        else:
            data[key] = value
    return data


class ActionTypeEnum(enum.Enum):
    """
    枚举所有动作条上的按钮类型

    Reference:

    - https://wowpedia.fandom.com/wiki/API_GetActionInfo
    """
    spell = "S"
    macro = "M"
    companion = "C"
    item = "I"


@attr.s
class SlotItem(AttrsClass):
    """
    :param id: 动作条格子的序号, 是 1 ~ 120 中的一个值
    :param type: 这个格子里的按钮是什么类型? 是 ActionTypeEnum 的成员.
    :param action: 这个格子里的东西到底是什么动作, 有很多种不同的可能, 宏, 技能, 坐骑
        物品.
    """
    id: int = attr.ib()
    type: str = attr.ib()
    action: 'Action' = attr.ib()

    def to_lua_syntax(self) -> str:
        tpl = '[%s]={["a"]="%s",["b"]=%s,},'
        return tpl % (self.id, self.type, self.action.to_lua_syntax())

    @classmethod
    def parse_dict(cls, id: int, dct: dict) -> 'SlotItem':
        action_type = dct["a"]
        if action_type == ActionTypeEnum.spell.value:
            action = SpellAction(name=dct["b"])
        elif action_type == ActionTypeEnum.macro.value:
            action = MacroAction(
                name=dct["b"]["b"],
                icon=dct["b"]["c"],
                body=dct["b"]["d"],
                per_char=dct["b"].get("e"),
            )
        elif action_type == ActionTypeEnum.companion.value:
            action = CompanionAction(
                type=dct["b"]["b"],
                id=dct["b"]["c"],
            )
        elif action_type == ActionTypeEnum.item.value:
            action = ItemAction(
                id=dct["b"]
            )
        else:
            raise NotImplementedError
        return cls(id=id, type=action_type, action=action)


@attr.s
class Action(AttrsClass):
    def to_lua_syntax(self) -> str:
        raise NotImplementedError


@attr.s
class SpellAction(Action):
    """

    """
    name: str = attr.ib()

    def to_lua_syntax(self) -> str:
        return f"\"{self.name}\""


@attr.s
class MacroAction(Action):
    """
    :param icon: 图标的数字 Id, 每个魔兽中的宏图标都是有一个 Id 的.
    :param per_char: 如果是 1 表示是人物特殊宏, 如果是 None 表示是通用宏
    """
    name: str = attr.ib()
    icon: T.Optional[int] = attr.ib()
    body: str = attr.ib()
    per_char: T.Optional[int] = attr.ib()

    def to_lua_syntax(self) -> str:
        tpl = '{["b"]="%s",["c"]=%d,["d"]=[[%s]],["e"]=%s,}'
        if self.per_char is None:
            per_char_encode = "nil"
        else:
            per_char_encode = str(self.per_char)
        return tpl % (
            self.name,
            self.icon,
            self.body,
            per_char_encode,
        )


class CompanionType(enum.Enum):
    mount = "MOUNT"
    companion = "COMPANION"


@attr.s
class CompanionAction(Action):
    """
    代表动作条上的坐骑或小宠物.

    :param type: 可以是坐骑或是小宠物
    :param id: 每个坐骑和小宠物在宠物栏里有一个 id
    """
    type: str = attr.ib()
    id: int = attr.ib()

    def to_lua_syntax(self) -> str:
        tpl = '{["b"]="%s",["c"]=%s}'
        return tpl % (self.type, self.id)


@attr.s
class ItemAction(Action):
    """
    代表一个动作条上的物品.
    """
    id: str = attr.ib()

    def to_lua_syntax(self) -> str:
        return f"\"{self.id}\""


@attr.s
class Keybind(AttrsClass):
    key: str = attr.ib()
    action: str = attr.ib()

    def to_lua_syntax(self) -> str:
        if self.key == "\\":
            key = "\\\\"
        else:
            key = self.key
        if self.action == "\\":
            action = "\\\\"
        else:
            action = self.action
        return '["%s"]="%s",' % (key, action)


@attr.s
class MySlotLuaData(AttrsClass):
    slot_item_list: T.List[SlotItem] = SlotItem.ib_list_of_nested()
    keybind_list: T.List[Keybind] = Keybind.ib_list_of_nested()

    def to_lua_syntax(self) -> str:
        slot_item_syntax_list = [
            slot_item.to_lua_syntax() for slot_item in self.slot_item_list
        ]
        keybind_syntax_list = [
            keybind.to_lua_syntax() for keybind in self.keybind_list
        ]
        keybind_syntax = "[999]={%s}," % ("".join(keybind_syntax_list),)
        return "{" + "".join(slot_item_syntax_list + [keybind_syntax, ]) + "}"


@attr.s
class MySlotHuffmanEncoded(AttrsClass):
    """
    代表 MySlot 插件导出时生成的用 Huffman 编码后再用 base64 编码后的字符串.

    大概长这个样子: ``4253dc1f967be08a...``
    """
    content: str = attr.ib()


@attr.s
class MySlotLuaSyntax(AttrsClass):
    """
    代表 MySlot 中 "序列化后的动作条数据".

    大概长这个样子: ``[1]={["a"]="S",["b"]="Hunter's Mark(Rank 3)",}, ..., [999]={["W"]="MOVEFORWARD", ...,},``
    """
    pass


# my_slot_huffman_encoded = MySlotHuffmanEncoded(content=Path(dir_here, "flychicken.txt").read_text(encoding="ascii").strip())
# print(humbase64.dec(Path(dir_here, "flychicken.txt").read_text(encoding="ascii")))

# data_lua = Path("flychicken-format.lua")
# data = lua.eval(data_lua.read_text())
# table_data = lua_table_to_dict(data)
#
# slot_item_list: T.List[SlotItem] = list()
# for k, v in table_data.items():
#     if k != 999:
#         slot_item = SlotItem.parse_dict(k, v)
#         slot_item_list.append(slot_item)
#     else:
#         keybind_list = [
#             Keybind(key=key, action=action)
#             for key, action in v.items()
#         ]
# myslot_lua_data = MySlotLuaData(slot_item_list=slot_item_list, keybind_list=keybind_list)
# myslot_lua_syntax = myslot_lua_data.to_lua_syntax()
# Path("flychicken-format-dump.lua").write_text(myslot_lua_syntax)
