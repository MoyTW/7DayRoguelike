__author__ = 'Travis Moy'

from modeexploration import ModeExploration
from uimodelist import UIModeList
import droneui


class UIController(object):

    def __init__(self, window, drone, level):
        self.window = window
        self.camera = droneui.camera.Camera(level, (0, 0), (640, 480))
        self.mode_list = UIModeList(drone, self.camera)
        self.key_input_mode = self.mode_list.exploration

        self._setup_callbacks()

    def center_on(self, x, y):
        self.camera.center_on(x, y)

    def _setup_callbacks(self):
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

        @self.window.event
        def on_draw():
            self.window.clear()
            self.camera.batch.draw()
            self.camera.cursor.draw()