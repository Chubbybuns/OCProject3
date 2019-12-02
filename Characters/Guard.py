from Characters.Characters import Characters

class Guard(Characters):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "../Images/Guard.png"