# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_body = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_body.sizePolicy().hasHeightForWidth())
        self.checkBox_body.setSizePolicy(sizePolicy)
        self.checkBox_body.setObjectName("checkBox_body")
        self.gridLayout_2.addWidget(self.checkBox_body, 0, 0, 1, 1)
        self.checkBox_hand = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_hand.sizePolicy().hasHeightForWidth())
        self.checkBox_hand.setSizePolicy(sizePolicy)
        self.checkBox_hand.setObjectName("checkBox_hand")
        self.gridLayout_2.addWidget(self.checkBox_hand, 0, 1, 1, 1)
        self.checkBox_face = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_face.sizePolicy().hasHeightForWidth())
        self.checkBox_face.setSizePolicy(sizePolicy)
        self.checkBox_face.setObjectName("checkBox_face")
        self.gridLayout_2.addWidget(self.checkBox_face, 0, 2, 1, 1)
        self.horizontalSlider_Face = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Face.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Face.setSizePolicy(sizePolicy)
        self.horizontalSlider_Face.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Face.setObjectName("horizontalSlider_Face")
        self.gridLayout_2.addWidget(self.horizontalSlider_Face, 1, 2, 1, 1)
        self.horizontalSlider_Hand = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Hand.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Hand.setSizePolicy(sizePolicy)
        self.horizontalSlider_Hand.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Hand.setObjectName("horizontalSlider_Hand")
        self.gridLayout_2.addWidget(self.horizontalSlider_Hand, 1, 1, 1, 1)
        self.horizontalSlider_Body = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Body.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Body.setSizePolicy(sizePolicy)
        self.horizontalSlider_Body.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Body.setObjectName("horizontalSlider_Body")
        self.gridLayout_2.addWidget(self.horizontalSlider_Body, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.treeView_file = QtWidgets.QTreeView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_file.sizePolicy().hasHeightForWidth())
        self.treeView_file.setSizePolicy(sizePolicy)
        self.treeView_file.setObjectName("treeView_file")
        self.verticalLayout.addWidget(self.treeView_file)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_frame = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_frame.sizePolicy().hasHeightForWidth())
        self.label_frame.setSizePolicy(sizePolicy)
        self.label_frame.setMinimumSize(QtCore.QSize(640, 480))
        self.label_frame.setMaximumSize(QtCore.QSize(640, 480))
        self.label_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout.addWidget(self.label_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Camera"))
        self.pushButton_4.setText(_translate("MainWindow", "Begin Recod"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Open Image Folder"))
        self.checkBox_body.setText(_translate("MainWindow", "Body"))
        self.checkBox_hand.setText(_translate("MainWindow", "Hand"))
        self.checkBox_face.setText(_translate("MainWindow", "Face"))
        self.label_frame.setText(_translate("MainWindow", "TextLabel"))
