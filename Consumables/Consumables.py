import random
from Maze.Path import Path


class Consumables:
    """
    Creates class of Consumables, parent class of Ether, Needle, Tube and Syringe
    """
    def __init__(self):
        pass

    def get_image_path(self):
        pass

    def place_object_randomly(self, maze):
        """
        Places item randomly in the maze, on a cell which has to be a Path Cell
        """
        final_non_wall_list = []
        for maze_line in maze.array:
            path_list = [cell for cell in maze_line if isinstance(cell, Path)]
            non_object_path_list = [cell for cell in path_list if len(cell.get_items()) == 0]
            if len(non_object_path_list) != 0:
                final_non_wall_list.append(non_object_path_list)
        cell_list = random.choice(final_non_wall_list)
        cell = random.choice(cell_list)
        cell.add_item(self)
