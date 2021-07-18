# 1. Importing Modules :-
import random
import time

def Dice(x):
    # 2. Defining Data :-
    total  = []
    # 3. Main Game Loop :-
    print("Welcome to The Game of Dice!")
    time.sleep(1.0)
    noOfTimes = int(input("How many times do you want to play? : "))
    time.sleep(1.0)
    for i in range(1, noOfTimes + 1):
        if noOfTimes > 30:
            print("Sorry, The Maximum limit is 30.\nPlease Play again.")
            break
        rand = random.choice(x)
        total.append(rand)
        print(i, ". -> ", rand)
        time.sleep(1.0)
    time.sleep(1.0)
    print("\nYou Got :-\n", total.count(1), " Ones,\n", total.count(2), " Twos,\n", total.count(3), " Threes,\n", total.count(4), " Fours,\n", total.count(5), " Fives, and\n", total.count(6), " Sixes.\n",)
    time.sleep(1.0)
    print("\nThank You!")

if __name__ == '__main__':
    Dice([1, 2, 3, 4, 5, 6])
