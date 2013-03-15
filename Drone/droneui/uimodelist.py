__author__ = 'Travis Moy'

import warnings
from modecombat import ModeCombat
from modeconsumable import ModeConsumable
from modeequip import ModeEquip
from modeexploration import ModeExploration
from modefreelook import ModeFreeLook
from modeinspectitem import ModeInspectItem
from modeinventory import ModeInventory


class UIModeList(object):
    def __init__(self, window, drone, camera, inventory, level):
        self.combat = ModeCombat(self)
        self.consumable = ModeConsumable(self)
        self.equip = ModeEquip(self)
        self.exploration = ModeExploration(self, drone, camera, window, level)
        self.freelook = ModeFreeLook(self, camera)
        self.inspectitem = ModeInspectItem(self)
        self.inventory = ModeInventory(self, window, inventory)

    def main_window(self):
        warnings.warn("get_main_window will only return exploration!")
        return self.exploration