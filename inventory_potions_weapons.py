import random


class item:
    def __init__(self, name):
        self._name = name

class potion(item):
    def __init__(self, name, effect, occurence_chance, id):
        super().__init__(name)
        self._effect = effect
        self._occurence_chance = occurence_chance
        self._id = id

    def apply(self, sloth):
        print('inv:')
        print(sloth._inventory)
        if self._effect == "small_potion":
            sloth.potion_heal(50)
        if self._effect == "medium_potion":
            sloth.potion_heal(100)
        if self._effect == "small_elixer":
            sloth.potion_elixer(50)
        
        sloth._inventory.remove_item(self)
        

   

            
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

    def remove_item(self, item):
        if isinstance(item, (potion, weapon)):
            self._items.remove(item)

    def potion_list(self, potion_l):
        # Create a dictionary of potion names and quantities
            name_to_quantity = {}
            name_to_id = {}
            
            for p in potion_l:
                #prevents from erroring out
                if name_to_quantity.get(p._name) == None:
                    name_to_quantity[p._name] = 0
                    name_to_id[p._name] = p._id
                
                name_to_quantity[p._name] = (name_to_quantity[p._name] +1)

            sorted_potions = sorted(name_to_id.items(), key=lambda x: x[1])
            for p,i in sorted_potions:
                q = name_to_quantity[p]
                #i = name_to_id[p]
                print(f"{p}, x {q}, Type: {i} to use.\n")

    def potion_inventory_options(self, sloth):
        potion_l = [p for p in self._items if isinstance(p, potion)]
        if len(potion_l) == 0:
            print("\nThere are currently no potions in the inventory\n")
        else:
            print("""\nList of potions:\n""")
            self.potion_list(potion_l)
            user_input = input()
            potion_selection = [p for p in potion_l if p._id == int(user_input)][0]
            potion_selection.apply(sloth)
            print(sloth._hp)









    #static because we dont need any information related to the class itself and we dont want to create another instance of inventory     
    @staticmethod
    def getRandomPotion():
        #can be written as potion_key = potion_list[0] instead of using index at the end
        potion_key = random.choices(list(potions.keys()), weights=[potion._occurence_chance for potion in potions.values()],k=1)[0]
        return potions[potion_key]

    def inv_options(self, sloth):
        while True:
            print(f"""\n****** Your current hp is {sloth._hp} ******""")
            print("""-----------------------------------------------------------------------------------------------------------
What would you like to do? A: Access your inventory? B: Take some time to rest? C: Continue into the cave?\n-----------------------------------------------------------------------------------------------------------
""")
            input_choice = input()
            if input_choice == "A":
                print("Would you like to access your A. weapons or B. potions?")
                inventory_choice = input()
                if inventory_choice == "A":
                    print("Not available at this time")
                elif inventory_choice == "B":
                    self.potion_inventory_options(sloth)

                    


              #######################################
              #######################################
              #######################################
              #######################################
              #######################################
              #######################################

            elif input_choice == "B":
                print("""
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_   

You decided to lay next to a rock in a dangerous cave, luckily no monsters snuck up on you! 

_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
""")
                sloth._hp = sloth._maxhp
                print(f"""\n****** Your health is now back to {sloth._maxhp} ******\n""")

            elif input_choice == "B":
                print("\nYou decided to lay next to a rock in a dangerous cave\n")
                print("\nLuckily no monsters snuck up on you\n")
                sloth._hp = sloth._maxhp
                print(f"""
                ****** Your health is now back to {sloth._maxhp} ******
                """) 

            elif input_choice == "C":
                print("\nYou decided to go deeper into the cave\n")
                break
            else:
                if input_choice not in ["A", "B", "C"]:
                    print("\nInput must be A, B, or C\n")



       



potions = {
    "small_potion": potion("small potion", "small_potion", occurence_chance = 0.4, id = 1),
    "medium_potion": potion("medium potion", "medium_potion", occurence_chance = 0.2, id = 2),
    "small_elixer": potion("small elixer of life", "small_elixer", occurence_chance = 0.4, id = 3)
}



weapons = {
    "small_torch": weapon("torch", "small_torch"),
    "sloth_claws": weapon("claws", "sloth_claws"),
}
