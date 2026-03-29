import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB1")

ledR = board.get_pin("d:9:p")
ledG = board.get_pin("d:10:p")
ledB = board.get_pin("d:11:p")

R=eval(input("enter value"))/255
G=eval(input("enter value"))/255
B=eval(input("enter value"))/25545


while True:
    ledR.write(R)
    ledG.write(G)
    ledB.write(B)

