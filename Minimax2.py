"""
Minimax2
@author: MrChapelle
last update: 19-05-16
"""

#Implémentation de l'algorithme du minimax
#Pour l'instant, on implémente le minimax pour le cas n = 2

# Détail des étapes à réaliser :

# 1) Creer une liste de tous les coups possibles pour le joueur humain
#    Chaque coup doit être reconnaissable à partir d'un indice

# 2) Creer une liste de même longueur que la liste des coups possibles
#    La compléter avec les importances des sommets associés

# 3) Creer une liste de nouveaux gobans, de même longueur
#    Chaque goban aura été complété (virtuellement) du coup de même indice

# 4) Pour chaque Goban de la liste, déterminé quel coup sera joué par l'IA
#    En appliquant la même recherche que IA_level1

# 5) Compléter les Goban de la liste avec le coup de l'IA

# 6) Pour chaque Goban de la liste, calculer l'importance maximale de importances
#    ie: déterminer quel coup sera joué par le joueur selon IA_level1 et renvoyer son importance
#    Ajouter cette importance à la liste des importances crée en étape 2

# 7) Déterminer le maximum de la liste des importances
#    Renvoyer l'indice associé

# 8) Renvoyer le coup choisi à partir de l'indice retenu et de la liste 1


import sys
import timeit
import random
from Joueur import Joueur
from Goban import *
from Exceptions import *
from Quality import Quality

class Minimax2(Joueur):
    """ Modélise les caractéristiques du joueur IA Minimax2 """

    def __init__(self, number, game, isHuman = False, score = 0):
        """
        Constructeur : Definit les caracteristiques du joueur IA
        isHuman : bool définit si le joueur est humain ou non
        clock   : float, temps de jeu courant du joueur
        score   : int, score du joueur
        number  : int, numero du joueur IA (0 ou 1)
        moves   : array de couples désigne les coups du joueur (lgn, col)
        """
        super().__init__(number, game, isHuman = False, score = score)
        self.quality = Quality(2, self.game, self)

    def copie_goban(self):
        """
        Fonction qui copie le goban actuel dans un goban a part
        """
        new_goban = []
        for old_lines in self.game.goban.cell:
            new_goban.append(list(old_lines))
        return(new_goban)


    def copie_bogan_ajout(self,emplacement):
        """
        Fonction qui copie le goban actuel et y insère une pierre
        """
        new_goban = copie_goban(self)
        new_goban.cell.emplacement[0]emplacement[1]= self.joueur.number
        return(new_goban)

    def liste_coups_possibles(self):
        """
        Fonction qui renvoie la liste des coups possibles du goban
        """

        # On récupère toutes les cases vides
        coord_none = [(i, j) for i in range(self.game.goban.taille) for j in range(self.game.goban.taille) if self.game.goban.cell[i][j] == None]

        possible_moves = []

        for (i, j) in coord_none:
            try:
                if self.game.goban.test_move(i, j, self) == False:
                    possible_moves.append((i, j))
            except:
                pass

        return possible_moves
            
