__author__ = 'Travis Moy'

from modefreelook import *
from pyglet.window import key

import warnings


class ModeMainWindow(UIMode):
    def __init__(self, mode_list):
        super(ModeMainWindow, self).__init__(mode_list)
        warnings.warn("ModeMainWindow is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        warnings.warn("ModeMainWindow.handle_keys() is not yet fully implemented")
        if symbol == key.L:
            return self.mode_list.freelook
        elif symbol == key.I:
            return self.mode_list.inventory
        elif symbol == key.U:
            return self.mode_list.consumable
        elif symbol == key.G:
            # warnings.warn("key.G in ModeMainWindow.handle_keys is not fully implemented!")
            return self.mode_list.main_window()
        elif symbol == key.Q:
            return self.mode_list.equip
        else:
            return None
