
class Villager:
    name = ""
    age = 0
    health = 100
    gender = ""
    probability_of_survival = int()

    def __init__(self,age,gender,health):
        self.name = assign_name_to_villager(gender)
        self.age = age
        self.gender = gender
        self.health = health

    def print_stats(self):
        print(
            f"{self.name:<8}",
            " Age: ", self.age,
            " health: ", self.health ,
            self.gender)

    def is_adult(self):
        return self.age > 17

femalenames = ["Anna","Agatha","Ophelia","Daisy","Mary","Alice", "Agnes", "Beatrice", "Cecilia", "Eleanor", "Emma",
               "Isabella", "Joan", "Margaret", "Matilda", "Philippa", "Rose", "Sybil", "Theresa", "Ysabel"]

malenames = ["John","Edward","Paul","Harold","Albert", "Arthur", "Bernard", "Cedric", "Charles", "Edgar", "Edmund",
             "Geoffrey", "Henry", "Hugh", "Lancelot", "Louis", "Richard", "Robert", "Stephen", "Thomas", "William"]

# function for giving a specific villager the first name from the list and then pushing it to the back of the list
def assign_name_to_villager(gender):
    if gender == "female":
        name = femalenames[0]
        usedname = femalenames.pop(0)
        femalenames.append(usedname)
    else:
        name = malenames[0]
        usedname = malenames.pop(0)
        malenames.append(usedname)
    return name

#function that creates a whole random villager!

def create_random_villager():
    import random
    age = random.randint(1, 85)
    gender = random.choice(["female","male"])
    health = random.randint(20, 100)
    return Villager(age,gender,health)

