import paho.mqtt.client as paho # import paho mqtt library
import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

servo=board.get_pin("d:10:s")

def right():
    servo.write(90)
    print("right")

def left():
    servo.write(0)
    print("left")

def setservo(state):
    if state == 1:
        right()
    elif state == 2:
        left()
    
def trig_action(client, userdata, message):  # this function will be called on receiving messages
    topic = message.topic # topic will be stored to this veriable
    msg = message.payload.decode("utf-8") # message will be decoded and stored to this veriable
    print('Topic:',topic) 
    print('Message:',msg)
    
    btn=eval(msg)
    if message.topic=='kite/pr2/rgb':
        setservo(btn)

rgbclient = paho.Client() # create paho client object
rgbclient.connect('192.168.43.56') # to connect with mqtt server (replace ip with your laptop ip)
rgbclient.loop_start() # to start paho client thread 
rgbclient.on_message = trig_action # linking to the function which will be called on receiving message
rgbclient.subscribe('kite/pr2/rgb')  # subscribing to a topic

while True:
    pass
 
