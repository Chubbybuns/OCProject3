from Characters.Characters import Characters
from Maze.Wall import Wall
from Consumables.Syringe import Syringe
from Consumables.Ether import Ether
from Consumables.Needle import Needle
from Consumables.Tube import Tube
from Maze.Finish import Finish


class MacGyver(Characters):
    """
    Creates class of MacGyver, child class of Characters
    """
    def __init__(self, x, y, maze, vel):
        super().__init__()
        self.x = x
        self.y = y
        self.maze = maze
        self.vel = vel
        self.item_list = []

    def load_img(self):
        """
        Returns image path
        """
        return "Images/MacGyver.png"

    def move_left(self):
        """
        Moves MacGyver to the left if possible
        """
        if self.x > 0:
            left_cell = self.maze.array[self.y // 20][self.x // 20 - 1]
            if not isinstance(left_cell, Wall):
                self.x -= self.vel

    def move_right(self):
        """
        Moves MacGyver to the right if possible
        """
        if self.x < (len(self.maze.array) * 20) - 20:
            right_cell = self.maze.array[self.y // 20][self.x // 20 + 1]
            if not isinstance(right_cell, Wall):
                self.x += self.vel

    def move_up(self):
        """
        Moves MacGyver up if possible
        """
        if self.y > 0:
            up_cell = self.maze.array[self.y // 20 - 1][self.x // 20]
            if not isinstance(up_cell, Wall):
                self.y -= self.vel

    def move_down(self):
        """
        Moves MacGyver down if possible
        """
        if self.y < (len(self.maze.array) * 20) - 20:
            down_cell = self.maze.array[self.y // 20 + 1][self.x // 20]
            if not isinstance(down_cell, Wall):
                self.y += self.vel

    def get_item_from_current_cell(self):
        """
        Moves item on Path Cell to MacGyver's itemlist
        """
        current_cell = self.maze.array[self.y // 20][self.x // 20]
        cell_item = current_cell.get_items()
        for item in cell_item:
            current_cell.remove_item(item)
            self.item_list.append(item)

    def make_syringe_if_possible(self):
        """
        Makes a syringe in MacGyver's itemlist if ether, needle and tube in his possession
        """
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
            self.item_list = []
            syringe = Syringe()
            self.item_list.append(syringe)

    def get_items(self):
        """
        Returns MacGyver's itemlist
        """
        return self.item_list

    def on_finish_cell(self):
        """
        Checks if MacGyver is on Finish Cell
        """
        current_cell = self.maze.array[self.y // 20][self.x // 20]
        return isinstance(current_cell, Finish)

    def has_syringe(self):
        """
        Checks if MacGyver has a syringe in his itemlist
        """
        for item in self.item_list:
            if isinstance(item, Syringe):
                return True
        return False
