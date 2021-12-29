# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import typing as tp


class model(object):
    def __init__(self, *args, **kwargs):
        super(model, self).__init__(*args, **kwargs)

    def debug(self):
        print("debug")

    def rename(self, base_file_path, new_file_path):
        os.rename(base_file_path, new_file_path)
        return new_file_path

    def replace(self, base, old, new):
        return base.replace(old, new)

    def consecutiveNumber(self, base, index, digits):
        digits_number = f"{index:0>{digits}}"

        new_name = base + digits_number
        print("digits_number", digits_number)
        print("new_name", new_name)

        return new_name

    def load_json(self, path) -> tp.Dict[str]:
        with open(path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
            return data

        ...
