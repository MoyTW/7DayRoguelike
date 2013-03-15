__author__ = 'Travis Moy'

from entity.mobile.mobile import Mobile
import inventory
import pyglet


class PlayerDrone(Mobile):
    def __init__(self, level):
        image = pyglet.resource.image('images/boxydrone.png')
        super(PlayerDrone, self).__init__(image, level)
        self.inventory = inventory.Inventory(52, 400)

    def pickup_item(self, item):
        cell = self.level.at(self.current_cell.x, self.current_cell.y)
        cell.contains.remove(item)
        self.inventory.add_item(item)

    def drop_item(self, item):
        cell = self.level.at(self.current_cell.x, self.current_cell.y)
        self.inventory.remove_item(item)
        cell.contains.append(item)