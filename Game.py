import pygame
from Maze.Maze import Maze
from Maze.Finish import Finish
from Consumables.Ether import Ether
from Consumables.Tube import Tube
from Consumables.Needle import Needle
from Characters.MacGyver import MacGyver
from Characters.Guard import Guard


def initialization():
    maze = Maze()

    maze.load_maze_from_file()
    macgyver = MacGyver(0, 0, maze, 20)
    needle = Needle()
    tube = Tube()
    ether = Ether()
    guard = Guard()
    ether.place_object_randomly(maze)
    tube.place_object_randomly(maze)
    needle.place_object_randomly(maze)
    victory = False
    defeat = False

    return macgyver, maze, guard, victory, defeat


macgyver, maze, guard, victory, defeat = initialization()

pygame.init()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")


def show_ending_screen(content, content2=None):  # content2 optionnel
    win.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render(content, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = win.get_width() / 2 - text_rect.width / 2
    text_y = win.get_height() / 2 - text_rect.height / 2
    if content2 is not None:
        font2 = pygame.font.Font(None, 20)
        text2 = font2.render(content2, True, (255, 255, 255))
        win.blit(text2, [text_x, text_y + 30])
    win.blit(text, [text_x, text_y])


# Main loop
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if macgyver.on_finish_cell():
        if macgyver.has_syringe():
            victory = True
        else:
            defeat = True

    if victory:
        show_ending_screen("Victory")

    elif defeat:
        show_ending_screen("Gameover", "Press Enter to restart")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            macgyver, maze, guard, victory, defeat = initialization()

    else:
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
        macgyver.get_item_from_current_cell()
        macgyver.make_syringe_if_possible()

    # Pour tout réafficher
        win.fill((0, 0, 0))

    # Maze and consumables display

        for line_number, line in enumerate(maze.array, start=0):
            y = line_number * 20

            for cell_number, cell in enumerate(line, start=0):
                x = cell_number * 20
                img_path = cell.load_img()
                img = pygame.image.load(img_path)
                win.blit(img, (x, y))
                if isinstance(cell, Finish):
                    img_path2 = guard.load_img()
                    img2 = pygame.image.load(img_path2)
                    win.blit(img2, (x, y))

                items = cell.get_items()
                for item in items:
                    Img_path = item.load_img()
                    Img = pygame.image.load(Img_path)
                    win.blit(Img, (x, y))

    # MacGyver Display
        img_path = macgyver.load_img()
        img = pygame.image.load(img_path)
        win.blit(img, (macgyver.x, macgyver.y))

        items_list = macgyver.get_items()
        for item_number, item in enumerate(items_list, start=0):
            Img_path = item.load_img()
            Img = pygame.image.load(Img_path)
            win.blit(Img, (10 + item_number * (20 + 20), len(maze.array) * 20 + 5))

    # Window update
    pygame.display.update()

# Game exit
pygame.quit()

maze.save_maze()

# commandes pip
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier
# python -m venv 'nom du venv' pour créer un environnement virtuel
# python -m pip uninstall abc
# "nom du venv" \Scripts\activate.bat pour activer l'environnement virtuel

# WORD : expliquer comment marche le jeu, les 3 états, la boucle principale etc
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/235020-distribuer-facilement-nos-programmes-python-avec-cx-freeze
# créer un .exe
# donner des noms clairs aux variables et fonctions qu'on comprenne en les lisant
# ajouter une fonction main() (google)
# mettre pygame dans un fichier requirements.txt (google)

