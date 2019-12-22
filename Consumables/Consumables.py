import random
from Maze.Path import Path


class Consumables:
    def __init__(self):
        pass

    def load_img(self):
        pass

    def place_object_randomly(self, maze):
        final_non_wall_list = []
        for maze_line in maze.array:
            non_wall_list = [cell for cell in maze_line if isinstance(cell, Path)]
            path_non_object_list = [cell for cell in non_wall_list if len(cell.get_items()) == 0]
            if len(path_non_object_list) != 0:  # il faut pas de ligne remplie de Wall
                final_non_wall_list.append(path_non_object_list)
        cell_list = random.choice(final_non_wall_list)
        cell = random.choice(cell_list)
        cell.add_item(self)
