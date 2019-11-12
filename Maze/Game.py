import pygame
import random
from Maze import Maze



pygame.init()

# Création de l'instance
maze = Maze()

# Appel des méthodes
maze.load_maze_from_file()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")
# bg = Surface((15,15))

# Coordonnées
pos_macgyver_x = 0
pos_macgyver_y = 0
width = 32
height = 43
vel = 20



EtherImg = pygame.image.load('../Images/Ether.png')
NeedleImg = pygame.image.load('../Images/Needle.png')
SyringeImg = pygame.image.load('../Images/Syringe.png')
GuardianImg = pygame.image.load('../Images/Guardian.png')

# Boucle principale
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pos_macgyver_x > 0:
        pos_macgyver_x -= vel
    elif keys[pygame.K_RIGHT] and pos_macgyver_x < (len(maze.array) * 20) - 20:
        pos_macgyver_x += vel
    elif keys[pygame.K_UP] and pos_macgyver_y > 0:
        pos_macgyver_y -= vel
    elif keys[pygame.K_DOWN] and pos_macgyver_y < (len(maze.array) * 20) - 20:
        pos_macgyver_y += vel

    # Pour qu'il n'y ait qu'une image de MacGyver
    win.fill((0,0,0))

    # boucles pour maze.array

    for line_number, line in enumerate(maze.array, start=0):
        y = line_number * 20

        for cell_number, cell in enumerate(line, start=0):
            x = cell_number * 20
            Img_path = cell.load_img()
            Img = pygame.image.load(Img_path)
            win.blit(Img, (x, y))


    # Chargement des images
    MacGyverImg = pygame.image.load('../Images/MacGyver.png')
    win.blit(MacGyverImg, (pos_macgyver_x, pos_macgyver_y))


    # mise à jour de la fenêtre
    pygame.display.update()

# quitter le jeu
pygame.quit()

maze.save_maze()

# Créer objet Macgyver
# Et un objet characters (macgyver et gardien sont enfants)
# utilisr l'objet macgyver dans game.py
# créer une fonction get macgyver_position pour déplacer le gros pâté

# commandes
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier