import random




class Villager:
    name = ""
    age = 0
    health = 100
    gender = ""
    spouse = "-"
    children = []
    siblings = []
    parents = []
    pregnant = -1

    def __init__(self,age,gender,health,spouse,children,siblings, parents, pregnant):
        self.name = assign_name_to_villager(gender)
        self.age = age
        self.gender = gender
        self.health = health
        self.spouse = spouse
        self.children = children
        self.siblings = siblings
        self.parents = parents
        self.pregnant = pregnant


    def print_stats(self):
        print(
            f"{self.name:<8}", "|",
            " Alter: ", f"{self.age:<3}", "|",
            " Gesundheit: ", self.health , "|",
            " Partner: ", self.spouse)

    def is_adult(self):
        return self.age >= 16

femalenames = ["Anna", "Agatha", "Ophelia", "Daisy", "Mary", "Alice", "Agnes", "Beatrice", "Cecilia", "Eleanor", "Emma",
               "Isabella", "Joan", "Margaret", "Matilda", "Philippa", "Rose", "Sybil", "Theresa", "Ysabel", "Bella",
               "Adela", "Elise", "Aenor", "Alma", "Amice", "Zora", "Arletta", "Aveline", "Avice", "Basilia",
               "Blanche", "Ruth", "Catalina", "Chrissy", "Clarice", "Conni", "Cordelia", "Denise", "Dionisia",
               "Dulcia", "Edith", "Eliane", "Ella", "Etta", "Ermentra", "Felice", "Flora", "Gabi",
               "Galiana", "Lucia", "Ginny", "Giselle", "Gracia", "Gundred", "Heloise","Niamh","Gloria"]

malenames = ["John", "Edward", "Paul", "Harold", "Albert", "Arthur", "Bernard", "Cedric", "Charles", "Edgar", "Edmund",
             "Geoffrey", "Henry", "Hugh", "Lancelot", "Louis", "Richard", "Robert", "Stephen", "Thomas", "William",
             "Albert", "Adam", "Aelfric", "Beowulf", "Alaric", "Alberic", "Alex", "Ansel", "Archie",
             "Baldwin", "Bertram", "Zion", "Eadric", "Erwin", "Emeric", "Jonas", "Nathan", "Hector",
             "Gerald", "Rolf", "Godfrey", "Harvey", "Hubert", "Ivo", "Hector", "Leopold", "Matthew", "Leopold"]


random.shuffle(femalenames)
random.shuffle(malenames)

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




def create_random_villager():
    return Villager(random.randint(1, 85), random.choice(["female","male"]), random.randint(20, 100),"-" , [],[],[],-1)

def create_random_old_villager():
    return Villager(random.randint(60, 85), random.choice(["female","male"]), random.randint(20, 100),"-" , [],[],[],-1)

def create_random_minor_villager():
    return Villager(random.randint(1, 14), random.choice(["female","male"]), random.randint(20, 100),"-" , [],[],[],-1)

def create_random_baby_villager():
    return Villager(random.randint(0, 2), random.choice(["female","male"]), random.randint(20, 100),"-" , [],[],[],-1)

def create_random_female_villager():
    return Villager(random.randint(1, 85), "female", random.randint(20, 100),"-" , [],[],[],-1)

def create_random_male_villager():
    return Villager(random.randint(1, 85), "male", random.randint(20, 100),"-" , [],[],[],-1)

def create_newborn(mother):
    age = 0
    gender = random.choice(["female", "male"])
    health = random.randint(20, 100)
    spouse = "-"
    parents = [mother.name, mother.spouse]
    children = []
    siblings = mother.children
    return Villager(age, gender, health, spouse, parents, children, siblings, -1)

    #old function that creates a whole random villager!

    # def create_random_villager():
    #   import random
    #   age = random.randint(1, 85)
    #   gender = random.choice(["female","male"])
    #   health = random.randint(20, 100)
    #   return Villager(age,gender,health)