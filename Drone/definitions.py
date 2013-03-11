__author__ = 'Travis Moy'

from collections import namedtuple


Position = namedtuple('Position', 'x y')


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# Fog of War states
FOW = enum('UNREVEALED', 'REVEALED', 'VISIBLE')

# Combat Move Orders
CMO = enum('TURN_LEFT', 'TURN_RIGHT', 'MOVE_FORWARD', 'MOVE_BACKWARDS', 'REVERSE',
           'STRAFE_FORWARD_RIGHT', 'STRAFE_RIGHT', 'STRAFE_BACKWARDS_RIGHT',
           'STRAFE_FORWARD_LEFT', 'STRAFE_LEFT', 'STRAFE_BACKWARDS_LEFT')


# This isn't an enum any more!
class DIR(object):
    N, NE, E, SE, S, SW, W, NW = range(0, 8)

    def position_to_of(self, direction, current_cell):
        if direction == DIR.N:
            return Position(current_cell[0], current_cell[1] + 1)
        elif direction == DIR.NE:
            return Position(current_cell[0] + 1, current_cell[1] + 1)
        elif direction == DIR.E:
            return Position(current_cell[0] + 1, current_cell[1])
        elif direction == DIR.SE:
            return Position(current_cell[0] + 1, current_cell[1] - 1)
        elif direction == DIR.S:
            return Position(current_cell[0], current_cell[1] - 1)
        elif direction == DIR.SW:
            return Position(current_cell[0] - 1, current_cell[1] - 1)
        elif direction == DIR.W:
            return Position(current_cell[0] - 1, current_cell[1])
        elif direction == DIR.NW:
            return Position(current_cell[0] - 1, current_cell[1] + 1)