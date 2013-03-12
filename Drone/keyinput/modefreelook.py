__author__ = 'Travis Moy'

from keyinputmode import KeyInputMode

import warnings


class ModeFreeLook(KeyInputMode):
    def __init__(self):
        warnings.warn("ModeFreeLook.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeFreeLook.handle_keys() was called with {0}".format(symbol)
        return self
