# kenmegne kamdem yvan junior
from pygame.locals import *
from interface import Interface
from interface import KST
from tableauDeJeu import TableauDeJeu

if __name__ == "__main__": 
    ecran = Interface(20, 20, "Tetris")
    tableaudejeu = TableauDeJeu(20, 10, ecran)
    score=0
    tetraminos_courants = [tableaudejeu.generer_tetramino()] 
    tetramino_actif = 0  # Indice du tétromino actif (0 ou 1)
    
    for y in range(20):
        for x in range(20):
            ecran.cursor = (x, y)
            ecran.write("X")
    position_precedente = None

    while True: 
        tetraminos_courants[tetramino_actif].translater(0, 1)
        # Gestion de la collision
        if tableaudejeu.verifier_collision(tetraminos_courants[tetramino_actif]):
            tetraminos_courants[tetramino_actif].translater(0, -1)
            for point in tetraminos_courants[tetramino_actif].image():
                if 0 <= point.y < tableaudejeu.hauteur:
                    tableaudejeu.grille[point.y, point.x] = tetraminos_courants[tetramino_actif].color
            # Générer un ou deux nouveaux tétrominos
            lignes_completes = tableaudejeu.verifier_lignes_completes()
            nb_nouveaux_tetrominos = min(2, lignes_completes + 1)
            score=tableaudejeu.calculer_score(lignes_completes)
            tetraminos_courants = [tableaudejeu.generer_tetramino() for _ in range(nb_nouveaux_tetrominos)]
            tetramino_actif = 0 
        # Gestion des entrées
        touche = ecran.lire_touche()
        if touche == KST.DROITE and not tableaudejeu.verifier_collision(tetraminos_courants[tetramino_actif]):
            tetraminos_courants[tetramino_actif].position.deplacement(1, 0)
        elif touche == KST.GAUCHE and not tableaudejeu.verifier_collision(tetraminos_courants[tetramino_actif]):
            tetraminos_courants[tetramino_actif].position.deplacement(-1, 0)
        elif touche == KST.HAUT and not tableaudejeu.verifier_collision(tetraminos_courants[tetramino_actif]):
            tetraminos_courants[tetramino_actif].tourne()
        elif touche == KST.ESPACE:
            # Changer de tétromino actif
            tetramino_actif = 1 - tetramino_actif  # Alterner entre 0 et 1
        elif touche == KST.BAS:  # Accélérer la chute
            if not tableaudejeu.verifier_collision(tetraminos_courants[tetramino_actif]): 
                tetraminos_courants[tetramino_actif].translater(0, 1)
                tableaudejeu.ecran.clock.tick(50)
        # Sauvegarder la position actuelle avant le mouvement
        position_precedente = tetraminos_courants[tetramino_actif].image().copy() 
        if tableaudejeu.est_partie_finie():
            ecran.curseur(10,6)
            ecran.write(
             " "+"game over"+ " ",
            fgcolor=ecran.COULEUR['rouge'],
            bgcolor=ecran.COULEUR['vert']
        )
        # Dessin et affichage
        tableaudejeu.dessiner(tetraminos_courants[tetramino_actif], position_precedente) 
        ecran.curseur(12, 15)
        ecran.write(
            "score:" + str(score) + " ",
            fgcolor=ecran.COULEUR['rouge'],
            bgcolor=ecran.COULEUR['vert']
        )
        ecran.mise_a_jour()
        #ecran.pause(int(1000 * vitesse_chute)) 

    ecran.fermer()
