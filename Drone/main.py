__author__ = 'Travis Moy'


import pyglet
from definitions import Position
from droneui.camera import Camera
from level.level import Level
from entity.mobile.mobile import Mobile
import droneui.uicontroller
from entity.entity import Entity
from entity.portable.module.module import Module


level = Level()
level.load(None)

ent = Entity()
level.place_entity_at(ent, 2, 2)
mod = Module()
level.place_entity_at(mod, 1, 3)

droneimage = pyglet.resource.image('images/boxydrone.png')
drone = Mobile(droneimage, level)

level.place_entity_at(drone, 1, 1)
drone.current_cell = Position(1, 1)

window = pyglet.window.Window()
controller = droneui.uicontroller.UIController(window, drone, level)
controller.center_on(1, 1)

look = False

pyglet.app.run()
