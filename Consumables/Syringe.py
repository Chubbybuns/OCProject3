from Consumables import Consumables


class Syringe(Consumables):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "../Images/Syringe.png"