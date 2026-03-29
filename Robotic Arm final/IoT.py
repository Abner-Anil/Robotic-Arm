import paho.mqtt.client as paho # import paho mqtt library
import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

servo1=board.get_pin("d:7:s")
servo2=board.get_pin("d:6:s")
servo3=board.get_pin("d:5:s")
servo4=board.get_pin("d:4:s")

def srv1_right():
    for angle in range(0,90,2):
        servo1.write(angle)
        time.sleep(0.001)

def srv1_left():
    for angle in range(90,180,2):
        servo1.write(angle)
        time.sleep(0.001)

def srv1_back():
    for angle in range(180,90,-2):
        servo1.write(angle)
        time.sleep(0.001)

def srv1_front():
    for angle in range(90,-1,-2):
        servo1.write(angle)
        time.sleep(0.001) 

def srv2_right():
    for angle in range(0,90,2):
        servo2.write(angle)
        time.sleep(0.01)

def srv2_left():
   for angle in range(90,0,-2):
        servo2.write(angle)
        time.sleep(0.001)

def srv3_right():
    for angle in range(40,80,2):
        servo3.write(angle)
        time.sleep(0.001)

def srv3_left():
    for angle in range(80,40,-2):
        servo3.write(angle)
        time.sleep(0.001)

def srv4_right():
    for angle in range(80,170,2):
        servo4.write(angle)
        time.sleep(0.001)

def srv4_left():
    for angle in range(170,60,-2):
        servo4.write(angle)
        time.sleep(0.001)

def setservo(state):
    if state == "A":
        srv1_right()
    elif state == "B":
        srv1_left()
    elif state == "C":
        srv1_back()
    elif state == "D":
        srv1_front()
    elif state == "E":
        srv2_right()
    elif state == "F":
        srv2_left()
    elif state == "G":
        srv3_right()
    elif state == "H":
        srv3_left()
    elif state == "I":
        srv4_right()
    elif state == "J":
        srv4_left()
    


    
def trig_action(client, userdata, message):  # this function will be called on receiving messages
    topic = message.topic # topic will be stored to this veriable
    msg = message.payload.decode("utf-8") # message will be decoded and stored to this veriable
    print('Topic:',topic) 
    print('Message:',msg)
    
    btn=str(msg)
    if message.topic=='kite/pr2/rgb':
        setservo(btn)

rgbclient = paho.Client() # create paho client object
rgbclient.connect('192.168.94.73') # to connect with mqtt server (replace ip with your laptop ip)
rgbclient.loop_start() # to start paho client thread 
rgbclient.on_message = trig_action # linking to the function which will be called on receiving message
rgbclient.subscribe('kite/pr2/rgb')  # subscribing to a topic

while True:
    pass
 
