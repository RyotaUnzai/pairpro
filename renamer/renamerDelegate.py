# -*- coding: utf-8 -*-

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *



class delegateAttr(object):
    def __init__(self, view=None, model=None, *args, **kwargs):
        self.__model = model
        self.__view = view
        self.__centralWidget = None

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
    def centralWidget(cls):
        return cls.__centralWidget

    @classmethod
    def centralWidget(cls, value):
        cls.__centralWidget = value


class delegate(delegateAttr):
    def __init__(self, view=None, model=None, *args, **kwargs):
        super(delegate, self).__init__(view, model, *args, **kwargs)
        self.__model = model
        self.__view = view
        self.__centralWidget = self.__view.centralWidget()

        self.initUI()

    def initUI(self):
        self.initCentralWidgetUI()

    def initCentralWidgetUI(self):
        pass
        #self.__centralWidget.pushButton.clicked.connect(self.__model.debug)