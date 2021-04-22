# this is just a test function

# for using serial port
# 1 define the device being talked to.
# 2 define the port to be used by the pi. ex com1
# 3 Send command to the sai
# 4 close port
# 5 listen to the device on com 2 for any errors back. byte byte ‘199’ (0xC7), following unknowen command.
import serial


def blinkybeinky():
    print('this works')

# this will set the max brightness
def brightnessset():
    print('test')
def trigger():
    ser = serial.Serial('COM6',19200)
    ser.write(b'\xc8')
def reset():
    ser = serial.Serial('COM6',19200)
    ser.write(b'\xd2')
    ser.write(b'\x0a')
    ser.write(b'\x6e')

def sendprof(profile):
    """
    TODO
    1 read the profile name from json
    2 determine what needs to be sent to the sai
    3 send it and re trigger
    4
    **do a check to make sure it will actualy work without a reset
***
    """
