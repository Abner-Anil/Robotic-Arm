import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

servo=board.get_pin("d:10:s")
ir1=board.get_pin("d:7:i")
ir2=board.get_pin("d:9:i")

it=pyfirmata.util.Iterator(board)

it.start()

while True:
    if ir1.read()==False and ir2.read ==False:
        servo.write(0)
        time.sleep(1)
        servo.write(0)
        time.sleep(1)
    elif ir2.read()==True:
        servo.write(180)
    elif ir1.read()==True:
        servo.write(0)
    else:
        servo.write(90)
        print:(90)
    
    
