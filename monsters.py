import random

class monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


    
    def takeDamage(self, damage):
        self.hp = self.hp - damage

#make attack more modular in the near future




def cave_enemy_selection(enemies):
    enemy_index = random.randint(0, len(enemies) - 1)
    print(f"The length of enemies is {len(enemies)}")
    return enemy_index

enemies = [{
        "monster": monster("Cave Spider",hp=50, damage=15),
        "encounter_chance": 0.47,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Spider",
        "possible_location": "cave_entrance",
        "run_chance": .9,
        "item_drop_chance":0.2
    },

    {   
        "monster": monster("Cave Monkey", 50, 20),
        "encounter_chance": 0.7,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "You have successfully defeated the Cave Monkey!", 
        "possible_location": "cave_entrance",
        "run_chance": .7,
        "item_drop_chance":0.3

    },
    
    {
        "monster": monster("Cave Troll", hp=70, damage=23),
        "encounter_chance": 0.10,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "You have successfully defeated the Cave Troll!",
        "possible_location": "cave_entrance",
        "run_chance": .2,
        "item_drop_chance":0.8

    }]
