import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB1")

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

    
while True:
    a=input("enter rgb, separated by comma")
    setcolor(a)
