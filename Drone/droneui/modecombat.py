__author__ = 'Travis Moy'

from modemainwindow import ModeMainWindow

import warnings


class ModeCombat(ModeMainWindow):
    def __init__(self, factory_modes):
        super(ModeCombat, self).__init__(factory_modes)
        warnings.warn("ModeCombat.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers, previous_mode):
        print "ModeCombat.handle_keys() was called with {0}".format(symbol)
        return self
