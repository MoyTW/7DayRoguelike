__author__ = 'Travis Moy'

from uimode import UIMode
from pyglet.window import key
from definitions import DIR

import warnings


class ModeFreeLook(UIMode):
    def __init__(self, mode_list, camera):
        super(ModeFreeLook, self).__init__(mode_list)
        self.camera = camera
        self.origin_position = None
        warnings.warn("ModeFreeLook.handle_keys() is not yet fully implemented!")

    def recenter(self):
        if self.origin_position is not None:
            self.camera.center_on(self.origin_position[0], self.origin_position[1])
        self.origin_position = None

    def handle_keys(self, symbol, modifiers):
        if self.origin_position is None:
            self.origin_position = list(self.camera.center_tile)

        if symbol == key.ESCAPE or symbol == key.BACKSPACE:
            self.recenter()
            return self.mode_list.main_window()

        elif symbol == key.W or symbol == key.NUM_7:
            self.camera.step(DIR.NW)
        elif symbol == key.E or symbol == key.NUM_8:
            self.camera.step(DIR.N)
        elif symbol == key.R or symbol == key.NUM_9:
            self.camera.step(DIR.NE)
        elif symbol == key.S or symbol == key.NUM_4:
            self.camera.step(DIR.W)
        elif symbol == key.F or symbol == key.NUM_6:
            self.camera.step(DIR.E)
        elif symbol == key.X or symbol == key.NUM_1:
            self.camera.step(DIR.SW)
        elif symbol == key.C or symbol == key.NUM_2:
            self.camera.step(DIR.S)
        elif symbol == key.V or symbol == key.NUM_3:
            self.camera.step(DIR.SE)

        elif symbol == key.D or symbol == key.NUM_5:
            self.recenter()

        return self
