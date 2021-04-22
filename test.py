import time

import serial


ser = serial.Serial('COM6', 19200)
print('test')
#cmd_hex = [0xC8, 0xFF]
#cmd_bytes = bytes(cmd_hex)
#ser.write(cmd_bytes)
#ser.write(200)device
ser.write(b'\xc8\xff')

#time.sleep(1)
#ser.write(b'\x68')