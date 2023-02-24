#!/bin/env python3
# -*- coding: utf-8 -*-


"""
    Mini projet Puissance 4 : déceler une victoire

 le programme ci-dessous, permet de jouer mais ne décèle pas les
 victoires ! votre travail, créer les fonctions pour rendre le jeu
 fonctionnel.

 Il s'agit bien sûr de respecter scrupuleusement les spécifications de
 chacune. Un commentaire pour les lignes de code non triviales est exigé
 Pour tester votre script, il suffit d'exécuter le programme, le jeu
 commence. Le jeu se joue avec la souris uniquement, les joueurs se la
 passe à tour de role. Si vos fonctions sont justes alors le jeu
 fonctionnera !

 Bon courage.

"""


import doctest
import pygame
from pygame.locals import *

COLOR_JAUNE = (255, 174, 0)
COLOR_ROUGE = (255, 0, 0)


"""
 -------------------------------

 DÉBUT DE ZONE DE MODIFICATIONS

 -------------------------------
"""


def quatre_a_la_suite(chaine: str) -> bool:
    """
    Renvoie vrai si on trouve dans chaine
    4 caracteres (sauf l'espace) identiques à la suite
    >>> quatre_a_la_suite('  abbabbbbba')
    True
    >>> quatre_a_la_suite('OOXXOO OOX')
    False
    >>> quatre_a_la_suite('OOXXOOO OX')
    False
    >>> quatre_a_la_suite('A    A       B')
    False
    """
    taille = len(chaine)
    car_debut = chaine[0]
    indice = 1
    a_la_suite = 1
    while indice < taille:
        car = chaine[indice]
        if car == car_debut:
            if car != ' ':
                a_la_suite += 1
                if a_la_suite > 3:
                    return True
        else:
            car_debut = car
            a_la_suite = 1
        indice += 1
    return False


def extraction_ligne(grille, n):
    return grille[n]


def extraction_colone(grille, n):
    """
    >>> grille = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', 'X', 'O', 'O', 'X', ' ', ' '],[' ', 'X', 'O', 'X', 'X', ' ', ' '],[' ', 'X', 'O', 'X', 'O', 'O', ' '],          [' ', 'X', 'X', 'O', 'O', 'X', ' '],['O', 'O', 'X', 'O', 'O', 'X', ' ']]

    >>> extraction_colone(grille , 1)
    [' ', 'X', 'X', 'X', 'X', 'O']
    """
    return [x[n] for x in grille]



##def diagonale(grille, n):
##    return [grille[i][n + i] for i in range(len(grille)) if 0 <= n + i < len(grille)]
##
##
##def diagonale2(grille, n):
##    return [grille[i][n - i] for i in range(len(grille)) if 0 <= n - i < len(grille)]
##
##
##def diagonale3(grille, n):
##    return [grille[i][n + i] for i in range(6) if n + i < 7]
##
##
##def diagonale4(grille, n):
##    return [grille[i][n - i] for i in range(len(grille)) if 0 <= n + i >= len(grille)]
##
##


def alignement_ligne(grille):
    """
    Renvoie vrai si il y a un
    alignement dans les lignes
    >>> grille =[[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', 'X', 'X', 'X', ' ', ' ', ' ']]
    >>> alignement_ligne(grille)
    True
    >>> grl = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', 'X', 'X', ' ', 'X', ' ', ' ']]
    >>> alignement_ligne(grl)
    False
    """

    text = ""
    bol = False
    for i in range(0,6):
        for y in range(len(grille[i])):
            text += str(grille[i][y])
        aligne = quatre_a_la_suite(text)
        if aligne:
            bol = True
        else:
            text = ""
    return bol


def alignement_colonne(grille):
    """
    Renvoie vrai si il y a un
    alignement dans les colonnes
    >>> grille = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> alignement_colonne(grille)
    True
    >>> grl = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> alignement_colonne(grl)
    False
    """
    text = ""
    bol = False

    for i in range(0,6):
        ligne = extraction_colone(grille,i)
        for y in range(len(ligne)):
            text += ligne[y]
        aligne = quatre_a_la_suite(text)
        if aligne:
            bol = True
        else:
            text = ""
            bol = False
    return bol


