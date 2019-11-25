from Consumables.Consumables import Consumables


class Ether(Consumables):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "Images/Ether.png"