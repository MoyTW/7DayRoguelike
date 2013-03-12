__author__ = 'Travis Moy'

from keyinputmode import KeyInputMode

import warnings


class ModeInventory(KeyInputMode):
    def __init__(self):
        warnings.warn("ModeInventory.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeInventory.handle_keys() was called with {0}".format(symbol)
        return self
