from .Characters import Characters


class Guard(Characters):
    """
    Creates class of Guard, child class of Characters
    """
    def __init__(self):
        super().__init__()

    def get_image_path(self):
        """
        Returns image path
        """
        return "Images/Guard.png"
