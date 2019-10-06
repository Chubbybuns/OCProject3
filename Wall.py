from Cell import Cell


class Wall(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Wall Cell"