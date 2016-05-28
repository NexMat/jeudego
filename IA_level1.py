"""
IA_level1
@author: MrChapelle
last update: 13-05-2016
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
        # je met la valeur de taille en memoire (gain de complexité)
        n = self.game.goban.taille
        # j'initialise des valeurs de lignes et colonnes
        lgn, col = 0, 0
        # j'initialise mon importance maximale
        imp_tmp  = 0
        # num correspond à la solution choisi pour le debut de partie (cf Quality -> Fuseki (num) )
        num = 0
        # je calcule ma liste des coups de debut de partie
        L = self.quality.fuseki(num)
        # je cree une liste annexe vide
        Liste = []
      
        # tant que L n'est pas vide , si le coup est jouable, je le joue
        for i in range (len(L)) :
            try:
                if self.game.goban.test_move(L[i][0],L[i][1],self)==False:
                    return L[i][0],L[i][1]
            except:
                pass

        # je cree une liste des coups non joués
        coord_none = [(i, j) for i in range(n) for j in range(n) if self.game.goban.cell[i][j] == None]

        
        # sinon, je parcours l'ensemble des coups non joués   
        for (i,j) in coord_none :
            importance = self.quality.importance(j, i)
            if (importance > imp_tmp): # si le coup est le plus important on le choisit seul
                Liste = [(i,j)]
                imp_tmp  = importance
            if (importance == imp_tmp): # au cas ou plusieurs coups soit d'importance maximale
                Liste+=[(i,j)]

                
        N = len(Liste)
        k = random.randint(1,N-1)
             
        #je renvoie un coup pris dans la liste des coups jouables avec une importance maximale (aléatoirement)
        if L != []:
            return(Liste[k][0],Liste[k][1])
        else:
            # si la liste est vide aucun coup n'est jouable, donc on ne joue pas
            pass

                     
        """ inutile ???
        if imp_tmp == 0 :
            for col in range(n):
                for lgn in range(n):
                    try: 
                        if not self.game.goban.test_move(col, lgn, self) == False:
                            coord = (col, lgn)
                            return coord
                    except:
                        pass"""
        
        
    
