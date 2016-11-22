# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 290)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.usernameEdit = QtGui.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(90, 30, 231, 27))
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.passwordEdit = QtGui.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(90, 80, 231, 27))
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 31, 68, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 68, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.loginButton = QtGui.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(100, 170, 99, 27))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.clearEdit = QtGui.QPushButton(self.centralwidget)
        self.clearEdit.setGeometry(QtCore.QRect(220, 170, 99, 27))
        self.clearEdit.setObjectName(_fromUtf8("clearEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Username", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))
        self.loginButton.setText(_translate("MainWindow", "Login", None))
        self.clearEdit.setText(_translate("MainWindow", "Clear", None))

