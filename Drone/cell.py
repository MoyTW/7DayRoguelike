__author__ = 'Travis Moy'


import pyglet
from definitions import FOW


class Cell:
    def __init__(self, image=None, passable=True):
        self.passable = passable
        self.fow_state = FOW.VISIBLE
        self.image = image
        self.contains = []