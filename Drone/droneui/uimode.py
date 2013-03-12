__author__ = 'Travis Moy'


class UIMode(object):

    def __init__(self, mode_list):
        self.mode_list = mode_list

    def handle_keys(self, symbol, modifiers):
        print "The parent KeyInputMode was called! This should never occur - something has gone horribly wrong!"
        return self

    def draw(self):
        print "The draw function of UIMode was called! This should never occur - something has gone horribly wrong!"