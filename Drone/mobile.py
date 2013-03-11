__author__ = 'Travis Moy'

from definitions import *
from entity import Entity


default_combat_costs = {CMO.MOVE_FORWARD: 1, CMO.MOVE_BACKWARDS: 1.5,
                        CMO.TURN_RIGHT: .33, CMO.TURN_LEFT: .33}


class MoveOrder(object):
    def __init__(self, order, end_tile, facing):
        self.order = order
        self.end_tile = end_tile
        self.facing = facing


class Mobile(Entity):
    current_cell = Position(0, 0)
    current_facing = DIR.N
    movement_queue = []
    _is_alerted = False

    # combat_costs = {}
    # _movement_points = 1

    def __init__(self, level, combat_costs=default_combat_costs, movement_points=1):
        self.level = level
        self.combat_costs = combat_costs
        self._movement_points = movement_points

    def queue_move(self, move):
        if not self.is_alerted:
            self._queue_exploration(move)
        else:
            self._queue_combat(move)

    def unqueue_move(self):
        if self.movement_queue:
            self.movement_queue.pop()

    def commit_moves(self):
        if not self.is_alerted:
            self._commit_exploration()
        else:
            self._commit_combat()

    def alert(self):
        self.alert = True

    def unalert(self):
        self.alert = False

    def is_alerted(self):
        return self._is_alerted

    # Returns the MoveOrder if the square is valid and passable, else returns None.
    def _find_exploration_move_end_tile(self, move):
        end_position = DIR.position_to_of(move, self.current_cell)
        end_cell = self.level.at(x=end_position.x, y=end_position.y)
        if end_cell is not None and end_cell.get_passable():
            return MoveOrder(move, end_cell, move)
        else:
            return None

    # We're ignoring combat movement for now.
    def _find_combat_move_end_tile(self, move):
        pass

    def _queue_exploration(self, move):
        move_order = self._find_exploration_move_end_tile(move)
        if (not self.movement_queue) and move_order is not None:
            self.movement_queue.append(move_order)

    def _queue_combat(self, move):
        move_order = self._find_combat_move_end_tile(move)
        if move in self.combat_costs and \
                move_order is not None and \
                self._movement_points >= self.combat_costs[move]:
            self.movement_points -= self.combat_costs[move]
            self.movement_queue.append(move_order)

    def _commit_exploration(self):
        if self.movement_queue:
            target_cell = self.movement_queue[0].end_tile
            self.level.move_entity_from_to(self, self.current_cell.x, self.current_cell.y,
                                           target_cell.x, target_cell.y)

    # We're ignoring combat movement for now.
    def _commit_combat(self):
        pass