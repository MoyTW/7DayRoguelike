__author__ = 'Travis Moy'


class StructureInternal(object):

    def __init__(self, damaged=False):
        self.damaged = damaged

    def repair(self):
        self.damaged = False

    def damage(self):
        self.damaged = True

    def destroy(self):
        pass