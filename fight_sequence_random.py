import random
from monsters import enemies
from text_decoration import text_decoration
import sys
import time


class fight_simulation:
    def __init__(self, enemy, sloth, enemy_index, enemy_counter):
        self._enemy = enemy
        self._sloth = sloth
        self._enemy_index = enemy_index
        self._fight_over = False
        self._enemy_counter = enemy_counter
     


    def engage_fight(self):
        actions = {
            "A": self.attack_enemy,
            "B": self.run_away,
        }
        print(enemies[self._enemy_index]["pre_encounter_message"], "\n\n")
        text_decoration.print_health([self._sloth._name, self._sloth._hp, self._enemy._name, self._enemy._hp])
        while not self._fight_over:
            text_decoration.input_decorator("What would you like to do?",["A - Attack!", "B - Run Away!"])
            choice = input().upper()

            if choice not in actions:
                print("Input must be A or B")
                continue

            action = actions[choice]
            result = action()
        
            if result is not None:
                self._fight_over = result
            # Enemy defeated
            if self._enemy._hp <= 0 and self._sloth._hp >= 0:
                print(enemies[self._enemy_index]["after_encounter_message"])
                self._sloth._inventory.add_item(self._enemy.drop_potion())
                self._fight_over = True
            # Enemy Victory
            if  self._sloth._hp <= 0 and self._enemy._hp >= 0:
                print(f"""{self._sloth._name} has fainted and you must go back to the start""")
                self._fight_over = True
                sys.exit()
            # Sloth takes damage
            if not self._fight_over:
                self._sloth._hp -= self._enemy._damage
                print(f"""\n* You did {self._sloth._damage} damage to {self._enemy._name} *\n""")
                text_decoration.print_health([self._sloth._name, self._sloth._hp, self._enemy._name, self._enemy._hp])
                
        self._fight_over = False

    def time_lapse(self, min_time, max_time, encounter_chance):
        for i in range(random.randint(min_time, max_time)):
            enemy_search = True
            enemy_found = self._enemy
            print(" . . . ")
            time.sleep(1)
            chance = random.random()
            if chance <= encounter_chance or not self._enemy:
                continue
            if not enemy_found and enemy_search == False:
                print("\nYou didn't encounter any enemies")
                break
            self.engage_fight()
            self._sloth.increment_enemy_counter()
            self._sloth.increment_total_enemy_counter()
            # print(f"You have encountered", self._sloth.get_enemy_counter())
            # print(f"You have encountered", self._sloth.get_total_enemy_counter())
            return self._sloth.get_enemy_counter()

    def attack_enemy(self):
        self._enemy._hp -= self._sloth._damage

    def run_away(self):
        if random.random() < enemies[self._enemy_index]["run_chance"]:
            print("""\nYou ran away successfully!\n""")
            print(f"""\nThe chance of escaping was {enemies[self._enemy_index]['run_chance']}"""
                  
                  )
            return True
        else:
            print("\nYou couldn't escape!")
            print(f"\nThe chance of escaping was {enemies[self._enemy_index]['run_chance']}")
            return False
        
    


    


