# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser_gui.ui'
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
        MainWindow.resize(608, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.dir_view = QTreeView(self.splitter)
        self.dir_view.setObjectName(u"dir_view")
        self.splitter.addWidget(self.dir_view)
        self.dir_view.header().setMinimumSectionSize(32)
        self.dir_details = QTreeView(self.splitter)
        self.dir_details.setObjectName(u"dir_details")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dir_details.sizePolicy().hasHeightForWidth())
        self.dir_details.setSizePolicy(sizePolicy1)
        self.dir_details.setDragEnabled(True)
        self.dir_details.setDragDropMode(QAbstractItemView.DragOnly)
        self.dir_details.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.splitter.addWidget(self.dir_details)
        self.dir_details.header().setMinimumSectionSize(64)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sequences_checkbox = QCheckBox(self.centralwidget)
        self.sequences_checkbox.setObjectName(u"sequences_checkbox")
        self.sequences_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.sequences_checkbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.png_checkbox = QCheckBox(self.centralwidget)
        self.png_checkbox.setObjectName(u"png_checkbox")
        self.png_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.png_checkbox)

        self.jpg_checkbox = QCheckBox(self.centralwidget)
        self.jpg_checkbox.setObjectName(u"jpg_checkbox")
        self.jpg_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.jpg_checkbox)

        self.exr_checkbox = QCheckBox(self.centralwidget)
        self.exr_checkbox.setObjectName(u"exr_checkbox")
        self.exr_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.exr_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"line_edit")

        self.horizontalLayout_2.addWidget(self.line_edit)

        self.add_nodes_button = QPushButton(self.centralwidget)
        self.add_nodes_button.setObjectName(u"add_nodes_button")

        self.horizontalLayout_2.addWidget(self.add_nodes_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sequences_checkbox.setText(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.png_checkbox.setText(QCoreApplication.translate("MainWindow", u"*.png", None))
        self.jpg_checkbox.setText(QCoreApplication.translate("MainWindow", u"*.jpg", None))
        self.exr_checkbox.setText(QCoreApplication.translate("MainWindow", u"*.exr", None))
        self.add_nodes_button.setText(QCoreApplication.translate("MainWindow", u"Add Node(s)", None))
    # retranslateUi

