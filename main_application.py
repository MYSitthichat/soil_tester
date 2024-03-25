""" create UI class that handle the main application """

import sys
import serial
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from test_ui import Ui_TESTER

from PySide6.QtCore import QTimer

from pymodbus.client import ModbusSerialClient
from datetime import datetime
from PySide6.QtWidgets import QFileDialog
import serial.tools.list_ports


class MainApplication(QMainWindow, Ui_TESTER):
    """ Main application class """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Main Application')

        self.read_comport()

        self.init_serial()
        self.read_only_textEdit()
        self.start_record = False

        # add events handler
        self.port_x_pushButton.clicked.connect(self.port_x_button)
        self.port_y_pushButton.clicked.connect(self.port_y_button)
        self.port_plc_pushButton.clicked.connect(self.port_plc_button)
        self.stop_pushButton.clicked.connect(self.stop_button)
        self.start_pushButton.clicked.connect(self.start_button)
        self.test_pushButton.clicked.connect(self.test_button)
        self.save_data_pushButton.clicked.connect(self.save_data_button)
        self.show()

    def read_comport(self):
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
                raw_data_int = int(raw_data, 16)
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

        self.plc_rtu = ModbusSerialClient(
            self.plc_ser.port, baudrate=4800, method='rtu')
        self.plc_rtu.connect()
        print("PLC connected")
        self.plc_rtu.write_coil(address=4, value=0, slave=1)

        self.plc_rtu.write_register(address=10, value=4000, slave=1)
        self.plc_rtu.write_register(address=1, value=1000, slave=1)

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

                horizontal_value = self.plc_rtu.read_input_registers(
                    address=0, count=1, slave=1)
                vertical_value = self.plc_rtu.read_input_registers(
                    address=2, count=1, slave=1)

                # add timestamp to data
                current_time = datetime.now()

                log_message = str(current_time.strftime("%H:%M:%S")) + "," + str(horizontal_value.registers[0]) + "," + str(
                    vertical_value.registers[0]) + "," + str(xloadcell_value) + "," + yloadcell_value
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
        file_name = QFileDialog.getSaveFileName(
            self.centralwidget, 'Save File', '', 'Text files (*.txt)')
        if file_name[0]:
            with open(file_name[0], 'w') as file:
                file.write(self.data_show_textEdit.toPlainText())
                print("Data saved to: ", file_name[0])
        # clear data
        self.data_show_textEdit.clear()

    def center(self):
        """ Center the application window """
        frame_geometry = self.frameGeometry()
        center_point = QApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def read_only_textEdit(self):
        self.displacment_x_lineEdit.setReadOnly(True)
        self.displacment_y_lineEdit.setReadOnly(True)
        self.data_show_textEdit.setReadOnly(True)

    def init_serial(self):
        self.xloadcell_ser = serial.Serial()
        self.yloadcell_ser = serial.Serial()
        self.plc_ser = serial.Serial()


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    MAIN_APP = MainApplication()
    sys.exit(APP.exec())
