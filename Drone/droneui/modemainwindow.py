__author__ = 'Travis Moy'

from modefreelook import *
from pyglet.window import key

import warnings


class ModeMainWindow(UIMode):

    def handle_keys(self, symbol, modifiers):
        warnings.warn("ModeMainWindow.handle_keys() is not yet fully implemented!")
        if symbol == key.L:
            return ModeFreeLook()
        elif symbol == key.I:
            print "i was pressed!"
        else:
            return None
