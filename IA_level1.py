"""
IA_level1
@author: MrChapelle
last update: 13-04-2016
"""

# Première stratégie , on recherche le coup optimal
# On ne se soucie pas de l'adversaire


import sys
import timeit
import random
from Joueur import Joueur
from Goban import *
from Exceptions import *
from Quality import Quality

class IA_level1(Joueur):
    """ Modélise les caractéristiques du joueur IA level1 """

    def __init__(self, number, game, isHuman = False,score = 0):
        """
        Constructeur : Definit les caracteristiques du joueur IA
        isHuman : bool définit si le joueur est humain ou non
        clock   : float, temps de jeu courant du joueur
        score   : int, score du joueur
        number  : int, numero du joueur IA (0 ou 1)
        moves   : array de couples désigne les coups du joueur (lgn, col)
        """
        super().__init__(number, game, isHuman = False, score = score)
        self.quality = Quality(1, self.game, self)

   

    def choose_move(self):
        """
        Détermine la qualité du coup proposé selon les critères suivants:
        -> le coup est-t-il jouable ?
        -> le coup est-il bon pour capturer l'adversaire
        -> si oui, combien de cases ?
        -> suicide ? etc ..
        """
        lgn, col = 0, 0
        imp_tmp  = 0
        
        for i in range(self.game.goban.taille):
            for j in range(self.game.goban.taille):
                importance = self.quality.importance(j, i)
                if importance > imp_tmp:
                    lgn, col = i, j 
                    imp_tmp  = importance
        
        return col, lgn
    
