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

    def __init__(self, niveau, game, joueur):
        """
        Constructeur
        """
        self.niveau = niveau
        self.game   = game
        self.joueur = joueur

    def capture_group(self, col, lgn):
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
            if (self.game.goban.cell[k][l]!= None and self.game.goban.cell[k][l]!= self.joueur.number):
                # si le groupe associé a cet emplacement n'a qu'une liberté et
                # que cette liberté correspond au coup qui va etre joué
                # on renvoie true
                if (len(self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color)))==1 and self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color))[0]==(k,l)):
                    return True
        return False

    def construct_group(self, col, lgn):
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

    def importance(self, col, lgn):
        try:
            ret = self.game.goban.test_move(col, lgn, self.joueur)
            # S'il n'y a pas de capture
            if ret == False:
                return 1
            # S'il y a capture
            else:
                imp = 0
                # On calcule le nombre de pierres utilisées
                for group in ret:
                    imp += len(group)
                return imp * 2
                    
        # S'il y a erreur
        except:
            return 0
           
