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
            print(f"\n\n-`♡´--`♡´--`♡´--`♡´--`♡´-{self._name} dropped a {potion._name}-`♡´--`♡´--`♡´--`♡´--`♡´-")
            return potion
    

enemies = [{
        "monster": Monster("Cave Spider",hp=50, damage=15, drop_potion_chance=0.05),
        "encounter_chance": 0.47,
        "pre_encounter_message": "A large Cave Spider fell ontop of you!",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "\n***** You have successfully defeated the Cave Spider! ***** \n",
        "possible_location": "cave_entrance",
        "run_chance": .9,
    },

    {   
        "monster": Monster("Cave Monkey", hp=60, damage=20, drop_potion_chance=0.1),
        "encounter_chance": 0.7,
        "pre_encounter_message": "Why is there a monkey in the cave?",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "\n***** You have successfully defeated the Cave Monkey! ***** \n", 
        "possible_location": "cave_entrance",
        "run_chance": .7,
    },
    
    {
        "monster": Monster("Cave Troll", hp=70, damage=23, drop_potion_chance=0.2),
        "encounter_chance": 0.10,
        "pre_encounter_message": "A Giant Troll started moving towards you!",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "\n***** You have successfully defeated the Cave Troll! ***** \n",
        "possible_location": "cave_caverns",
        "run_chance": .2,
    },
{
        "monster": Monster(" ?????? ",hp=50, damage=15, drop_potion_chance=0.1),
        "encounter_chance": 0.47,
        "pre_encounter_message": "A large ????? fell ontop of you!",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "\n***** You have successfully defeated the ????! ***** \n",
        "possible_location": "cave_caverns",
        "run_chance": .9,
    },

    {   
        "monster": Monster("Gloom Gobbler", hp=160, damage=30, drop_potion_chance=0.1),
        "encounter_chance": 0.7,
        "pre_encounter_message": "A Gloom Gobbler came from beneath the ground!",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "\n***** You have successfully defeated the Gloom Gobbler! ***** \n", 
        "possible_location": "cave_caverns",
        "run_chance": .7,
    },
    
    {
        "monster": Monster("Batsquatch", hp=200, damage=35, drop_potion_chance=0.25),
        "encounter_chance": 0.10,
        "pre_encounter_message": "A Batsquatch started attacking you!",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "\n***** You have successfully defeated the Batsquatch! ***** \n",
        "possible_location": "cave_caverns",
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


    def cave_enemy_selection(self, location):
        # Get a list of indices of enemies in the cave entrance
        entrance_enemies_indices = [
            i for i, e in enumerate(self._enemies)
            if e["possible_location"] == location]
        # Select a random enemy from the list of cave entrance enemies
        enemy_index = random.choice(entrance_enemies_indices)
        # Reset the enemy list to its original state
        self._enemies = copy.deepcopy(self._enemies_copy)
        return enemy_index
    



