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
        self.data_show_frame.setStyleSheet(u"background:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 255, 230, 255), stop:0.55 rgba(224, 235, 188, 255), stop:0.98 rgba(210, 219, 165, 255), stop:1 rgba(0, 0, 0, 0))")
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
        self.displacment_parameter_frame.setObjectName(u"displacment_parameter_frame")
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
        self.displacment_x_lineEdit = QLineEdit(self.displacment_parameter_frame)
        self.displacment_x_lineEdit.setObjectName(u"displacment_x_lineEdit")
        self.displacment_x_lineEdit.setGeometry(QRect(20, 50, 131, 41))
        self.displacment_x_lineEdit.setFont(font1)
        self.displacment_x_lineEdit.setAlignment(Qt.AlignCenter)
        self.displacment_x_label = QLabel(self.displacment_parameter_frame)
        self.displacment_x_label.setObjectName(u"displacment_x_label")
        self.displacment_x_label.setGeometry(QRect(20, 0, 131, 51))
        self.displacment_x_label.setFont(font)
        self.displacment_y_lineEdit = QLineEdit(self.displacment_parameter_frame)
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

        self.init_serial()
        self.read_only_textEdit()

        self.start_record = False

        QMetaObject.connectSlotsByName(TESTER)
    # setupUi
        
    def read_only_textEdit(self):
        self.displacment_x_lineEdit.setReadOnly(True)
        self.displacment_y_lineEdit.setReadOnly(True)
        self.data_show_textEdit.setReadOnly(True)


    def init_serial(self):
        self.xloadcell_ser = serial.Serial()
        self.yloadcell_ser = serial.Serial()
        self.plc_ser = serial.Serial()

    def retranslateUi(self, TESTER):
        TESTER.setWindowTitle(QCoreApplication.translate("TESTER", u"TESTER", None))
        self.port_X_label.setText(QCoreApplication.translate("TESTER", u"\u0e41\u0e01\u0e19 X", None))
        self.port_Y_label.setText(QCoreApplication.translate("TESTER", u"\u0e41\u0e01\u0e19 Y", None))
        self.port_plc_label.setText(QCoreApplication.translate("TESTER", u"PLC", None))
        self.port_y_comboBox.setCurrentText("")
        self.port_plc_comboBox.setCurrentText("")
        self.port_x_pushButton.setText(QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.port_y_pushButton.setText(QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.port_plc_pushButton.setText(QCoreApplication.translate("TESTER", u"CONNECT", None))
        self.start_pushButton.setText(QCoreApplication.translate("TESTER", u"START", None))
        self.stop_pushButton.setText(QCoreApplication.translate("TESTER", u"STOP", None))
        self.test_pushButton.setText(QCoreApplication.translate("TESTER", u"TEST", None))
        self.unit_y_label.setText(QCoreApplication.translate("TESTER", u"\u0e21\u0e34\u0e25\u0e25\u0e34\u0e40\u0e21\u0e15\u0e23", None))
        self.displacment_y_label.setText(QCoreApplication.translate("TESTER", u"\u0e23\u0e30\u0e22\u0e30\u0e41\u0e01\u0e19Y", None))
        self.unit_x_label.setText(QCoreApplication.translate("TESTER", u"\u0e21\u0e34\u0e25\u0e25\u0e34\u0e40\u0e21\u0e15\u0e23", None))
        self.displacment_x_label.setText(QCoreApplication.translate("TESTER", u"\u0e23\u0e30\u0e22\u0e30\u0e41\u0e01\u0e19X", None))
        self.save_data_pushButton.setText(QCoreApplication.translate("TESTER", u"SAVE DATA", None))
        self.port_x_pushButton.clicked.connect(self.port_x_button)
        self.port_y_pushButton.clicked.connect(self.port_y_button)
        self.port_plc_pushButton.clicked.connect(self.port_plc_button)
        self.stop_pushButton.clicked.connect(self.stop_button)
        self.start_pushButton.clicked.connect(self.start_button)
        self.test_pushButton.clicked.connect(self.test_button)
        self.save_data_pushButton.clicked.connect(self.save_data_button)
    # retranslateUi
        self.read_comport()

    # retranslateUi

    def read_comport(self):
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.port_x_comboBox.addItem(port.device)
            self.port_y_comboBox.addItem(port.device)
            self.port_plc_comboBox.addItem(port.device)

    def read_loadcell(self):
        # Read data from the serial port byte by byte
        # Reset the data stream and state
        data_stream = []
        data_state = 0
        raw_data = 0
        while self.xloadcell_ser.in_waiting:
            in_bin = self.xloadcell_ser.read()
            in_hex = hex(int.from_bytes(
                in_bin, byteorder='little')).lstrip('0x')
            if len(in_hex) == 0:
                in_hex = '00'
            elif len(in_hex) == 1:
                in_hex = '0' + in_hex
            data_stream.append(in_hex)

            # Process the received data
            if data_state == 0:
                if in_hex == 'cf':
                    data_state = 1
                else:
                    data_state = 0
            elif data_state == 1:
                if in_hex == 'fc':
                    data_state = 2
                else:
                    data_state = 0
            elif data_state == 2:
                if in_hex == 'cc':
                    data_state = 3
                else:
                    data_state = 0
            elif data_state == 3:
                if in_hex == 'ff':
                    data_state = 4
                else:
                    data_state = 0
            else:
                data_state = 0

            if data_state == 4:
                raw_data = data_stream[-9:-4]
                # print(raw_data)
                raw_data = ''.join(raw_data)
                raw_data_int = int(raw_data,16)
                if raw_data_int > 0x7FFFFF:
                    raw_data_int = 0
                raw_data = raw_data_int


        return raw_data

    def port_x_button(self):
        selected_port = self.port_x_comboBox.currentText()
        try:
            self.xloadcell_ser.port = selected_port
            self.xloadcell_ser.baudrate = 9600
            self.xloadcell_ser.timeout = 1
            self.xloadcell_ser.open()
            self.xloadcell_ser.close()
            # disable port button
            self.port_x_pushButton.setEnabled(False)
            # disable combobox
            self.port_x_comboBox.setEnabled(False)
            print("Connected to port: ", selected_port)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")


    def port_y_button(self):
        selected_port = self.port_y_comboBox.currentText()
        try:
            self.yloadcell_ser.port = selected_port
            self.yloadcell_ser.baudrate = 9600
            self.yloadcell_ser.timeout = 1
            self.yloadcell_ser.open()
            self.yloadcell_ser.close()
            # disable port button
            self.port_y_pushButton.setEnabled(False)
            # disable combobox
            self.port_y_comboBox.setEnabled(False)
            print("Connected to port: ", selected_port)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def port_plc_button(self):
        selected_port = self.port_plc_comboBox.currentText()
        try:
            self.plc_ser.port = selected_port
            self.plc_ser.baudrate = 4800
            self.plc_ser.timeout = 1
            self.plc_ser.open()
            self.plc_ser.close()
            # disable port button
            self.port_plc_pushButton.setEnabled(False)
            # disable combobox
            self.port_plc_comboBox.setEnabled(False)
            print("Connected to port: ", selected_port)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def stop_button(self):
        print("stop_button")
        self.start_record = False

    def start_button(self):
        # check vertical loadcell connection
        if self.yloadcell_ser.is_open == False:
            self.yloadcell_ser.open()
            print("Y loadcell connected")

        # check horizontal loadcell connection
        if self.xloadcell_ser.is_open == False:
            self.xloadcell_ser.open()
            print("X loadcell connected")

        self.plc_rtu = ModbusSerialClient(self.plc_ser.port, baudrate=4800, method='rtu')
        self.plc_rtu.connect()
        print("PLC connected")
        self.plc_rtu.write_coil(address=4, value=0, slave=1)

        self.plc_rtu.write_register(address=10, value=4000,slave=1)
        self.plc_rtu.write_register(address=1, value=1000,slave=1)

        self.plc_rtu.write_coil(address=10, value=1, slave=1)
        self.plc_rtu.write_coil(address=0, value=1, slave=1)

        self.plc_rtu.write_coil(address=2, value=1, slave=1)

        # set timer
        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.timer_event)
        self.start_record = True


    def timer_event(self):
        # reset timer and run timer again
        if self.start_record == True:
            self.timer.start(50)
            try:
                # xloadcell_value = self.xloadcell_ser.readline().decode('utf-8').strip()
                xloadcell_value = self.read_loadcell()
                yloadcell_value = self.yloadcell_ser.readline().decode('utf-8').strip()


                horizontal_value = self.plc_rtu.read_input_registers(address=0, count=1, slave=1)
                vertical_value = self.plc_rtu.read_input_registers(address=2, count=1, slave=1)

                # add timestamp to data
                current_time = datetime.now()

                log_message = str(current_time.strftime("%H:%M:%S")) + "," + str(horizontal_value.registers[0]) +"," + str(vertical_value.registers[0]) + "," + str(xloadcell_value) +"," + yloadcell_value
                self.data_show_textEdit.append(log_message)
            except Exception as e:
                print(f"Error connecting to PLC: {e}")
        else:
            self.timer.stop()
            if self.plc_rtu.is_socket_open():
                self.plc_rtu.close()
                print("PLC disconnected")

            if self.xloadcell_ser.is_open:
                self.xloadcell_ser.close()
                print("X loadcell disconnected")

            if self.yloadcell_ser.is_open:
                self.yloadcell_ser.close()
                print("Y loadcell disconnected")

    def test_button(self):
        print("test_button")

    def save_data_button(self):
        if self.start_record == True:
            self.timer.stop()
            self.start_record = False
            if self.plc_rtu.is_socket_open():
                self.plc_rtu.close()
                print("PLC disconnected")

            if self.xloadcell_ser.is_open:
                self.xloadcell_ser.close()
                print("X loadcell disconnected")

            if self.yloadcell_ser.is_open:
                self.yloadcell_ser.close()
                print("Y loadcell disconnected")

        # open save file dialog
        file_name = QFileDialog.getSaveFileName(self.centralwidget, 'Save File', '', 'Text files (*.txt)')
        if file_name[0]:
            with open(file_name[0], 'w') as file:
                file.write(self.data_show_textEdit.toPlainText())
                print("Data saved to: ", file_name[0])
        # clear data
        self.data_show_textEdit.clear()



if __name__ == "__main__":
    app = QApplication([])
    tester = QMainWindow()
    ui = Ui_TESTER()
    ui.setupUi(tester)
    tester.show()
    app.exec()
