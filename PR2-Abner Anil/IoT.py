import paho.mqtt.client as paho # import paho mqtt library
import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

ledR = board.get_pin("d:9:p")
ledG = board.get_pin("d:10:p")
ledB = board.get_pin("d:11:p")

def setcolor(rgb):
    rgb=rgb.split(",")
    r=eval(rgb[0])/255
    g=eval(rgb[1])/255
    b=eval(rgb[2])/255
    
    ledR.write(r)
    ledG.write(b)
    ledB.write(g)
    
def trig_action(client, userdata, message):  # this function will be called on receiving messages
    topic = message.topic # topic will be stored to this veriable
    msg = message.payload.decode("utf-8") # message will be decoded and stored to this veriable
    print('Topic:',topic) 
    print('Message:',msg) 

    if message.topic=='kite/pr2/rgb':
        setcolor(msg)

rgbclient = paho.Client() # create paho client object
rgbclient.connect('192.168.43.56') # to connect with mqtt server (replace ip with your laptop ip)
rgbclient.loop_start() # to start paho client thread 
rgbclient.on_message = trig_action # linking to the function which will be called on receiving message
rgbclient.subscribe('kite/pr2/rgb')  # subscribing to a topic

while True:
    pass
 
