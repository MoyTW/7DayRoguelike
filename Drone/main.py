__author__ = 'Travis Moy'


import pyglet
from definitions import Position
from level.level import Level
from player.playerdrone import PlayerDrone
import droneui.uicontroller
from entity.entity import Entity
from entity.portable.module.module import Module


level = Level()
level.load(None)

ent = Entity()
level.place_entity_at(ent, 2, 2)
mod = Module()
level.place_entity_at(mod, 1, 3)

drone = PlayerDrone(level)

level.place_entity_at(drone, 1, 1)
drone.current_cell = Position(1, 1)

window = pyglet.window.Window(width=1024, height=768)
controller = droneui.uicontroller.UIController(window, drone, level)
controller.center_on(1, 1)

look = False


pyglet.app.run()
