"""
IA_level1
@author: MrChapelle
last update: 13-04-2016
"""

# Première stratégie , on recherche le coup optimal
# On ne se soucie pas de l'adversaire
# On utilise la classe Quality

import sys
import timeit
import random
from Gui import *
from Goban import *
from Joueur import *
from Exceptions import *
from Quality import *
from Colors import cprint
from optparse import OptionParser;

class IA_level1:
    """ Modélise les caractéristiques du joueur IA level1 """

    def __init__(self, number, game, isHuman = False,score = 0, niveau = 1):
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

    def find_coup(self):
        """
        Détermine la qualité du coup proposé selon les critères suivants:
        -> le coup est t'il jouable ?
        -> le coup est il bon pour capturer l'adversaire
        -> si oui, combien de cases ?
        -> suicide ? etc ..
        """
        col, lgn = 0, 0
        for i in range(self.goban.taille):
            for j in range(self.goban.taille):
                if self.quality.importance(self,i,j)> self.quality.importance(self,col,lgn):
                    i,j = col, lgn
        coord = col, lgn   
        return coord
    
