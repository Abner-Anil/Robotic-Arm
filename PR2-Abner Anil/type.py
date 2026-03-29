import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

led1 = board.get_pin("d:11:o")
led2 = board.get_pin("d:10:o")
led3 = board.get_pin("d:9:o")



while True:
    value=input("enter value")
    if value=="blue":
        led1.write(1)
    elif
    value=="green":
        led2.write(1)
    elif value=="red":
        led3.write(1)
    else:
        led1.write(0)
        led2.write(0)
        led3.write(0)

    
    
