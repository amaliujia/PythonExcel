from Cell import Cell

__author__ = 'amaliujia'

class Sheet:
    cells = {}

    def set_cell(self, x, y, value):
        if x not in self.cells:
            cell = Cell(x, y, value)
            self.cells[x] = {y : cell}
        elif y not in self.cells[x]:
            cell = Cell(x, y, value)
            self.cells[x][y] = Cell
        else:
            self.cells[x][y].set_data(value)


    def get_cell(self, x, y):
        if x not in self.cells or y not in self.cells[x]:
            return None
        else:
            return self.cells[x][y].get_data()

    def cell_constraint_add(self, parents=[], child=None):
        if len(parents) == 0 or child == None:
            return False




if __name__=="__main__":
    aSheet = Sheet()

    aSheet.set_cell(0, 1, 1);
    aSheet.set_cell(3, 1, 5);
    aSheet.set_cell(8, 10, 2);
    print aSheet.get_cell(0, 1)
    print aSheet.get_cell(3, 1)
    print aSheet.get_cell(8, 10)


