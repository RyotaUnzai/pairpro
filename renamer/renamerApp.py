# -*- coding: utf-8 -*-
import os
import sys

from PySide2.QtGui import QGuiApplication

try:
    from PySide.QtGui import *
except ImportError:
    from PySide2.QtWidgets import *

import renamerDelegate
import renamerModel
import renamerView


class renamerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super(renamerApp, self).__init__(*args, **kwargs)
        self.__model = None
        self.__view = None
        self.__delegate = None

    @classmethod
    def model(cls):
        return cls.__model

    @classmethod
    def model(cls, value):
        cls.__model = value

    @classmethod
    def view(cls):
        return cls.__view

    @classmethod
    def view(cls, value):
        cls.__view = value

    @classmethod
    def delegate(cls):
        return cls.__delegate

    @classmethod
    def delegate(cls, value):
        cls.__delegate = value

        return cls.__delegate


def main():
    app = renamerApp(sys.argv)
    app.view = renamerView.view()
    app.model = renamerModel.model()
    app.delegate = renamerDelegate.delegate(
        view=app.view,
        model=app.model
    )
    app.view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
