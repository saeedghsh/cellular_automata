# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GOL.ui'
#
# Created: Fri Jul 24 08:18:41 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 717)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(280, 10, 650, 650))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridType = QtGui.QGroupBox(self.centralwidget)
        self.gridType.setGeometry(QtCore.QRect(50, 240, 181, 61))
        self.gridType.setObjectName("gridType")
        self.cellTypeScroll = QtGui.QComboBox(self.gridType)
        self.cellTypeScroll.setEnabled(True)
        self.cellTypeScroll.setGeometry(QtCore.QRect(0, 20, 171, 31))
        self.cellTypeScroll.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cellTypeScroll.setObjectName("cellTypeScroll")
        self.cellTypeScroll.addItem("")
        self.cellTypeScroll.addItem("")
        self.cellTypeScroll.addItem("")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 140, 181, 61))
        self.groupBox.setObjectName("groupBox")
        self.initAliveButton = QtGui.QPushButton(self.groupBox)
        self.initAliveButton.setGeometry(QtCore.QRect(90, 30, 91, 31))
        self.initAliveButton.setObjectName("initAliveButton")
        self.initAlive = QtGui.QTextEdit(self.groupBox)
        self.initAlive.setGeometry(QtCore.QRect(0, 30, 81, 31))
        self.initAlive.setTabChangesFocus(True)
        self.initAlive.setObjectName("initAlive")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 40, 181, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.changeSizeButton = QtGui.QPushButton(self.groupBox_2)
        self.changeSizeButton.setGeometry(QtCore.QRect(90, 30, 91, 31))
        self.changeSizeButton.setObjectName("changeSizeButton")
        self.sizeValue = QtGui.QTextEdit(self.groupBox_2)
        self.sizeValue.setGeometry(QtCore.QRect(0, 30, 81, 31))
        self.sizeValue.setTabChangesFocus(True)
        self.sizeValue.setObjectName("sizeValue")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 330, 171, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ruleScroll = QtGui.QComboBox(self.groupBox_3)
        self.ruleScroll.setEnabled(True)
        self.ruleScroll.setGeometry(QtCore.QRect(0, 20, 171, 31))
        self.ruleScroll.setObjectName("ruleScroll")
        self.ruleScroll.addItem("")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 430, 171, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.speedSlider = QtGui.QSlider(self.groupBox_4)
        self.speedSlider.setGeometry(QtCore.QRect(0, 20, 171, 29))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(100)
        self.speedSlider.setProperty("value", 100)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 520, 181, 80))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.stopButton = QtGui.QPushButton(self.groupBox_5)
        self.stopButton.setGeometry(QtCore.QRect(90, 10, 81, 27))
        self.stopButton.setObjectName("stopButton")
        self.startButton = QtGui.QPushButton(self.groupBox_5)
        self.startButton.setGeometry(QtCore.QRect(10, 10, 81, 27))
        self.startButton.setObjectName("startButton")
        self.resetButton = QtGui.QPushButton(self.groupBox_5)
        self.resetButton.setGeometry(QtCore.QRect(10, 40, 161, 27))
        self.resetButton.setObjectName("resetButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cellTypeScroll.setCurrentIndex(0)
        self.ruleScroll.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.gridType.setTitle(QtGui.QApplication.translate("MainWindow", "Grid (cell) Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cellTypeScroll.setItemText(0, QtGui.QApplication.translate("MainWindow", "square", None, QtGui.QApplication.UnicodeUTF8))
        self.cellTypeScroll.setItemText(1, QtGui.QApplication.translate("MainWindow", "triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.cellTypeScroll.setItemText(2, QtGui.QApplication.translate("MainWindow", "hexagon", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Initial Alive Cells (in%):", None, QtGui.QApplication.UnicodeUTF8))
        self.initAliveButton.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.initAlive.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.15</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Grid Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.changeSizeButton.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeValue.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">200</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Rules:", None, QtGui.QApplication.UnicodeUTF8))
        self.ruleScroll.setItemText(0, QtGui.QApplication.translate("MainWindow", "conway", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))

