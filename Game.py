import pygame
from Maze.Maze import Maze
from Consumables.Ether import Ether
from Consumables.Syringe import Syringe
from Consumables.Tube import Tube
from Consumables.Needle import Needle
from Characters.MacGyver import MacGyver
from Characters.Guard import Guard

pygame.init()

maze = Maze()

# Appel des méthodes
maze.load_maze_from_file()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")


# Coordonnées
"""width = 32
height = 43"""

macgyver = MacGyver(0, 0, maze, 20)

needle = Needle()
tube = Tube()
ether = Ether()
guard = Guard()
ether.place_object_randomly(maze)
tube.place_object_randomly(maze)
needle.place_object_randomly(maze)

finish_cell = maze.array[len(maze.array) // 20 * 15][len(maze.array) // 20 * 15]
print(finish_cell)

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
    # macgyver.get_item_from_current_cell()

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

# commandes pip
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier

# finir collision + ajouter et enlever les objets quand macgyver passe + afficher les objet récupérés quelque part en agrandissant la fenêtre de jeu