# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
        self.port_X_label.setGeometry(QRect(10, 20, 261, 31))
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(18)
        font.setBold(True)
        self.port_X_label.setFont(font)
        self.port_Y_label = QLabel(self.centralwidget)
        self.port_Y_label.setObjectName(u"port_Y_label")
        self.port_Y_label.setGeometry(QRect(10, 70, 251, 31))
        self.port_Y_label.setFont(font)
        self.port_plc_label = QLabel(self.centralwidget)
        self.port_plc_label.setObjectName(u"port_plc_label")
        self.port_plc_label.setGeometry(QRect(10, 110, 91, 51))
        self.port_plc_label.setFont(font)
        self.port_x_comboBox = QComboBox(self.centralwidget)
        self.port_x_comboBox.setObjectName(u"port_x_comboBox")
        self.port_x_comboBox.setGeometry(QRect(250, 20, 151, 31))
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(28)
        font1.setBold(True)
        self.port_x_comboBox.setFont(font1)
        self.port_y_comboBox = QComboBox(self.centralwidget)
        self.port_y_comboBox.setObjectName(u"port_y_comboBox")
        self.port_y_comboBox.setGeometry(QRect(250, 70, 151, 31))
        self.port_y_comboBox.setFont(font1)
        self.port_plc_comboBox = QComboBox(self.centralwidget)
        self.port_plc_comboBox.setObjectName(u"port_plc_comboBox")
        self.port_plc_comboBox.setGeometry(QRect(250, 120, 151, 31))
        self.port_plc_comboBox.setFont(font1)
        self.connect_pushButton = QPushButton(self.centralwidget)
        self.connect_pushButton.setObjectName(u"connect_pushButton")
        self.connect_pushButton.setGeometry(QRect(410, 20, 161, 71))
        self.connect_pushButton.setFont(font)
        self.connect_pushButton.setAutoDefault(False)
        self.data_show_frame = QFrame(self.centralwidget)
        self.data_show_frame.setObjectName(u"data_show_frame")
        self.data_show_frame.setGeometry(QRect(5, 173, 1061, 601))
        self.data_show_frame.setStyleSheet(u"background:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 255, 230, 255), stop:0.55 rgba(224, 235, 188, 255), stop:0.98 rgba(210, 219, 165, 255), stop:1 rgba(0, 0, 0, 0))")
        self.data_show_frame.setFrameShape(QFrame.Box)
        self.data_show_frame.setFrameShadow(QFrame.Plain)
        self.data_show_frame.setLineWidth(3)
        self.data_show_textEdit = QTextEdit(self.data_show_frame)
        self.data_show_textEdit.setObjectName(u"data_show_textEdit")
        self.data_show_textEdit.setGeometry(QRect(11, 10, 1038, 581))
        font2 = QFont()
        font2.setFamilies([u"TH Niramit AS"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.data_show_textEdit.setFont(font2)
        self.data_show_textEdit.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.start_pushButton = QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(1090, 190, 191, 61))
        self.start_pushButton.setFont(font)
        self.stop_pushButton = QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setGeometry(QRect(1090, 260, 191, 61))
        self.stop_pushButton.setFont(font)
        self.setD_pushButton = QPushButton(self.centralwidget)
        self.setD_pushButton.setObjectName(u"setD_pushButton")
        self.setD_pushButton.setGeometry(QRect(1100, 10, 181, 71))
        self.setD_pushButton.setFont(font)
        self.displacment_parameter_frame = QFrame(self.centralwidget)
        self.displacment_parameter_frame.setObjectName(u"displacment_parameter_frame")
        self.displacment_parameter_frame.setGeometry(QRect(630, 20, 431, 131))
        self.displacment_parameter_frame.setFrameShape(QFrame.Box)
        self.displacment_parameter_frame.setFrameShadow(QFrame.Plain)
        self.displacment_parameter_frame.setLineWidth(2)
        self.unit_y_label = QLabel(self.displacment_parameter_frame)
        self.unit_y_label.setObjectName(u"unit_y_label")
        self.unit_y_label.setGeometry(QRect(360, 70, 31, 41))
        self.unit_y_label.setFont(font)
        self.displacment_y_label = QLabel(self.displacment_parameter_frame)
        self.displacment_y_label.setObjectName(u"displacment_y_label")
        self.displacment_y_label.setGeometry(QRect(10, 80, 131, 31))
        self.displacment_y_label.setFont(font)
        self.displacment_x_lineEdit = QLineEdit(self.displacment_parameter_frame)
        self.displacment_x_lineEdit.setObjectName(u"displacment_x_lineEdit")
        self.displacment_x_lineEdit.setGeometry(QRect(200, 10, 191, 41))
        self.displacment_x_lineEdit.setFont(font2)
        self.displacment_x_lineEdit.setAlignment(Qt.AlignCenter)
        self.displacment_x_label = QLabel(self.displacment_parameter_frame)
        self.displacment_x_label.setObjectName(u"displacment_x_label")
        self.displacment_x_label.setGeometry(QRect(10, 10, 171, 41))
        self.displacment_x_label.setFont(font)
        self.displacment_y_lineEdit = QLineEdit(self.displacment_parameter_frame)
        self.displacment_y_lineEdit.setObjectName(u"displacment_y_lineEdit")
        self.displacment_y_lineEdit.setGeometry(QRect(200, 70, 131, 41))
        self.displacment_y_lineEdit.setFont(font2)
        self.displacment_y_lineEdit.setAlignment(Qt.AlignCenter)
        self.save_data_pushButton = QPushButton(self.centralwidget)
        self.save_data_pushButton.setObjectName(u"save_data_pushButton")
        self.save_data_pushButton.setGeometry(QRect(1090, 710, 191, 61))
        self.save_data_pushButton.setFont(font)
        self.clear_data_pushButton = QPushButton(self.centralwidget)
        self.clear_data_pushButton.setObjectName(u"clear_data_pushButton")
        self.clear_data_pushButton.setGeometry(QRect(1090, 430, 181, 61))
        self.clear_data_pushButton.setFont(font)
        TESTER.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TESTER)
        self.statusbar.setObjectName(u"statusbar")
        TESTER.setStatusBar(self.statusbar)

        self.retranslateUi(TESTER)

        QMetaObject.connectSlotsByName(TESTER)
    # setupUi

    def retranslateUi(self, TESTER):
        TESTER.setWindowTitle(QCoreApplication.translate("TESTER", u"TESTER", None))
        self.port_X_label.setText(QCoreApplication.translate("TESTER", u"Comport for Loadcell : X axis", None))
        self.port_Y_label.setText(QCoreApplication.translate("TESTER", u"Comport for Loadcell : Y axis", None))
        self.port_plc_label.setText(QCoreApplication.translate("TESTER", u"PLC", None))
        self.port_y_comboBox.setCurrentText("")
        self.port_plc_comboBox.setCurrentText("")
        self.connect_pushButton.setText(QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.start_pushButton.setText(QCoreApplication.translate("TESTER", u"START", None))
        self.stop_pushButton.setText(QCoreApplication.translate("TESTER", u"STOP", None))
        self.setD_pushButton.setText(QCoreApplication.translate("TESTER", u"Set Displacemenrt", None))
        self.unit_y_label.setText(QCoreApplication.translate("TESTER", u"mm", None))
        self.displacment_y_label.setText(QCoreApplication.translate("TESTER", u"Target X axis", None))
        self.displacment_x_label.setText(QCoreApplication.translate("TESTER", u"Original X axis value", None))
        self.save_data_pushButton.setText(QCoreApplication.translate("TESTER", u"SAVE DATA", None))
        self.clear_data_pushButton.setText(QCoreApplication.translate("TESTER", u"Clear data", None))
    # retranslateUi

