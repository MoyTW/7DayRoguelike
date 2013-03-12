__author__ = 'Travis Moy'

from keyinputmode import KeyInputMode
from pyglet.window import key

import warnings


class ModeMainWindow(KeyInputMode):

    def handle_keys(self, symbol, modifiers):
        warnings.warn("ModeMainWindow.handle_keys() is not yet fully implemented!")
        if symbol == key.L:
            print "l was pressed!"
            return self
        elif symbol == key.I:
            print "i was pressed!"
        else:
            return None
