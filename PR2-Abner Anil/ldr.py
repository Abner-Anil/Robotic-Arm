import pyfirmata
board = pyfirmata.Arduino("/dev/ttyUSB0")

ir=board.get_pin("d:9:i")

it=pyfirmata.util.Iterator(board)

it.start()

while True:
    a=ir.read()
    print(a)
