import random

class monster:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints

    def attack(self):
        return random.randint(5, 15)

    


