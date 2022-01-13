# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import typing as tp

from PySide2.QtWidgets import QLineEdit, QSpinBox


class model(object):
    def __init__(self, *args, **kwargs):
        super(model, self).__init__(*args, **kwargs)

    def debug(self):
        print("debug")

    def rename(self, base_file_path, new_file_path):
        os.rename(base_file_path, new_file_path)
        return new_file_path

    def replace(self, base_file_path, lineedit_old: QLineEdit, lineedit_new: QLineEdit):
        base_dir, base_name, ext = model._separate_file_path(base_file_path)

        new = lineedit_new.text()
        old = lineedit_old.text()

        print("base_file_path", base_file_path)
        print("new", new)
        print("old", old)

        new_name = base_name.replace(old, new)
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    def consecutiveNumber(self, base_file_path: str,
                          line_edit: QLineEdit,
                          zero_padding: QSpinBox,
                          digits: QSpinBox):

        base_dir, base_name, ext = model._separate_file_path(base_file_path)

        between_text = line_edit.text()
        index = zero_padding.value()
        digits = digits.value()

        digits_number = f"{index:0>{digits}}"

        new_name = base_name + between_text + digits_number
        print("between_text", between_text)
        print("digits_number", digits_number)
        print("new_name", new_name)

        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")

        return new_file_path

    def fix(self, base_file_path: str, string_edit: QLineEdit, is_prefix=False):
        base_dir, base_name, ext = model._separate_file_path(base_file_path)
        fix_text = string_edit.text()

        if is_prefix:
            new_name = self.prefix(fix_text, base_name)
        else:
            new_name = self.suffix(fix_text, base_name)
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    def prefix(self, fix_text: str, base_name: str):
        """接頭辞
        """
        return f"{fix_text}{base_name}"

    def suffix(self, fix_text: str, base_name: str):
        """接尾辞
        """
        return f"{base_name}{fix_text}"

    def upperCase(self, base_file_path: str):
        """小文字→大文字
        """

        base_dir, base_name, ext = model._separate_file_path(base_file_path)
        new_name = base_name.upper()
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    def lowerCase(self, base_file_path: str):
        """大文字→小文字
        """

        base_dir, base_name, ext = model._separate_file_path(base_file_path)
        new_name = base_name.lower()
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    def capitalCase(self, base_file_path: str):
        """先頭大文字
        """

        base_dir, base_name, ext = model._separate_file_path(base_file_path)
        new_name = base_name.capitalize()
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    def titleCase(self, base_file_path: str):
        """先頭大文字
        """

        base_dir, base_name, ext = model._separate_file_path(base_file_path)
        new_name = base_name.title()
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        return new_file_path

    @classmethod
    def _separate_file_path(cls, base_file_path) -> tp.Tuple(str, str, str):
        base_name, ext = os.path.splitext(os.path.basename(base_file_path))
        base_dir = os.path.dirname(base_file_path)
        return base_dir, base_name, ext

    def load_json(self, path) -> tp.Dict[str]:
        with open(path, mode="r", encoding="utf-8") as f:
            self.__config = json.load(f)
            return self.__config

        ...

    def getOperationMode(self, operationName):
        return self.__config["operations"][operationName]["mode"]
