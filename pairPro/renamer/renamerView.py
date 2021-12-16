# -*- coding: utf-8 -*-
import os
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import *

absPath = os.path.dirname(__file__)
uiPath = os.path.join(absPath, "view.ui")
uiclass, baseclass = loadUiType(uiPath)

class uiClass(baseclass, uiclass):
    def __init__(self, parent=None, *args, **kwargs):
        super(uiClass, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class view(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(view, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        #self.setCentralWidget(uiClass(parent=self.parent))
