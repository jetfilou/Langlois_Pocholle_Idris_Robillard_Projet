import tkinter as tk  # Import de Tkinter pour créer l'interface graphique

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

# Interface graphique
class MorpionApp:
    def __init__(self, root):
        """
        Classe principale de l'application Morpion.
        Gère l'interface graphique et l'état du jeu.
        """
        self.root = root                    # Fenêtre principale Tkinter
        self.root.title("Morpion")          # Titre de la fenêtre
        self.joueur = "X"                   # Joueur courant (X commence)
        self.grille = [" "] * 9             # État de la grille (9 cases vides)

        self.boutons = []                   # Liste pour stocker les boutons
        # Création des 9 boutons (3x3)
        for i in range(9):
            # Chaque bouton représente une case du morpion
            btn = tk.Button(
                root,
                text="",                    # Texte initial vide
                font=("Arial", 30),         # Police et taille
                width=5, height=2           # Taille du bouton
                command=lambda i=i: self.clic_case(i)  # Appel de la méthode clic_case
            )
            # Positionnement du bouton dans une grille 3x3
            btn.grid(row=i//3, column=i%3)
            self.boutons.append(btn)        # On stocke le bouton dans la liste

    def clic_case(self, index):
        """
        Gère le clic sur une case :
        - Place le symbole du joueur courant si la case est vide
        - Passe au joueur suivant (pas encore de vérification de victoire ici)
        """

# --- Lancement de l'application ---
if __name__ == "__main__":
    root = tk.Tk()              # Création de la fenêtre Tkinter
    app = MorpionApp(root)      # Instanciation de l'application
    root.mainloop()             # Boucle principale Tkinter
