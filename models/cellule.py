# models/cellule.py

class Cell:
    def __init__(self, x, y, i, j, isAlive=False):
        """Initialise une cellule avec des coordonnées, un état initial, et des positions dans la grille."""
        self.isAlive = isAlive
        self.nextStatus = None  # Prochain état de la cellule
        self.pos_screen = (x, y)  # Position à l'écran
        self.pos_matrix = (i, j)  # Position dans la matrice

    def __str__(self):
        """Représentation sous forme de chaîne de la cellule."""
        return str(self.isAlive)

    def __repr__(self):
        """Représentation de la cellule pour l'affichage."""
        return str(self.isAlive)

    def switchStatus(self):
        """Inverse l'état de la cellule (vivante devient morte et vice versa)."""
        self.isAlive = not self.isAlive
