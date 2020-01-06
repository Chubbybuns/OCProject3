from Maze.Cell import Cell


class Start(Cell):
    """
    Creates class of Start, child class of Cell
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Start Cell"

    def get_image_path(self):
        """
        Returns image path
        """
        return "Images/Start.png"

    def initial(self):
        """
        Returns initial of Start
        """
        return "S"
