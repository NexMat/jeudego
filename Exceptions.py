"""
Exceptions
@author: Nexmat, MrChapelle, MorfoisseT
last update: 08-04-2016
"""

class Forbidden_move(Exception):
    def __init__(self, lgn, col, msg):
        self.lgn = lgn
        self.col = col
        self.msg = msg

    def __str__(self):
        return self.msg + " en (" + str(self.lgn) + ", " + str(self.col) +")"
