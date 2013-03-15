__author__ = 'Travis Moy'

from entity.entity import Entity
import pyglet.resource


class Portable(Entity):

    def __init__(self, image=pyglet.resource.image('images/defaults/defaultportable.png'),
                 name='Unnamed Portable', description='This Portable has no description!'):
        super(Portable, self).__init__(image, name, description)
        print self.name