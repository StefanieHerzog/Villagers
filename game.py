import threading
import time


class Game:
    game_on = False
    time_step = 1
    year = 0
    month = 0

    def __init__(self):
        print("Want to play game?")
        answer = input()
        if answer.lower() == "yes":
            self.game_on = True
            self.thread = threading.Thread(target=self.start_timer)
            self.thread.start()
            print("juhu!")
        else:
            print("oooh...")
            exit(1)

    def start_timer(self):
        while self.game_on:
            time.sleep(self.time_step)
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
            # survival_check()
            print(self.month)


