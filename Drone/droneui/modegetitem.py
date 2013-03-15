__author__ = 'Travis Moy'

import screenitemselect
import pyglet
from uimode import UIMode
from pyglet.window import key


# This is a disposable Mode!
class ModeGetItem(UIMode):
    def __init__(self, window, inventory, position):
        print "ModeGetItem was constructed!"
        self.window = window
        self.inventory = inventory
        self.position = position

        self._current_page = 0
        self._labels = []
        self._sprites = []
        self._col_width = 200
        self._batch = pyglet.graphics.Batch()

    def handle_keys(self, symbol, modifiers, previous_mode):
        if key.A <= symbol <= key.Z:
            print "{0} was pressed! (Should be lowercase)".format(key.symbol_string(symbol).lower())
        elif symbol == key.COMMA:
            if self._current_page > 0:
                self._current_page -= 1
        elif symbol == key.PERIOD:
            if self._current_page < self.inventory.num_pages - 1:
                self._current_page += 1
        elif symbol == key.ESCAPE or symbol == key.BACKSPACE:
            self._current_page = 0
            return previous_mode

        return self

    def draw(self):
        screenitemselect.create_sprites_and_labels(self._labels, self._sprites,
                                                   self._batch, self._current_page, self.inventory)
        header_string = "Items at Position X={0} Y={1}".format(self.position.x, self.position.y)
        self._labels.append(pyglet.text.Label(header_string, font_size=20,
                                              x=self.window.width // 2, y=self.window.height - 20,
                                              anchor_x='center', anchor_y='center'))
        for label in self._labels:
            label.draw()
        self._batch.draw()

