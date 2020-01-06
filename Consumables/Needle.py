from Consumables.Consumables import Consumables


class Needle(Consumables):
    """
    Creates class of Needle, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Needle.png"
