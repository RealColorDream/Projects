#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
programme permetant de simuler le jeu du tictactoe / tictactoe
"""

import random
import math


class TicTacToe:
    """
    classe permetant de simuler le jeu du tictactoe / tictactoe
    """

    def __init__(self):
        """
        initialisation des variables utiles a la classe
        self.liste : liste qui contient les cases de la grille
        self.joueur : joueur qui doit jouer en premier
        self.gagnant : le gagant de la partie
        self.partie_gagner : permet de savoir si la partie est fini
        self.nbcasevide : permet de savoir combien de case sont vide
        """

        print("""
1|2|3
4|5|6
7|8|9""")

        self.liste = ([" ", " ", " "], [" ", " ", " "], [" ", " ", " "])
        self.joueur = "0"
        self.gagnant = ""
        self.partie_gagner = False
        self.nbcasevide = 9

    def est_fini(self):
        """
        Fonction permetant de savoir si la partie est fini
        retourne le gagnant ou null si le match est  nul
        """

        liste = self.liste

        for i in range(3):
            if liste[i][0] == liste[i][1] and liste[i][1] == liste[i][2] and liste[i][2] == liste[i][0]:
                gagnant = liste[i][0]
                return gagnant

        for i in range(3):
            if liste[0][i] == liste[1][i] and liste[1][i] == liste[2][i] and liste[2][i] == liste[0][i]:
                gagnant = liste[0][i]
                return gagnant

        if liste[0][0] == liste[1][1] and liste[1][1] == liste[2][2] and liste[2][2] == liste[0][0]:
            gagnant = liste[0][0]
            return gagnant

        if liste[0][2] == liste[1][1] and liste[1][1] == liste[2][0] and liste[2][0] == liste[0][2]:
            gagnant = liste[0][2]
            return gagnant

        if self.nbcasevide == 0 and self.gagnant == "":
            gagnant = "null"
            return gagnant
        else:
            return ""

    def tour_de(self):
        """
        Fonction permetant de savoir a qui est le tour de jouer
        Renvoie "x" ou "0"
        """

        if self.joueur == "X":
            self.joueur = "0"
        else:
            self.joueur = "X"

    def joue(self, joueur, pos):
        """
        fonction permetant au joueur d'inscrire un symbole dans la grille
        parametre ( joueur : "X" ou "0" , pos : position de la case )
        """
        liste = self.liste
        emplacement_tuple = math.ceil(pos/3) - 1
        emplacement_variable = pos % 3-1
        if liste[emplacement_tuple][emplacement_variable] != " ":
            print("Un joueur a deja jouer cette case")
            self.tour_de()
        if liste[emplacement_tuple][emplacement_variable] == " ":
            liste[emplacement_tuple][emplacement_variable] = self.joueur
            self.nbcasevide = self.nbcasevide - 1
        print(self)
        if self.est_fini() == "X" or self.est_fini() == "0" or self.est_fini() == "null":
            self.partie_gagner = True
        else:
            self.partie_gagner = False

        print(self.est_fini())

    def reset(self):
        """
        fonction permetant de réinitialiser la partie
        """

        print("""
1|2|3
4|5|6
7|8|9""")

        self.liste = ([" ", " ", " "], [" ", " ", " "], [" ", " ", " "])
        self.joueur = "0"
        self.gagnant = ""
        self.partie_gagner = False
        self.nbcasevide = 9

    def __str__(self):
        """
        fonction permetant d'afficher la grille au joueur
        renvoie : la grille
        """

        chaine = ""
        liste = self.liste
        for nbligne in range(3):
            chaine = chaine + "\n"
            for nbcol in range(3):
                chaine = chaine + liste[nbligne][nbcol]
                if nbcol < 2:
                    chaine += "|"
        return chaine

# niveau 1


random.seed(2023)
o = TicTacToe()
while o.partie_gagner is not True:
    joueur = int(input("Joueur : "))
    o.joue(o.tour_de(), joueur)
    if o.joue(o.tour_de(), random.randint(1, 9)) == "Un joueur a deja jouer cette case":
        o.joue(o.tour_de(), random.randint(1, 9))
