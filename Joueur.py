"""
Joueur
@author: Mathieu, Robin & Théo
last update: 16-03-2016
"""

import time
import sys
import timeit
import random
from Gui import *
from Goban import *
from Exceptions import *
from Colors import cprint
from optparse import OptionParser;
#from IA_random import *
from Quality import *
#from IA_level1 import *

class Joueur:
    """ Modélise les caractéristiques du joueur """
    
    def __init__(self, number, game, isHuman = True, score = 0):
        """ Constructeur : Definit les caracteristiques du joueur 
            isHuman : bool définit si le joueur est humain ou non
            clock   : float, temps de jeu courant du joueur
            score   : int, score du joueur
            number  : int, numero du joueur (0 ou 1)
            moves   : array de couples désigne les coups du joueur (lgn, col)
        """
        self.isHuman  = isHuman
        self.number   = number
        self.clock    = 0
        self.score    = score
        self.komi     = score
        self.game     = game
        self.moves    = []
        self.captures = 0
        
        
    def begin_tour(self):
        """
        Determine le moment ou le joueur commence a joueur
        joueur : int, 0 ou 1
        Return : float, temps en secondes
        """
        if (self.tour % 2) == (joueur % 2):
            begin = time.time()
        else :
            print("Pas mon tour")
        return(begin)
        
    def update_clock(self,begin):
        """
        Modifie le temps de jeu du joueur
        joueur : int, 0 ou 1
        begin : float, la valeur du début du tour 
        return : none
        """
        if (self.tour % 2) == (joueur % 2):
            print("C'est pas normal")
        else :
            end = time.time()
            self.clock += (end - begin)
            
    def update_score(self):
        """
        Actualise le score du joueur a la fin d'un tour
        return : none
        """
        self.score = 0
        value = 0
        for i in range(self.game.goban.taille):
            for j in range(self.game.goban.taille):
                if self.number == self.game.goban.cell[i][j]:
                    value += 1
        self.score = value + self.captures
        self.score += self.komi
    
    def choose_move(self):
        """
        Determine le mouvement du joueur
        return: les coordonnées entrées
        """
        coord = input(" ")
        return coord

    def save_move(self, lgn, col):
        """Sauvegarde les coups du joueur
        Tableau de couple (ligne, colonne)
        """
        self.moves.append((lgn, col))

    def detect_territory(self):
        """Detection du territoire par un parcours en largeur"""

        # On récupère toutes les cases vides
        coord_none = [(i, j) for i in range(self.game.goban.taille) for j in range(self.game.goban.taille) if self.game.goban.cell[i][j] == None]

        while coord_none != []:
            (lgn, col) = coord_none.pop(0)
            (empty_cells, adverse_cells) = self.BFS(lgn, col)

            # Si on ne rencontre pas de pierres adverses lors du parcours, le 
            if adverse_cells == []:
                pass

            

        
    def BFS(self, lgn, col):
        """Parcourt en largeur pour déterminer les territoires"""

        # Cellules vides
        empty_cells = []
        # Cellules adverses
        adverse_cells = []

        # Initialisation de la file
        queue = [(lgn, col)]

        while queue != []:
            # On récupère le premier élément de la file
            (i,j) = queue.pop(0)
            # On récupère la liste des voisins 
            voisins = self.game.goban.get_neighbour(i, j)

            for (k, l) in voisins:

                # Si le voisin est vide
                if self.game.goban.cell[k][l] == None:
                    queue.append((k,l)) # On ajoute à la file
                    empty_cells.append((k,l)) # On l'enregistre pour optimisation

                # Si il est de la même couleur
                elif self.game.goban.cell[k][l] == self.number:
                    pass # On ne fait rien

                # Si il est de couleur différente
                else:
                    adverse_cells.append((k, l)) # On l'enregistre

        return empty_cells, adverse_cells

