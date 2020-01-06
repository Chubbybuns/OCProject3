class Cell:
    """
    Creates class of Cell, parent cell of Start, Path, Wall and Finish
    """
    def __init__(self):
        self.item_list = []

    def get_image_path(self):
        pass

    def initial(self):
        pass

    def add_item(self, item):
        """
        Adds an item to the cell's itemlist
        """
        self.item_list.append(item)

    def remove_item(self, item):
        """
        Removes an item from the cell's itemlist
        """
        self.item_list.remove(item)

    def get_items(self):
        """
        Returns the cell's itemlist
        """
        return self.item_list
