from inventory_potions_weapons import inventory
from sloth import mainsloth

sloth_name = input("""Enter your sloth name:
""")

sloth = mainsloth(sloth_name, "Nomad")


inventory = inventory()
inventory.add_item(inventory.getRandomPotion())
inventory.add_item(inventory.getRandomPotion())
inventory.add_item(inventory.getRandomPotion())
inventory.add_item(inventory.getRandomPotion())
inventory.add_item(inventory.getRandomPotion())
inventory.add_item(inventory.getRandomPotion())

inventory.inv_options(sloth)


# inventory.apply(