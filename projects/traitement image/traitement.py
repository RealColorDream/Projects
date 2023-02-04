#!/bin/python3
# -*- coding: utf-8 -*-

import time
from PIL import Image

img = Image.open("nb.png")



def mystere_img(img):
	"""
	traitement mystère sur une image
	"""
	(width, height) = img.size
	for col in range(width):
		for ligne in range(height):
			pix = (col, ligne)
			couleur = img.getpixel(pix)
			inverse = 255 - couleur
			img.putpixel(pix, inverse)



def mystere(img):
	"""
	traitement mystere sur une image
	"""
	(width, height) = img.size
	for col in range(width):
		for ligne in range(height):
			pix = (col, ligne)
			couleur = img.getpixel(pix)
			inverse = 255 - couleur
			img.putpixel(pix, inverse)


def vrai_nb(img, seuil):
	"""
	transforme une image en vrai noir et blanc

	si la valeur du pixel > seuil -> blanc
	si la valeur du pixel <= seuil -> noir
	"""
	(width, height) = img.size
	for col in range(width):
		for ligne in range(height):
			pix = (col, ligne)
			couleur = img.getpixel(pix)
			if img.getpixel(pix) < seuil :
				img.putpixel(pix, 0)
			else: img.putpixel(pix, 255)


def quadrillage(img):
    (width, height) = img.size
    for col in range(0, width,50):
        for ligne in range(0, height):

            pix = (col, ligne)
            couleur = img.getpixel(pix)
            img.putpixel(pix, 255)

    for col in range (0,width):
        for ligne in range (0,height,50):

            pix = (col, ligne)
            couleur = img.getpixel(pix)
            img.putpixel(pix, 255)


def quadrillage2(img):
    (width, height) = img.size
    for col in range(0, width):
        if col%50 == 0:
            for ligne in range(0, height):
                pix = (col, ligne)
                couleur = img.getpixel(pix)
                img.putpixel(pix, 255)

    for ligne in range(0, height):
        if ligne%50 == 0:
            for col in range(0, width):
                pix = (col, ligne)
                couleur = img.getpixel(pix)
                img.putpixel(pix, 255)

def rotation (img):
    img = img.rotate(angle=90,expand=True)
    img.show()

print("taille de l'image:")
print(img.size)
print('Fonction disponible: \n 1) mystere(img) \n 2) vrai_nb(img) \n 3) quadrillage(img) \n 4) quadrillage2(img)\n 5) rotation(img)')
reponse=int(input('Quelle est la fonction que vous voulez executer ? '))


if reponse == 1:
    print("traitement en cours ...")
    duree_start = time.time()
    mystere(img)
    img.show()
    duree = time.time() - duree_start
    print("Durée du traitement : %s s" % duree)
    print("appuyer sur ctrl + F9 pour lancer une autre fonction")

if reponse == 2:
    print("traitement en cours ...")
    duree_start = time.time()
    vrai_nb(img , 40)
    img.show()
    duree = time.time() - duree_start
    print("Durée du traitement : %s s" % duree)
    print("appuyer sur ctrl + F9 pour lancer une autre fonction")

if reponse == 3:
    print("traitement en cours ...")
    duree_start = time.time()
    quadrillage(img)
    img.show()
    duree = time.time() - duree_start
    print("Durée du traitement : %s s" % duree)
    print("appuyer sur ctrl + F9 pour lancer une autre fonction")

if reponse == 4:
    print("traitement en cours ...")
    duree_start = time.time()
    quadrillage2(img)
    img.show()
    duree = time.time() - duree_start
    print("Durée du traitement : %s s" % duree)
    print("appuyer sur ctrl + F9 pour lancer une autre fonction")

if reponse == 5:
    print("traitement en cours ...")
    duree_start = time.time()
    rotation(img)
    duree = time.time() - duree_start
    print("Durée du traitement : %s s" % duree)
    print("appuyer sur ctrl + F9 pour lancer une autre fonction")
