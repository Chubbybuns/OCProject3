from Consumables.Consumables import Consumables

class Needle(Consumables):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "Images/Needle.png"
