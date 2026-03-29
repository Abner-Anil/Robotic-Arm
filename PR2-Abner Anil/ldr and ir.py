import pyfirmata
import time
board = pyfirmata.Arduino("/dev/ttyUSB1")

ir=board.get_pin("d:8:i")
ldr=board.get_pin("d:6:i")
led=board.get_pin("d:7:o")

it=pyfirmata.util.Iterator(board)

it.start()

while True:
    if ir.read() and ldr.read()==True:
        led.write(1)
                
    else:
        led.write(0)
