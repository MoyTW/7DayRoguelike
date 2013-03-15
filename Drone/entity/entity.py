__author__ = 'Travis Moy'

import warnings
import pyglet.resource


class Entity(object):
    exclusive_inhabitant = False

    def __init__(self, image=pyglet.resource.image('images/defaults/defaultentity.png'),
                 name='Unnamed Entity', description='This Entity has no description!'):
        self.name = name
        self.description = description
        self.image = image

    def get_image(self):
        warnings.warn("Function get_image() in Entity is a placeholder!")
        return self.image
