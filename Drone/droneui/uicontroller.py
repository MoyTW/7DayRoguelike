__author__ = 'Travis Moy'

import pyglet
from uimode import UIMode
from modeexploration import ModeExploration


class UIController(object):

    def __init__(self, window):
        self.window = window
        self.key_input_mode = ModeExploration()

        @self.window.event
        def on_key_press(symbol, modifiers):
            self.key_input_mode = self.key_input_mode.handle_keys(symbol, modifiers)
            if self.key_input_mode is None:
                # Commit the turn
                # Get the Alerted status
                # If not alerted, self.key_input_mode = ExplorationMode()
                # Else self.key_input_mode = CombatMode()
                pass

