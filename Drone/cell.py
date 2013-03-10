__author__ = 'Travis Moy'


import pyglet
from definitions import FOW


class Cell:
    def __init__(self, image, passable=False):
        self.passable = passable
        self.fow_state = FOW.UNREVEALED
        self.image = image
        self.contains = []