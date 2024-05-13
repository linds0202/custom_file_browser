# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser_gui_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 10, 761, 521))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.dir_view = QTreeView(self.splitter)
        self.dir_view.setObjectName(u"dir_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dir_view.sizePolicy().hasHeightForWidth())
        self.dir_view.setSizePolicy(sizePolicy1)
        self.dir_view.setMinimumSize(QSize(100, 0))
        self.dir_view.setMaximumSize(QSize(300, 16777215))
        self.dir_view.setSizeIncrement(QSize(0, 0))
        self.dir_view.setBaseSize(QSize(200, 0))
        self.splitter.addWidget(self.dir_view)
        self.dir_details = QTreeView(self.splitter)
        self.dir_details.setObjectName(u"dir_details")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dir_details.sizePolicy().hasHeightForWidth())
        self.dir_details.setSizePolicy(sizePolicy2)
        self.dir_details.setMinimumSize(QSize(100, 0))
        self.dir_details.setSizeIncrement(QSize(0, 0))
        self.dir_details.setBaseSize(QSize(480, 0))
        self.splitter.addWidget(self.dir_details)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 821, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

