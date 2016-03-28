"""
Joueur
@author: Mathieu, Robin & Théo
last update: 16-03-2016
"""

import time

class Joueur:
    """ Modélise les caractéristiques du joueur """
    
    def __init__(self, number, game, isHuman = True, score = 0):
        """ Constructeur : Definit les caracteristiques du joueur 
            isHuman : bool définit si le joueur est humain ou non
            clock   : float, temps de jeu courant du joueur
            score   : int, score du joueur
            number  : int, numero du joueur : 0 ou 1
        """
        self.isHuman = isHuman
        self.number  = number
        self.clock   = 0
        self.score   = score
        self.game    = game
        
        
    def begin_tour(joueur):
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
        
    def update_clock(joueur,begin):
        """
        Modifie le temps de jeu du joueur
        joueur : int, 0 ou 1
        begin : float, la valeur du début du tour 
        return : rien
        """
        if (self.tour % 2) == (joueur % 2):
            print("C'est pas normal")
        else :
            end = time.time()
            self.clock += (end - begin)
            
    def update_score(self):
        """
        Actualise le score du joueur a la fin d'un tour
        return : rien
        """
        self.score = 0
        value = 0
        for i in range(self.game.goban.taille):
            for j in range(self.game.goban.taille):
                if self.number == self.game.goban[i][j]:
                    value += 1
        self.score = value
    
    def choose_move(self):
        """
        Determine le mouvement du joueur
        return: les coordonnées entrées
        """
        if self.isHuman == True:
            coord = input(" ")
        else : 
            print("Au tour de l'IA")

        return coord

