__author__ = 'Travis Moy'

from definitions import DIR
from modemainwindow import ModeMainWindow
from pyglet.window import key
from modegetitem import ModeGetItem
from player.inventory import Inventory

import warnings


class ModeExploration(ModeMainWindow):
    def __init__(self, factory_modes, player_drone, camera, window, level):
        super(ModeExploration, self).__init__(factory_modes)
        self.player_drone = player_drone
        self.camera = camera
        self.window = window
        self.level = level
        warnings.warn("ModeExploration.handle_keys() is not yet fully implemented!")

    def handle_keys(self, symbol, modifiers, previous_mode):
        next_mode = super(ModeExploration, self).handle_keys(symbol, modifiers, None)
        if next_mode is None:
            return self.exploration_handle_keys(symbol, modifiers)
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
        elif symbol == key.D or symbol == key.NUM_5:
            print "This should open the drop item menu."
        elif symbol == key.SPACE:
            if self.player_drone.inventory.is_full():
                print "You cannot get anything! Your inventory is full!"
                return self
            cell = self.level.at(self.player_drone.current_cell.x, self.player_drone.current_cell.y)
            # See if you can't compress these into one line.
            list_without_drone = list(cell.contains)
            list_without_drone.remove(self.player_drone)

            if len(list_without_drone) == 1:
                self.player_drone.pickup_item(list_without_drone[0])
                return self
            else:
                inventory = Inventory(contains=list_without_drone)
                return self.factory_modes.create_GetItem(inventory)

        return self