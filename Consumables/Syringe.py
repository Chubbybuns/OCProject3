from Consumables.Consumables import Consumables


class Syringe(Consumables):
    """
    Creates class of Syringe, child class of Consumables
    """
    def __init__(self):
        super().__init__()

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Syringe.png"
