import json

# for using serial port
# 1 define the device being talked to. and the baud rate
# 3 Send command to the sai
# all sai commands will be stored as functions in this file
import serial

def trigger():
    ser = serial.Serial('COM3',19200)
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
    """
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
    # set_global_max_1(global_max_1)
    # set_global_max_2(global_max_2)
    # set_looping(looping)
    # set_propagation_dampening(propagation_dampening)
    # set_propagation_delay(propagation_delay)
    # set_sensor_mirror(sensor_mirror)
    # set_sequence(sequence)
    set_time_random(time_random)
    # set_trigger_cooldown(trigger_cooldown)
    # set_trigger_latch(trigger_latch)
    # set_trigger_reset(trigger_reset)
    # set_trigger_threshold(trigger_threshold)
    # set_value_max_1(value_max_1)
    # set_value_max_2(value_max_2)
    # set_value_random(value_random)
    # set_x_attenuation(x_attenuation)
    # set_y_attenuation(y_attenuation)

def set_global_max_1(global_max_1):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(global_max_1*255))
    ser.write(b'0x6E')
    ser.write(b'{}'.format(byte))

def set_global_max_2(global_max_2):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(global_max_2*255))
    ser.write(b'0x6F')
    ser.write(b'{}'.format(byte))

def set_looping(looping):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    if looping: 
        pass
    else:
        ser.write(b'0x76')
        ser.write(b'0')

def set_propagation_dampening(propagation_dampening):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(propagation_dampening*255))
    ser.write(b'0x6A')
    ser.write(b'{}'.format(byte))

# !TODO
def set_propagation_delay(propagation_delay):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(propagation_delay))
    ser.write(b'0x6B')
    ser.write(b'{}'.format(byte))

# !TODO
def set_sensor_mirror(sensor_mirror):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    ser.write(b'0x6E')

# !TODO
def set_sequence(sequence):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    ser.write(b'0x6E')

def set_time_random(time_random):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(time_random*255))
    ser.write(b'0x78')
    ser.write(b'{}'.format(byte))

# !TODO
def set_trigger_cooldown(trigger_cooldown):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    ser.write(b'0x70')

def set_trigger_latch(trigger_latch):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    if trigger_latch:
        pass
    else:
        ser.write(b'0x72')
        ser.write(b'0')

def set_trigger_reset(trigger_reset):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(trigger_reset*255))
    ser.write(b'0x71')
    ser.write(b'{}'.format(byte))

def set_trigger_threshold(trigger_threshold):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(trigger_threshold*255))
    ser.write(b'0x69')
    ser.write(b'{}'.format(byte))

def set_value_max_1(value_max_1):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(value_max_1*255))
    ser.write(b'0x65')
    ser.write(b'{}'.format(byte))

def set_value_max_2(value_max_2):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(value_max_2*255))
    ser.write(b'0x66')
    ser.write(b'{}'.format(byte))

def set_value_random(value_random):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    byte = hex(int(value_random*255))
    ser.write(b'0x77')
    ser.write(b'{}'.format(byte))
# !TODO
def set_x_attenuation(x_attenuation):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    ser.write(b'0x6E')

# !TODO
def set_y_attenuation(y_attenuation):
    # Connect to the SAI
    ser = serial.Serial('COM3',19200)
    # Convert variable to byte
    ser.write(b'0x6E')

def saveprofile():
    ser = serial.Serial('COM6',19200)
    ser.write(b'\x67')


sendprof('AS-Angry')