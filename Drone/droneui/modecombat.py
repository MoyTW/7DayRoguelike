__author__ = 'Travis Moy'

from modemainwindow import ModeMainWindow

import warnings


class ModeCombat(ModeMainWindow):
    def __init__(self):
        warnings.warn("ModeCombat.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeCombat.handle_keys() was called with {0}".format(symbol)
        return self
