__author__ = 'Travis Moy'

from definitions import DIR
from modemainwindow import ModeMainWindow
from pyglet.window import key

import warnings


class ModeExploration(ModeMainWindow):
    def __init__(self, mode_list, player_drone, camera):
        super(ModeExploration, self).__init__(mode_list)
        self.player_drone = player_drone
        self.camera = camera
        warnings.warn("ModeExploration.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers, previous_mode):
        next_mode = super(ModeExploration, self).handle_keys(symbol, modifiers, None)
        if next_mode is None:
            self.exploration_handle_keys(symbol, modifiers)
            return self
        else:
            return next_mode

    def draw(self):
        self.camera.draw()

    def exploration_handle_keys(self, symbol, modifiers):
        if symbol == key.W or symbol == key.NUM_7:
            if self.player_drone.queue_move(DIR.NW):
                self.player_drone.commit_moves()
                self.camera.step(DIR.NW)
        elif symbol == key.E or symbol == key.NUM_8:
            if self.player_drone.queue_move(DIR.N):
                self.player_drone.commit_moves()
                self.camera.step(DIR.N)
        elif symbol == key.R or symbol == key.NUM_9:
            if self.player_drone.queue_move(DIR.NE):
                self.player_drone.commit_moves()
                self.camera.step(DIR.NE)
        elif symbol == key.S or symbol == key.NUM_4:
            if self.player_drone.queue_move(DIR.W):
                self.player_drone.commit_moves()
                self.camera.step(DIR.W)
        elif symbol == key.F or symbol == key.NUM_6:
            if self.player_drone.queue_move(DIR.E):
                self.player_drone.commit_moves()
                self.camera.step(DIR.E)
        elif symbol == key.X or symbol == key.NUM_1:
            if self.player_drone.queue_move(DIR.SW):
                self.player_drone.commit_moves()
                self.camera.step(DIR.SW)
        elif symbol == key.C or symbol == key.NUM_2:
            if self.player_drone.queue_move(DIR.S):
                self.player_drone.commit_moves()
                self.camera.step(DIR.S)
        elif symbol == key.V or symbol == key.NUM_3:
            if self.player_drone.queue_move(DIR.SE):
                self.player_drone.commit_moves()
                self.camera.step(DIR.SE)