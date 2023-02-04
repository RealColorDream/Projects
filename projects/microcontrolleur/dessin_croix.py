from microbit import *

def affiche_slash ():

    j=4
    for i in range (0,5):
        display.set_pixel(i,j,9)
        j=j-1


def affiche_antislash ():

    for i in range (0,5):
        display.set_pixel(i,i,9)

def affiche_croix ():
    affiche_antislash ()
    affiche_slash ()

affiche_croix()