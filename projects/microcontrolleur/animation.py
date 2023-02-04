from microbit import *



dot = Image('00300:')

for loop in range (0,3):

    display.show(Image.SQUARE)
    sleep(500)
    display.show(Image.SQUARE_SMALL)
    sleep(500)
    display.show(dot)
    sleep(500)
