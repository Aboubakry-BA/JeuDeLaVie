# views/game_ui.py
import random
from tkinter import *
from tkinter import messagebox
from models.cellule import Cell
from controllers.game_logic import gogame, arretgame

def clik_xy(x, y):
    """Retourne les coordonnées de la cellule cliquée."""
    return (int(x - x % 10), int(y - y % 10))

def show_rules_popup():
    """Affiche les règles du Jeu de la Vie."""
    rules_text = (
        "Règles du Jeu de la Vie de Conway :\n\n"
        "1. Toute cellule vivante avec moins de 2 voisins meurt de sous-population.\n"
        "2. Toute cellule vivante avec 2 ou 3 voisins survit à la prochaine génération.\n"
        "3. Toute cellule vivante avec plus de 3 voisins meurt de surpopulation.\n"
        "4. Toute cellule morte avec exactement 3 voisins devient vivante par reproduction.\n\n"
        "Notez que ces règles s'appliquent à chaque étape de l'évolution du jeu."
    )
    messagebox.showinfo("Règles du Jeu de la Vie", rules_text)

def show_guide_popup():
    """Affiche le guide du Jeu de la Vie."""
    guide_text = (
        "Guide du Jeu de la Vie :\n\n"
        "- Cliquez sur une cellule pour changer son état.\n"
        "- Le bouton Démarrer lance le jeu, faisant évoluer la grille automatiquement.\n"
        "- Utilisez le bouton Reset pour réinitialiser la grille.\n"
        "- Pendant le jeu, utilisez le bouton Pause pour mettre en pause l'évolution.\n"
        "- Le bouton Arrêter stoppe complètement le jeu.\n"
        "- Les boutons Règles et Guide affichent ces popups pour plus d'informations.\n"
        "- Vous pouvez influencer le jeu en modifiant l'état des cellules manuellement.\n"
        "- Expérimentez avec différentes configurations pour observer les résultats !"
    )
    messagebox.showinfo("Guide du Jeu de la Vie", guide_text)

def setup_game_ui(root, random_pattern=False):
    """Configure l'interface utilisateur du jeu."""
    frame = Frame(root, width=800, height=800)
    frame.pack()

    canvas = Canvas(frame, width=500, height=500)
    canvas.pack()

    g = []
    rec = []

    def table(random_pattern):
        """Initialise la grille du jeu."""
        x = 10
        y = 10
        nonlocal g, rec
        rec = []
        g = []
        for i in range(70):
            g.append([])
            rec.append([])
            for j in range(70):
                rect = canvas.create_rectangle(x, y, x + 10, y + 10, fill="white")
                rec[i].append(rect)
                if random_pattern and random.choice([True, False]):
                    canvas.itemconfig(rect, fill="black")
                    g[i].append(Cell(x, y, i, j, isAlive=True))
                else:
                    g[i].append(Cell(x, y, i, j))
                x += 10
            x = 10
            y += 10

    def whi_to_blk(event, g, rec):
        """Change l'état d'une cellule lorsqu'elle est cliquée."""
        x, y = clik_xy(event.x, event.y)
        try:
            iy = int(x / 10) - 1
            ix = int(y / 10) - 1
            if ix == -1 or iy == -1:
                raise IndexError
            if g[ix][iy].isAlive:
                canvas.itemconfig(rec[ix][iy], fill="white")
            else:
                canvas.itemconfig(rec[ix][iy], fill="black")
            g[ix][iy].switchStatus()
        except IndexError:
            return

    def paint_grid(root, canvas, g, rec):
        """Met à jour l'affichage de la grille."""
        for i in g:
            for j in i:
                if j.nextStatus != j.isAlive:
                    x, y = j.pos_matrix
                    if j.nextStatus:
                        canvas.itemconfig(rec[x][y], fill="black")
                    else:
                        canvas.itemconfig(rec[x][y], fill="white")
                    j.switchStatus()

    def pause_game():
        """Met en pause le jeu."""
        arretgame(root)

    def reset_game():
        """Réinitialise la grille du jeu."""
        arretgame(root)
        table(random_pattern)

    def stop_game():
        """Arrête complètement le jeu."""
        arretgame(root)

    button_frame = Frame(root)
    button_frame.pack(side=BOTTOM)

    start = Button(button_frame, text="Démarrer", command=lambda: gogame(root, canvas, g, rec), bg="green")
    pause = Button(button_frame, text="Pause", command=pause_game, bg="orange")
    reset = Button(button_frame, text="Reset", command=reset_game, bg="blue")
    stop = Button(button_frame, text="Arrêter", command=stop_game, bg="red")
    guide = Button(button_frame, text="Guide", command=show_guide_popup, bg="yellow")
    rules = Button(button_frame, text="Règles", command=show_rules_popup, bg="purple")

    start.grid(row=0, column=0, padx=5)
    pause.grid(row=0, column=1, padx=5)
    reset.grid(row=0, column=2, padx=5)
    stop.grid(row=0, column=3, padx=5)
    guide.grid(row=0, column=4, padx=5)
    rules.grid(row=0, column=5, padx=5)

    table(random_pattern)

    canvas.bind("<Button-1>", lambda event: whi_to_blk(event, g, rec))

    return root
