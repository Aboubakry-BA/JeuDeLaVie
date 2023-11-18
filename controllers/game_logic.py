# controllers/game_logic.py
import random
from models.cellule import Cell

def changeInStatus(cell, g):
    """Vérifie si l'état d'une cellule doit changer en fonction de ses voisins vivants."""
    num_alive = 0
    x, y = cell.pos_matrix
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if i == x and j == y:
                continue
            if i == -1 or j == -1:
                continue
            try:
                if g[i][j].isAlive:
                    num_alive += 1
            except IndexError:
                pass
    if cell.isAlive:
        return not (num_alive == 2 or num_alive == 3)
    else:
        return num_alive == 3

def gogame(root, canvas, g, rec):
    """Évolution automatique du jeu."""
    for i in g:
        for j in i:
            if changeInStatus(j, g):
                j.nextStatus = not j.isAlive
    paint_grid(root, canvas, g, rec)
    global begin_id
    begin_id = root.after(200, gogame, root, canvas, g, rec)

def paint_grid(root, canvas, g, rec):
    """Mise à jour de l'affichage de la grille."""
    for i in g:
        for j in i:
            if j.nextStatus != j.isAlive:
                x, y = j.pos_matrix
                if j.nextStatus:
                    canvas.itemconfig(rec[x][y], fill="black")
                else:
                    canvas.itemconfig(rec[x][y], fill="white")
                j.switchStatus()

def arretgame(root):
    """Arrêt du jeu."""
    root.after_cancel(begin_id)

def table(random_pattern=False):
    """Initialise la grille."""
    x = 10
    y = 10
    global g, rec
    rec = []
    g = []
    for i in range(70):
        g.append([])
        rec.append([])
        for j in range(70):
            if random_pattern and random.choice([True, False]):
                g[i].append(Cell(x, y, i, j, isAlive=True))
            else:
                g[i].append(Cell(x, y, i, j))
            x += 10
        x = 10
        y += 10
