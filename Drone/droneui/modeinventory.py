__author__ = 'Travis Moy'

from uimode import UIMode
from pyglet.window import key
import pyglet
import screenitemselect

import warnings


class ModeInventory(UIMode):
    def __init__(self, mode_list, window, inventory):
        super(ModeInventory, self).__init__(mode_list)
        self.window = window
        self.inventory = inventory

        self._current_page = 0
        self._labels = []
        self._sprites = []
        self._init_fixed_labels()
        self._col_width = 200
        self._batch = pyglet.graphics.Batch()

        warnings.warn("ModeInventory.handle_keys() is not yet fully implemented!")

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
            return self.mode_list.main_window()
        return self

    def draw(self):
        screenitemselect.create_sprites_and_labels(self._labels, self._sprites,
                                                   self._batch, self._current_page, self.inventory)
        for label in self._labels:
            label.draw()
        for fixed_label in self._fixed_labels:
            fixed_label.draw()
        self._batch.draw()

    def _init_fixed_labels(self):
        self._fixed_labels = []
        self._fixed_labels.append(pyglet.text.Label('Inventory', font_size=20,
                                                x=self.window.width // 2, y=self.window.height - 20,
                                                anchor_x='center', anchor_y='center'))