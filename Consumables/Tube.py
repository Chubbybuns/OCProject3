from Consumables.Consumables import Consumables


class Tube(Consumables):
    """
    Creates class of Tube, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Tube.png"
