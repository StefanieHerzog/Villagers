class Village:
    name = ""
    resources = int()

    def __init__(self):
        self.name = input("Definiere einen Namen für dein Dorf: ")
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
        counter = 0
        for villager in villagers:
            if adult and villager.age > 17:
                counter += 1
            elif not adult and villager.age <= 17:
                counter += 1
        return counter

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

