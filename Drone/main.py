__author__ = 'Travis Moy'


import pyglet
from definitions import DIR
from pyglet.window import key
from camera import Camera
from level import Level
from mobile import *


level = Level()
level.load(None)

droneimage = pyglet.resource.image('images/boxydrone.png')
drone = Mobile(droneimage, level)

level.place_entity_at(drone, 5, 9)
drone.current_cell = Position(5, 9)

cam = Camera(level, (0, 0), (640, 480))
cam.center_on(5, 9)

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.NUM_2:
        drone.queue_move(DIR.S)
        drone.commit_moves()
        cam.step(DIR.S)
    elif symbol == key.NUM_6:
        drone.queue_move(DIR.E)
        drone.commit_moves()
        cam.step(DIR.E)
    elif symbol == key.NUM_8:
        drone.queue_move(DIR.N)
        drone.commit_moves()
        cam.step(DIR.N)
    elif symbol == key.NUM_4:
        drone.queue_move(DIR.W)
        drone.commit_moves()
        cam.step(DIR.W)
    elif symbol == key.NUM_9:
        cam.step(DIR.NE)
    elif symbol == key.NUM_3:
        cam.step(DIR.SE)
    elif symbol == key.NUM_1:
        cam.step(DIR.SW)
    elif symbol == key.NUM_7:
        cam.step(DIR.NW)

@window.event
def on_draw():
    window.clear()
    cam.batch.draw()
    cam.cursor.draw()

pyglet.app.run()
