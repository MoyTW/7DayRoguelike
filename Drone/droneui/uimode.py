__author__ = 'Travis Moy'


class UIMode(object):

    def __init__(self, factory_modes):
        self.factory_modes = factory_modes

    def handle_keys(self, symbol, modifiers, previous_mode):
        print "The parent KeyInputMode was called! This should never occur - something has gone horribly wrong!"
        return self

    def draw(self):
        print "The draw function of UIMode was called! This should never occur - something has gone horribly wrong!"