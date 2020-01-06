from Maze.Cell import Cell


class Finish(Cell):
    """
    Creates class of Finish, child class of Cell
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Finish Cell"

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Finish.png"

    def initial(self):
        """
        Returns the initial of Finish
        """
        return "F"

