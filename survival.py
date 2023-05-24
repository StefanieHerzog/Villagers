from villager import Villager

# functions to determine if a specific villager dies each month
# to do: function to see if each villager dies each month

def survival_check(villagers):
    print("")
    print("Es ist wieder Winter. Wer wird sterben?")
    for villager in villagers:
        probability = set_probability_of_survival(villager)
        roll_the_die(probability,villager)
    print("...")
    delete_dead_villagers(villagers)


def set_probability_of_survival(villager):
    if villager.age < 5 or villager.age > 60:
        probability_of_survival = 35
    elif villager.age < 12 or villager.age > 50:
        probability_of_survival = 50
    else:
        probability_of_survival = 90

    return (probability_of_survival + villager.health) / 2


# print (villager1.probability_of_survival)

def roll_the_die(probability,villager):
    import random
    random_number = random.randint(1, 90)
    if random_number > probability:
        villager.health = 0

def delete_dead_villagers(villagers):
    dead_villagers = []
    index = 0
    while index < len(villagers):
        villager = villagers[index]
        if villager.health <= 0:
            dead_villagers.append(villager)
            villagers.remove(villager)
        else:
            index += 1
    if len(dead_villagers) != 0:
        print("Diese Dorfbewohner sind leider gestorben:")
        for villager in dead_villagers:
            villager.print_stats()
        print("------------------------------------------------")
    else:
        print("Alle leben noch!")


def relative_check(game):
    villagers_names = []
    for villager in game.villagers:
        villagers_names.append(villager.name)
    for villager1 in game.villagers:
        for element in villager1.parents:
            if element not in villagers_names:
                villager1.parents.remove(element)
    for villager1 in game.villagers:
        for element in villager1.siblings:
            if element not in villagers_names:
                villager1.siblings.remove(element)
    for villager1 in game.villagers:
        for element in villager1.children:
            if element not in villagers_names:
                villager1.children.remove(element)
    for villager1 in game.villagers:
        if villager1.spouse not in villagers_names:
            villager1.spouse = "-"
