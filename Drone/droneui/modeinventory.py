__author__ = 'Travis Moy'

from uimode import UIMode
from pyglet.window import key

import warnings


class ModeInventory(UIMode):
    def __init__(self, mode_list):
        super(ModeInventory, self).__init__(mode_list)
        warnings.warn("ModeInventory.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        if modifiers & key.MOD_SHIFT and key.A <= symbol <= key.Z:
            print "{0} was pressed! (Should be uppercase)".format(key.symbol_string(symbol))
        elif key.A <= symbol <= key.Z:
            print "{0} was pressed! (Should be lowercase)".format(key.symbol_string(symbol).lower())
        elif symbol == key.ESCAPE or symbol == key.BACKSPACE:
            return self.mode_list.main_window()
        return self
