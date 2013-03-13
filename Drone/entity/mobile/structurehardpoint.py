__author__ = 'Travis Moy'

import warnings
from entity.mobile.structureinternal import StructureInternal


class StructureHardpoint(StructureInternal):

    def __init__(self, hardpoint_type, damaged=False, contains=None, fixed=False):
        super(StructureHardpoint, self).__init__(damaged)
        self.hardpoint_type = hardpoint_type
        self.contains = contains
        self.fixed = fixed

    def mount(self, module):
        warnings.warn("StructureHardpoint.mount() is not complete!")
        self.unmount()
        self.contains = module

    def unmount(self):
        warnings.warn("StructureHardpoint.unmount is not complete!")

    def repair(self):
        pass

    def damage(self):
        pass

    def destroy(self):
        pass