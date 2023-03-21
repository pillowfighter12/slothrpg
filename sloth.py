tom = "3"

class mainsloth:
    #Private so nobody can modify outside of the class, will always be same data.
    __sloth_types = {
        "Nomad": {
            "attributes": {
                "maxhp": 100,
                "hp": 100,
                "dmg": 25,
            },
            "weapons": ["claws"]
        },

        "Tank": {
            "attributes": {
                "maxhp": 200,
                "hp": 200,
                "dmg": 25,
            },
            "weapons": ["sword", "axe"]
        },
        "Slinger": {
            "attributes": {
                "maxhp": 125,
                "hp": 125,
                "dmg": 50,
            },
            "weapons": ["slingshot", "bow"]
        },
    }
    
    def __init__(self, name, hero):
        self.name = name
        self.maxhp = self.__sloth_types[hero]["attributes"]["maxhp"]
        self.hp = self.maxhp
        self.damage = self.__sloth_types[hero]["attributes"]["dmg"]
        self.weapons = self.__sloth_types[hero]["weapons"]
       
    def increase_maxhp(sloth, amount):
        sloth.maxhp += amount
    



    


