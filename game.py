import threading
import time

from villager import Villager


class Game:
    game_on = False
    time_step = 1
    year = 0
    month = 1

    def __init__(self):
        print("Want to play game?")
        answer = input()
        if answer.lower() == "yes":
            self.game_on = True
            self.create_villagers()
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

    def create_villagers(self):
        villager1 = Villager("Susie",15,"female",70)
        villager2 = Villager("Otto",17,"male",80)
        villager3 = Villager("Marie", 2, "female", 70)

        self.villagers = [villager1,villager2,villager3]


    def print_stats_all_villagers(self):
        for villager in self.villagers:
            villager.print_stats()

