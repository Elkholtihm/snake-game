#importation des biblio
import curses
import random

#initialiser l'ecran
ecran = curses.initscr()

#masquer la soris
curses.curs_set(0)

#la longeur/largeur de l'ecran
longeur, largeur = ecran.getmaxyx()
 
#creation dune fenaitre
fenetre  = curses.newwin(longeur, largeur, 0, 0)

#Permettre aux fenêtres de recevoir des entrées du clavier.
fenetre.keypad(1)

#le délai de mise à jour de l'écran
fenetre.timeout(50)


#la position initial du serpent
y_serpent = longeur // 4
x_serpent = largeur // 2

serpent = [
    [y_serpent, x_serpent],
    [y_serpent, x_serpent-1],
    [y_serpent, x_serpent-2]
]

def next_mov(next_key, key): 
    fenetre.addch(serpent[-1][0], serpent[-1][1], ' ')
    for i in range(len(serpent)-1, 0, -1):
        serpent[i] = serpent[i-1].copy()

    if next_key == curses.KEY_DOWN:
        serpent[0][0] += 1

    elif next_key == curses.KEY_UP:
        serpent[0][0] -= 1

    elif next_key == curses.KEY_LEFT:
        serpent[0][1] -= 1    

    elif next_key == curses.KEY_RIGHT:
        serpent[0][1] += 1
        
#position initial du nouritture
food = [longeur // 2, largeur //2]

#ajouter la nouritture au position initial
fenetre.addch(food[0], food[1], curses.ACS_PI)

#la movement initial
key = curses.KEY_RIGHT
next_key = key

#la boucle du jeu, La boucle du jeu s'arrête lorsque le joueur échoue
while True:
    next_key = fenetre.getch()
    if next_key == -1:
        next_key = key
    if (next_key == curses.KEY_DOWN and key !=curses.KEY_UP 
    or next_key == curses.KEY_UP and key != curses.KEY_DOWN
    or next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT
    or next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT
    ):
        next_mov(next_key, key)
        key = key if next_key == -1 else next_key

    for i in serpent:
        fenetre.addch(i[0], i[1], curses.ACS_CKBOARD)
    
    if (serpent[0][0] in [0, longeur] 
        or serpent[0][1] in [0, largeur] 
        or serpent[0] in serpent[1:]
        ):
        curses.endwin()
        quit()


    if serpent[0] == food:
        serpent.append([serpent[-1][0], serpent[-1][1]-1])
        food = None
        while food is None:
            new_food = [
            random.randint(1, longeur-1),
            random.randint(1, largeur-1) ]
            food = new_food if new_food not in serpent else None
        fenetre.addch(food[0], food[1], curses.ACS_PI)
        