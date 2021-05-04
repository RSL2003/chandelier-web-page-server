

# for using serial port
# 1 define the device being talked to. and the baud rate
# 3 Send command to the sai
# all sai commands will be stored as functions in this file
import serial

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
def setglbbright(level):

def setbrightact1(level):
    #random
def setbrightact2(level):

def actseq(npoints, nchunks, a1val, a1flat, a2val, a2flat):
# act sequenes

def saveprofile():
    ser = serial.Serial('COM6',19200)
    ser.write(b'\x67')



