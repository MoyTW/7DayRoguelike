__author__ = 'Travis Moy'

import warnings
from modecombat import ModeCombat
from modeconsumable import ModeConsumable
from modeequip import ModeEquip
from modeexploration import ModeExploration
from modefreelook import ModeFreeLook
from modeinspectitem import ModeInspectItem
from modeinventory import ModeInventory
from modegetitem import ModeGetItem


class FactoryModes(object):
    def __init__(self, window, player_drone, camera, level):
        self.window = window
        self.player_drone = player_drone
        self.camera = camera
        self.level = level
        self.player_inventory = player_drone.inventory

    def create_Combat(self):
        return ModeCombat(self)

    def create_Consumable(self):
        return ModeConsumable(self)

    def create_Equip(self):
        return ModeEquip(self)

    def create_Exploration(self):
        return ModeExploration(self, self.player_drone, self.camera, self.window, self.level)

    def create_FreeLook(self):
        return ModeFreeLook(self, self.camera)

    def create_InspectItem(self):
        return ModeInspectItem(self)

    def create_Inventory(self):
        return ModeInventory(self, self.window, self.player_inventory)

    def create_GetItem(self, inventory):
        return ModeGetItem(self, self.window, self.player_drone, inventory)

    def create_MainWindow(self):
        warnings.warn("get_main_window will only return exploration!")
        return self.create_Exploration()