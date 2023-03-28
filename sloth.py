from inventory_potions_weapons import inventory
from text_decoration import text_decoration

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
                "maxhp": 300,
                "hp": 300,
                "dmg": 35,
            },
            "weapons": ["sword", "axe"]
        },
        "Slinger": {
            "attributes": {
                "maxhp": 225,
                "hp": 225,
                "dmg": 50,
            },
            "weapons": ["slingshot", "bow"]
        },
    }
    

    def __init__(self, name, sloth_type, enemy_counter=0):
        self._name = name
        self._maxhp = self.__sloth_types[sloth_type]["attributes"]["maxhp"]
        self._hp = self._maxhp
        self._damage = self.__sloth_types[sloth_type]["attributes"]["dmg"]
        self._weapons = self.__sloth_types[sloth_type]["weapons"]
        self._inventory = inventory()
        self._enemy_counter = enemy_counter
        self._location = []


    def get_enemy_counter(self):
        return self._enemy_counter
    

    def increment_enemy_counter(self):
        self._enemy_counter += 1
        return self._enemy_counter


    def reset_enemy_counter(self):
        self._enemy_counter = 0
        return self._enemy_counter


    def potion_heal(self, hp):
        self._hp += hp 
        if self._hp > self._maxhp:
            self._hp = self._maxhp


    def potion_elixer(self, maxhp):
        self._maxhp += maxhp
        self._hp += maxhp


    def add_location_visited(self, location):
        if location not in self._location:
            self._location.append(location)
        else:
            pass
    

    def change_sloth_type(self):
        text_decoration.input_decorator("What weapon would you like to select?", ["A - To use the axe", "B - To use the slingshot"])
        user_input = input()
        if user_input == "A":
            print("You have chosen the axe!")
            self._damage = self.__sloth_types["Tank"]["attributes"]["dmg"]
            self._maxhp += self.__sloth_types["Tank"]["attributes"]["maxhp"]
        elif user_input == "B":
            print("You have chosen the sling shot!")
            self._damage = self.__sloth_types["Slinger"]["attributes"]["dmg"]
            self._maxhp += self.__sloth_types["Slinger"]["attributes"]["maxhp"]
        self._hp = self._maxhp
            





    


