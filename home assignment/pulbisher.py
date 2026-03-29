import paho.mqtt.client as paho # import paho mqtt library


test_client = paho.Client() # create paho client object
test_client.connect('192.168.43.56') # to connect with mqtt server (replace ip with your laptop ip)

while True:
    state = input('enter value:') # to input RGB value by user
    test_client.publish('kite/pr2/rgb', state) # publush RGB Value to the topic'kite/office/rgb'
