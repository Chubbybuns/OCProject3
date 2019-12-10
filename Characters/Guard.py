from Characters.Characters import Characters
from Maze.Finish import Finish
from Maze.Maze import Maze


class Guard(Characters):
    def __init__(self):
        super().__init__()

    def load_img(self):
        return "Images/Guard.png"
