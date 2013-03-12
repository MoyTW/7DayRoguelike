__author__ = 'Travis Moy'


import pyglet
from definitions import Position
from droneui.camera import Camera
from level.level import Level
from entity.mobile import Mobile
import droneui.uicontroller


level = Level()
level.load(None)

droneimage = pyglet.resource.image('images/boxydrone.png')
drone = Mobile(droneimage, level)

level.place_entity_at(drone, 1, 1)
drone.current_cell = Position(1, 1)

cam = Camera(level, (0, 0), (640, 480))
cam.center_on(1, 1)

window = pyglet.window.Window()
controller = droneui.uicontroller.UIController(window, cam)

look = False

@window.event
def on_draw():
    window.clear()
    cam.batch.draw()
    cam.cursor.draw()

pyglet.app.run()
