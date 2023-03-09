class mainsloth:
    def __init__(self, name, maxhp, hp, damage):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.damage = damage

        

def create_sloth(name, maxhp, hp, damage):
    sloth = mainsloth(name, maxhp, hp, damage)
    return sloth

    


