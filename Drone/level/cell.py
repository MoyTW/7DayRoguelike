__author__ = 'Travis Moy'


import pyglet
from definitions import FOW
import warnings


class Cell(object):

    def __init__(self, image_file='images/defaults/defaultcell.png',
                 passable=True, fow_state=FOW.VISIBLE):
        self.passable = passable
        self.fow_state = fow_state
        self._image = pyglet.resource.image(image_file)
        self.contains = []

    # This should be modified so as to return different images depending on the fow_state!
    def get_cell_image(self):
        warnings.warn("Function get_image() in Cell is a placeholder!")
        return self._image

    def get_entity_image(self):
        if self.contains:
            return self.contains[-1].get_image()
        else:
            return None

    def get_passable(self):
        return self.passable