__author__ = 'Travis Moy'

from keyinputmode import KeyInputMode

import warnings


class ModeInspectItem(KeyInputMode):
    def __init__(self):
        warnings.warn("ModeInspectItem.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeInspectItem.handle_keys() was called with {0}".format(symbol)
        return self
