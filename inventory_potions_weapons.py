class inventory:
    def __init__(self):
        self.item = []

    def add_potions(self, potions):
        self.item.append(potions)
    
    
    def use_item(self, item):
        if isinstance(item, potion):
            item.use(sloth)
            

class potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


    def apply(self, sloth):
        if self.effect == "small_potion":
            sloth.heal(50)
        if self.effect == "medium_potion":
            sloth.heal(100)
        if self.effect == "small_elixer":
            sloth.maxhitpoints += 50

potions = {
    "small_potion": potion("small potion", "small_potion"),
    "medium_potion": potion("medium potion", "medium_potion"),
    "small_elixer": potion("small elixer of life", "small_elixer"),
}




