__author__ = 'Travis Moy'

from definitions import CMO


default_combat_costs = {CMO.MOVE_FORWARD: 1, CMO.MOVE_BACKWARDS: 1.5,
                        CMO.TURN_RIGHT: .33, CMO.TURN_LEFT: .33}


class Mobile:
    def __init__(self, combat_costs=default_combat_costs, movement_points=1):
        self.movement_queue = []
        self.combat_costs = combat_costs
        self._is_alerted = False
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

    # Need access to the map for this!
    def _is_valid_exploration_move(self, move):
        pass

    # Need access to the map for this!
    def _is_valid_combat_move(self, move):
        pass

    def _queue_exploration(self, move):
        if (not self.movement_queue) and self._is_valid_exploration_move(move):
            self.movement_queue.append(move)

    def _queue_combat(self, move):
        if move in self.combat_costs and \
                self.is_valid_combat_move(move) and \
                self._movement_points >= self.combat_costs[move]:
            self.movement_points -= self.combat_costs[move]
            self.movement_queue.append(move)

    # Need access to map for this!
    def _commit_exploration(self):
        pass

    # Need access to map for this!
    def _commit_combat(self):
        pass