# creating some villagers by hand:

villager1 = Villager()
villager1.name = "Susie"
villager1.age = 15
villager1.gender = "female"
villager1.health = 70
villager1.probability_of_survival = str()

villager2 = Villager()
villager2.name = "Otto"
villager2.age = 17
villager2.gender = "male"
villager2.health = 70
villager2.probability_of_survival = str()

villager3 = Villager()
villager3.name = "Marie"
villager3.age = 2
villager3.gender = "female"
villager3.health = 70
villager3.probability_of_survival = str()




# functions to determine if a specific villager dies each month
# to do: function to see if each villager dies each month

def survival_check():
    set_probability_of_survival()
    roll_the_die()


def set_probability_of_survival():
    if villager1.age < 6 or villager1.age > 60:
        villager1.probability_of_survival = 30
    elif villager1.age < 12 or villager1.age > 50:
        villager1.probability_of_survival = 50
    else:
        villager1.probability_of_survival = 80

    villager1.probability_of_survival = villager1.probability_of_survival * villager1.health * 1.5 / 100


# print (villager1.probability_of_survival)

def roll_the_die():
    import random
    random_number = random.randint(1, 100)
    if random_number > villager1.probability_of_survival:
        print("survival =" + str(villager1.probability_of_survival) + "... must be higher than " + str(random_number))
        print("villager1 dies!")
    else:
        print("survival =" + str(villager1.probability_of_survival) + "... must be higher than " + str(random_number))
        print("villager1 lives!")


set_probability_of_survival()
roll_the_die()