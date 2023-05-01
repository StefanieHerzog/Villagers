import threading
import time
from survival import survival_check


from villager import Villager, create_random_villager


class Game:
    game_on = False
    time_step = 5 #150
    year = 0
    month = 1

    def __init__(self):
        print("Want to play game?")
        answer = input()
        if answer.lower() == "yes":
            self.game_on = True
            self.print_rules()
            self.create_first_villagers(8)
            self.sort_and_print_villagers_by_age()
            self.thread = threading.Thread(target=self.main_loop)
            self.thread.start()
            print("juhu!")
        else:
            print("oooh...")
            exit(1)

    def main_loop(self):
        while self.game_on:
            time.sleep(self.time_step)
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
                survival_check()
            print(self.month)

    def create_first_villagers(self, num):
        self.villagers = []
        for i in range (num):
            self.villagers.append (create_random_villager())

    def print_stats_all_villagers(self):
        for villager in self.villagers:
            villager.print_stats()


#sort villagers by different members (TO DO)

    def sort_and_print_villagers_by_age(self):
        self.villagers = sorted(self.villagers, key=lambda villager: villager.age)
        self.print_stats_all_villagers()

    def print_rules(self):
        print("Gratulation! Du bist soeben der Verwalter eines kleinen Dorfes geworden. \nDeine Interaktionen werden darüber entscheiden, ob dein Dorf wächst oder eingeht.")
        print("Arbeitsfähige Dorfbewohner kreieren Ressourcen, welche alle Dorfbewohner für ihre Gesundheit benötigen. \nWenn du keinen Dorfbewohner mehr hast, hast du verloren.")
        print("Mit 40 Dorfbewohnern hast du gewonnen. \n Du kannst jederzeit folgende Befehle eingeben:")
        print("show_stats()" ": zeigt dir den Status deines Dorfes und der Dorfbewohner")
        print("marry(person1,person2)" ": verheiratet  zwei Dorfbewohner miteinander.")

        # ToDo show how to get statistics of villagers and village

        print("Verheiratete Paare versuchen automatisch jeden Monat, ein Kind zu bekommen. Erfolgschancen variieren je nach Alter, Gesundheit und Zufall.")
        print("Die Ressourcen deines Dorfes beeinflussen die Gesundheit der Bewohner.Achtung, Minderjährige verbrauchen nur Ressourcen, aber schaffen keine")
        print("Du kannst ausserdem bei Ereignissen über weitere Kommandos mit dem Spiel interagieren.")
