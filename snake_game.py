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
fenetre.timeout(100)


#la position initial du serpent
y_serpent = longeur // 4
x_serpent = largeur // 2

serpent = [
    [y_serpent, x_serpent],
    [y_serpent, x_serpent-1],
    [y_serpent, x_serpent-2]
]

def next_mov(next_key, key):
    if next_key == curses.KEY_DOWN and key !=curses.KEY_UP:
        fenetre.addch(serpent[2][0], serpent[2][1], ' ')
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][0] += 1

    elif next_key == curses.KEY_UP and key != curses.KEY_DOWN:
        fenetre.addch(serpent[2][0], serpent[2][1], ' ')
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][0] -= 1

    elif next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
        fenetre.addch(serpent[2][0], serpent[2][1], ' ')       
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][1] -= 1 
        
    elif next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
        fenetre.addch(serpent[2][0], serpent[2][1], ' ')
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
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
    fenetre.addch(serpent[0][0], serpent[0][1], curses.ACS_CKBOARD)
    fenetre.addch(serpent[1][0], serpent[1][1], curses.ACS_CKBOARD)
    fenetre.addch(serpent[2][0], serpent[2][1], curses.ACS_CKBOARD)
    next_mov(next_key, key)
    key = key if next_key == -1 else next_key
    
    if serpent[0][0] in [0, longeur] or serpent[0][1] in [0, largeur] or serpent[0] in serpent[1] or serpent[0] in serpent[2]:
        curses.endwin()
        quit()


    if serpent[0] == food:
        food = None
        while food is None:
            new_food = [
            random.randint(1, longeur-1),
            random.randint(1, largeur-1) ]
            food = new_food if new_food not in serpent else None
        fenetre.addch(food[0], food[1], curses.ACS_PI)



'''
import curses
import random

ecran = curses.initscr()
curses.curs_set(0)
longeur, largeur = ecran.getmaxyx()
fenetre = curses.newwin(longeur, largeur, 0, 0)
fenetre.keypad(1)
fenetre.timeout(100)

x_serpent = longeur // 4
y_serpent = largeur // 2
serpent = [
    [y_serpent, x_serpent],
    [y_serpent, x_serpent - 1],
    [y_serpent, x_serpent - 2]
]

def next_mov(next_key, key):
    if next_key == curses.KEY_DOWN and key != curses.KEY_UP:
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][0] += 1
    elif next_key == curses.KEY_UP and key != curses.KEY_DOWN:
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][0] -= 1
    elif next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][1] -= 1
    elif next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
        serpent[2] = serpent[1].copy()
        serpent[1] = serpent[0].copy()
        serpent[0][1] += 1

food = [longeur // 2, largeur // 2]
fenetre.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
next_key = key

while True:
    next_key = fenetre.getch()
    if next_key != -1:
        next_mov(next_key, key)
    key = key if next_key == -1 else next_key

    if (
        serpent[0][0] in range(0, longeur)
        and serpent[0][1] in range(0, largeur)
        and serpent[0] not in serpent[1:]
    ):
        fenetre.clear()

        for segment in serpent:
            fenetre.addch(segment[0], segment[1], curses.ACS_CKBOARD)

        if serpent[0] == food:
            food = None
            while food is None:
                new_food = [
                    random.randint(1, longeur - 2),
                    random.randint(1, largeur - 2)
                ]
                food = new_food if new_food not in serpent else None
            fenetre.addch(food[0], food[1], curses.ACS_PI)

        fenetre.refresh()
    else:
        curses.endwin()
        quit()

'''


    