class Cell: #objet parent
    def __init__(self, ):
        self.item_list = []

    def load_img(self):
        pass

    def initial(self):
        pass

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        self.item_list.remove(item)

    def get_items(self):
        return self.item_list
