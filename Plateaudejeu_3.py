from Interface import *

class Plateau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[0] * largeur for _ in range(hauteur)]
        self.score = 0
        self.current_tetramino = None

    def dessiner(self, interface):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if self.grille[y][x] != 0:
                    interface.cursor = (x, y)
                    interface.write("  ", fgcolor=interface.COULEUR['gris'])

        if self.current_tetramino:
            for point in self.current_tetramino.image():
                interface.curseur(point.x, point.y)
                interface.write("  ", fgcolor=interface.COULEUR[self.current_tetramino.couleur])
        interface.clock.tick(6)
        
    def poser_tetramino(self):
        for point in self.current_tetramino.image():
            self.grille[point.y][point.x] = 1
        self.verifier_lignes()
        self.current_tetramino = None

    def verifier_lignes(self):
        full_lignes = [i for i, row in enumerate(self.grille) if all(row)]
        for i in full_lignes:
            self.grille.pop(i)
            self.grille.insert(0, [0] * self.largeur)
        self.update_score(len(full_lignes))

    def update_score(self, lignes):
        if lignes == 1:
            self.score += 40
        elif lignes == 2:
            self.score += 200
        elif lignes == 3:
            self.score += 300
        elif lignes == 4:
            self.score += 1200

    def collision(self, tetramino):
        for point in tetramino.image():
            if point.x < 0 or point.x >= self.largeur or point.y >= self.hauteur or self.grille[point.y][point.x] != 0:
                return True
        return False

    def nouvelle_piece(self, tetramino):
        self.current_tetramino = tetramino
        if self.collision(self.current_tetramino):
            print("Game Over")

            import inspect
            # Get the current file
            current_file = _file_
            # Get the current line number
            current_line = inspect.currentframe().f_lineno
            print(f"Current file: {current_file}")
            print(f"Current line: {current_line}")

            # exit()
