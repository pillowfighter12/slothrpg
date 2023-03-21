import random
import copy


class Monster:
    def __init__(self, name, hp, damage):
        self._name = name
        self._hp = hp
        self._damage = damage
        #self._drop_potion_chance = drop_potion_chance

    
    # @property
    # def drop_potion_chance(self):
    #     return self._drop_potion_chance

enemies = [{
        "monster": Monster("Cave Spider",hp=50, damage=15),
        "encounter_chance": 0.47,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Spider",
        "possible_location": "cave_entrance",
        "run_chance": .9,
        "drop_potion_chance":0.2
    },

    {   
        "monster": Monster("Cave Monkey", hp=60, damage=20),
        "encounter_chance": 0.7,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Monkey!", 
        "possible_location": "cave_entrance",
        "run_chance": .7,
        "drop_potion_chance":0.3

    },
    
    {
        "monster": Monster("Cave Troll", hp=70, damage=23),
        "encounter_chance": 0.10,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "You have successfully defeated the Cave Troll!",
        "possible_location": "cave_entrance",
        "run_chance": .2,
        "drop_potion_chance":0.8

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


