# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'test_UI.ui'
##
# Created by: Qt User Interface Compiler version 6.6.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QStatusBar, QTextEdit, QWidget)
import serial
# import minimalmodbus
from PySide6.QtCore import QTimer

from pymodbus.client import ModbusSerialClient
from datetime import datetime
from PySide6.QtWidgets import QFileDialog


class Ui_TESTER(object):
    def setupUi(self, TESTER):
        if not TESTER.objectName():
            TESTER.setObjectName(u"TESTER")
        TESTER.resize(1300, 800)
        TESTER.setMinimumSize(QSize(1300, 800))
        TESTER.setMaximumSize(QSize(1300, 800))
        self.centralwidget = QWidget(TESTER)
        self.centralwidget.setObjectName(u"centralwidget")
        self.port_X_label = QLabel(self.centralwidget)
        self.port_X_label.setObjectName(u"port_X_label")
        self.port_X_label.setGeometry(QRect(10, 10, 91, 51))
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(28)
        font.setBold(True)
        self.port_X_label.setFont(font)
        self.port_Y_label = QLabel(self.centralwidget)
        self.port_Y_label.setObjectName(u"port_Y_label")
        self.port_Y_label.setGeometry(QRect(10, 70, 91, 51))
        self.port_Y_label.setFont(font)
        self.port_plc_label = QLabel(self.centralwidget)
        self.port_plc_label.setObjectName(u"port_plc_label")
        self.port_plc_label.setGeometry(QRect(10, 130, 91, 51))
        self.port_plc_label.setFont(font)
        self.port_x_comboBox = QComboBox(self.centralwidget)
        self.port_x_comboBox.setObjectName(u"port_x_comboBox")
        self.port_x_comboBox.setGeometry(QRect(110, 10, 101, 41))
        self.port_x_comboBox.setFont(font)
        self.port_y_comboBox = QComboBox(self.centralwidget)
        self.port_y_comboBox.setObjectName(u"port_y_comboBox")
        self.port_y_comboBox.setGeometry(QRect(110, 70, 101, 41))
        self.port_y_comboBox.setFont(font)
        self.port_plc_comboBox = QComboBox(self.centralwidget)
        self.port_plc_comboBox.setObjectName(u"port_plc_comboBox")
        self.port_plc_comboBox.setGeometry(QRect(110, 130, 101, 41))
        self.port_plc_comboBox.setFont(font)
        self.port_x_pushButton = QPushButton(self.centralwidget)
        self.port_x_pushButton.setObjectName(u"port_x_pushButton")
        self.port_x_pushButton.setGeometry(QRect(240, 10, 141, 41))
        self.port_x_pushButton.setFont(font)
        self.port_x_pushButton.setAutoDefault(False)
        self.port_y_pushButton = QPushButton(self.centralwidget)
        self.port_y_pushButton.setObjectName(u"port_y_pushButton")
        self.port_y_pushButton.setGeometry(QRect(240, 70, 141, 41))
        self.port_y_pushButton.setFont(font)
        self.port_plc_pushButton = QPushButton(self.centralwidget)
        self.port_plc_pushButton.setObjectName(u"port_plc_pushButton")
        self.port_plc_pushButton.setGeometry(QRect(240, 130, 141, 41))
        self.port_plc_pushButton.setFont(font)
        self.data_show_frame = QFrame(self.centralwidget)
        self.data_show_frame.setObjectName(u"data_show_frame")
        self.data_show_frame.setGeometry(QRect(5, 189, 1061, 585))
        self.data_show_frame.setStyleSheet(
            u"background:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 255, 230, 255), stop:0.55 rgba(224, 235, 188, 255), stop:0.98 rgba(210, 219, 165, 255), stop:1 rgba(0, 0, 0, 0))")
        self.data_show_frame.setFrameShape(QFrame.Box)
        self.data_show_frame.setFrameShadow(QFrame.Plain)
        self.data_show_frame.setLineWidth(3)
        self.data_show_textEdit = QTextEdit(self.data_show_frame)
        self.data_show_textEdit.setObjectName(u"data_show_textEdit")
        self.data_show_textEdit.setGeometry(QRect(11, 10, 1038, 563))
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.data_show_textEdit.setFont(font1)
        self.data_show_textEdit.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.start_pushButton = QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(1090, 190, 191, 81))
        self.start_pushButton.setFont(font)
        self.stop_pushButton = QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setGeometry(QRect(1090, 690, 191, 81))
        self.stop_pushButton.setFont(font)
        self.test_pushButton = QPushButton(self.centralwidget)
        self.test_pushButton.setObjectName(u"test_pushButton")
        self.test_pushButton.setGeometry(QRect(1090, 290, 191, 81))
        self.test_pushButton.setFont(font)
        self.displacment_parameter_frame = QFrame(self.centralwidget)
        self.displacment_parameter_frame.setObjectName(
            u"displacment_parameter_frame")
        self.displacment_parameter_frame.setGeometry(QRect(400, 10, 331, 161))
        self.displacment_parameter_frame.setFrameShape(QFrame.Box)
        self.displacment_parameter_frame.setFrameShadow(QFrame.Plain)
        self.displacment_parameter_frame.setLineWidth(2)
        self.unit_y_label = QLabel(self.displacment_parameter_frame)
        self.unit_y_label.setObjectName(u"unit_y_label")
        self.unit_y_label.setGeometry(QRect(190, 100, 111, 51))
        self.unit_y_label.setFont(font)
        self.displacment_y_label = QLabel(self.displacment_parameter_frame)
        self.displacment_y_label.setObjectName(u"displacment_y_label")
        self.displacment_y_label.setGeometry(QRect(180, 0, 131, 51))
        self.displacment_y_label.setFont(font)
        self.unit_x_label = QLabel(self.displacment_parameter_frame)
        self.unit_x_label.setObjectName(u"unit_x_label")
        self.unit_x_label.setGeometry(QRect(30, 100, 111, 51))
        self.unit_x_label.setFont(font)
        self.displacment_x_lineEdit = QLineEdit(
            self.displacment_parameter_frame)
        self.displacment_x_lineEdit.setObjectName(u"displacment_x_lineEdit")
        self.displacment_x_lineEdit.setGeometry(QRect(20, 50, 131, 41))
        self.displacment_x_lineEdit.setFont(font1)
        self.displacment_x_lineEdit.setAlignment(Qt.AlignCenter)
        self.displacment_x_label = QLabel(self.displacment_parameter_frame)
        self.displacment_x_label.setObjectName(u"displacment_x_label")
        self.displacment_x_label.setGeometry(QRect(20, 0, 131, 51))
        self.displacment_x_label.setFont(font)
        self.displacment_y_lineEdit = QLineEdit(
            self.displacment_parameter_frame)
        self.displacment_y_lineEdit.setObjectName(u"displacment_y_lineEdit")
        self.displacment_y_lineEdit.setGeometry(QRect(180, 50, 131, 41))
        self.displacment_y_lineEdit.setFont(font1)
        self.displacment_y_lineEdit.setAlignment(Qt.AlignCenter)
        self.save_data_pushButton = QPushButton(self.centralwidget)
        self.save_data_pushButton.setObjectName(u"save_data_pushButton")
        self.save_data_pushButton.setGeometry(QRect(1090, 390, 191, 81))
        self.save_data_pushButton.setFont(font)
        TESTER.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TESTER)
        self.statusbar.setObjectName(u"statusbar")
        TESTER.setStatusBar(self.statusbar)

        self.retranslateUi(TESTER)
        QMetaObject.connectSlotsByName(TESTER)
    # setupUi

    def retranslateUi(self, TESTER):
        TESTER.setWindowTitle(
            QCoreApplication.translate("TESTER", u"TESTER", None))
        self.port_X_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e41\u0e01\u0e19 X", None))
        self.port_Y_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e41\u0e01\u0e19 Y", None))
        self.port_plc_label.setText(
            QCoreApplication.translate("TESTER", u"PLC", None))
        self.port_y_comboBox.setCurrentText("")
        self.port_plc_comboBox.setCurrentText("")
        self.port_x_pushButton.setText(
            QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.port_y_pushButton.setText(
            QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.port_plc_pushButton.setText(
            QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.start_pushButton.setText(
            QCoreApplication.translate("TESTER", u"START", None))
        self.stop_pushButton.setText(
            QCoreApplication.translate("TESTER", u"STOP", None))
        self.test_pushButton.setText(
            QCoreApplication.translate("TESTER", u"TEST", None))
        self.unit_y_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e21\u0e34\u0e25\u0e25\u0e34\u0e40\u0e21\u0e15\u0e23", None))
        self.displacment_y_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e23\u0e30\u0e22\u0e30\u0e41\u0e01\u0e19Y", None))
        self.unit_x_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e21\u0e34\u0e25\u0e25\u0e34\u0e40\u0e21\u0e15\u0e23", None))
        self.displacment_x_label.setText(QCoreApplication.translate(
            "TESTER", u"\u0e23\u0e30\u0e22\u0e30\u0e41\u0e01\u0e19X", None))
        self.save_data_pushButton.setText(
            QCoreApplication.translate("TESTER", u"SAVE DATA", None))
        
    # retranslateUi
        

    # retranslateUi

    


if __name__ == "__main__":
    app = QApplication([])
    tester = QMainWindow()
    ui = Ui_TESTER()
    ui.setupUi(tester)
    tester.show()
    app.exec()
