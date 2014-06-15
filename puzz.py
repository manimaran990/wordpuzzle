# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'puzz.ui'
#
# Created: Sun Jun 15 18:41:35 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_puzzle(object):
    def setupUi(self, puzzle):
        puzzle.setObjectName(_fromUtf8("puzzle"))
        puzzle.resize(422, 395)
        self.centralwidget = QtGui.QWidget(puzzle)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 381, 311))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.text_pattern = QtGui.QLineEdit(self.frame)
        self.text_pattern.setGeometry(QtCore.QRect(110, 40, 151, 27))
        self.text_pattern.setObjectName(_fromUtf8("text_pattern"))
        self.text_result = QtGui.QTextEdit(self.frame)
        self.text_result.setGeometry(QtCore.QRect(110, 100, 231, 191))
        self.text_result.setObjectName(_fromUtf8("text_result"))
        self.button_go = QtGui.QPushButton(self.frame)
        self.button_go.setGeometry(QtCore.QRect(270, 40, 51, 27))
        self.button_go.setObjectName(_fromUtf8("button_go"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        puzzle.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(puzzle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        puzzle.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(puzzle)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        puzzle.setStatusBar(self.statusbar)

        self.retranslateUi(puzzle)
        QtCore.QMetaObject.connectSlotsByName(puzzle)
        puzzle.setTabOrder(self.text_pattern, self.button_go)
        puzzle.setTabOrder(self.button_go, self.text_result)

    def retranslateUi(self, puzzle):
        puzzle.setWindowTitle(QtGui.QApplication.translate("puzzle", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("puzzle", "Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.text_pattern.setToolTip(QtGui.QApplication.translate("puzzle", "<html><head/><body><p>use ? for wildcard matches</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_go.setText(QtGui.QApplication.translate("puzzle", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("puzzle", "Result", None, QtGui.QApplication.UnicodeUTF8))