def alignement_diagonale(grille):

##    text = ""
##    bol = False
##
##    for i in range(0,6):
##        ligne = diagonale(grille,i)
##        for y in range(len(ligne)):
##            text += ligne[y]
##        aligne = quatre_a_la_suite(text)
##
##    for i in range(0,6):
##        ligne = diagonale2(grille,i)
##        for y in range(len(ligne)):
##            text += ligne[y]
##        aligne = quatre_a_la_suite(text)
##
##    for i in range(0,6):
##        ligne = diagonale3(grille,i)
##        for y in range(len(ligne)):
##            text += ligne[y]
##        aligne = quatre_a_la_suite(text)
##
##    for i in range(0,6):
##        ligne = diagonale4(grille,i)
##        for y in range(len(ligne)):
##            text += ligne[y]
##        aligne = quatre_a_la_suite(text)
##
##
##        if aligne:
##            bol = True
##        else:
##            text = ""
##            bol = False
##    return bol


    bol = False
    for x in range(3):
        for y in range(4):
            if grille[x][y] == grille[x+1][y+1] == grille[x+2][y+2] == grille[x+3][y+3] != " ":
                bol = True
                return bol
    for xx in range(3):
        for yy in range(3, 7):
            if grille[xx][yy] == grille[xx+1][yy-1] == grille[xx+2][yy-2] == grille[xx+3][yy-3] != " ":
                bol = True
                return bol
    return False

def alignement(grille):

    """
    Renvoie Vrai s'il y a un alignement
    >>> grille =[[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],['X', 'X', 'X', 'X', ' ', ' ', ' ']]
    >>> alignement(grille)
    True
    """

    bool = False
    if alignement_ligne(grille) or alignement_colonne(grille) or alignement_diagonale(grille):
        bool = True
    return bool

"""
 -------------------------------

 FIN DE ZONE DE MODIFICATIONS

 -------------------------------
"""


def affichage_menu():
    ecran_menu = pygame.display.set_mode((700, 600), RESIZABLE)
    (WIDTH, HEIGHT) = ecran_menu.get_size()
    bouton_jouer = pygame.Rect(90,
                               145,
                               int(WIDTH*0.75),
                               int(HEIGHT*0.3)
                               )
    bouton_sortie = pygame.Rect(90,
                                345,
                                int(WIDTH*0.75),
                                int(HEIGHT*0.3)
                                )

    pygame.draw.rect(ecran_menu, COLOR_JAUNE, bouton_jouer)
    txt = font_menu.render("JOUER", True, COLOR_ROUGE)
    x = bouton_jouer.x + bouton_jouer.width//2 - txt.get_width()//2
    y = bouton_jouer.y + bouton_jouer.height//2 - txt.get_height()//2
    ecran_menu.blit(txt, (x, y))

    pygame.draw.rect(ecran_menu, COLOR_ROUGE, bouton_sortie)
    txt = font_menu.render("QUITTER", True, COLOR_JAUNE)
    x = bouton_sortie.x + bouton_sortie.width//2 - txt.get_width()//2
    y = bouton_sortie.y + bouton_sortie.height//2 - txt.get_height()//2
    ecran_menu.blit(txt, (x, y))

    msg = "PUISSANCE 4"
    txt = font_menu.render(msg, True, (255, 0, 255))
    x = WIDTH//2 - txt.get_width()//2
    ecran_menu.blit(txt, (x, 50))
    pygame.display.flip()


def chargement_partie():
    global fenetre
    global grille
    global fond
    global pionr
    global pionj

    pygame.init()
    fenetre = pygame.display.set_mode((700, 600), RESIZABLE)
    fond = pygame.image.load("images/grille.png")
    pionr = pygame.image.load("images/PionRouge.png").convert_alpha()
    pionj = pygame.image.load("images/PionJaune.png").convert_alpha()

    fenetre.blit(fond, (0, 0))
    pygame.display.flip()
    grille = [[' '] * 7 for _ in range(6)]
    afficher_tableau()


