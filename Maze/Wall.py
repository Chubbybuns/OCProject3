from Maze.Cell import Cell


class Wall(Cell):
    """
    Creates class of Wall, child class of Cell
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Wall Cell"

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Wall.png"

    def initial(self):
        """
        Return inital of Wall
        """
        return "W"
