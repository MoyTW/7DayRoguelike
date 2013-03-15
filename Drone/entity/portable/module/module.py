__author__ = 'Travis Moy'

from entity.portable.portable import Portable
import pyglet.resource


class Module(Portable):

    def __init__(self, image=pyglet.resource.image('images/defaults/defaultmodule.png'),
                 name='Unnamed Module', description='This Module has no description!'):
        super(Portable, self).__init__(image, name, description)

    def apply_effects(self, mobile, section):
        pass

    def remove_effects(self, mobile, section):
        pass

    def repair(self):
        pass

    def damage(self):
        pass

    def destroy(self):
        pass