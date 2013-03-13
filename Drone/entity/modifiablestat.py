__author__ = 'Travis Moy'


class ModifiableStat:
    def __init__(self, base_value, name="Unnamed Stat"):
        self.name = name
        self._base_value = base_value
        self.maximum_value = base_value
        self.current_value = base_value
        self.bonuses = []

    def add(self, value):
        self.current_value += value
        if self.current_value > self.maximum_value:
            self.current_value = self.maximum_value

    def sub(self, value):
        self.current_value -= value
        if self.current_value < 0:
            self.current_value = 0

    def apply_bonus(self, bonus):
        self.bonuses.append(bonus)
        self.maximum_value += bonus.value

    def remove_bonus(self, bonus):
        self.bonuses.remove(bonus)
        self.maximum_value -= bonus.value
        if self.current_value > self.maximum_value:
            self.current_value = self.maximum_value