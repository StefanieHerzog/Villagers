#todo:- wenn jemand stirbt oder removed wird, muss dessen Name bei allen Objekten beim Member "Partner" gesucht und entfernt werden


import threading
import time
from survival import survival_check
from survival import relative_check
from survival import delete_dead_villagers
from utils import get_villager_by_name

from villager import Villager, create_random_villager
from village import Village, marry

from events import random_event



class Game:
    game_on = False
    time_step = 2
    year = 0
    month = 1

    def __init__(self):
        print("Möchtest du loslegen?")
        answer = input()
        if answer.lower() == "ja":
            self.game_on = True
            self.print_rules()
            print("")
            self.village = Village()
            self.create_first_villagers(8)
            self.village.show_stats(self.villagers, self.year, self.month)
            self.ask_for_marriage()
            self.thread = threading.Thread(target=self.main_loop)
            self.thread.start()
            print("Die Zeit läuft!")
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
                self.village.villagers_age(self.villagers)
            print(f"Jahr {self.year}, Monat {self.month}")
            self.village.adjust_resources(self.villagers)
            self.village.adjust_health(self.villagers)
            delete_dead_villagers(self.villagers)
            self.village.advance_pregnancy(self.villagers)
            self.village.try_for_baby(self.villagers)
            self.village.show_stats(self.villagers, self.year, self.month)
            random_event(self)
            if len(self.villagers) == 0:
                self.game_on = False
                print("Alle deine Bewohner sind gestorben. Das Spiel ist vorbei.")
                return
            if len(self.villagers) >= 40:
                    self.game_on = False
                    print("Dein Dorf floriert - du hast gewonnen!")
                    return
            if self.month == 1:
                survival_check(self.villagers)
                relative_check(self)
                if len(self.villagers) == 0:
                    self.game_on = False
                    print("Alle deine Bewohner sind gestorben. Das Spiel ist vorbei.")
                    return
                self.ask_for_marriage()



    def create_first_villagers(self, num):
        self.villagers = []
        for i in range (num):
            self.villagers.append (create_random_villager())

    def print_stats_all_villagers(self):
        print("")
        for villager in self.villagers:
            villager.print_stats()
        print("")


#sort villagers by different members (TO DO)

    def sort_and_print_villagers_by_age(self):
        self.villagers = sorted(self.villagers, key=lambda villager: villager.age)
        self.print_stats_all_villagers()

    def print_rules(self):
        print("")
        print("Gratulation! Du bist soeben der Verwalter eines kleinen Dorfes geworden. \nDeine Interaktionen werden darüber entscheiden, ob dein Dorf wächst oder eingeht.")
        print("Arbeitsfähige Dorfbewohner kreieren Ressourcen, welche alle Dorfbewohner für ihre Gesundheit benötigen. \nWenn du keinen Dorfbewohner mehr hast, hast du verloren.")
        print("Mit 40 Dorfbewohnern hast du gewonnen.\nDu kannst bei Ereignissen mit dem Spiel interagieren.")
        print("Ausserdem kannst du jeden Monat Leute verheiraten.")
        print("Verheiratete Paare versuchen automatisch jeden Monat, ein Kind zu bekommen. Erfolgschancen variieren je nach Alter, Gesundheit und Zufall.")
        print("Die Ressourcen deines Dorfes beeinflussen die Gesundheit der Bewohner. Achtung, Minderjährige verbrauchen nur Ressourcen, aber schaffen keine.")


    def ask_for_marriage(self):
        self.sort_and_print_villagers_by_age()
        answer = input("Das sind all deine Dorfbewohner. Möchtest du zwei von ihnen verheiraten? ")
        while answer.lower() != "nein":
            print("Wen möchtest du verheiraten?")
            person1 = input("1. Dorfbewohner: ")
            villager1 = get_villager_by_name(self.villagers, person1)
            if villager1 is None:
                print("Es gibt keinen Dorfbewohner mit dem Namen", person1)
                answer = input("Möchtest du nochmal versuchen, ein Paar zu verheiraten? ")
                continue

            person2 = input("2. Dorfbewohner: ")
            villager2 = get_villager_by_name(self.villagers, person2)
            if villager2 is None:
                print("Es gibt keinen Dorfbewohner mit dem Namen", person2)
                answer = input("Möchtest du nochmal versuchen, ein Paar zu verheiraten? ")
                continue

            marry(villager1, villager2)
            answer = input("Möchtest du nochmal jemanden verheiraten? ")



