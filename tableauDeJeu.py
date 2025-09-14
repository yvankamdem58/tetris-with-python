# kenmegne kamdem yvan junior

import numpy as np
from point import Point
from tetramino import Tetramino
import random

class TableauDeJeu:
    COULEURS =[
        'noir',  
        'gris', 
        'bleu',  
        'violet',
        'vert',  
        'orange',
        'rouge',  
        'jaune'   
              ]

    def __init__(self, ligne, colonne, ecran):
        self.ecran = ecran
        self.largeur = colonne
        self.hauteur = ligne
        self.grille = np.zeros((ligne, colonne), dtype=int)
        self.score = 0

    def generer_tetramino(self):
        formes_tetraminos = {
            "I": ([Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)], 1),
            "J": ([Point(0, 0), Point(0, 1), Point(0, 2), Point(-1, 2)], 2),
            "L": ([Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2)], 3),
            "O": ([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)], 4),
            "S": ([Point(0, 0), Point(-1, 0), Point(0, 1), Point(1, 1)], 5),
            "T": ([Point(0, 0), Point(-1, 0), Point(1, 0), Point(0, 1)], 6),
            "Z": ([Point(0, 0), Point(1, 0), Point(0, 1), Point(-1, 1)], 7)
        }
        nom_forme = random.choice(list(formes_tetraminos.keys()))
        points, indice_couleur = formes_tetraminos[nom_forme]
        return Tetramino(points, indice_couleur)

    def verifier_collision(self, tetramino):
        for point in tetramino.image():
            if (point.x < 0 or point.x >= self.largeur or 
                point.y >= self.hauteur or 
                (point.y >= 0 and self.grille[point.y, point.x] != 0)):
                return True
        return False
    
    def verifier_lignes_completes(self):
        lignes_completes = 0
        for i in range(self.hauteur):
            if 0 not in self.grille[i]:
                self.grille = np.delete(self.grille, i, 0)
                self.grille = np.insert(self.grille, 0, np.zeros(self.largeur), 0)
                lignes_completes += 1
        return lignes_completes
    
    def calculer_score(self, lignes_completes):
        if lignes_completes == 1:
            self.score += 40
        elif lignes_completes == 2:
            self.score += 200
        elif lignes_completes == 3:
            self.score += 300
        elif lignes_completes == 4:
            self.score += 1200
        return self.score
    
    def dessiner(self, tetramino, position_precedente=None):  # Ajout du paramètre position_precedente
        # 1. Effacer le tétromino à sa position précédente (si elle existe)
        if position_precedente:
            for point in position_precedente:
                if 0 <= point.x < self.largeur and 0 <= point.y < self.hauteur:
                    self.ecran.curseur(point.x, point.y)
                    self.ecran.write("  ", self.ecran.COULEUR['noir'], self.ecran.COULEUR['noir'])

        # 2. Dessiner les blocs de la grille 
        for y in range(self.hauteur):
            for x in range(self.largeur):
                self.ecran.curseur(x, y)
                indice_couleur = self.grille[y, x]
                nom_couleur = self.COULEURS[indice_couleur]
                self.ecran.write("  ", self.ecran.COULEUR['noir'], self.ecran.COULEUR[nom_couleur])
        
        # 3. Dessiner le tétromino à sa nouvelle position
        for point in tetramino.image():
            if 0 <= point.x < self.largeur and 0 <= point.y < self.hauteur:
                self.ecran.curseur(point.x, point.y)
                nom_couleur = self.COULEURS[tetramino.color]
                self.ecran.write("  ", self.ecran.COULEUR['noir'], self.ecran.COULEUR[nom_couleur])
        self.ecran.clock.tick(5)
        
    def est_partie_finie(self):
        """Retourne True si la partie est terminée (tétromino bloqué en haut)."""
        for x in range(self.largeur):
            if self.grille[0, x] != 0:  # Vérifier la première ligne
                return True
        return False
