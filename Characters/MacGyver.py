from Characters.Characters import Characters
from Maze.Wall import Wall


class MacGyver(Characters):
    def __init__(self, x, y, maze, vel):
        super().__init__()
        self.x = x
        self.y = y
        self.maze = maze
        self.vel = vel
        self.item_list = []

    def load_img(self):
        return "Images/MacGyver.png"

    # MacGyver movements + collisions
    def move_left(self):
        # [ligne][colonne] car maze.Array = tableau de lignes
        left_cell = self.maze.array[self.y // 20][self.x // 20 - 1]
        if self.x > 0 and not isinstance(left_cell, Wall):
            self.x -= self.vel

    def move_right(self):
        right_cell = self.maze.array[self.y // 20][self.x // 20 + 1]
        if self.x < (len(self.maze.array) * 20) - 20 and not isinstance(right_cell, Wall):
            self.x += self.vel

    def move_up(self):
        up_cell = self.maze.array[self.y // 20 - 1][self.x // 20]
        if self.y > 0 and not isinstance(up_cell, Wall):
            self.y -= self.vel

    def move_down(self):
        down_cell = self.maze.array[self.y // 20 + 1][self.x // 20]
        if self.y < (len(self.maze.array) * 20) - 20 and not isinstance(down_cell, Wall):
            self.y += self.vel

    def get_item_from_current_cell(self):
        cell = self.maze.array[self.y // 20][self.x // 20]
        cell.get_items()
        cell.remove_items()
