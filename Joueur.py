"""
Joueur
@author: Mathieu, Robin & Théo
last update: 16-03-2016
"""

import time

class Joueur:
    """ Modélise les caractéristiques du joueur """
    
    def __init__(self, humanity, number, score = 0):
        """ Constructeur : Definit les caracteristiques du joueur 
            humanity : int (0 ou 1) qui définit si le joueur est humain(1) ou non(0)
            clock : float, temps de jeu courant du joueur
            score : int, score du joueur
            number : int, numero du joueur : 0 ou 1
        """
        self.humanity = humanity
        self.number = number
        self.clock = 0
        self.score = score
        
        
    def begin_tour (joueur):
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
            
    def update_number(joueur):
        """
        Actualise le score du joueur a la fin d'un tour
        joueur : int, 0 ou 1
        return : rien
        """
        
        self.score = 0
        value = 0
        for i in range(len(Partie.goban)):
            for j in range(len(Partie.goban)):
                if self.number == Partie.goban[i][j]:
                    value += 1
        self.score = value
    
    def choose_moove(joueur):
        """
        Determine le mouvement du joueur
        joueur : int, 0 ou 1
        """
        if joueur :
            ligne = input(" entrez votre numero de ligne de type int entre 1 et taille ")
            column = input(" entrez votre numero de colonne de type int entre 1 et taille ")
        else : 
            print(" Au tour de l IA ")
        return( ligne, column )
        
