class Villager:
    name = ""
    age = 0
    health = 100
    gender = ""
    probability_of_survival = int()

    def __init__(self,name,age,gender,health):
        self.name = name
        self.age = age
        self.gender = gender
        self.health = health

    def print_stats(self):
        print ("Name: ", self.name, " Age: ", self.age, " health: ", self.health , " gender: " , self.gender)

femalenames = ["Anna","Agatha","Ophelia","Daisy","Mary","Alice", "Agnes", "Beatrice", "Cecilia", "Eleanor", "Emma", "Isabella", "Joan", "Margaret", "Matilda", "Philippa", "Rose", "Sybil", "Theresa", "Ysabel"]

malenames = ["John","Edward","Paul","Harold","Albert", "Arthur", "Bernard", "Cedric", "Charles", "Edgar", "Edmund", "Geoffrey", "Henry", "Hugh", "Lancelot", "Louis", "Richard", "Robert", "Stephen", "Thomas", "William"]

# function for giving a specific villager the first name from the list and then pushing it to the back of the list
def assign_name_to_villager():
    if villager2.gender == "female":
        villager2.name = femalenames[0]
        usedname = femalenames.pop(0)
        femalenames.append(usedname)
    else:
        villager2.name = malenames[0]
        usedname = malenames.pop(0)
        malenames.append(usedname)