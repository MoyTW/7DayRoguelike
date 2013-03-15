__author__ = 'Travis Moy'

from uimodelist import UIModeList
import droneui


class UIController(object):

    def __init__(self, window, drone, level):
        self.window = window
        self.camera = droneui.camera.Camera(level, (0, 0), (self.window.width, self.window.height))
        self.mode_list = UIModeList(window, drone, self.camera, level)
        self.key_input_mode = self.mode_list.exploration
        self.previous_mode = None

        self._setup_callbacks()

    def center_on(self, x, y):
        self.camera.center_on(x, y)

    def _setup_callbacks(self):
        @self.window.event
        def on_key_press(symbol, modifiers):
            new_mode = self.key_input_mode.handle_keys(symbol, modifiers, self.previous_mode)
            if self.previous_mode != self.key_input_mode and self.key_input_mode != new_mode:
                print "Changing previous_mode from {0} to {1}".format(self.previous_mode, self.key_input_mode)
                self.previous_mode = self.key_input_mode
            self.key_input_mode = new_mode

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
            self.key_input_mode.draw()