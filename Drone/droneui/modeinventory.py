__author__ = 'Travis Moy'

from uimode import UIMode

import warnings


class ModeInventory(UIMode):
    def __init__(self, mode_list):
        super(ModeInventory, self).__init__(mode_list)
        warnings.warn("ModeInventory.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeInventory.handle_keys() was called with {0}".format(symbol)
        return self
