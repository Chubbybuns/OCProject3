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


def show_ending_screen(window, content, content2=None):  # content2 optionnel
    window.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render(content, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = window.get_width() / 2 - text_rect.width / 2
    text_y = window.get_height() / 2 - text_rect.height / 2
    if content2 is not None:
        font2 = pygame.font.Font(None, 20)
        text2 = font2.render(content2, True, (255, 255, 255))
        window.blit(text2, [text_x, text_y + 30])
    window.blit(text, [text_x, text_y])


# Main loop
def main():

    macgyver, maze, guard, victory, defeat = initialization()
    pygame.init()

    # win = window
    win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

    # Nommer la fenêtre
    pygame.display.set_caption("Macgyver")
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
            show_ending_screen(win, "Victory")

        elif defeat:
            show_ending_screen(win, "Gameover", "Press Enter to restart")
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
                    cell_img_path = cell.load_img()
                    cell_img = pygame.image.load(cell_img_path)
                    win.blit(cell_img, (x, y))
                    if isinstance(cell, Finish):
                        guard_img_path = guard.load_img()
                        guard_img = pygame.image.load(guard_img_path)
                        win.blit(guard_img, (x, y))

                    items = cell.get_items()
                    for item in items:
                        item_img_path = item.load_img()
                        item_img = pygame.image.load(item_img_path)
                        win.blit(item_img, (x, y))

        # MacGyver Display
            macgyver_img_path = macgyver.load_img()
            macgyver_img = pygame.image.load(macgyver_img_path)
            win.blit(macgyver_img, (macgyver.x, macgyver.y))

            # MacGyver itemlist display
            items_list = macgyver.get_items()
            for item_number, item in enumerate(items_list, start=0):
                item_img_path = item.load_img()
                item_img = pygame.image.load(item_img_path)
                win.blit(item_img, (10 + item_number * (20 + 20), len(maze.array) * 20 + 5))

        # Window update
        pygame.display.update()

    # Game exit
    pygame.quit()

    maze.save_maze()


if __name__.endswith('__main__'):
    main()

# commandes pip
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier
# python -m pip uninstall abc
# python -m venv 'nom du venv' pour créer un environnement virtuel
# "nom du venv" \Scripts\activate.bat pour activer l'environnement virtuel

# WORD : expliquer comment marche le jeu, les 3 états, la boucle principale etc
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/235020-distribuer-facilement-nos-programmes-python-avec-cx-freeze
# créer un .exe
# donner des noms clairs aux variables et fonctions qu'on comprenne en les lisant
# ajouter une fonction main() (google)
# mettre pygame dans un fichier requirements.txt (google)

