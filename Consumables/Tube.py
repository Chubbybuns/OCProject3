from .Consumables import Consumables


class Tube(Consumables):
    """
    Creates class of Tube, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def get_image_path(self):
        """
        Returns image path
        """
        return "Images/Tube.png"
