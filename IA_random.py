"""
IA_random
@author: MrChapelle
last update: 12-04-2016
"""

import sys
import timeit
import random
from Gui import *
from Goban import *
from Joueur import *
from Exceptions import *
from Colors import cprint
from optparse import OptionParser;

class IA_random:
    """ Modélise les caractéristiques du joueur IA random """

    def __init__(self, number, game, isHuman = False,score = 0, niveau = 0):
        """
        Constructeur : Definit les caracteristiques du joueur IA
        isHuman : bool définit si le joueur est humain ou non
        clock   : float, temps de jeu courant du joueur
        score   : int, score du joueur
        number  : int, numero du joueur IA (0 ou 1)
        moves   : array de couples désigne les coups du joueur (lgn, col)
        """
        self.isHuman = isHuman
        self.number  = number
        self.clock   = 0
        self.score   = score
        self.game    = game
        self.moves   = []
        self.niveau = niveau

    def play_turn(self):
        """
        Determine le mouvement de l'IA de manière récursive jusqu'à
        obtenir un coup possible
        
        return: les coordonnées entrées
        """
        for i in range(100):                #on teste aléatoirement 100 fois 
            col = random.randint(0,8)
            lgn = randomm.randint(0,8)
            if self.goban.test_move(self, col, lgn, number):
                coord = (col, lgn)
                break
            return coord
        else:
            for col in range(self.goban.taille):
                for lgn in range(self.goban.taille):
                    if self.gaban.cell[col][lgn] == None:
                        coord = (col, lgn)
                        break
                break
            return coord
















        
    
