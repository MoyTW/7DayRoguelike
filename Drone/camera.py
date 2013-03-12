__author__ = 'Travis Moy'

import pyglet
import math
from definitions import DIR


class Camera(object):
    IMAGE_ACROSS = 64
    batch = pyglet.graphics.Batch()
    cursor_image = pyglet.resource.image('images/camera_cursor.png')

    _center_tile = [0, 0]
    _magnification = 1
    _num_rows = 0
    _num_cols = 0
    _lower_left_pixel = (0, 0)
    _sprites = []

    def __init__(self, level, lower_left=(0, 0), upper_right=(200, 100)):
        self.cursor = pyglet.sprite.Sprite(self.cursor_image)
        self.level = level
        self.resize_view(lower_left, upper_right)

    def center_on(self, x, y):
        self._center_tile = [x, y]
        lower_left_index = (x - math.floor(self._num_rows / 2),
                            y - math.floor(self._num_cols / 2))
        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                self._sprites[row][col] = self._get_sprite_at(lower_left_index, row, col)
        print self._sprites

    def _get_sprite_at(self, lower_left_index, row, col):
        sprite_across = self.IMAGE_ACROSS * self._magnification
        cell = self.level.at(lower_left_index[0] + row,
                             lower_left_index[1] + col)

        print "Cell at ({0}, {1}) is {2}".format(lower_left_index[0] + row, lower_left_index[1] + col, cell)

        sprite = None
        if cell is not None:
            sprite = pyglet.sprite.Sprite(
                cell.get_image(),
                x=self._lower_left_pixel[0] + row * sprite_across,
                y=self._lower_left_pixel[1] + col * sprite_across,
                batch=self.batch
            )
        return sprite

    def step(self, direction):
        if direction == DIR.N or direction == DIR.E or direction == DIR.S or direction == DIR.W:
            self._step_cardinal(direction)
        elif direction == DIR.NE:
            self._step_cardinal(DIR.N)
            self._step_cardinal(DIR.E)
        elif direction == DIR.SE:
            self._step_cardinal(DIR.S)
            self._step_cardinal(DIR.E)
        elif direction == DIR.NW:
            self._step_cardinal(DIR.N)
            self._step_cardinal(DIR.W)
        elif direction == DIR.SW:
            self._step_cardinal(DIR.S)
            self._step_cardinal(DIR.W)

    def resize_view(self, lower_left, upper_right):
        sprite_across = self.IMAGE_ACROSS * self._magnification
        center_pixel = ((upper_right[0] + lower_left[0]) / 2,
                        (upper_right[1] + lower_left[1]) / 2)
        self.cursor.set_position(center_pixel[0] - sprite_across / 2, center_pixel[1] - sprite_across / 2)
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
        if direction == DIR.N:
            self._center_tile[1] += 1
        elif direction == DIR.E:
            self._center_tile[0] += 1
        elif direction == DIR.S:
            self._center_tile[1] -= 1
        elif direction == DIR.W:
            self._center_tile[0] -= 1
        self.center_on(self._center_tile[0], self._center_tile[1])