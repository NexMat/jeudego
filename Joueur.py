"""
Joueur
@author: Mathieu, Robin & Théo
last update: 09-03-2016
"""

import time

class Joueur:
    """ Modélise les caractéristiques du joueur """
    
    def __init__(self, humanity, number, clock = 0, score = 0):
        """ Constructeur : Definit les caracteristiques du joueur 
            humanity : int (0 ou 1) qui définit si le joueur est humain(1) ou non(0)
            clock : float, temps de jeu courant du joueur
            score : int, score du joueur
            number : int, numero du joueur : 0 ou 1
        """
        self.humanity = humanity
        this.number = number
        
        
    def update_clock(tour,joueur):
        """test à réaliser dans partie :
            if (tour % 2) == (joueur % 2):
        """
        begin = time.time()
        while (tour % 2) == (joueur % 2):
            end = time.time()
        if (tour % 2) != (joueur % 2):
            end2 = time.time()
        med = (end+end2)/2
        clock += med - begin
        
    
            
    pass

