# Importation des bibliothèques nécessaires
import curses
import random

# Initialisation de l'écran
ecran = curses.initscr()

# Masquage du curseur
curses.curs_set(0)

# Récupération des dimensions de l'écran
longeur, largeur = ecran.getmaxyx()

# Création d'une fenêtre occupant tout l'écran
fenetre = curses.newwin(longeur, largeur, 0, 0)

# Autorisation de recevoir des entrées du clavier
fenetre.keypad(1)

# Délai de rafraîchissement de l'écran
fenetre.timeout(100)

# Position initiale du serpent
y_serpent = longeur // 4
x_serpent = largeur // 2
serpent = [
    [y_serpent, x_serpent],
    [y_serpent, x_serpent - 1],
    [y_serpent, x_serpent - 2]
]

# Dessin des bordures de la fenêtre
for i in range(0, largeur):
        if i == largeur // 8:
            for j in range(longeur // 8, longeur - (longeur // 8)):
                fenetre.addch(j, i, curses.ACS_SBSB)
        if i == largeur - (largeur // 8):
            for j in range(longeur // 8, longeur - (longeur // 8)):
                fenetre.addch(j, i, curses.ACS_SBSB)

for j in range(0, longeur):
        if j==longeur // 8:
            for i in range(largeur // 8, largeur - (largeur // 8)):
                fenetre.addch(j, i, curses.ACS_BSBS)
        if j==longeur - (longeur // 8):
            for i in range(largeur // 8, largeur - (largeur // 8)):
                fenetre.addch(j, i, curses.ACS_BSBS)

            
# Fonction pour effectuer le déplacement du serpent
def next_mov(next_key, key):
    fenetre.addch(serpent[-1][0], serpent[-1][1], ' ')

    # Mise à jour des positions du serpent
    for i in range(len(serpent) - 1, 0, -1):
        serpent[i] = serpent[i - 1].copy()

    # Déplacement en fonction de la touche pressée
    if next_key == curses.KEY_DOWN:
        serpent[0][0] += 1
    elif next_key == curses.KEY_UP:
        serpent[0][0] -= 1
    elif next_key == curses.KEY_LEFT:
        serpent[0][1] -= 1
    elif next_key == curses.KEY_RIGHT:
        serpent[0][1] += 1
#Dans cet fonction je commence par  eliminee le tail et deplacer par la suite le corps du serpent a la position du tete
#et deplacer la tete selon 'next_key'
        

# Position initiale de la nourriture
food = [longeur // 2, largeur // 2]

# Ajout de la nourriture à sa position initiale
fenetre.addch(food[0], food[1], curses.ACS_DIAMOND)

# Initialisation du mouvement
key = curses.KEY_RIGHT
next_key = key

#initialisation du score
score = 0

# Boucle principale du jeu, s'arrêtant lorsque le joueur échoue
while True:
    # Récupération de la prochaine touche pressée
    next_key = fenetre.getch()
    if next_key == -1:
        next_key = key

    # Vérification de la validité du mouvement
    if (next_key == curses.KEY_DOWN and key != curses.KEY_UP
            or next_key == curses.KEY_UP and key != curses.KEY_DOWN
            or next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT
            or next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT
    ):
        next_mov(next_key, key)
        key = key if next_key == -1 else next_key

    # Affichage du serpent selon la nouvelle position
    for i in serpent:
        fenetre.addch(i[0], i[1], curses.ACS_BLOCK)  

    # Vérification des conditions de fin de jeu
    if (serpent[0][0] in [longeur // 8, longeur - (longeur // 8)]
            or serpent[0][1] in [largeur // 8, largeur - (largeur // 8)]
            or serpent[0] in serpent[1:]
    ):
        curses.endwin()
        quit()
    
    # Vérifie si la tête du serpent atteint la position de la nourriture
    if serpent[0] == food:

        # Ajuste la vitesse du jeu en fonction du score
        if 2*score <= 80:
            fenetre.timeout(100-2*score)

        # afficher le score
        score +=1
        fenetre.addstr(longeur // 12, largeur // 12, "YOU'RE SCORE IS : {}".format(score))
        curses.beep()

        # Ajout d'un nouveau segment au serpent
        serpent.append([serpent[-1][0], serpent[-1][1] - 1])

        # Réinitialisation de la position de la nourriture
        food = None
        while food is None:
            new_food = [
                random.randint((longeur // 8) + 1, longeur- (longeur // 8) - 1),
                random.randint((largeur // 8) + 1, largeur- (largeur // 8) - 1)
            ]
            food = new_food if new_food not in serpent else None
        fenetre.addch(food[0], food[1], curses.ACS_DIAMOND)


