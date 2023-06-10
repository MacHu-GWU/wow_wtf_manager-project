# -*- coding: utf-8 -*-

def right_zfill(s: str, length: int = 20) -> str:
    """
    在字符串右边填充 "0" 字符串, 以保证字符串有确定的长度, 可以用于排序.
    """
    return s + "0" * (length - len(s))