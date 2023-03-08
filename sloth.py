class mainsloth:
    def __init__(self, name, hitpoints, damage):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage

    def attack_with_claws(self):
        return 24
    
    def attack_with_torch(self):
        return 100
    

        

def create_sloth(name, hitpoints, damage):
    sloth = mainsloth(name, hitpoints, damage)
    print(sloth.name)
    return sloth

    


