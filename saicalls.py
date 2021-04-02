# this is just a test function

# for using serial port
# 1 define the device being talked to.
# 2 define the port to be used by the pi. ex com1
# 3 Send command to the sai
# 4 close port
# 5 listen to the device on com 2 for any errors back. byte byte ‘199’ (0xC7), following unknowen command.

def blinkybeinky():
    print('this works')

# this will set the max brightness
def brightnessset():
    print('test')