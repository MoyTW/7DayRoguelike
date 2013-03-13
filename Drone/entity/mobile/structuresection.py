__author__ = 'Travis Moy'

from modifiablestat import ModifiableStat


class StructureSection(object):

    def __init__(self, angle_begins_at, angle_ends_at, base_armor, base_structure, hardpoints):
        self.angle_begins_at = angle_begins_at
        self.angle_ends_at = angle_ends_at
        self.armor = ModifiableStat(base_armor)
        self.structure = ModifiableStat(base_structure)

        # The number of hardpoints on the section is fixed!
        self.hardpoints = hardpoints


        # self.internals = [StructureHardpoint() for i in range(0, len(hardpoints))]

    def section_length(self):
        ret_len = self.angle_ends_at - self.angle_begins_at
        if ret_len < 0:
            ret_len = 360 - self.angle_ends_at + self.angle_begins_at
        return ret_len