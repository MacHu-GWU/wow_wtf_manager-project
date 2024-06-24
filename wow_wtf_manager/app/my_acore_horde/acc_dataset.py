# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_acc.api import Dataset

dir_root = Path(__file__).absolute().parent
ds = Dataset.from_yaml(dir_root.joinpath("acc_dataset.yml").read_text())

if __name__ == "__main__":
    path = dir_root.joinpath("acc_enum.py")
    content = ds.to_module(
        import_line="from .acc_dataset import ds",
    )
    path.write_text(content)
