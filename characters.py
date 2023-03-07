class maincharacter:
    def __init__(self, name, hitpoints, damage):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage

    def attack_with_claws(self):
        return 24
    
    def attack_with_torch(self):
        return 100
    

        

def create_character(name, hitpoints, damage):
    player = maincharacter(name, hitpoints, damage)
    print(player.name)
    return player

    


