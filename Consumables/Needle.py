from .Consumables import Consumables


class Needle(Consumables):
    """
    Creates class of Needle, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def get_image_path(self):
        """
        Returns image path
        """
        return "Images/Needle.png"
