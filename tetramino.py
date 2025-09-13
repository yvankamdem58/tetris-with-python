# kenmegne kamdem yvan junior 

from point import Point
import numpy as np

class Tetramino:
    def __init__(self,forme,couleur):
        self.position=Point(5,0)
        self.color=couleur
        self.degre_rotation=0
        self.forme=forme
        
    def tourne(self):
        self.degre_rotation = (self.degre_rotation + 90) % 360
        
    def image(self):
        return [point.rotation(self.degre_rotation).add(self.position) for point in self.forme]
    
    def translater(self,x,y):
        self.position=self.position.deplacement(x,y)
        
    def cloner(self):
        clone = Tetramino(self.forme, self.color)
        clone.degre_rotation=self.degre_rotation
        clone.position=self.position
        return clone
    
    def couleur(self)->str:
        return self.color
   