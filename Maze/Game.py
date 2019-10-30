import pygame
import random
from Maze import Maze
from Start import Start
from Path import Path
from Wall import Wall
from Finish import Finish


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
x = 0
y = 0
width = 32
height = 43
vel = 20

# Boucle principale
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    elif keys[pygame.K_RIGHT] and x < (len(maze.array) * 20) - 20:
        x += vel
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
    elif keys[pygame.K_DOWN] and y < (len(maze.array) * 20) - 20:
        y += vel

    # Pour qu'il n'y ait qu'une image de MacGyver
    win.fill((0,0,0))

    # boucles pour maze.array
    # for line_number, line in enumerate(maze.array, start=1):

    """for cell_number, cell in enumerate(line, start=1):
            if isinstance(cell, Start):
                win.blit(StartImg, ( Startx, Starty))
            if isinstance(cell, Path):
                win.blit(PathImg, (Pathx, Pathy))
            if isinstance(cell, Wall):
                win.blit(WallImg, (Wallx, Wally))
            if isinstance(cell, Finish):
                win.blit(FinishImg, (Finishx, Finishy)"""


    # Chargement des images
    MacGyverImg = pygame.image.load('../Images/MacGyver.png')
    win.blit(MacGyverImg, (x, y))
    PathImg = pygame.image.load('../Images/Path.png')
    WallImg = pygame.image.load('../Images/Wall.png')
    StartImg = pygame.image.load('../Images/Start.png')
    FinishImg = pygame.image.load('../Images/Finish.png')
    EtherImg = pygame.image.load('../Images/Ether.png')
    NeedleImg = pygame.image.load('../Images/Needle.png')
    SyringeImg = pygame.image.load('../Images/Syringe.png')
    GuardianImg = pygame.image.load('../Images/Guardian.png')

    # mise à jour de la fenêtre
    pygame.display.update()

# quitter le jeu
pygame.quit()

maze.save_maze()

# Afficher les murs du labyrinthe et les sols avec win.blit() avec l'array (1 bloc pour le sol et 1 bloc pour le mur)
# Changer la taille du window en fonction de la taille des images et du labyrinthe
# avec len(self.array)
# Changer la taille des images en 20x20

# commandes
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier