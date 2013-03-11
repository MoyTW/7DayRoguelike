__author__ = 'Travis Moy'


from tile import Tile
import math
import warnings


class Level(object):
    TILES_ACROSS = 4

    def __init__(self):
        self.all_entities = []
        self.tiles = [[Tile() for _ in range(self.TILES_ACROSS)] for _ in range(self.TILES_ACROSS)]

    # Returns the cell at x, y; otherwise, returns None
    def at(self, x, y):
        tile = self.tile_at(x, y)
        if tile is not None:
            return tile.at(int(x % Tile.SIZE_ACROSS), int(y % Tile.SIZE_ACROSS))
        else:
            return None

    def tile_at(self, x, y):
        try:
            x_index = int(math.floor(x / Tile.SIZE_ACROSS))
            y_index = int(math.floor(y / Tile.SIZE_ACROSS))
            tile = self.tiles[x_index][y_index]
            return tile
        except IndexError:
            return None

    # Next task: HANDLE ENTITY PLACEMENT, REMOVAL!
    def place_entity_at(self, entity, x, y):
        tile = self.tile_at(x, y)
        if tile is not None:
            self.all_entities.append(entity)
            tile.place_entity_at(entity, int(x % Tile.SIZE_ACROSS), int(y % Tile.SIZE_ACROSS))
        else:
            raise IndexError("Targeted cell x={0} y={1} does not exist!".format(x, y))

    def remove_entity_from(self, entity, x, y):
        tile = self.tile_at(x, y)
        if tile is not None:
            self.all_entities.remove(entity)
            tile.remove_entity_from(entity, int(x % Tile.SIZE_ACROSS), int(y % Tile.SIZE_ACROSS))
        else:
            raise IndexError("Targeted cell x={0} y={1} does not exist!".format(x, y))

    def move_entity_from_to(self, entity, old_x, old_y, new_x, new_y):
        old_tile = self.tile_at(old_x, old_y)
        new_tile = self.tile_at(new_x, new_y)
        if old_tile is not None and new_tile is not None:
            old_tile.remove_entity_from(entity, old_x, old_y)
            new_tile.place_entity_at(entity, new_x, new_y)
        else:
            raise IndexError("One of the cells ({0}, {1}) ({2}, {3}) is invalid!".format(old_x, old_y, new_x, new_y))

    def load(self, file):
        warnings.warn("Function load() is a placeholder! It is hardcoded to load testtile.txt!")
        for row in range(0, self.TILES_ACROSS):
            for col in range(0, self.TILES_ACROSS):
                self.tiles[row][col].load("testtile.txt")