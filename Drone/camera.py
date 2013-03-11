from pyglet.gl.glext_arb import GL_SPRITE_AXIAL_SGIX

__author__ = 'Travis Moy'

import pyglet
import math


class Camera:
    IMAGE_ACROSS = 64
    batch = pyglet.graphics.Batch()

    _magnification = 1
    _center_tile = [0, 0]
    _num_rows = 0
    _num_cols = 0
    _lower_left_pixel = (0, 0)
    _sprites = []

    def __init__(self, level, lower_left=(0, 0), upper_right=(200, 100)):
        self.resize_view(lower_left, upper_right)
        self.level = level

    def center_on(self, x, y):
        sprite_across = self.IMAGE_ACROSS * self._magnification
        lower_left_index = (x - math.floor(self._num_rows / 2),
                            y - math.floor(self._num_cols / 2))
        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                cell = self.level.at(lower_left_index[0] + row,
                                     lower_left_index[1] + col)
                self._sprites[row][col] = pyglet.sprite.Sprite(
                    cell.get_image(),
                    x=self._lower_left_pixel[0] + row * sprite_across,
                    y=self._lower_left_pixel[1] + col * sprite_across,
                    batch=self.batch
                )

    def step(self, direction):
        pass

    def resize_view(self, lower_left, upper_right):
        center_pixel = ((upper_right[0] + lower_left[0]) / 2,
                        (upper_right[1] + lower_left[1]) / 2)
        sprite_across = self.IMAGE_ACROSS * self._magnification
        self._num_rows = 1 + int(math.ceil((float(upper_right[0] - lower_left[0])) /
                                 float(sprite_across)))
        self._num_cols = 1 + int(math.ceil(float((upper_right[1] - lower_left[1])) /
                                 float(sprite_across)))
        self._lower_left_pixel = ((center_pixel[0] - (float(self._num_rows) / 2.0) *
                                  sprite_across),
                                 (center_pixel[1] - (float(self._num_cols) / 2.0) *
                                  sprite_across))
        self._sprites = self.cells = [[None for _ in range(self._num_cols)]
                                      for _ in range(self._num_rows)]

    def _step_cardinal(self, direction):
        pass