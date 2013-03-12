__author__ = 'Travis Moy'


class KeyInputMode(object):

    def handle_keys(self, symbol, modifiers):
        print "The parent KeyInputMode was called! This should never occur - something has gone horribly wrong!"
        return self