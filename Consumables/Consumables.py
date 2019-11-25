import random
from Maze.Wall import Wall

class Consumables: #objet parent
    def __init__(self):
        pass

    def load_img(self):
        pass

    def place_object_randomly(self, maze):
        final_non_wall_list = []
        for maze_line in maze.array:
            non_wall_list = [cell for cell in maze_line if isinstance(cell, Wall) == False]
            if len(non_wall_list) != 0: # il faut pas de ligne remplie de Wall
                final_non_wall_list.append(non_wall_list)
        Cell_list = random.choice(final_non_wall_list)
        Cell = random.choice(Cell_list)
        Cell.add_item(self)

        print(final_non_wall_list)

