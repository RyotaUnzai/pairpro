# -*- coding: utf-8 -*-

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

import os

import renamerModel
import renamerView


class delegateAttr(object):
    def __init__(self, view=None, model=None, *args, **kwargs):
        self.__model = model
        self.__view = view
        self.__centralWidget = None

    @property
    def model(self) -> renamerModel.model:
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def view(self) -> renamerView.view:
        return self.__view

    @view.setter
    def view(self, value):
        self.__view = value

    @property
    def centralWidget(self):
        return self.__centralWidget

    @centralWidget.setter
    def centralWidget(self, value):
        self.__centralWidget = value


class delegate(delegateAttr):
    def __init__(self, view=None, model=None, *args, **kwargs):
        super(delegate, self).__init__(view, model, *args, **kwargs)
        self.model = model
        self.view = view
        self.centralWidget = self.view.centralWidget()

        self.__initUI()

    def __initUI(self):
        self.__initCentralWidgetUI()
        self.consecutiveNumber()

    def __initCentralWidgetUI(self):
        self.centralWidget.button_apply.clicked.connect(self.rename)
        ...
        # self.__centralWidget.pushButton.clicked.connect(self.__model.debug)

    def rename(self):
        base_file_path = self.centralWidget.lineedit_base_file.text()

        # TODO: modelに移行予定
        new = self.centralWidget.lineedit_new.text()
        old = self.centralWidget.lineedit_old.text()
        print("base_file_path", base_file_path)
        print("new", new)
        print("old", old)

        base_name, ext = os.path.splitext(os.path.basename(base_file_path))
        base_dir = os.path.dirname(base_file_path)

        new_name = self.model.replace(base_name, old, new)
        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")

        result = self.model.rename(base_file_path, new_file_path)
        print("result", result)
        ...

    def consecutiveNumber(self):
        base_file_path = self.centralWidget.lineedit_base_file.text()

        # GUIの値を取る

        base_name, ext = os.path.splitext(os.path.basename(base_file_path))
        base_dir = os.path.dirname(base_file_path)

        new_name = self.model.consecutiveNumber(base_name, 1, 3)

        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")
        print("new_file_path", new_file_path)
