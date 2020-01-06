from .Consumables import Consumables


class Ether(Consumables):
    """
    Creates class of Ether, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def get_image_path(self):
        """
        Returns image path
        """
        return "Images/Ether.png"
