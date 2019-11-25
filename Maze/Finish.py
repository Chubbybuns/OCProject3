from Maze.Cell import Cell


class Finish(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Finish Cell"

    def load_img(self):
        return "Images/Finish.png"
    def initial(self):
        return "F"

