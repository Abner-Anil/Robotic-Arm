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


def setservo():
    if state == 1:
        right()
    elif state == 2:
        left()


