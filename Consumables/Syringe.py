from Consumables.Consumables import Consumables
# from dossier.ficher import class


class Syringe(Consumables):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "Images/Syringe.png"
