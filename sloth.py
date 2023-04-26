from inventory_potions_weapons import inventory
from text_decoration import text_decoration
import requests
from requests.exceptions import RequestException

class mainsloth:
    #Private so nobody can modify outside of the class, will always be same data.
    __sloth_types = {
        "Nomad": {
            "attributes": {
                "maxhp": 100,
                "hp": 100,
                "dmg": 25,
            },
        },

        "Tank": {
            "attributes": {
                "maxhp": 600,
                "hp": 300,
                "dmg": 135,
            },
        },
        "Slinger": {
            "attributes": {
                "maxhp": 500,
                "hp": 225,
                "dmg": 150,
            },
        },
    }
    

    def __init__(self, name, sloth_type, enemy_counter=0, total_enemy_counter=0):
        self._name = name
        self._maxhp = self.__sloth_types[sloth_type]["attributes"]["maxhp"]
        self._hp = self._maxhp
        self._damage = self.__sloth_types[sloth_type]["attributes"]["dmg"]
        self._inventory = inventory()
        self._enemy_counter = enemy_counter
        self._location = []
        self._total_enemy_counter = total_enemy_counter


    def get_enemy_counter(self):
        return self._enemy_counter
    
    def increment_total_enemy_counter(self):
        self._total_enemy_counter += 1
        return self._total_enemy_counter
    
    def get_total_enemy_counter(self):
        return self._total_enemy_counter
    

    def increment_enemy_counter(self):
        self._enemy_counter += 1
        return self._enemy_counter


    def reset_enemy_counter(self):
        self._enemy_counter = 0
        return self._enemy_counter


    def potion_heal(self, hp):
        self._hp += hp 
        if self._hp > self._maxhp:
            self._hp = self._maxhp


    def potion_elixer(self, maxhp):
        self._maxhp += maxhp
        self._hp += maxhp


    def add_location_visited(self, location):
        if location not in self._location:
            self._location.append(location)
        else:
            pass
    

    def change_sloth_type(self):
        text_decoration.input_decorator("What weapon would you like to select?", ["A - To use the axe", "B - To use the slingshot"])
        user_input = input()
        if user_input == "A":
            print("You have chosen the axe!")
            self._damage = self.__sloth_types["Tank"]["attributes"]["dmg"]
            self._maxhp += self.__sloth_types["Tank"]["attributes"]["maxhp"]
        elif user_input == "B":
            print("You have chosen the sling shot!")
            self._damage = self.__sloth_types["Slinger"]["attributes"]["dmg"]
            self._maxhp += self.__sloth_types["Slinger"]["attributes"]["maxhp"]
        self._hp = self._maxhp
            


    @staticmethod
    def create_sloth():
        text_decoration.center_message(""">>> Enter your sloth name <<<""")
        sloth_name = input()
        sloth = mainsloth(sloth_name, "Nomad")
        text_decoration.center_message(f"""\nWelcome {sloth_name}""")
        sloth.add_sloth()
        return sloth


    def add_sloth(self) -> dict:
        data = {
            "name": self._name,
            "max_hp": self._maxhp,
            "current_hp": self._hp,
            "dmg": self._damage
        }
        make_request('POST', 'sloths', data)


    # def get_all_sloths(self):
    #     response = make_request("GET", "sloths", {})
    #     for sloth in response:
    #         print(f"ID: {sloth['id']}, {sloth['name']}")
    #     return response


    @staticmethod
    def get_all_sloths():
        response = make_request("GET", "sloths", {})
        for sloth in response:
            print(f"ID: {sloth['id']}, {sloth['name']}")
        return response


    def select_sloth(id):
        return make_request("GET", f"sloths/{id}", {})





def make_request(request_type, path, data):
    url = f"http://127.0.0.1:9090/{path}"
    try:
        response = ""

        if request_type == 'POST':
            response = requests.post(url, json=data)
        elif request_type == 'GET':
            response = requests.get(url)
        elif request_type == 'PATCH':
            response = requests.patch(url, json=data)
            # ask user if they want to delete the sloth, say at end of the game.
        elif request_type == 'DELETE':
            response = requests.delete(url, json=data)

        if response.status_code == 200:
            print("POST request was successful!")
            return response.json()  # If the response is JSON
        else:
            print(f"Request failed with status code: {response.status_code}")
            return {"error": f"Request failed with status code: {response.status_code}"}
    except RequestException as e:
        print(f"An error occurred while sending the POST request: {e}")
        return {"error": f"An error occurred while sending the POST request: {e}"}



mainsloth.create_sloth()

sloths = mainsloth.get_all_sloths()

