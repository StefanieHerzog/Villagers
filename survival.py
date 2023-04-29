from villager import Villager

# functions to determine if a specific villager dies each month
# to do: function to see if each villager dies each month

def survival_check():
    for villager in self.villagers:
        set_probability_of_survival()
        roll_the_die()
        print_stats_all_dead_villagers()
        delete_dead_villagers ()


def set_probability_of_survival():
    if age < 6 or age > 60:
        probability_of_survival = 30
    elif age < 12 or age > 50:
        probability_of_survival = 50
    else:
        probability_of_survival = 80

    probability_of_survival = probability_of_survival * health * 1.5 / 100


# print (villager1.probability_of_survival)

def roll_the_die():
    import random
    random_number = random.randint(1, 100)
    if random_number > probability_of_survival:
        health = 0
        print("survival =" + str(villager1.probability_of_survival) + "... must be higher than " + str(random_number))
        print(name , "dies!")
    else:
        health = 0
        print("survival =" + str(villager1.probability_of_survival) + "... must be higher than " + str(random_number))
        print(name , "lives!")


def print_stats_all_dead_villagers(self):
    for villager in self.villagers:
        if health == 0:
                "The following villagers have died this month:"
                villager.print_stats()


def delete_dead_villagers():
    for villager in self.villagers:
        if health == 0:
            del()