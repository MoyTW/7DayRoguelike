__author__ = 'Travis Moy'

from uimode import UIMode
from pyglet.window import key
from definitions import DIR

import warnings


class ModeFreeLook(UIMode):
    def __init__(self, mode_list, camera):
        super(ModeFreeLook, self).__init__(mode_list)
        self.camera = camera
        self.reverse_moves = []
        warnings.warn("ModeFreeLook.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers):
        if symbol == key.ESCAPE or symbol == key.BACKSPACE:
            self.reverse_moves = []
            return self.mode_list.main_window()
        elif symbol == key.W:
            self.camera.step(DIR.NW)
            self.reverse_moves.append(DIR.SE)
        elif symbol == key.E:
            self.camera.step(DIR.N)
            self.reverse_moves.append(DIR.S)
        elif symbol == key.R:
            self.camera.step(DIR.NE)
            self.reverse_moves.append(DIR.SW)
        elif symbol == key.S:
            self.camera.step(DIR.W)
            self.reverse_moves.append(DIR.E)
        elif symbol == key.F:
            self.camera.step(DIR.E)
            self.reverse_moves.append(DIR.W)
        elif symbol == key.X:
            self.camera.step(DIR.SW)
            self.reverse_moves.append(DIR.NE)
        elif symbol == key.C:
            self.camera.step(DIR.S)
            self.reverse_moves.append(DIR.N)
        elif symbol == key.V:
            self.camera.step(DIR.SE)
            self.reverse_moves.append(DIR.NW)
        elif symbol == key.D:
            for dir in self.reverse_moves:
                self.camera.step(dir)
            self.reverse_moves = []
        return self
