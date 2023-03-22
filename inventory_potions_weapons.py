import random

class item:
    def __init__(self, name):
        self._name = name

class potion(item):
    def __init__(self, name, effect, occurence_chance):
        super().__init__(name)
        self._effect = effect
        self._occurence_chance = occurence_chance

    def apply(self, sloth):
        if self._effect == "small_potion":
            sloth.heal(50)
        if self._effect == "medium_potion":
            sloth.heal(100)
        if self._effect == "small_elixer":
            sloth._max_hp += 50

            
class weapon(item):
    def __init__(self, item, effect):
        self._item = item
        self._effect = effect

    def equip(self, sloth):
        if self._effect == "small_torch":
            sloth._damage = 50
        if self.effect == "sloth_claws":
            sloth._damage = 24

class inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        if isinstance(item, (potion, weapon)):
            self._items.append(item)

    def potion_list(self):
        potion_l = [p for p in self._items if isinstance(p, potion)]
        if len(potion_l) == 0:
            print("There are currently no potions in the inventory")
        else:
            print("List of potions:")
            name_to_quantity = {}
            for p in potion_l:
                #prevents from erroring out
                if name_to_quantity.get(p._name) == None:
                    name_to_quantity[p._name] = 0

                name_to_quantity[p._name] = (name_to_quantity[p._name] +1)
            for p in name_to_quantity:
                print(p, name_to_quantity[p])
                
    #static because we dont need any information related to the class itself and we dont want to create another instance of inventory     
    @staticmethod
    def getRandomPotion():
        potion_key = random.choices(list(potions.keys()), weights=[potion._occurence_chance for potion in potions.values()],k=1)[0]
        return potions[potion_key]

    def inv_options(self, sloth):
        while True:
            print(f"""
                ****** Your current hp is {sloth._hp} ******""")
            print("""-----------------------------------------------------------------------------------------------------------
What would you like to do? A: Access your inventory? B: Take some time to rest? C: Continue into the cave?
-----------------------------------------------------------------------------------------------------------""")
            input_choice = input()
            if input_choice == "A":
                print("Would you like to access your A. weapons or B. potions?")
                inventory_choice = input()
                if inventory_choice == "A":
                    print("Not available at this time")
                elif inventory_choice == "B":
                    self.potion_list()
                    print("Would you like to use a potion?")
                  # pot_selection = input()

            elif input_choice == "B":
                print("You decided to lay next to a rock in a dangerous cave")
                print("Luckily no monsters snuck up on you")
                sloth._hp = sloth._maxhp
                print(f"""
                ****** Your health is now back to {sloth._maxhp} ******
                """)
            elif input_choice == "B":
                print("You decided to lay next to a rock in a dangerous cave")
                print("Luckily no monsters snuck up on you")
                sloth._hp = sloth._maxhp
                print(f"""
                ****** Your health is now back to {sloth._maxhp} ******
                """) 

            elif input_choice == "C":
                print("You decided to go deeper into the cave")
                break
            else:
                if input_choice not in ["A", "B", "C"]:
                    print("Input must be A, B, or C")



       



potions = {
    "small_potion": potion("small potion", "small_potion", occurence_chance = 0.9),
    "medium_potion": potion("medium potion", "medium_potion", occurence_chance = 0.9),
    "small_elixer": potion("small elixer of life", "small_elixer", occurence_chance = 0.9)
}



weapons = {
    "small_torch": weapon("torch", "small_torch"),
    "sloth_claws": weapon("claws", "sloth_claws"),
}
