def verifier_gagnant(grille):
    """
    Vérifie si un joueur a gagné au morpion.
    Paramètre :
        grille : liste de 9 cases contenant "X", "O" ou " " (vide)
    Retourne :
        True si un joueur a aligné 3 symboles identiques, False sinon
    """

    # Liste de toutes les combinaisons gagnantes possibles
    # Ce sont les indices dans la grille à vérifier
    combinaisons = [
        (0, 1, 2),  # Ligne du haut
        (3, 4, 5),  # Ligne du milieu
        (6, 7, 8),  # Ligne du bas
        (0, 3, 6),  # Colonne de gauche
        (1, 4, 7),  # Colonne du milieu
        (2, 5, 8),  # Colonne de droite
        (0, 4, 8),  # Diagonale principale
        (2, 4, 6)   # Diagonale secondaire
    ]

    # Pour chaque combinaison possible
    for (x, y, z) in combinaisons:
        # Si les trois cases contiennent le même symbole (X ou O) et ne sont pas vides
        if grille[x] == grille[y] == grille[z] and grille[x] != " ":
            # Cela signifie qu’un joueur a gagné
            return True

    # Si aucune combinaison gagnante n’a été trouvée
    return False
