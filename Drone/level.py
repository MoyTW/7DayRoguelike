__author__ = 'Travis Moy'


from tile import Tile
import math
import warnings


class Level:
    TILES_ACROSS = 4

    def __init__(self):
        self.tiles = [[Tile() for _ in range(self.TILES_ACROSS)] for _ in range(self.TILES_ACROSS)]

    # Returns the cell at x, y; otherwise, returns None
    def at(self, x, y):
        try:
            x_index = int(math.floor(x / Tile.SIZE_ACROSS))
            y_index = int(math.floor(y / Tile.SIZE_ACROSS))
            tile = self.tiles[x_index][y_index]
        except IndexError:
            return None
        return tile.at(int(x % Tile.SIZE_ACROSS), int(y % Tile.SIZE_ACROSS))

    def load(self, file):
        warnings.warn("Function load() is a placeholder! It is hardcoded to load testtile.txt!")
        for row in range(0, self.TILES_ACROSS):
            for col in range(0, self.TILES_ACROSS):
                self.tiles[row][col].load("testtile.txt")