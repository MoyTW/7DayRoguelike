__author__ = 'Travis Moy'

from entity.mobile.structureinternal import StructureInternal
from entity.portable.module.moduletypes import MOD_TYPE
from entity.portable.module.module import Module


class StructureHardpoint(StructureInternal):

    # The parent is the Mobile to which this is attached.
    def __init__(self, hardpoint_type, parent, damaged=False, module=Module(), fixed=False):
        super(StructureHardpoint, self).__init__(damaged)
        self.hardpoint_type = hardpoint_type
        self.parent = parent
        self.fixed = fixed
        self.mount(module)

    def can_mount(self, module):
        module_type = module.module_type
        if self.hardpoint_type == module_type:
            return True
        elif self.hardpoint_type == MOD_TYPE.weapon_large and (
                module_type == MOD_TYPE.weapon_medium or
                module_type == MOD_TYPE.weapon_small):
            return True
        elif self.hardpoint_type == MOD_TYPE.weapon_medium and module_type == MOD_TYPE.weapon_small:
            return True
        else:
            return False

    def mount(self, module):
        if self.can_mount(module):
            self.unmount()
            self.module = module
            self.module.apply_effects(mobile=self.parent, section=self)
            return True
        else:
            return False

    def unmount(self):
        self.module.remove_effects(mobile=self.parent, section=self)
        self.module = Module()

    def repair(self):
        self.module.repair()

    def damage(self):
        self.module.damage()

    def destroy(self):
        self.module.destroy()