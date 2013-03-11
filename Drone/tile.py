__author__ = 'Travis Moy'


from cell import Cell


class Tile:
    SIZE_ACROSS = 4

    def __init__(self):
        self.cells = [[Cell() for _ in range(self.SIZE_ACROSS)] for _ in range(self.SIZE_ACROSS)]

    def at(self, x, y):
        return self.cells[x][y]

    def load(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        index_begin_map = [i for i, x in enumerate(lines) if x.strip() == '!MAP!'][0]

        # First, verify that the size matches.
        first_line = lines[0].split(',')
        if first_line[0] != '!SIZE!' or int(first_line[1]) != self.SIZE_ACROSS:
            return

        # For lines between 1 and index_begin_map, make a dictionary.
        cell_types = dict()
        for i in range(1, index_begin_map):
            line = lines[i].strip().split(',')
            cell_types[line[0]] = (line[1], line[2])

        # For each line, break it into columns and create the appropriate Cell objects.
        for row_offset in range(index_begin_map + 1, len(lines)):
            line = lines[row_offset].strip()
            cols = line.strip().split(',')
            for col in range(0, self.SIZE_ACROSS):
                cell_type = cell_types[cols[col]]
                self.cells[row_offset - index_begin_map - 1][col] = Cell(cell_type[0], cell_type[1])
