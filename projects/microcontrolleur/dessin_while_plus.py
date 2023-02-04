from microbit import *

x=0
while x != 5:
    display.set_pixel(x,2,9)
    x = x +1


y=0
while y != 5:
    display.set_pixel(2,y,9)
    y = y +1