def case_libre_la_plus_basse(grille, num_colonne):
    ''' Dans une colonne donnée cette fonction retourne le numéro de
    la ligne de la case vide la plus basse
    entrée: grille, un tableau de 6 lignes et 7 colonnes
            num_colonne, le numéro de la colonne a analyser
    return: (num_ligne,num_colonne) numéro de ligne et numéro de colonne
            de la case vide la plus basse (dans la colonne donnée).
    '''
    num_ligne = len(grille) - 1
    while grille[num_ligne][num_colonne] != ' ':
        num_ligne -= 1
    return (num_ligne, num_colonne)


def collage_du_pion_rouge():
    global pionr
    global p
    global fond
    fond.blit(pionr, p)  # collage du pion rouge au bon endroit
    fenetre.blit(fond, (0, 0))
    pygame.display.flip()


def collage_du_pion_jaune():
    global pionj
    global p
    global fond
    fond.blit(pionj, p)  # collage du pion rouge au bon endroit
    fenetre.blit(fond, (0, 0))
    pygame.display.flip()


def recuperation_des_coordonnées_pix():
    global pion_x
    global pion_y
    pion_x = event.pos[0]  # abscisse du clic en pixels
    pion_y = event.pos[1]  # ordonnée du clic en pixels


def Victoire_message(joueur, color):
    (WIDTH, HEIGHT) = fenetre.get_size()
    msg = "Le joueur {} a gagné !".format(joueur)
    txt = myfont.render(msg, True, color)
    x = WIDTH//2 - txt.get_width()//2
    y = HEIGHT//3 - txt.get_height()//2
    fenetre.blit(txt, (x, y))
    pygame.display.flip()


def Victoirejaune():
    Victoire_message("Jaune", COLOR_JAUNE)


def Victoirerouge():
    Victoire_message("Rouge", COLOR_ROUGE)


def recuperation_des_coordonnées():
    global x
    global y
    recuperation_des_coordonnées_pix()
    x = int(pion_x/100)
    y = int(pion_y/100)


def afficher_tableau():
    for ligne in grille:
        print(ligne)


def analyse(grille):
    if alignement(grille):
        return True
    else:
        return False


pygame.init()
myfont = pygame.font.SysFont('monospace', 44)
font_menu = pygame.font.SysFont('monospace', 80)
doctest.testmod(verbose=True)


pion_x = 0
pion_y = 0
continuer_menu = 1
fin = False
while continuer_menu == 1:
    affichage_menu()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continuer_menu = 0
        if event.type == MOUSEBUTTONDOWN:  # capture de l'evenement clic gauche
            if event.button == 1:
                recuperation_des_coordonnées_pix()
                if 93 <= pion_x <= 606 and 347 <= pion_y <= 504:
                    pygame.quit()
                    continuer_menu = 0
                if 90 <= pion_x <= 608 and 145 <= pion_y <= 299:
                    chargement_partie()
                    tour = 0
                    fin = False
                    continuer_menu = 0
                    continuer = 1
                    while continuer == 1:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                continuer = 0
                                continuer_menu = 1

                            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                                print(event.pos)
                                recuperation_des_coordonnées()

                                if not fin:
                                    if grille[y][x] == ' ':

                                        (y, x) = case_libre_la_plus_basse(grille, x)
                                        if grille[y][x] == ' ':
                                            afficher_tableau()
                                            print("ligne :", y, "colonne :", x)
                                            p = (x*100, y*100)
                                            if tour % 2 == 0:
                                                grille[y][x] = 'O'
                                                collage_du_pion_rouge()
                                                if analyse(grille):
                                                    Victoirerouge()
                                                    fin = True
                                            else:
                                                grille[y][x] = 'X'
                                                collage_du_pion_jaune()
                                                if analyse(grille):
                                                    Victoirejaune()
                                                    fin = True
                                            tour = tour + 1
