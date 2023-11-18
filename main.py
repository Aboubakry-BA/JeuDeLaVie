# main.py
from tkinter import Tk
from views.game_ui import setup_game_ui

# Appel de la fonction pour configurer l'interface utilisateur
if __name__ == "__main__":
    root = Tk()
    root.title("Galsen Coding Challenge: Jeu de la vie")
    setup_game_ui(root, random_pattern=True)
    root.mainloop()
