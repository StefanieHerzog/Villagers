import random

from villager import create_newborn

class Village:
    name = ""
    resources = int()

    def __init__(self):
        self.name = input("Wie soll dein Dorf heissen?")
        self.resources = 50

    def show_stats(self, villagers, year, month):
        print(
            f"{self.name:<8}",
            f"Alter: {year} Jahre, {month} Monate",
            " Bewohner: ", len(villagers),
            " Erwachsene: ", self.count_villagers_of_ages(villagers, adult=True),
            " Kinder: ", self.count_villagers_of_ages(villagers, adult=False),
            "Weiblich: ", self.count_villagers_of_gender(villagers, gender="female"),
            "Männlich: ", self.count_villagers_of_gender(villagers, gender="male"),
            "Durchschn. Gesundheit: ", self.avg_health(villagers),
            "Ressourcen: ", self.resources,
        )

    def count_villagers_of_ages(self, villagers, adult):
       villager_counter = 0
       for villager in villagers:
            if adult and villager.is_adult():
                villager_counter += 1
            elif not adult and not villager.is_adult():
                villager_counter += 1
       return villager_counter


    def count_villagers_of_gender(self, villagers, gender):
        assert(gender is not None)
        counter = 0
        for villager in villagers:
            if villager.gender == gender:
                counter += 1
        return counter

    def avg_health(self, villagers):
        total_health = 0
        for villager in villagers:
            total_health += villager.health
        return total_health / len(villagers)

    def villagers_age(self,villagers):
        for villager in villagers:
            villager.age += 1

    def adjust_resources(self, villagers):
        change_resources = 0
        for villager in villagers:
            if villager.is_adult():
                change_resources += 5
            change_resources -= 4
        print("Ressourcen Veränderung: ", change_resources)
        self.resources += change_resources

    def adjust_health(self, villagers):
        if self.resources > 90:
            for villager in villagers:
                villager.health += 25
        elif self.resources > 70:
            for villager in villagers:
                villager.health += 15
        elif self.resources > 50:
            for villager in villagers:
                villager.health += 10
        elif self.resources > 40:
            for villager in villagers:
                villager.health -= 5
        elif self.resources > 35:
            for villager in villagers:
                villager.health -= 10
        elif self.resources > 20:
            for villager in villagers:
                villager.health -= 20
        else:
            for villager in villagers:
                villager.health -= 30
        if villager.health > 100:
            villager.health = 100

    def advance_pregnancy(self, villagers):
        for villager in villagers:
            if villager.pregnant == 9:
                newborns = self.birth(villager)
                villagers.extend(newborns)
            if villager.pregnant != -1:
                villager.pregnant +=1

    def try_for_baby(self, villagers):
        for villager in villagers:
            if villager.gender == "female" and villager.pregnant == -1 and villager.spouse != "none":
                if villager.age < 25:
                    chance_tfb = int(random.randint(-50, 50)) + villager.health
                elif villager.age < 40:
                    chance_tfb = int(random.randint(-70, 20)) + villager.health
                elif villager.age < 50:
                    chance_tfb = int(random.randint(-100, 0)) + villager.health
                elif villager.age < 60:
                    chance_tfb = int(random.randint(-100, -20)) + villager.health
                else:
                    chance_tfb = int(random.randint(-100, -45))
                if chance_tfb > 50:
                    villager.pregnant = 0
                    print("Gratulation, ", villager.name, " ist schwanger!")
    def birth(self, villager):
        villager.pregnant = -1
        father = villager.spouse
        mother = villager.name
        if int(random.randint(1, 250)) != 250:
            newborn = create_newborn(mother,father)
            print(mother, "und",father, "haben ein Baby bekommen! Es heisst",newborn.name)
            return [newborn]
        else:
            twin1 = create_newborn(mother, father)
            twin2 = create_newborn(mother, father)
            print("Unglaublich!",mother, "und",father, "haben Zwillinge bekommen! Sie heissen",twin1.name ,"und",twin2.name)
            return [twin1, twin2]

def marry(person1, person2):
    if person1.spouse == person2.name:
        print("Diese Dorfbewohner sind schon miteinander verheiratet!")
    elif person1.spouse != "none" or person2.spouse != "none":
        print("Verheiratete Dorfbewohner dürfen nicht heiraten!")
    elif person1.gender == person2.gender:
        print("Leider wurde die gleichgeschlechtliche Ehe in deinem Königreich noch nicht erlaubt")
    elif person1.age <16 or person2.age <16:
        print("Zum heiraten muss man mindestens 16 sein!")
    else:
        person1.spouse = person2.name
        person2.spouse = person1.name
        print(person1.name, "und", person2.name, "haben geheiratet!")




