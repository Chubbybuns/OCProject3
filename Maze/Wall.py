from Maze.Cell import Cell


class Wall(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Wall Cell"

    def load_img(self):
        return "Images/Wall.png"

    def initial(self):
        return "W"
