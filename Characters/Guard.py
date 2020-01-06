from Characters.Characters import Characters


class Guard(Characters):
    """
    Creates class of Guard, child class of Characters
    """
    def __init__(self):
        super().__init__()

    def load_img(self):
        """
        Returns image path
        """
        return "Images/Guard.png"
