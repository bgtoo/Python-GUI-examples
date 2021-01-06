# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbLevel = QtWidgets.QProgressBar(self.centralwidget)
        self.pbLevel.setEnabled(True)
        self.pbLevel.setGeometry(QtCore.QRect(11, 12, 20, 441))
        self.pbLevel.setMinimumSize(QtCore.QSize(0, 360))
        self.pbLevel.setMaximum(1000)
        self.pbLevel.setProperty("value", 123)
        self.pbLevel.setTextVisible(False)
        self.pbLevel.setOrientation(QtCore.Qt.Vertical)
        self.pbLevel.setObjectName("pbLevel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 10, 621, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 132, 16))
        self.label.setObjectName("label")
        self.grFFT = PlotWidget(self.frame)
        self.grFFT.setGeometry(QtCore.QRect(0, 20, 341, 141))
        self.grFFT.setObjectName("grFFT")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 180, 99, 16))
        self.label_2.setObjectName("label_2")
        self.grPCM = PlotWidget(self.frame)
        self.grPCM.setGeometry(QtCore.QRect(0, 200, 341, 141))
        self.grPCM.setObjectName("grPCM")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 256, 256))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setLineWidth(2)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(350, 300, 81, 51))
        self.exitButton.setObjectName("exitButton")
        self.freqSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.freqSpinBox.setGeometry(QtCore.QRect(470, 320, 68, 24))
        self.freqSpinBox.setDecimals(1)
        self.freqSpinBox.setMinimum(2.6)
        self.freqSpinBox.setMaximum(22.0)
        self.freqSpinBox.setSingleStep(0.2)
        self.freqSpinBox.setProperty("value", 22.0)
        self.freqSpinBox.setObjectName("freqSpinBox")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(470, 300, 81, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "frequency data (FFT):"))
        self.label_2.setText(_translate("MainWindow", "raw data (PCM):"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "F max (kHz)"))

from pyqtgraph import PlotWidget
