__author__ = 'Travis Moy'


import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image = pyglet.resource.image('images/floor.png')

sprite = pyglet.sprite.Sprite(image)
sprite.scale = .5

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.NUM_2:
        sprite.y -= 64
    elif symbol == key.NUM_6:
        sprite.x += 64
    elif symbol == key.NUM_8:
        sprite.y += 64
    elif symbol == key.NUM_4:
        sprite.x -= 64
    elif symbol == key.NUM_7:
        sprite.rotation -= 45
    elif symbol == key.NUM_9:
        sprite.rotation += 45

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()
