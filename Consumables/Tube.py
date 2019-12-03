from Consumables.Consumables import Consumables


class Tube(Consumables):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "Images/Tube.png"
