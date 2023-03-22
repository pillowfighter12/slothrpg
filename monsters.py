import random
import copy
from inventory_potions_weapons import inventory


class Monster:
    def __init__(self, name, hp, damage, drop_potion_chance):
        self._name = name
        self._hp = hp
        self._damage = damage
        self._drop_potion_chance = drop_potion_chance

    def drop_potion(self):
        if random.random() <= self._drop_potion_chance:
            potion = inventory.getRandomPotion()
            print(f"{self._name} dropped a {potion._name}!")
            return potion
    
enemies = [{
        "monster": Monster("Cave Spider",hp=50, damage=15, drop_potion_chance=0.9),
        "encounter_chance": 0.47,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Spider",
        "possible_location": "cave_entrance",
        "run_chance": .9,
    },

    {   
        "monster": Monster("Cave Monkey", hp=60, damage=20, drop_potion_chance=0.9),
        "encounter_chance": 0.7,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Monkey!", 
        "possible_location": "cave_entrance",
        "run_chance": .7,
    },
    
    {
        "monster": Monster("Cave Troll", hp=70, damage=23, drop_potion_chance=0.9),
        "encounter_chance": 0.10,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "You have successfully defeated the Cave Troll!",
        "possible_location": "cave_entrance",
        "run_chance": .2,
    }]


# bosses = [{
#         "boss": Monster("Godrick the Beetle",hp=1000, damage=75),
#         "encounter_chance": 1,
#         "pre_encounter_message": "The cave continues to get darker the deeper you go in",
#         "time_lapse_min_value": 10,
#         "time_lapse_max_value": 20,
#         "after_encounter_message": "You have successfully defeated the Godrick the Beetle",
#         "possible_location": "cave_pit",
#         "run_chance": .0,
#         "drop_potion_chance":1
#     }]

enemies_copy = copy.deepcopy(enemies)

class MonsterManager:
    def __init__(self, enemies):
        self._enemies = copy.deepcopy(enemies)
        self._enemies_copy = copy.deepcopy(enemies)

    def cave_enemy_selection(self):
        enemy_index = random.randint(0, len(self._enemies) - 1)
        self._enemies = copy.deepcopy(self._enemies_copy)
        return enemy_index



