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