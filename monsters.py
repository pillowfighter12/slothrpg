import random

class monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

#make attack more modular in the near future


def cave_enemy_selection(enemies):
    enemy_index = random.randint(0, len(enemies) - 1)
    return enemy_index

def attack_enemy(enemy, sloth, enemy_counter):
    damage_given = sloth.damage
    enemy.hp -= damage_given
    print(f"You attack the {enemy.name} for {damage_given} damage!")
    return check_fight_status(enemy, sloth, enemy_counter)


def run_away(enemy, sloth, enemy_counter):
    chance = random.random()
    if chance <= enemies[enemy_index]["run_chance"]:
        print("You successfully ran away from the fight")
        return True
    else:
        print("You failed to run away and the fight continues")
        return False
    
def check_fight_status(enemy, sloth, enemy_counter):
    if enemy.hp <= 0 and sloth.hp >= 0:
        print(f"You defeated the {enemy.name}!")
        return True
    elif enemy.hp >= 0 and sloth.hp <= 0:
        print(f"{sloth.name} has fainted and you must go back to the start")
        main()
        return True
    else:
        return False

enemies = [{
        "monster": monster("Cave Spider",hp=50, damage=15),
        "encounter_chance": 0.47,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "After defeating the cave spider you found a torch and some armor",
        "possible_location": "cave_entrance",
        "run_chance": .9
    },

    {   
        "monster": monster("Cave Monkey", 50, 20),
        "encounter_chance": 0.7,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 10,
        "time_lapse_max_value": 20,
        "after_encounter_message": "After defeating the cave monkey you found a torch and some armor", 
        "possible_location": "cave_entrance",
        "run_chance": .7 
    },
    
    {
        "monster": monster("Cave Troll", hp=70, damage=23),
        "encounter_chance": 0.10,
        "pre_encounter_message": "The cave continues to get darker the deeper you go in",
        "time_lapse_min_value": 3,
        "time_lapse_max_value": 6,
        "after_encounter_message": "After defeating the cave troll you found a torch and some armor",
        "possible_location": "cave_entrance",
        "run_chance": .2
    }]
