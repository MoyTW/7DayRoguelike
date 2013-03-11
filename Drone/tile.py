__author__ = 'Travis Moy'


from cell import Cell
import warnings


class Tile(object):
    SIZE_ACROSS = 4
    all_entities = []

    def __init__(self):
        self.cells = [[Cell() for _ in range(self.SIZE_ACROSS)] for _ in range(self.SIZE_ACROSS)]

    def at(self, x, y):
        return self.cells[x][y]

    def place_entity_at(self, entity, x, y):
        self.all_entities.append(entity)
        self.cells[x][y].contains.append(entity)

    def remove_entity_from(self, entity, x, y):
        print self.cells[x][y].contains
        self.all_entities.remove(entity)
        self.cells[x][y].contains.remove(entity)

    def load(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        index_begin_map = [i for i, x in enumerate(lines) if x.strip() == '!MAP!'][0]

        # First, verify that the size matches.
        first_line = lines[0].split(',')
        if first_line[0] != '!SIZE!' or int(first_line[1]) != self.SIZE_ACROSS:
            warnings.warn("Cannot load file %s - SIZE_ACROSS is %i, file is of size %s" % (file, self.SIZE_ACROSS,
                                                                                           first_line[1].strip()))
            return

        # For lines between 1 and index_begin_map, make a dictionary.
        # cell_type[1] is the image file location, cell_type[0] is the truth value.
        cell_types = dict()
        for i in range(1, index_begin_map):
            line = lines[i].strip().split(',')
            cell_types[line[0]] = (line[1], line[2])

        # For each line, break it into columns and create the appropriate Cell objects.
        # This is just confusing as heck. You will have to revisit this at some point.
        for row_offset in range(index_begin_map + 1, len(lines)):
            line = lines[row_offset].strip()
            cols = line.strip().split(',')
            for col in range(0, self.SIZE_ACROSS):
                cell_type = cell_types[cols[col]]
                self.cells[row_offset - index_begin_map - 1][col] = Cell(cell_type[1],
                                                                         cell_type[0])
