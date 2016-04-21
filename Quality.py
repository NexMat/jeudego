"""
Quality
@author: MrChapelle
last update: 21-04-2016
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

class Quality :
    """ Evalue la qualité d'un coup proposé """

    def __init__(self,niveau):
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
        for (k,l) in goban.get_neighbour(col,lgn):
            # on test si c'est un emplacement adverse
            if (goban.cell[k][l]!= None and goban.cell[k][l]!= joueur.number):
                # si le groupe associé a cet emplacement n'a qu'une liberté et
                # que cette liberté correspond au coup qui va etre joué
                # on renvoie true
                if (len(goban.return_liberty(self,goban, find_group(self, k, l, [], color)))==1 and goban.return_liberty(self,goban, find_group(self, k, l, [], color))[0]==(k,l)):
                    return True
        return False

    def construct_group(self,col,lgn,goban):
        """
        :param col : colonne du coup testé
        :param lgn : ligne du coup testé
        :param goban : état actuel du plateau
        Détecte si le coup testé contribue a la formation d'un groupe
        """
        # on parcourt les voisins du coup testé
        for (k, l) in goban.get_neighbour(self, lgn, col):
            # si un des voisins est déjà en possession du joueur alors cela contribue
            if goban.cell[k][l] == joueur.number :
                return True
        return False

    def importance(self,col,lgn):
        imp = 1
        if not self.goban.test_move(self,col,lgn,self.joueur.number):
            return(0)
        if construct_group(self,col,lgn,goban):
            imp += len(goban.find_group(self, lgn, col, [], color))
        if capture_group(self,col,lgn,goban):
            # 3 est un nombre arbitraire, a discuter ..
            imp += 3*len(goban.find_group(self, lgn, col, [], color))
        return(imp)
