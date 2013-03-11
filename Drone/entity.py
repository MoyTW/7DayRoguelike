__author__ = 'Travis Moy'

import warnings


class Entity:
    exclusive_inhabitant = False

    def __init__(self, image):
        self.image = image

    def get_image(self):
        warnings.warn("Function get_image() in Entity is a placeholder!")
        return self.image
