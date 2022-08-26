# -*- coding: utf-8 -*-

import os
from rich import print

from wow_wtf_manager.paths import dir_tests
from wow_wtf_manager.exp.e03_wotlk.myslot import (
    huffman_encode,
    huffman_decode,
    MySlotHuffmanEncoded,
    MySlotPythonData,
)

dir_root = dir_tests / "e03_wotlk" / "myslot"


def test_huffman_encode_decode():
    decode_input_file = dir_root / "flychicken.txt"
    decode_output_file = dir_root / "flychicken.lua"
    encode_input_file = dir_root / "flychicken.lua"
    encode_output_file = dir_root / "flychicken-enc.txt"

    huffman_decode(decode_input_file, decode_output_file)
    huffman_encode(encode_input_file, encode_output_file)
    assert decode_input_file.read_text() == encode_output_file.read_text()


class TestMySlotPythonData:
    def test(self):
        decode_input_file = dir_root / "flychicken.txt"
        decode_output_file = dir_root / "flychicken.lua"
        huffman_decode(decode_input_file, decode_output_file)

        my_slot_python_data = MySlotPythonData.from_lua_syntax(
            decode_output_file.read_text()
        )
        # print(my_slot_python_data)
        # print(my_slot_python_data.to_lua_syntax())


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=wow_wtf_manager.exp.e03_wotlk.myslot",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
