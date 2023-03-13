import random

class monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

#make attack more modular in the near future


def cave_enemy_selection(enemies):
    enemy_index = random.randint(0, len(enemies) - 1)
    return enemy_index


