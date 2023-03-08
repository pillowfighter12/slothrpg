class mainsloth:
    def __init__(self, name, maxhp, hp, damage):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.damage = damage

    def attack_with_claws(self):
        return 24
    
    def attack_with_torch(self):
        return 100
    

        

def create_sloth(name, maxhp, hp, damage):
    sloth = mainsloth(name, maxhp, hp, damage)
    return sloth

    


