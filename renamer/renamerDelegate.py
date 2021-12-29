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
        self.listModel = QStringListModel()

        self.__config = None
        self.__initUI()

    def __initUI(self):
        """UI初期化
        """

        self.load_config()
        self.__initCentralWidgetUI()
        self.consecutiveNumber()

    def __initCentralWidgetUI(self):
        self.centralWidget.button_apply.clicked.connect(self.rename)
        self.listModel.setStringList(self.collect_operation())
        self.centralWidget.combo_mode.setModel(self.listModel)
        self.centralWidget.combo_mode.currentTextChanged.connect(self.changeLayout)
        self.changeLayout()

    def __hide_all_frame(self):
        self.centralWidget.frame_replace.hide()
        self.centralWidget.frame_fix.hide()
        self.centralWidget.frame_consecutiveNumber.hide()

    def changeLayout(self):
        self.__hide_all_frame()

        operation_mode = self.model.getOperationMode(self.centralWidget.combo_mode.currentText())
        frame_mode = f"frame_{operation_mode}"

        frame = getattr(self.centralWidget, frame_mode, None)
        if not frame:
            return

        frame.show()

        # f"self.centralWidget.{frame_mode}.show()"

    def rename(self):
        """リネーム
        """
        operation_mode = self.centralWidget.combo_mode.currentText()
        base_file_path = self.centralWidget.lineedit_base_file.text()

        if operation_mode == "replace":
            self.model.replace(base_file_path,
                               self.centralWidget.lineedit_old,
                               self.centralWidget.lineedit_new)

    def consecutiveNumber(self):
        """連番
        """
        base_file_path = self.centralWidget.lineedit_base_file.text()

        # GUIの値を取る
        base_name, ext = os.path.splitext(os.path.basename(base_file_path))
        base_dir = os.path.dirname(base_file_path)

        new_name = self.model.consecutiveNumber_old(base_name, 1, 3)

        new_file_path = os.path.join(base_dir, f"{new_name}{ext}")

        self.model.consecutiveNumber(base_file_path,
                                     self.centralWidget.lineedit_between,
                                     self.centralWidget.spinbox_number)

        print("new_file_path", new_file_path)

    def load_config(self):
        data = self.model.load_json("renamer/settings.json")
        self.__config = data
        ...

    def collect_operation(self):
        result_list = list()
        for key, value in self.__config["operations"].items():
            result_list.append(key)

        return result_list
