__author__ = 'Travis Moy'


from tile import Tile


class Level:
    TILES_ACROSS = 4

    def __init__(self):
        self.tiles = [[None for _ in range(self.TILES_ACROSS)] for _ in range(self.TILES_ACROSS)]

    def load(self, file):
        pass