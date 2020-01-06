import pygame
from Maze.Maze import Maze
from Maze.Finish import Finish
from Consumables.Ether import Ether
from Consumables.Tube import Tube
from Consumables.Needle import Needle
from Characters import MacGyver, Guard


def initialization():
    """
    Creates and returns instances of Macgyver, guard, needle, tube and ether
    Places the objects randomly in the maze
    """
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


def show_ending_screen(window, content, content2=None):
    """
    Ending screen display depending on victory or defeat
    """
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


def main():
    """
    Main loop
    """

    macgyver, maze, guard, victory, defeat = initialization()
    pygame.init()

    win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20 + 30))

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

            macgyver.get_item_from_current_cell()
            macgyver.make_syringe_if_possible()

            win.fill((0, 0, 0))

            for line_number, line in enumerate(maze.array, start=0):
                y = line_number * 20

                for cell_number, cell in enumerate(line, start=0):
                    x = cell_number * 20
                    cell_img_path = cell.get_image_path()
                    cell_img = pygame.image.load(cell_img_path)
                    win.blit(cell_img, (x, y))
                    if isinstance(cell, Finish):
                        guard_img_path = guard.get_image_path()
                        guard_img = pygame.image.load(guard_img_path)
                        win.blit(guard_img, (x, y))

                    items = cell.get_items()
                    for item in items:
                        item_img_path = item.get_image_path()
                        item_img = pygame.image.load(item_img_path)
                        win.blit(item_img, (x, y))

            macgyver_img_path = macgyver.get_image_path()
            macgyver_img = pygame.image.load(macgyver_img_path)
            win.blit(macgyver_img, (macgyver.x, macgyver.y))

            items_list = macgyver.get_items()
            for item_number, item in enumerate(items_list, start=0):
                item_img_path = item.get_image_path()
                item_img = pygame.image.load(item_img_path)
                win.blit(item_img, (10 + item_number * (20 + 20), len(maze.array) * 20 + 5))

        pygame.display.update()

    pygame.quit()

    maze.save_maze()


if __name__.endswith('__main__'):
    main()

# réduire mainloop + python -m flake8
# faire module pour consumables et Maze avec __init__
# revoir tous les imports
