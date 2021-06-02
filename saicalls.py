import json

# for using serial port
# 1 define the device being talked to. and the baud rate
# 3 Send command to the sai
# all sai commands will be stored as functions in this file
import serial
port = 'COM6'
def trigger():
    global port 
    ser = serial.Serial(port ,19200)
    ser.write(b'\xc8')
    ser.close()

def reset():
    global port 
    ser = serial.Serial(port ,19200)
    ser.write(b'\xd2')
    ser.write(b'\x0a')
    ser.write(b'\x6e')
    ser.close()

def set_global_max_1(global_max_1):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(global_max_1*255)
    a = [110, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def set_global_max_2(global_max_2):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(global_max_2*255)
    a = [ 110, byte ]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def set_looping(looping):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    if looping: 
        a = [118, 1]
        a = bytearray(a)
        ser.write(a)
        ser.close()
    else:
        a = [ 118, 0 ]
        a = bytearray(a)
        ser.write(a)
        ser.close()

def set_propagation_dampening(propagation_dampening):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(propagation_dampening*255)
    a = [106, byte]
    a =  bytearray(a)
    ser.write(a)
    ser.close()


def set_sequence(sequence, x_attenuation):
    global port 
    ser = serial.Serial(port ,19200)
    points = int(len(sequence [ 0 ]))
    chunks = int(x_attenuation * 100 / (points - 1))
    msgHeader = [ 100, points, chunks ]
    msginterp = [ [ ], [ ] ]
    messageSequance = [ [ ], [ ] ]
    for i in range(len(sequence)):
        for j in range(len(sequence [ 0 ])):
            point = sequence [ i ] [ j ]
            if (point > 1 and point < 1.5):
                point = 1.0
            while (sequence [ i ] [ j ] > 1.5):
                point = point - 2.0

            messageSequance [ i ].append(int(point * 255))
            msginterp [ i ].append(0)
            # else:
            #     point = sequence [ i ] [ j ]
            #     print(point)
            #     messageSequance [ i ].append(int(point * 255))
            #     msginterp [ i ].append(1)
    message = msgHeader + messageSequance [ 0 ] + msginterp [ 0 ] + messageSequance [ 1 ] + msginterp [ 1 ]
    finalMessage = bytearray(message)
    ser.write(finalMessage)
    ser.close()


def set_time_random(time_random):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(time_random*255)
    a = [120, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()


def set_trigger_latch(trigger_latch):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    if trigger_latch:
        a = [114, 1]
        a = bytearray(a)
        ser.write(a)
        ser.close()
    else:
        a = [ 114, 0 ]
        a = bytearray(a)
        ser.write(a)
        ser.close()

def set_trigger_reset(trigger_reset):

    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(trigger_reset*255)
    a = [113, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()
    
def set_trigger_threshold(trigger_threshold):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(trigger_threshold*255)
    a = [105, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def set_value_max_1(value_max_1):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(value_max_1*255)
    a = [101, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def set_value_max_2(value_max_2):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(value_max_2*255)
    a = [102, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def set_value_random(value_random):
    # Connect to the SAI
    global port 
    ser = serial.Serial(port ,19200)
    # Convert variable to byte
    byte = int(value_random*255)
    a = [119, byte]
    a = bytearray(a)
    ser.write(a)
    ser.close()

def saveprofile():
    global port 
    ser = serial.Serial(port ,19200)
    ser.write(b'\x67')
    ser.close()


def sendprof(profile):
    """
    TODO
    1 read the profile name from json
    2 determine what needs to be sent to the sai
    3 send it and re trigger
    4
    **do a check to make sure it will actualy work without a reset
    """
    finished = 0
    with open('SAI_PROFILES.json') as f:
        data = json.load(f)
    # Load all variables to local variables
    global_max_1 = data[profile]["global_max_1"]
    global_max_2 = data[profile]["global_max_2"]
    looping = data[profile]["looping"]
    propagation_dampening = data[profile]["propagation_dampening"]
    propagation_delay = data[profile]["propagation_delay"]
    sensor_mirror = data[profile]["sensor_mirror"]
    sequence = data[profile]["sequence"]
    time_random = data[profile]["time_random"]
    trigger_cooldown = data[profile]["trigger_cooldown"]
    trigger_latch = data[profile]["trigger_latch"]
    trigger_reset = data[profile]["trigger_reset"]
    trigger_threshold = data[profile]["trigger_threshold"]
    value_max_1 = data[profile]["value_max_1"]
    value_max_2 = data[profile]["value_max_2"]
    value_random = data[profile]["value_random"]
    x_attenuation = data[profile]["x_attenuation"]
    y_attenuation = data[profile]["y_attenuation"]

    set_global_max_1(global_max_1)
    set_global_max_2(global_max_2)
    set_looping(looping)
    set_propagation_dampening(propagation_dampening)
    set_sequence(sequence, x_attenuation)
    set_time_random(time_random)
    set_trigger_latch(trigger_latch)
    set_trigger_reset(trigger_reset)
    set_trigger_threshold(trigger_threshold)
    set_value_max_1(value_max_1)
    set_value_max_2(value_max_2)
    set_value_random(value_random)
    saveprofile()

