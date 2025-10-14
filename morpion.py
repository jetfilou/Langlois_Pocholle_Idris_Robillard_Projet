import tkinter as tk                     # Import du module Tkinter pour l'interface graphique
from tkinter import messagebox            # Import de messagebox pour afficher les fenêtres d'information

def verifier_gagnant(grille):
    """
    Vérifie si un joueur a gagné au morpion.
    Paramètre :
        grille : liste de 9 cases contenant "X", "O" ou " " (vide)
    Retourne :
        True si un joueur a aligné 3 symboles identiques, False sinon
    """

    # Liste de toutes les combinaisons gagnantes possibles (indices dans la grille)
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

    # Vérifie chaque combinaison
    for (x, y, z) in combinaisons:
        if grille[x] == grille[y] == grille[z] and grille[x] != " ":
            return True  # Un joueur a gagné

    return False  # Aucun gagnant trouvé


# --- Classe principale de l'application ---
class MorpionApp:
    def __init__(self, root):
        """
        Classe principale du jeu Morpion.
        Crée la fenêtre, la grille et initialise le jeu.
        """
        self.root = root
        self.root.title("Morpion")

        self.joueur = "X"         # Joueur qui commence
        self.grille = [" "] * 9   # Représente la grille du jeu (vide au départ)

        self.boutons = []         # Liste pour stocker les boutons

        # Création des 9 boutons (3x3)
        for i in range(9):
            btn = tk.Button(
                root,
                text="",
                font=("Arial", 30),
                width=5, height=2,
                command=lambda i=i: self.clic_case(i)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.boutons.append(btn)

    def clic_case(self, index):
        """
        Gère le clic sur une case :
        - Place le symbole du joueur courant si la case est vide.
        - Vérifie ensuite si le joueur a gagné ou s'il y a match nul.
        - Passe au joueur suivant sinon.
        """
        if self.grille[index] == " ":
            # Place le symbole du joueur courant
            self.grille[index] = self.joueur
            self.boutons[index].config(text=self.joueur)

            # Vérifie si le joueur a gagné
            if verifier_gagnant(self.grille):
                messagebox.showinfo("Fin de partie", f"Le joueur {self.joueur} a gagné !")
                self.reinitialiser()
                return

            # Vérifie le match nul (aucune case vide)
            if " " not in self.grille:
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.reinitialiser()
                return

            # Passe au joueur suivant
            self.joueur = "O" if self.joueur == "X" else "X"

    def reinitialiser(self):
        """
        Réinitialise la grille et les boutons pour recommencer une partie.
        """
        self.grille = [" "] * 9
        for btn in self.boutons:
            btn.config(text="")
        self.joueur = "X"


# --- Lancement de l'application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MorpionApp(root)
    root.mainloop()
