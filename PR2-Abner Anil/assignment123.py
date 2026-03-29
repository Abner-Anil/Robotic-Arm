import pyfirmata
import time
board = pyfirmata.Arduino("/dev/ttyUSB1")

ir=board.get_pin("d:9:i")
buz=board.get_pin("d:8:o")
led=board.get_pin("d:11:o")
servo=board.get_pin("d:12:s")
led1=board.get_pin("d:7:o")
'
ldr=board.get_pin("d:6:i")

it=pyfirmata.util.Iterator(board)

it.start()

while True:
    if ir.read():
        print("no motion")
        buz.write(1)
        led.write(0)
    else:
        print("motion detected")
        buz.write(0)
        led.write(1)
        time.sleep(0.05)
        led.write(0)
        time.sleep(0.05)
        for angle in range(0,181,4):
            servo.write(angle)
            time.sleep(0.01)
        for angle in range(180,-1,-4):
            servo.write(angle)
            time.sleep(0.01)
    if ldr.read()==False:
        led1.write(0)
                
    else:
        led1.write(1)


    
