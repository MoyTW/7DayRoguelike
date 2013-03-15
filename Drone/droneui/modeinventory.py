__author__ = 'Travis Moy'

from uimode import UIMode
from pyglet.window import key
import pyglet

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
        if modifiers & key.MOD_SHIFT and key.A <= symbol <= key.Z:
            print "{0} was pressed! (Should be uppercase)".format(key.symbol_string(symbol))
        elif key.A <= symbol <= key.Z:
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

    def redo_labels(self):
        self._labels = []
        self._sprites = []

        self._labels.append(pyglet.text.Label(
            'Page {0} of {1}'.format(self._current_page, self.inventory.num_pages - 1),
            font_size=14, x=self.window.width - 120, y=20))

        inventory_list = self.inventory.get_keys_and_entities_on_page(self._current_page)
        row = 8
        col = 0
        for key, entity in inventory_list:
            x_pos = 20 + col * 344
            y_pos = 100 + row * 64
            row -= 1
            if row < 0:
                row = 8
                col += 1

            if entity is not None:
                text = "{0} - {1}".format(key, entity.name)
                self._sprites.append(pyglet.sprite.Sprite(entity.get_image(), x=x_pos, y=y_pos, batch=self._batch))
                self._sprites[-1].scale = .75
            else:
                text = "{0} - Empty".format(key)

            self._labels.append(pyglet.text.Label(text, font_size=14, x=x_pos + 56, y=y_pos + 19))

    def draw(self):
        self.redo_labels()
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