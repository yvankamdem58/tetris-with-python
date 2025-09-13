from random import *
from Point_2 import *


class Tetramino:
    formes = [
        ([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]),  # O
        ([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]),  # I
        ([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1)]),  # T
        ([Point(0, 0), Point(1, 0), Point(0, 1), Point(-1, 1)]),  # S
        ([Point(0, 0), Point(-1, 0), Point(0, 1), Point(1, 1)]),  # Z
        ([Point(0, 0), Point(-1, 0), Point(1, 0), Point(1, 1)]),  # L
        ([Point(0, 0), Point(1, 0), Point(-1, 0), Point(-1, 1)])  # J
    ]

    couleurs = [
        (11, 240, 11),  # vert
        (213, 11, 11),  # rouge
        (213, 180, 11),  # orange
        (213, 213, 11),  # jaune
        (40, 40, 240),  # bleu
        (255, 255, 255),  # blanc
        (210, 210, 210),  # gris
        (0, 0, 0)  # noir
    ]

    def __init__(self, shape, color):
        self.forme = shape  # random.choice(Tetramino.formes)
        self.couleur = color  # random.choice(Tetramino.couleurs)
        self.position = Point(5, 0)  # Position initiale au centre en haut
        self.degre = 0

    def translater(self, delta):
        self.position += delta

    def tourner(self):
        
        self.forme = [p.rotation(90) for p in self.forme]
        self.degre = (self.degre + 90) % 360

    def image(self):
        return [p.rotation(90) + self.position for p in self.forme]

    def clone(self):
        return Tetramino(self.forme,self.couleur)
    
a=[Point(4,5),Point(2,5),Point(5,6),Point(9,7)]
couleur=5
c=Tetramino(a,couleur)
b=c.image()
print(b)