__author__ = 'Travis Moy'

from modefreelook import *
from pyglet.window import key

import warnings


class ModeMainWindow(UIMode):
    def __init__(self, factory_modes):
        super(ModeMainWindow, self).__init__(factory_modes)
        warnings.warn("ModeMainWindow is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers, previous_mode):
        warnings.warn("ModeMainWindow.handle_keys() is not yet fully implemented")
        if symbol == key.L:
            return self.factory_modes.create_FreeLook()
        elif symbol == key.I:
            return self.factory_modes.create_Inventory()
        elif symbol == key.U:
            return self.factory_modes.create_Consumable()
        elif symbol == key.G:
            # warnings.warn("key.G in ModeMainWindow.handle_keys is not fully implemented!")
            return self.factory_modes.create_MainWindow()
        elif symbol == key.Q:
            return self.factory_modes.create_Equip()
        else:
            return None
