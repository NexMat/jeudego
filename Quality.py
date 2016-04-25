"""
Quality
@author: MrChapelle
last update: 21-04-2016
"""

import sys
import timeit
import random
from Goban import *
from Joueur import *
from Exceptions import *

class Quality :
    """ Evalue la qualité d'un coup proposé """

    def __init__(self, niveau):
        """
        Constructeur
        """
        self.niveau = niveau

    def capture_group(self,col,lgn,goban):
        """
        :param col : colonne du coup testé
        :param lgn : ligne du coup testé
        :param goban : état actuel du plateau
        Détecte si le coup joué permettra de capturer un groupe
        Un groupe est capturé si sa liberté passe à 0
        """
        # on parcourt les voisins du coup testé
        for (k,l) in self.game.goban.get_neighbour(col,lgn):
            # on test si c'est un emplacement adverse
            if (self.game.goban.cell[k][l]!= None and self.game.goban.cell[k][l]!= joueur.number):
                # si le groupe associé a cet emplacement n'a qu'une liberté et
                # que cette liberté correspond au coup qui va etre joué
                # on renvoie true
                if (len(self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color)))==1 and self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color))[0]==(k,l)):
                    return True
        return False

    def construct_group(self,col,lgn,goban):
        """
        :param col : colonne du coup testé
        :param lgn : ligne du coup testé
        :param goban : état actuel du plateau
        Détecte si le coup testé contribue a la formation d'un groupe
        """
        num = 0
        # on parcourt les voisins du coup testé
        for (k, l) in self.game.goban.get_neighbour(lgn, col):
            # si un des voisins est déjà en possession du joueur alors cela contribue
            if self.game.goban.cell[k][l] == num :
                return True
        return False

    def importance(self,col,lgn):
        imp = 1
        num = 0   # a modifier avec le numéro du joueur IA
        if not self.game.goban.test_move(col,lgn,num):
            return(0)

        #Mauvais Choix, par forcément un bon coup
        #if construct_group(self,col,lgn,goban):
        #    imp += len(self.game.goban.find_group(self, lgn, col, [], color))
        
        if self.game.goban.capture_group(col,lgn,goban):
            # 3 est un nombre arbitraire, a discuter ..
            imp += 3*len(self.game.goban.find_group(lgn, col, [], color))
            
        return imp
