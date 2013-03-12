__author__ = 'Travis Moy'

from uimode import UIMode

import warnings


class ModeInspectItem(UIMode):
    def __init__(self, mode_list):
        super(ModeInspectItem, self).__init__(mode_list)
        warnings.warn("ModeInspectItem.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        print "ModeInspectItem.handle_keys() was called with {0}".format(symbol)
        return self
