# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 374)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sleepTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.sleepTimeLabel.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.sleepTimeLabel.setObjectName("sleepTimeLabel")
        self.handednessLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.handednessLabel.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.handednessLabel.setObjectName("handednessLabel")
        self.brightnessLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.brightnessLabel.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.sineLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.sineLabel.setGeometry(QtCore.QRect(10, 140, 141, 16))
        self.sineLabel.setObjectName("sineLabel")
        self.noiseLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.noiseLabel.setGeometry(QtCore.QRect(10, 170, 141, 16))
        self.noiseLabel.setObjectName("noiseLabel")
        self.userLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(10, 200, 141, 16))
        self.userLabel.setObjectName("userLabel")
        self.pulseLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.pulseLabel.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.pulseLabel.setObjectName("pulseLabel")
        self.sineComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sineComboBox.setGeometry(QtCore.QRect(160, 140, 73, 22))
        self.sineComboBox.setObjectName("sineComboBox")
        self.sineComboBox.addItem("")
        self.sineComboBox.addItem("")
        self.sineComboBox.addItem("")
        self.sineComboBox.addItem("")
        self.sineComboBox.addItem("")
        self.sineComboBox.addItem("")
        self.noiseComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.noiseComboBox.setGeometry(QtCore.QRect(160, 170, 73, 22))
        self.noiseComboBox.setObjectName("noiseComboBox")
        self.noiseComboBox.addItem("")
        self.userComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.userComboBox.setGeometry(QtCore.QRect(160, 200, 73, 22))
        self.userComboBox.setObjectName("userComboBox")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.pulseComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.pulseComboBox.setGeometry(QtCore.QRect(160, 230, 73, 22))
        self.pulseComboBox.setObjectName("pulseComboBox")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.pulseComboBox.addItem("")
        self.sleepTimeEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sleepTimeEdit.setGeometry(QtCore.QRect(160, 10, 71, 22))
        self.sleepTimeEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sleepTimeEdit.setObjectName("sleepTimeEdit")
        self.brightnessEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.brightnessEdit.setGeometry(QtCore.QRect(160, 70, 71, 22))
        self.brightnessEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.brightnessEdit.setObjectName("brightnessEdit")
        self.resetDevicebutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetDevicebutton.setGeometry(QtCore.QRect(10, 260, 131, 61))
        self.resetDevicebutton.setObjectName("resetDevicebutton")
        self.graphWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(270, 10, 501, 241))
        self.graphWidget.setObjectName("graphWidget")
        self.sineComboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sineComboBox_2.setGeometry(QtCore.QRect(160, 40, 73, 22))
        self.sineComboBox_2.setObjectName("sineComboBox_2")
        self.sineComboBox_2.addItem("")
        self.sineComboBox_2.addItem("")
        self.sineComboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        self.menuOpen_File = QtWidgets.QMenu(parent=self.menubar)
        self.menuOpen_File.setObjectName("menuOpen_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(parent=MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionLoad_from_Tweezers = QtGui.QAction(parent=MainWindow)
        self.actionLoad_from_Tweezers.setObjectName("actionLoad_from_Tweezers")
        self.actionSave_to_Device = QtGui.QAction(parent=MainWindow)
        self.actionSave_to_Device.setObjectName("actionSave_to_Device")
        self.menuOpen_File.addAction(self.actionOpen_File)
        self.menuOpen_File.addAction(self.actionSave)
        self.menuOpen_File.addAction(self.actionSave_As)
        self.menuOpen_File.addSeparator()
        self.menuOpen_File.addAction(self.actionLoad_from_Tweezers)
        self.menuOpen_File.addAction(self.actionSave_to_Device)
        self.menubar.addAction(self.menuOpen_File.menuAction())

        self.retranslateUi(MainWindow)
        self.noiseComboBox.setCurrentIndex(0)
        self.userComboBox.setCurrentIndex(2)
        self.pulseComboBox.setCurrentIndex(3)
        self.sineComboBox_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DT71 Configuration Utility"))
        self.sleepTimeLabel.setText(_translate("MainWindow", "Sleep Time:"))
        self.handednessLabel.setText(_translate("MainWindow", "Left/Right Hand Mode:"))
        self.brightnessLabel.setText(_translate("MainWindow", "Display Brightness:"))
        self.sineLabel.setText(_translate("MainWindow", "Sine wave frequency:"))
        self.noiseLabel.setText(_translate("MainWindow", "Noise signal frequency:"))
        self.userLabel.setText(_translate("MainWindow", "User-defined frequency:"))
        self.pulseLabel.setText(_translate("MainWindow", "Pulse signal frequency:"))
        self.sineComboBox.setItemText(0, _translate("MainWindow", "10KHz"))
        self.sineComboBox.setItemText(1, _translate("MainWindow", "5KHz"))
        self.sineComboBox.setItemText(2, _translate("MainWindow", "2KHz"))
        self.sineComboBox.setItemText(3, _translate("MainWindow", "1KHz"))
        self.sineComboBox.setItemText(4, _translate("MainWindow", "500Hz"))
        self.sineComboBox.setItemText(5, _translate("MainWindow", "200Hz"))
        self.noiseComboBox.setItemText(0, _translate("MainWindow", "100KHz"))
        self.userComboBox.setItemText(0, _translate("MainWindow", "10KHz"))
        self.userComboBox.setItemText(1, _translate("MainWindow", "5KHz"))
        self.userComboBox.setItemText(2, _translate("MainWindow", "2KHz"))
        self.userComboBox.setItemText(3, _translate("MainWindow", "1KHz"))
        self.userComboBox.setItemText(4, _translate("MainWindow", "500Hz"))
        self.userComboBox.setItemText(5, _translate("MainWindow", "200Hz"))
        self.pulseComboBox.setItemText(0, _translate("MainWindow", "100KHz"))
        self.pulseComboBox.setItemText(1, _translate("MainWindow", "50KHz"))
        self.pulseComboBox.setItemText(2, _translate("MainWindow", "20KHz"))
        self.pulseComboBox.setItemText(3, _translate("MainWindow", "10KHz"))
        self.pulseComboBox.setItemText(4, _translate("MainWindow", "5KHz"))
        self.pulseComboBox.setItemText(5, _translate("MainWindow", "2KHz"))
        self.pulseComboBox.setItemText(6, _translate("MainWindow", "1KHz"))
        self.pulseComboBox.setItemText(7, _translate("MainWindow", "500Hz"))
        self.pulseComboBox.setItemText(8, _translate("MainWindow", "200Hz"))
        self.sleepTimeEdit.setText(_translate("MainWindow", "60"))
        self.brightnessEdit.setText(_translate("MainWindow", "2"))
        self.resetDevicebutton.setText(_translate("MainWindow", "Reset Device"))
        self.sineComboBox_2.setItemText(0, _translate("MainWindow", "R/H"))
        self.sineComboBox_2.setItemText(1, _translate("MainWindow", "L/H"))
        self.sineComboBox_2.setItemText(2, _translate("MainWindow", "Auto"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionLoad_from_Tweezers.setText(_translate("MainWindow", "Load from Device"))
        self.actionSave_to_Device.setText(_translate("MainWindow", "Save to Device"))
