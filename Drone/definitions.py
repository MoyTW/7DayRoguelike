__author__ = 'Travis Moy'


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# Fog of War states
FOW = enum('UNREVEALED', 'REVEALED', 'VISIBLE')

# Combat Move Orders
CMO = enum('TURN_LEFT', 'TURN_RIGHT', 'MOVE_FORWARD', 'MOVE_BACKWARDS', 'REVERSE',
           'STRAFE_FORWARD_RIGHT', 'STRAFE_RIGHT', 'STRAFE_BACKWARDS_RIGHT',
           'STRAFE_FORWARD_LEFT', 'STRAFE_LEFT', 'STRAFE_BACKWARDS_LEFT')

# Directional enum
DIR = enum('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')