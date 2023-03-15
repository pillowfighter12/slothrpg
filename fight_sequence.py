import random
from monsters import *

def engage_fight(enemy, sloth, enemy_counter):
    print("You have encountered a enemy!", enemy.name)

    #Flag to know if fight is over or not
    fight_over = False

    def attack_enemy(enemy, sloth, enemy_counter):
        damage_done = sloth.damage
        enemy.hp -= damage_done
        print(f"You did {damage_done} damage to {enemy.name}!")
        return False

    def run_away(enemy, sloth, enemy_index):
        if random.random() < enemies[enemy_index]["run_chance"]:
            print("You ran away successfully!")
            return True
        else:
            print("You couldn't escape!")
            return False

    actions = {
        "A": attack_enemy,
        "B": run_away,
    }

    while not fight_over:
        print("""A: to attack
B: to run!""")
        choice = input().upper()
        
        if choice not in actions:
            print("Input must be A or B")
            continue

        action = actions[choice]
        result = action(enemy, sloth, enemy_counter)

        if result is not None:
            
            fight_over = result
            
            

        if enemy.hp <= 0 and sloth.hp >= 0:
            print(f"You defeated the {enemy.name}")
            fight_over = True

        if enemy.hp >= 0 and sloth.hp <= 0:
            print(f"""{sloth.name} has fainted and you must go back to the start
            ***************""")
            main()
            fight_over = True

        if not fight_over:
            damage_taken = enemy.damage
            sloth.hp -= damage_taken
            print(f"""You have taken {damage_taken} damage to the face"
{sloth.name} has  {sloth.hp} health remaining
{enemy.name} has  {enemy.hp} health remaining""")
