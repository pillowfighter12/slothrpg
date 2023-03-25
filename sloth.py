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
    

    def __init__(self, name, hero, enemy_counter=0):
        self._name = name
        self._maxhp = self.__sloth_types[hero]["attributes"]["maxhp"]
        self._hp = self._maxhp
        self._damage = self.__sloth_types[hero]["attributes"]["dmg"]
        self._weapons = self.__sloth_types[hero]["weapons"]
        self._inventory = inventory()
        self._enemy_counter = enemy_counter
        # self._locations_visited = {}
        # self._current_location = "start"

    def get_enemy_counter(self):
        return self._enemy_counter
    

    def increment_enemy_counter(self):
        self._enemy_counter += 1
        return self._enemy_counter


    def potion_heal(self, hp):
        self._hp += hp 
        if self._hp > self._maxhp:
            self._hp = self._maxhp


    def potion_elixer(self, maxhp):
        self._maxhp += maxhp
        self._hp += maxhp

    def add_location_visited(self, location):
        self._locations_visited[location] = True

    def get_location_visited(self):
        return self._current_location


        



    


