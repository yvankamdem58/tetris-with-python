import Interface
from Interface import *
from Plateaudejeu_3 import *
from Point_2 import *
from tetramino_3 import *
from random import *
 

if _name_ == "__main__":
    interface = Interface(10, 10, "Tetris")
    plateau = Plateau(10, 10)
    
    pieces = [
        ([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)], 'jaune'),  # O-Shape
        ([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)], 'noir'),  # I-Shape
        ([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)], 'vert'),  # S-Shape
        ([Point(0, 1), Point(1, 1), Point(1, 0), Point(2, 0)], 'rouge'),  # Z-Shape
        ([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)], 'bleu'),  # J-Shape
        ([Point(0, 1), Point(1, 1), Point(2, 1), Point(2, 0)], 'orange'),  # L-Shape
        ([Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 0)], 'gris'),  # T-Shape
    ]

    def nouvelle_piece():
        shape, color = pieces[randint(0, len(pieces) - 1)]
        return Tetramino(shape, color)

    plateau.nouvelle_piece(nouvelle_piece())
    
    while True:
        interface.pause(10)
        touche = interface.lire_touche()
        if touche == KST.HAUT:
            plateau.current_tetramino.tourner()
        elif touche == interface.KST.BAS:
            plateau.current_tetramino.translater(Point(0, 1))
            if plateau.collision(plateau.current_tetramino):
                plateau.current_tetramino.translater(Point(0, -1))
                plateau.poser_tetramino()
                plateau.nouvelle_piece(nouvelle_piece())
        elif touche == KST.GAUCHE:
            plateau.current_tetramino.translater(Point(-1, 0))
            if plateau.collision(plateau.current_tetramino):
                plateau.current_tetramino.translater(Point(1, 0))
        elif touche == KST.DROITE:
            plateau.current_tetramino.translater(Point(1, 0))
            if plateau.collision(plateau.current_tetramino):
                plateau.current_tetramino.translater(Point(-1, 0))
        
        plateau.current_tetramino.translater(Point(0, 1))
        if plateau.collision(plateau.current_tetramino):
            plateau.current_tetramino.translater(Point(0, -1))
            plateau.poser_tetramino()
            plateau.nouvelle_piece(nouvelle_piece())

        interface.ecran.fill(interface.COULEUR['noir'])
        plateau.dessiner(interface)
        interface.mise_a_jour()