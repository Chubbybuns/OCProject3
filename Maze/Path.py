from Maze.Cell import Cell


class Path(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Path Cell"

    def load_img(self):
        return "Images/Path.png"

    def initial(self):
        return "P"