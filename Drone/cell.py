__author__ = 'Travis Moy'


import pyglet
from definitions import FOW
import warnings


class Cell:

    def __init__(self, image=pyglet.resource.image('images/defaultcell.png'),
                 passable=True, fow_state=FOW.VISIBLE):
        self.passable = passable
        self.fow_state = fow_state
        self._image = image
        self.contains = []

    # This should be modified so as to return different images depending on the fow_state!
    def get_image(self):
        warnings.warn("Function get_image() is a placeholder!")
        return self._image