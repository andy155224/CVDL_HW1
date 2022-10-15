# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CVDL_HW1_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

from CameraCalibration import *

class Ui_MainWindow(object):

    def __init__(self):
        self.cameraCalibration = CameraCalibration()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 231, 461))
        self.groupBox.setObjectName("groupBox")

        self.loadFolder = QtWidgets.QPushButton(self.groupBox)          # LoadFolder
        self.loadFolder.setGeometry(QtCore.QRect(30, 80, 171, 51))
        self.loadFolder.setObjectName("loadFolder")
        self.loadFolder.clicked.connect(self.LoadFolderClicked)

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 210, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 40, 231, 461))
        self.groupBox_2.setObjectName("groupBox_2")

        self.findCorners = QtWidgets.QPushButton(self.groupBox_2)
        self.findCorners.setGeometry(QtCore.QRect(30, 40, 171, 51))
        self.findCorners.setObjectName("findCorners")
        self.findCorners.clicked.connect(self.FindCornersClicked)

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 110, 171, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 211, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 70, 171, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(50, 30, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 400, 171, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(520, 40, 231, 461))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setGeometry(QtCore.QRect(30, 200, 171, 51))
        self.pushButton_12.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.pushButton_13.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 151, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(770, 40, 231, 461))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 200, 171, 51))
        self.pushButton_14.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_14.setObjectName("pushButton_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CVDL_HW1"))
        self.groupBox.setTitle(_translate("MainWindow", "Load Image"))

        self.loadFolder.setText(_translate("MainWindow", "Load Folder"))

        self.pushButton_2.setText(_translate("MainWindow", "Load Image_L"))
        self.pushButton_3.setText(_translate("MainWindow", "Load Image_R"))
        self.groupBox_2.setTitle(_translate("MainWindow", "1. Calibration"))

        self.findCorners.setText(_translate("MainWindow", "1.1 Find Corners"))

        self.pushButton_5.setText(_translate("MainWindow", "1.2 Find Intrinsic"))
        self.groupBox_3.setTitle(_translate("MainWindow", "1.3 Find Extrinsic"))
        self.pushButton_6.setText(_translate("MainWindow", "1.3 Find Extrinsic"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox.setItemText(14, _translate("MainWindow", "15"))
        self.pushButton_7.setText(_translate("MainWindow", "1.4 Find Distortion"))
        self.pushButton_8.setText(_translate("MainWindow", "1.5 Show Result"))
        self.groupBox_4.setTitle(_translate("MainWindow", "2. Augmented Reality"))
        self.pushButton_12.setText(_translate("MainWindow", "2.1 Show Words on Board"))
        self.pushButton_13.setText(_translate("MainWindow", "2.2 Show Words Vertically"))
        self.groupBox_6.setTitle(_translate("MainWindow", "3. Stereo Disparity Map"))
        self.pushButton_14.setText(_translate("MainWindow", "3.1 Stereo Disparity Map"))

    def LoadFolderClicked(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Load folder", "./")
        self.cameraCalibration.LoadFolder(folder_path)

    def FindCornersClicked(self):
        self.cameraCalibration.FindCorners()
