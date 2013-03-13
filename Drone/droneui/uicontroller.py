__author__ = 'Travis Moy'

from modeexploration import ModeExploration
from uimodelist import UIModeList


class UIController(object):

    def __init__(self, window, drone, camera):
        self.window = window
        self.mode_list = UIModeList(drone, camera)
        self.key_input_mode = self.mode_list.exploration

        @self.window.event
        def on_key_press(symbol, modifiers):
            self.key_input_mode = self.key_input_mode.handle_keys(symbol, modifiers)
            if self.key_input_mode is None:
                # Commit the turn
                # Get the Alerted status
                # If not alerted, self.key_input_mode = ExplorationMode()
                # Else self.key_input_mode = CombatMode()
                pass

            return True
