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


