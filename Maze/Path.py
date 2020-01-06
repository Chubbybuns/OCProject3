from Maze.Cell import Cell


class Path(Cell):
    """
    Creates class of Path, child class of Cell
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Path Cell"

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Path.png"

    def initial(self):
        """
        Returns, initial of Path
        """
        return "P"
