__author__ = 'Travis Moy'

from uimode import UIMode

import warnings


class ModeInspectItem(UIMode):
    def __init__(self, factory_modes):
        super(ModeInspectItem, self).__init__(factory_modes)
        warnings.warn("ModeInspectItem.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers, previous_mode):
        print "ModeInspectItem.handle_keys() was called with {0}".format(symbol)
        return self
