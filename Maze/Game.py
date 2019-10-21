import pygame
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
win = pygame.display.set_mode((500, 500))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")

# Coordonnées
x = 0
y = 0
width = 32
height = 43
vel = 5

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
    elif keys[pygame.K_RIGHT] and x < 460:
        x+= vel
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
    elif keys[pygame.K_DOWN] and y < 440:
        y += vel

    win.fill((0,0,0))

    # boucles pour maze.array
    for line_number, line in enumerate(maze.array, start=1):

        """for cell_number, cell in enumerate (line, start=1):
            if isinstance(cell, Start):

            if isinstance(cell, Path):
            if isinstance(cell, Wall):
            if isinstance(cell, Finish):

                pass"""

    # Chargement des images
    MacGyverImg = pygame.image.load('../Images/MacGyver.png')
    win.blit(MacGyverImg, (x, y))
    PathImg = pygame.image.load('../Images/Path.png')
    WallImg = pygame.image.load('../Images/Wall.png')
    StartImg = pygame.image.load('../images/Start.png')
    FinishImg = pygame.image.load('../images/Finish.png')

    pygame.display.update()

# quitter le jeu
pygame.quit()

maze.save_maze()

# Afficher les murs du labyrinthe et les sols avec win.blit() avec l'array (1 bloc pour le sol et 1 bloc pour le mur)
# Changer la taille du window en fonction de la taille des images et du labyrinthe
# avec len(self.array)

#commandes
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier