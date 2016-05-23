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

# 6) Pour chaque Goban de la liste, calculer l'importance maximale des importances
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
        new_goban.cell[emplacement[0]][emplacement[1]]= self.joueur.number
        return(new_goban)

    def liste_coups_possibles(self):             # etape 1
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

    def liste_importances_coups_possibles(self):    #etape  2
        """
        Fonction qui renvoie la liste des importances des coups possibles
        """
        L = liste_coups_possibles()
        Res = []
        for i in range(len(L)) :
            Res.append(self.quality.importance(L[i][1],L[i][0]))
        return Res

    def etape_3 (self):
        """
        Fonction qui réalise l'étape 2
        """
        L = liste_coups_possibles()
        Liste_Gobans = []
        for element in L:
            Liste_Gobans.append(copie_bogan_ajout(element))
        return Liste_Gobans

                

    def etape_4_5 (self, Liste_Gobans):
        """
        Fonction qui réalise les étapes 4 et 5
        La liste des gobans en paramètre est calculée à partir de la fonction
        étape_3
        """
        #copie du goban actuel"
        Aux = copie_goban(self)
        Liste_Aux = Liste_Gobans
        for Goban in Liste_Aux :
                        
            #le goban prend les valeurs des gobans possibles"
            self.game.goban = Goban
            #on choisit le coup du goban virtuel
            coup = self.IA_level1.choose_move()
            #on ajoute ce coup au Bogan de la liste
            Goban = copie_bogan_ajout(coup)
            #on rend sa valeur initial au goban
            self.game.goban = Aux

        return Liste_Aux
             
    def etape_6 (self, Liste_Gobans, Liste_Importances):
        """
        Fonction qui réalise l'étape 6
        """
        Aux = copie_goban(self)
        imp = 0
        Liste_Importances2 = Liste_Importances
        
        for k in range (len(Liste_Gobans)):
            self.game.goban = Liste_Gobans[k]
            imp = self.quality.importance(self.IA_level1.choose_move()[0],self.IA_level1.choose_move()[1])
            Liste_Importances2[k] += imp
            self.game.goban = Aux
            imp = 0
            
        return Liste_Importances2

    def etape_7 (self, Liste_Importances):
        """
        Fonction qui réalise l'étape 7
        """
        
        k = 0
        imp_max = 0
        for i in range(len(Liste_Importances)):
            if Liste_Importances[i]> imp_max :
                imp_max = Liste_Importances[i]
                k = i
        return k
    

    def etape_8 (self, indice, liste_initiale):
        return(liste_initiale[indice])

    

    def choose_move_minimax2(self):
        """
        Renvoie le coup choisi à partir de l'algorithme du minimax pour n=2
        """
        #etape 1
        try:
            Liste_Initiale = liste_coups_possibles()        
            if Liste_Initiale != [] :
                #etape 2 :
                Liste_Importances = liste_importances_coups_possibles()
                #etape 3 :
                Liste_Gobans = etape_3()
                #etape 4_5 :
                Liste_Gobans2 = etape_4_5(Liste_Gobans)
                #etape 6 :
                Liste_Importances2 = etape_6(Liste_Gobans2 , Liste_Importances)
                #etape 7_8 :
                return(etape_8(etape_7(Liste_Importances2),Liste_Initiale))
        except:
            pass


        for (i,j) in coord_none :
            importance = self.quality.importance(i, j)
            if (importance > imp_tmp):
                Liste = [(i,j)]
                imp_tmp  = importance
            if (importance == imp_tmp):
                Liste+=[(i,j)]
                
        N = len(Liste)
        k = random.randint(1,N-1)
        
                

        if imp_tmp == 0 :
            for col in range(self.game.goban.taille):
                for lgn in range(self.game.goban.taille):
                    try: 
                        if not self.game.goban.test_move(col, lgn, self) == False:
                            coord = (col, lgn)
                            return coord
                    except:
                        pass

        return(Liste[k][0],Liste[k][1])
        
            

    




        
