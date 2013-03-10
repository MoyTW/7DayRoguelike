__author__ = 'Travis Moy'


class Entity:
    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.image = image
        self.exclusive_inhabitant = False