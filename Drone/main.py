__author__ = 'Travis Moy'


import pyglet
from tile import Tile
from camera import Camera
from level import Level


window = pyglet.window.Window()
level = Level()
level.load(None)
image = pyglet.resource.image('images/Frame268x268.png')
sprite = pyglet.sprite.Sprite(image)

cam = Camera(level, (6, 6), (262, 262))
cam.center_on(5, 9)

@window.event
def on_draw():
    window.clear()
    Camera.batch.draw()
    sprite.draw()

pyglet.app.run()
