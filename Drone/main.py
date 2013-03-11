__author__ = 'Travis Moy'


import pyglet
from definitions import DIR
from pyglet.window import key
from camera import Camera
from level import Level


level = Level()
level.load(None)

cam = Camera(level, (0, 0), (640, 480))
cam.center_on(5, 9)

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.NUM_2:
        cam.step(DIR.S)
    elif symbol == key.NUM_6:
        cam.step(DIR.E)
    elif symbol == key.NUM_8:
        cam.step(DIR.N)
    elif symbol == key.NUM_4:
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
