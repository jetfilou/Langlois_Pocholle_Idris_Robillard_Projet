import tkinter as tk  # Import de Tkinter pour l'interface graphique

# --- Logique du morpion ---
def verifier_gagnant(grille):
    """
    Vérifie si un joueur a gagné au morpion.
    Paramètre :
        grille : liste de 9 cases contenant "X", "O" ou " " (vide)
    Retourne :
        True si un joueur a aligné 3 symboles identiques, False sinon
    """
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
    for (x, y, z) in combinaisons:
        if grille[x] == grille[y] == grille[z] and grille[x] != " ":
            return True
    return False


# Interface graphique
class MorpionApp:
    def __init__(self, root):
        """
        Classe principale de l'application Morpion.
        Gère l'interface graphique et l'état du jeu.
        """
        self.root = root
        self.root.title("Morpion")
        self.joueur = "X"                   # Joueur courant
        self.grille = [" "] * 9             # 9 cases vides au départ

        self.boutons = []
        for i in range(9):
            # Chaque bouton représente une case du morpion
            btn = tk.Button(
                root,
                text="",                    # Texte initial vide
                font=("Arial", 30),
                width=5, height=2,
                command=lambda i=i: self.clic_case(i)  # Appel de la méthode clic_case
            )
            btn.grid(row=i//3, column=i%3)
            self.boutons.append(btn)

    def clic_case(self, index):
        """
        Gère le clic sur une case :
        - Place le symbole du joueur courant si la case est vide
        - Passe au joueur suivant (pas encore de vérification de victoire ici)
        """

# --- Lancement de l'application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MorpionApp(root)
    root.mainloop()
