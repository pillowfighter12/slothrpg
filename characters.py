class maincharacter:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints

    def attack_with_claws(self):
        return 24
        

def create_character(name):
    player = maincharacter(name, 100)
    print("Welcome " + player.name)
    return player
    

