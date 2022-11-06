# -*- coding: utf-8 -*-

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
