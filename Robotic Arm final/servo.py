import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0")

servo1=board.get_pin("d:3:s")
servo2=board.get_pin("d:4:s")
servo3=board.get_pin("d:5:s")
servo4=board.get_pin("d:6:s")


while True:
    value=str(input("enter the value"))
    if value == "A":    
        for angle in range(0,90,1):
            servo1.write(angle)
            time.sleep(0.01)
    if value == "B":
        for angle in range(90,180,1):
            servo1.write(angle)
            time.sleep(0.01)
    if value == "C": 
        for angle in range(180,90,-1):
            servo1.write(angle)
            time.sleep(0.01)
    if value == "D": 
        for angle in range(90,-1,-1):
            servo1.write(angle)
            time.sleep(0.01)
            
    if value == "E": 
        for angle in range(60,120,1):
            servo2.write(angle)
            time.sleep(0.01)
    if value == "F": 
        for angle in range(120,60,-1):
            servo2.write(angle)
            time.sleep(0.01)

    if value == "G": 
        for angle in range(100,160,1):
            servo3.write(angle)
            time.sleep(0.01)
    if value == "H": 
        for angle in range(100,160,-1):
            servo3.write(angle)
            time.sleep(0.01)

    if value == "I": 
        for angle in range(0,90,1):
            servo4.write(angle)
            time.sleep(0.01)
    if value == "J": 
        for angle in range(90,0,-1):
            servo4.write(angle)
            time.sleep(0.01)
