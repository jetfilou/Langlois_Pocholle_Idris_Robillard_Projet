import tkinter as tk
from tkinter import messagebox

# --- Logique du morpion ---
def verifier_gagnant(grille):
    combinaisons = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for (x, y, z) in combinaisons:
        if grille[x] == grille[y] == grille[z] and grille[x] != " ":
            return True
    return False

# --- Interface graphique ---
class MorpionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morpion")
        self.joueur = "X"
        self.grille = [" "] * 9

        self.boutons = []
        for i in range(9):
            btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
                            command=lambda i=i: self.clic_case(i))
            btn.grid(row=i//3, column=i%3)
            self.boutons.append(btn)

    def clic_case(self, index):
        if self.grille[index] == " ":
            self.grille[index] = self.joueur
            self.boutons[index].config(text=self.joueur)

            if verifier_gagnant(self.grille):
                messagebox.showinfo("Fin de partie", f"Le joueur {self.joueur} a gagnÃ© !")
                self.reinitialiser()
                return

            if " " not in self.grille:
                messagebox.showinfo("Fin de partie", "Match nul !!")
                self.reinitialiser()
                return

            self.joueur = "O" if self.joueur == "X" else "X"

    def reinitialiser(self):
        self.grille = [" "] * 9
        for btn in self.boutons:
            btn.config(text="")
        self.joueur = "X"

# --- Lancement ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MorpionApp(root)
    root.mainloop()