class mainsloth:
    def __init__(self, name,hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack_with_claws(self):
        return 24
    
    def attack_with_torch(self):
        return 100
    

        

def create_sloth(name, hp, damage):
    sloth = mainsloth(name, hp, damage)
    print(sloth.name)
    return sloth

    


