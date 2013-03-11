__author__ = 'Travis Moy'


import pyglet
from definitions import FOW


class Cell:
    #image = pyglet.resource.image('images/boxydrone.png')

    def __init__(self, image=pyglet.resource.image('images/boxydrone.png'), passable=True):
        self.passable = passable
        self.fow_state = FOW.VISIBLE
        self.image = image
        self.contains = []