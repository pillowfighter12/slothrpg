class item:
    def __init__(self, name):
        self.name = name

class potion(item):
    def __init__(self, name, effect):
        super().__init__(name)
        self.effect = effect

    def apply(self, sloth):
        if self.effect == "small_potion":
            sloth.heal(50)
        if self.effect == "medium_potion":
            sloth.heal(100)
        if self.effect == "small_elixer":
            sloth.max_hp += 50

class weapon:
    def __init__(self, item, effect):
        self.item = item
        self.effect = effect

    def equip(self, sloth):
        if self.equip == "small_torch":
            sloth.damage = 50
        if self.equip == "sloth_claws":
            sloth.damage = 24

class inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, (potion, weapon)):
            self.items.append(item)

    def potion_list(self):
        potion_l = [p for p in self.items if isinstance(p, potion)]
        if len(potion_l) == 0:
            print("There are currently no potions in the inventory")
        else:
            print("List of potions:")
        for p in potion_l:
            print("- " + p.name)



potions = {
    "small_potion": potion("small potion", "small_potion"),
    "medium_potion": potion("medium potion", "medium_potion"),
    "small_elixer": potion("small elixer of life", "small_elixer"),
}

weapons = {
    "small_torch": weapon("torch", "small_torch"),
    "sloth_claws": weapon("claws", "sloth_claws"),
}
