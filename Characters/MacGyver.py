from Characters.Characters import Characters
from Maze.Wall import Wall
from Consumables.Syringe import Syringe
from Consumables.Ether import Ether
from Consumables.Needle import Needle
from Consumables.Tube import Tube


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
        if self.x < (len(self.maze.array) * 20) - 20:
            right_cell = self.maze.array[self.y // 20][self.x // 20 + 1]
            if not isinstance(right_cell, Wall):
                self.x += self.vel

    def move_up(self):
        up_cell = self.maze.array[self.y // 20 - 1][self.x // 20]
        if self.y > 0 and not isinstance(up_cell, Wall):
            self.y -= self.vel

    def move_down(self):
        if self.y < (len(self.maze.array) * 20) - 20:
            down_cell = self.maze.array[self.y // 20 + 1][self.x // 20]
            if not isinstance(down_cell, Wall):
                self.y += self.vel

    def get_item_from_current_cell(self):
        current_cell = self.maze.array[self.y // 20][self.x // 20]
        new_items = current_cell.get_items()
        for item in new_items:
            current_cell.remove_item(item)
            self.item_list.append(item)

    def make_syringe_if_possible(self):
        one_ether = False
        one_needle = False
        one_tube = False
        for item in self.item_list:
            if isinstance(item, Ether):
                one_ether = True
            if isinstance(item, Tube):
                one_tube = True
            if isinstance(item, Needle):
                one_needle = True
        if one_ether and one_tube and one_needle:
            # True or False
            self.item_list = []
            syringe = Syringe()
            self.item_list.append(syringe)

    def get_items(self):
        return self.item_list
