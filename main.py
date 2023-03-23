import time

#function for turning game on
def turning_game_on ():
    print("want to play?")
    time.sleep(5)
    answer = input()
    if answer == "yes" or "YES" or "Yes":
        game_on = True

#function for turning game off
def turning_game_off ():
    print("want to end the game?")
    answer = input()
    if answer == "yes" or "YES" or "Yes":
        game_on = False


# #creating class Villager:
#
# class Villager:
#
#     name = ""
#     age = 0
#     health = 100
#     gender = ""
#     probability_of_survival = int()
#
#
# #creating lists with names for the villagers(Lists with Names enriched by ChatGPT)
# femalenames = ["Anna","Agatha","Ophelia","Daisy","Mary","Alice", "Agnes", "Beatrice", "Cecilia", "Eleanor", "Emma", "Isabella", "Joan", "Margaret", "Matilda", "Philippa", "Rose", "Sybil", "Theresa", "Ysabel"]
#
# malenames = ["John","Edward","Paul","Harold","Albert", "Arthur", "Bernard", "Cedric", "Charles", "Edgar", "Edmund", "Geoffrey", "Henry", "Hugh", "Lancelot", "Louis", "Richard", "Robert", "Stephen", "Thomas", "William"]
#
# #setting the timer back
#
# year = 0
# months = 1
#
# # #starting the timer
#
# while game_on == true:
#     time.sleep(150)
#     months += 1
#     if months == 13:
#         year += 1
#         months = 1
#    survival_check()


   #game actually starts

if __name__ == '__main__':
    print("Game Starting")
    turning_game_on()

