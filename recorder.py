import serial
import datetime
import os


def get_data(port='COM5'):
    """
    Reads data from a serial port and writes it to a file with a timestamp.

    Args:
        None

    Returns:
        None
    """
    # Open the serial port
    ser = serial.Serial(port=port, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=None, baudrate=9600)  # Replace 'COM1' with the appropriate port and baud rate

    # Flush the serial input
    ser.flushInput()

    # Rest of the code
    data_stream = []
    data_state = 0
    while True:
        # Read data from the serial port byte by byte
        while ser.in_waiting:
            in_bin = ser.read()
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
                print(raw_data_int)

                # Write the data to a file
                with open('data.txt', 'a') as file:
                    file.write(str(datetime.datetime.now()) +
                               ',' + str(raw_data_int) + '\n')

                # Reset the data stream and state
                data_stream = []
                data_state = 0


if __name__ == "__main__":
    os.system('del data.txt')
    get_data("COM5")
