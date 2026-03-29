import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

led = board.get_pin("d:9:o")
hi = board.get_pin("d:8:o")
hello = board.get_pin("d:7:o")

a=float(input("enter first value"))

while True:
    led.write(1)
    time.sleep(a)
    led.write(0)
    hi.write(1)
    time.sleep(a)
    hi.write(0)
    hello.write(1)
    time.sleep(a)
    hello.write(0)
