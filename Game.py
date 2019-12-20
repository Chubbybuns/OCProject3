import pygame
from Maze.Maze import Maze
from Maze.Finish import Finish
from Consumables.Ether import Ether
from Consumables.Tube import Tube
from Consumables.Needle import Needle
from Consumables.Syringe import Syringe
from Characters.MacGyver import MacGyver
from Characters.Guard import Guard

#changement

pygame.init()

maze = Maze()

maze.load_maze_from_file()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")

macgyver = MacGyver(0, 0, maze, 20)

needle = Needle()
tube = Tube()
ether = Ether()
guard = Guard()
ether.place_object_randomly(maze)
tube.place_object_randomly(maze)
needle.place_object_randomly(maze)

"""finish_cell = maze.array[len(maze.array) // 20 * 15][len(maze.array) // 20 * 15]
print(finish_cell)"""

# Main loop
gameover = False
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif macgyver.x == (len(macgyver.maze.array) * 20) - 20 and macgyver.y == (len(macgyver.maze.array) * 20) - 20:
            first_item = macgyver.item_list[0]
            if isinstance(first_item, Syringe):
                gameover = True
            elif not isinstance(first_item, Syringe):
                gameover = False

    if gameover:
        print("gameover")
        win.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = win.get_width() / 2 - text_rect.width / 2
        text_y = win.get_height() / 2 - text_rect.height / 2
        win.blit(text, [text_x, text_y])

    if not gameover:
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
                Img_path = cell.load_img()
                Img = pygame.image.load(Img_path)
                win.blit(Img, (x, y))
                if isinstance(cell, Finish):
                    Img_path2 = guard.load_img()
                    Img2 = pygame.image.load(Img_path2)
                    win.blit(Img2, (x, y))

                items = cell.get_items()
                for item in items:
                    Img_path = item.load_img()
                    Img = pygame.image.load(Img_path)
                    win.blit(Img, (x, y))

    # MacGyver Display
        Img_path = macgyver.load_img()
        Img = pygame.image.load(Img_path)
        win.blit(Img, (macgyver.x, macgyver.y))

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

# si on arrive sur le garde sans seringue, mort sans faire run = False
# sinon, win
# le faire en haut de la boucle principale avec un booléen

# corrigé place_object_randomly() pour que les objets ne puissent pas se mettre sur la case finish
