import random

class monster:
    def __init__(self, name, hitpoints, damage):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage

    def attack(self):
        return random.randint(5, 15)

    


