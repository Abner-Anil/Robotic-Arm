import paho.mqtt.client as paho # import paho mqtt library


test_client = paho.Client() # create paho client object
test_client.connect('192.168.204.73') # to connect with mqtt server (replace ip with your laptop ip)

while True:
    rgb = input('rbg value seperated by coma:') # to input RGB value by user
    test_client.publish('kite/pr2/rgb', rgb) # publush RGB Value to the topic'kite/office/rgb'
