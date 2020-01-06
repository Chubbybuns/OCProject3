from Consumables.Consumables import Consumables


class Ether(Consumables):
    """
    Creates class of Ether, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Ether.png"
