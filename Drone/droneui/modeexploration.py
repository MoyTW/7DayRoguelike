__author__ = 'Travis Moy'

from modemainwindow import ModeMainWindow

import warnings


class ModeExploration(ModeMainWindow):
    def __init__(self, mode_list):
        super(ModeExploration, self).__init__(mode_list)
        warnings.warn("ModeExploration.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        next_mode = super(ModeExploration, self).handle_keys(symbol, modifiers)
        if next_mode is None:
            print "next_mode is none! ExplorationMode should take it from here (but obviously isn't yet!)"
            return self
        else:
            return next_mode