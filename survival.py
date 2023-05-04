from villager import Villager

# functions to determine if a specific villager dies each month
# to do: function to see if each villager dies each month

def survival_check(villagers):
    for villager in villagers:
        probability = set_probability_of_survival(villager)
        roll_the_die(probability,villager)
    delete_dead_villagers(villagers)


def set_probability_of_survival(villager):
    if villager.age < 6 or villager.age > 60:
        probability_of_survival = 30
    elif villager.age < 12 or villager.age > 50:
        probability_of_survival = 50
    else:
        probability_of_survival = 90

    return probability_of_survival * villager.health * 1.5 / 100


# print (villager1.probability_of_survival)

def roll_the_die(probability_of_survival,villager):
    import random
    random_number = random.randint(1, 90)
    print("survival =" + str(probability_of_survival) + "... must be higher than " + str(random_number))
    if random_number > probability_of_survival:
        villager.health = 0
        print(villager.name , "stirbt!")
    else:
        print(villager.name , "lebt!")


def delete_dead_villagers(villagers):
    print("Diese Dorfbewohner sind leider gestorben:")
    index = 0
    while index < len(villagers):
        villager = villagers[index]
        if villager.health == 0:
            villager.print_stats()
            villagers.remove(villager)
        else:
            index += 1
    print("------------------------------------------------")