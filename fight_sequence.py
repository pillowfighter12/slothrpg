import random
from monsters import enemies


import time


class fight_simulation:
    def __init__(self, enemy, sloth, enemy_index, enemy_counter):
        self.enemy = enemy
        self.sloth = sloth
        self.enemy_index = enemy_index
        self.fight_over = False
        self.enemy_counter = enemy_counter

    def engage_fight(self):
        actions = {
            "A": self.attack_enemy,
            "B": self.run_away,
        }

        while not self.fight_over:
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
                self.fight_over = result

            if self.enemy.hp <= 0 and self.sloth.hp >= 0:
                print(f"You defeated the {self.enemy.name}")
                self.fight_over = True

            if self.enemy.hp >= 0 and self.sloth.hp <= 0:
                print(f"""{self.sloth.name} has fainted and you must go back to the start
                ***************""")
                main()
                self.fight_over = True

            if not self.fight_over:
                self.sloth.hp -= self.enemy.damage

                print(f"""You have taken {self.enemy.damage} damage to the face"
-------------------------------------------------------                
{self.sloth.name} has  {self.sloth.hp} health remaining
{self.enemy.name} has  {self.enemy.hp} health remaining""")

        self.fight_over = False

    def time_lapse(self, min_time, max_time, encounter_chance):
        print(enemies[self.enemy_counter]["pre_encounter_message"])
        for i in range(random.randint(min_time, max_time)):
            enemy_search = True
            enemy_found = self.enemy
            print(" . . . ")
            time.sleep(1)
            chance = random.random()
            if chance <= encounter_chance or not self.enemy:
                continue
            if not enemy_found and enemy_search == False:
                print("You didn't encounter any enemies")
                break
            print("A", self.enemy.name, "approaches!")
            self.engage_fight()
            self.enemy_counter += 1
            print(self.enemy_counter)
            return self.enemy_counter

    def attack_enemy(self):
        self.enemy.hp -= self.sloth.damage
        print(f"You did {self.sloth.damage} damage to {self.enemy.name}!")

    def run_away(self):
        print("Enemy index:", self.enemy_index)
        if random.random() < enemies[self.enemy_index]["run_chance"]:
            print("You ran away successfully!")
            print(f"The chance of escaping was {enemies[self.enemy_index]['run_chance']}")
            return True
        else:
            print("You couldn't escape!")
            print(f"The chance of escaping was {enemies[self.enemy_index]['run_chance']}")
            return False



    


