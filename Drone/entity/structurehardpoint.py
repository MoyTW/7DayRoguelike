__author__ = 'Travis Moy'

from structureinternal import StructureInternal


class StructureHardpoint(StructureInternal):

    def __init__(self, hardpoint_type, damaged=False, contains=None, fixed=False):
        super(StructureHardpoint, self).__init__(damaged)
        self.hardpoint_type = hardpoint_type
        self.contains = contains
        self.fixed = fixed

    def mount(self, module):
        pass

    def unmount(self):
        pass

    def repair(self):
        pass

    def damage(self):
        pass

    def destroy(self):
        pass