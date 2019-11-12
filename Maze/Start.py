from Cell import Cell


class Start(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Start Cell"

    def load_img(self):
        return "../Images/Start.png"

    def initial(self):
        return "S"