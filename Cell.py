__author__ = 'amaliujia'

class Cell:
    data = None
    x = -1
    y = -1
    parents = []
    children = []

    def __init__(self, x, y, value):
        self.data = value
        self.x = x
        self.y = y

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y