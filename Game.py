import pygame
import random
from Maze.Maze import Maze
from Consumables.Ether import Ether
from Consumables.Syringe import Syringe
from Consumables.Tube import Tube
from Consumables.Needle import Needle
from Characters.MacGyver import MacGyver





pygame.init()

# Création de l'instance
maze = Maze()


# Appel des méthodes
maze.load_maze_from_file()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")


# Coordonnées
width = 32
height = 43

macgyver = MacGyver(0, 0, maze, 20)

Needle = Needle()
Tube = Tube()
Ether = Ether()
Ether.place_object_randomly(maze)
Tube.place_object_randomly(maze)
Needle.place_object_randomly(maze)

# Boucle principale
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        macgyver.move_left()
    elif keys[pygame.K_RIGHT]:
        macgyver.move_right()
    elif keys[pygame.K_UP]:
        macgyver.move_up()
    elif keys[pygame.K_DOWN]:
        macgyver.move_down()

    # donner l'item à macgyver s'il y en a un

    # Pour qu'il n'y ait qu'une image de MacGyver
    # win.fill((0,0,0))

    # boucles pour maze.array

    for line_number, line in enumerate(maze.array, start=0):
        y = line_number * 20

        for cell_number, cell in enumerate(line, start=0):
            x = cell_number * 20
            Img_path = cell.load_img()
            Img = pygame.image.load(Img_path)
            win.blit(Img, (x, y))

            items = cell.get_items()
            for item in items:
                Img_path = item.load_img()
                Img = pygame.image.load(Img_path)
                win.blit(Img, (x, y))

    # Chargement des images
    Img_path = macgyver.load_img()
    Img = pygame.image.load(Img_path)
    win.blit(Img, (macgyver.x, macgyver.y))

    # mise à jour de la fenêtre
    pygame.display.update()

# quitter le jeu
pygame.quit()

maze.save_maze()

# Créer objet Macgyver
# Et un objet characters (macgyver et gardien sont enfants)
# utilisr l'objet macgyver dans game.py
# créer une fonction get macgyver_position pour déplacer le gros pâté
# créer des items (seringue..) et les faire apparaître randomly sur des paths avec random.choice(list)
# créer une fonction add_item dans cell.py puis créer une fonction qui récupère les items des cases

# mettre les objets (gestion) en aléatoire à la l37 (get random cell from array) puis afficher
# faire la différence entre mur et chemin (récupérer toutes les cases puis retirer les mauvaises)
# dans game, seulement création d'instance et appel de fonctions

# compléter fonction macgver

# commandes pip
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier

# objet + class macgyver + collision
#finir collision + ajouter et enlever les objets quand macgyver passe + afficher les objet récupérés quelque part en agrandissant la fenêtre de jeu