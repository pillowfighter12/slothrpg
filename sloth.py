from inventory_potions_weapons import inventory

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
        self._name = name
        self._maxhp = self.__sloth_types[hero]["attributes"]["maxhp"]
        self._hp = self._maxhp
        self._damage = self.__sloth_types[hero]["attributes"]["dmg"]
        self._weapons = self.__sloth_types[hero]["weapons"]
        self._inventory = inventory()
    



    


