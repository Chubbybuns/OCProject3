import random
from Maze.Wall import Wall


class Consumables:
    def __init__(self):
        pass

    def load_img(self):
        pass

    def place_object_randomly(self, maze):
        final_non_wall_list = []
        for maze_line in maze.array:
            non_wall_list = [cell for cell in maze_line if isinstance(cell, Wall) is False]
            non_wall_non_object_list = [cell for cell in non_wall_list if len(cell.get_items()) == 0]
            if len(non_wall_non_object_list) != 0:  # il faut pas de ligne remplie de Wall
                final_non_wall_list.append(non_wall_non_object_list)
        cell_list = random.choice(final_non_wall_list)
        cell = random.choice(cell_list)
        cell.add_item(self)
