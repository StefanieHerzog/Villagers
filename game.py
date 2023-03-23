import threading
import time

from villager import Villager, create_random_villager


class Game:
    game_on = False
    time_step = 150
    year = 0
    month = 1

    def __init__(self):
        print("Want to play game?")
        answer = input()
        if answer.lower() == "yes":
            self.game_on = True
            self.create_first_villagers(8)
            self.print_stats_all_villagers()
            self.thread = threading.Thread(target=self.start_time_passing)
            self.thread.start()
            print("juhu!")
        else:
            print("oooh...")
            exit(1)

    def start_time_passing(self):
        while self.game_on:
            time.sleep(self.time_step)
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
            # survival_check()
            print(self.month)

    def create_first_villagers(self, num):
        self.villagers = []
        for i in range (num):
            self.villagers.append (create_random_villager())


    def print_stats_all_villagers(self):
        for villager in self.villagers:
            villager.print_stats()

