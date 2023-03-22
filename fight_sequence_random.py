import random
from monsters import enemies


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

        while not self._fight_over:
            print("""-----------------------
A: to attack B: to run!
-----------------------""")
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
                print(f"You defeated the {self._enemy._name}")
                print(enemies[self._enemy_index]["after_encounter_message"])
                self._sloth._inventory.add_item(self._enemy.drop_potion())
                self._fight_over = True
            # Enemy Victory
            if self._enemy._hp >= 0 and self._sloth._hp <= 0:
                print(f"""{self._sloth._name} has fainted and you must go back to the start
                ***************""")
                main()
                self._fight_over = True
            # Sloth takes damage
            if not self._fight_over:
                self._sloth._hp -= self._enemy._damage
                print(f"""You have taken {self._enemy._damage} damage to the face"
-------------------------------------------------------                
{self._sloth._name} has  {self._sloth._hp} health remaining
{self._enemy._name} has  {self._enemy._hp} health remaining""")
                #self._sloth._inventory.inv_options(self._sloth)

        self._fight_over = False

    def time_lapse(self, min_time, max_time, encounter_chance):
        print(enemies[self._enemy_index]["pre_encounter_message"])
        for i in range(random.randint(min_time, max_time)):
            enemy_search = True
            enemy_found = self._enemy
            print(" . . . ")
            time.sleep(1)
            chance = random.random()
            if chance <= encounter_chance or not self._enemy:
                continue
            if not enemy_found and enemy_search == False:
                print("You didn't encounter any enemies")
                break
            print("A", self._enemy._name, "approaches!")
            print(f"The enemy {self._enemy._name} has {self._enemy._hp} hitpoints!")
            self.engage_fight()
            self._enemy_counter += 1
            print(self._enemy_counter)
            return self._enemy_counter

    def attack_enemy(self):
        self._enemy._hp -= self._sloth._damage
        print(f"You did {self._sloth._damage} damage to {self._enemy._name}!")

    def run_away(self):
        print("Enemy index:", self._enemy_index)
        if random.random() < enemies[self._enemy_index]["run_chance"]:
            print("You ran away successfully!")
            print(f"The chance of escaping was {enemies[self._enemy_index]['run_chance']}")
            return True
        else:
            print("You couldn't escape!")
            print(f"The chance of escaping was {enemies[self._enemy_index]['run_chance']}")
            return False
        
    


    


