import time

import serial


ser = serial.Serial('COM3', 19200)

# Send global max 1
ser.write(b'0x6E')
byteToSend = float.hex(0.8*255)
ser.write(b'{byteToSend}')
# # Send global max 2
# ser.write(b'0x6F')
# # Send looping
# ser.write(b'0x77')
# # Send propagtion dampening
# ser.write(b'0x6A')
# # Send propagation delay
# ser.write(b'0x6B')
# # Send sensor mirror
# ser.write(b'0x6C')
# # Send sequence
# ser.write(b'0x64')
# # Send time random
# ser.write(b'0x78')
# # Send trigger cooldown
# ser.write(b'0x70')
# # Send trigger latch
# ser.write(b'0x72')
# # Send trigger reset
# ser.write(b'0x71')
# # Send trigger threshold
# ser.write(b'0x69')
# # Send value max 1
# ser.write(b'0x65')
# # Send value max 2
# ser.write(b'0x66')
# # Send value random
# ser.write(b'0x77')
# # Send x attenuation

# # Send y attenuation