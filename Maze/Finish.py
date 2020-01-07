from .Cell import Cell


class Finish(Cell):
    """
    Creates class of Finish, child class of Cell
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Finish Cell"

    def get_image_path(self):
        """
        Returns image path of Finish
        """
        return "Images/Finish.png"

    def initial(self):
        """
        Returns the initial of Finish
        """
        return "F"
