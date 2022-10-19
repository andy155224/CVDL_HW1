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
from AugmentedReality import *
from StereoDisparityMap import *

class Ui_MainWindow(object):

    def __init__(self):
        self.cameraCalibration = CameraCalibration()
        self.augmentedReality = AugmentedReality()
        self.stereoDisparityMap = StereoDisparityMap()

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

        self.loadImageL = QtWidgets.QPushButton(self.groupBox)
        self.loadImageL.setGeometry(QtCore.QRect(30, 210, 171, 51))
        self.loadImageL.setObjectName("loadImageL")
        self.loadImageL.clicked.connect(self.LoadImageLClicked)

        self.loadImageR = QtWidgets.QPushButton(self.groupBox)
        self.loadImageR.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.loadImageR.setObjectName("loadImageR")
        self.loadImageR.clicked.connect(self.LoadImageRClicked)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 40, 231, 461))
        self.groupBox_2.setObjectName("groupBox_2")

        self.findCorners = QtWidgets.QPushButton(self.groupBox_2)
        self.findCorners.setGeometry(QtCore.QRect(30, 40, 171, 51))
        self.findCorners.setObjectName("findCorners")
        self.findCorners.clicked.connect(self.FindCornersClicked)

        self.findIntrinsic = QtWidgets.QPushButton(self.groupBox_2)
        self.findIntrinsic.setGeometry(QtCore.QRect(30, 110, 171, 51))
        self.findIntrinsic.setObjectName("findIntrinsic")
        self.findIntrinsic.clicked.connect(self.FindIntrinsicClicked)

        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 211, 131))
        self.groupBox_3.setObjectName("groupBox_3")

        self.findExtrinsic = QtWidgets.QPushButton(self.groupBox_3)
        self.findExtrinsic.setGeometry(QtCore.QRect(20, 70, 171, 51))
        self.findExtrinsic.setObjectName("findExtrinsic")
        self.findExtrinsic.clicked.connect(self.FindExtrinsicClicked)

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

        self.findDistortion = QtWidgets.QPushButton(self.groupBox_2)
        self.findDistortion.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.findDistortion.setObjectName("findDistortion")
        self.findDistortion.clicked.connect(self.FindDistortionClicked)

        self.showResult = QtWidgets.QPushButton(self.groupBox_2)
        self.showResult.setGeometry(QtCore.QRect(30, 400, 171, 51))
        self.showResult.setObjectName("showResult")
        self.showResult.clicked.connect(self.ShowResultClicked)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(520, 40, 231, 461))
        self.groupBox_4.setObjectName("groupBox_4")

        self.showWordsOnBoard = QtWidgets.QPushButton(self.groupBox_4)
        self.showWordsOnBoard.setGeometry(QtCore.QRect(30, 200, 171, 51))
        self.showWordsOnBoard.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.showWordsOnBoard.setObjectName("showWordsOnBoard")
        self.showWordsOnBoard.clicked.connect(self.ShowWordsOnBoardClicked)

        self.showWordsVertically = QtWidgets.QPushButton(self.groupBox_4)
        self.showWordsVertically.setGeometry(QtCore.QRect(30, 330, 171, 51))
        self.showWordsVertically.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.showWordsVertically.setObjectName("showWordsVertically")
        self.showWordsVertically.clicked.connect(self.ShowWordsVerticallyClicked)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 151, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(770, 40, 231, 461))
        self.groupBox_6.setObjectName("groupBox_6")

        self.stereo_Disparity_Map = QtWidgets.QPushButton(self.groupBox_6)
        self.stereo_Disparity_Map.setGeometry(QtCore.QRect(30, 200, 171, 51))
        self.stereo_Disparity_Map.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.stereo_Disparity_Map.setObjectName("stereo_Disparity_Map")
        self.stereo_Disparity_Map.clicked.connect(self.StereoDisparityMapClicked)


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
        self.loadImageL.setText(_translate("MainWindow", "Load Image_L"))
        self.loadImageR.setText(_translate("MainWindow", "Load Image_R"))
        self.groupBox_2.setTitle(_translate("MainWindow", "1. Calibration"))
        self.findCorners.setText(_translate("MainWindow", "1.1 Find Corners"))
        self.findIntrinsic.setText(_translate("MainWindow", "1.2 Find Intrinsic"))
        self.groupBox_3.setTitle(_translate("MainWindow", "1.3 Find Extrinsic"))
        self.findExtrinsic.setText(_translate("MainWindow", "1.3 Find Extrinsic"))
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
        self.findDistortion.setText(_translate("MainWindow", "1.4 Find Distortion"))
        self.showResult.setText(_translate("MainWindow", "1.5 Show Result"))
        self.groupBox_4.setTitle(_translate("MainWindow", "2. Augmented Reality"))
        self.showWordsOnBoard.setText(_translate("MainWindow", "2.1 Show Words on Board"))
        self.showWordsVertically.setText(_translate("MainWindow", "2.2 Show Words Vertically"))
        self.groupBox_6.setTitle(_translate("MainWindow", "3. Stereo Disparity Map"))
        self.stereo_Disparity_Map.setText(_translate("MainWindow", "3.1 Stereo Disparity Map"))

    def LoadFolderClicked(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Load folder", "./")
        self.cameraCalibration.LoadFolder(folder_path)
        self.augmentedReality.LoadFolder(folder_path)

    def LoadImageLClicked(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile', './')
        self.stereoDisparityMap.SetImgPath(fileName[0], 0)

    def LoadImageRClicked(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile', './')
        self.stereoDisparityMap.SetImgPath(fileName[0], 1)

    def FindCornersClicked(self):
        self.cameraCalibration.FindCorners()

    def FindIntrinsicClicked(self):
        self.cameraCalibration.FindIntrinsic()

    def FindExtrinsicClicked(self):
        self.cameraCalibration.FindExtrinsic(self.comboBox.currentIndex())

    def FindDistortionClicked(self):
        self.cameraCalibration.FindDistortion()

    def ShowResultClicked(self):
        self.cameraCalibration.ShowResult()

    def GetText(self):
        word = self.lineEdit.text()
        return word.upper()
    
    def ShowWordsOnBoardClicked(self):
        word = self.GetText()
        self.augmentedReality.ShowWordsOnBoard(word)

    def ShowWordsVerticallyClicked(self):
        word = self.GetText()
        self.augmentedReality.ShowWordsVertically(word)

    def StereoDisparityMapClicked(self):
        self.stereoDisparityMap.Execute()
