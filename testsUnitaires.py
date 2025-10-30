import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk

# Import du module à tester
import morpion

class TestVerifierGagnant(unittest.TestCase):
    def test_aucun_gagnant(self):
        grille = [" "] * 9
        self.assertFalse(morpion.verifier_gagnant(grille))

    def test_ligne_haut_gagnante(self):
        grille = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(morpion.verifier_gagnant(grille))

    def test_colonne_milieu_gagnante(self):
        grille = [" ", "O", " ", " ", "O", " ", " ", "O", " "]
        self.assertTrue(morpion.verifier_gagnant(grille))

    def test_diagonale_principale_gagnante(self):
        grille = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertTrue(morpion.verifier_gagnant(grille))

    def test_aucun_gagnant_cas_mixte(self):
        grille = ["X","O","X","O","X","O","O","X","O"]
        self.assertFalse(morpion.verifier_gagnant(grille))

    def test_diagonale_secondaire_gagnante(self):
        grille = ["X","X","O"," ","O"," ","O"," "," "]
        self.assertTrue(morpion.verifier_gagnant(grille))


class TestMorpionApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # empêche l'affichage de la fenêtre
        self.app = morpion.MorpionApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_clic_case_vide(self):
        self.app.clic_case(0)
        self.assertEqual(self.app.grille[0], "X")
        self.assertEqual(self.app.boutons[0]["text"], "X")

    def test_alternance_joueur(self):
        self.app.clic_case(0)
        self.app.clic_case(1)
        self.assertEqual(self.app.joueur, "X")  # Après deux tours, retour à X

    @patch("morpion.messagebox.showinfo")
    def test_victoire_detectee(self, mock_info):
        self.app.grille = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
        self.app.clic_case(2)  # X gagne
        mock_info.assert_called_once_with("Fin de partie", "Le joueur X a gagné !")

    @patch("morpion.messagebox.showinfo")
    def test_match_nul(self, mock_info):
        self.app.grille = ["X","O","X","X","O","O","O","X"," "]
        self.app.joueur = "X"
        self.app.clic_case(8)  # Dernier coup, match nul
        mock_info.assert_called_once_with("Fin de partie", "Match nul !")

    def test_reinitialisation(self):
        self.app.grille = ["X"] * 9
        self.app.reinitialiser()
        self.assertEqual(self.app.grille, [" "] * 9)
        for btn in self.app.boutons:
            self.assertEqual(btn["text"], "")
        self.assertEqual(self.app.joueur, "X")


if __name__ == "__main__":
    unittest.main()
