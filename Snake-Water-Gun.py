# Importing Modules :-
import random
import time

# Defining Data:-
SWG = ["Snake", "Water", "Gun"]
i = True
disclaimer = "[Disclaimer -      "
disclaimer2 = "              This Game don't do any sort of cheating."
disclaimer3 = "              Please do not think that it does the process according to your input."
disclaimer4 = "              Everything is pre-defined and it generate a random value only. "
disclaimer5 = "THANK YOU!]"
def s(g):
    time.sleep(g)
score = 0
miss = 0
def show():
    print("                                                        Score - ", score, "  Miss - ", miss)
def miss1():
    time.sleep(0.5)
    print("Oops! You missed it...", end='')
    global miss
    miss += 1
    show()
def win():
    time.sleep(0.5)
    print("Yeah! You got it...   ", end='')
    global score
    score += 1
    show()

# Welcome User :-
time.sleep(1)
print("Hey, Let's play a Snake-Water-Gun Game!")
time.sleep(0.5)
print(disclaimer)
print(disclaimer2)
print(disclaimer3)
print(disclaimer4)
print(disclaimer5)
time.sleep(1.0)
print("Please turn your Caps-Lock on!")

# Main Game Logic :-
while i == True:
    Comp = random.choice(SWG)
    s(0.5)
    try:
        x = input('''Type 'S' for "Snake", 'W' for "Water" and 'G' for "Gun" - ''')
        if x == 'S':
            y = "Snake"
        if x == 'W':
            y = "Water"
        if x == 'G':
            y = "Gun"
        time.sleep(0.5)

        # Working according to Conditions :-
        if y == Comp:
            print("Computer - ", Comp,"    ", end='')
            show()
        else:
            print("Computer - ", Comp)
            if y == "Snake" and Comp == "Water":
                win()
            if y == "Snake" and Comp == "Gun":
                miss1()
            if y == "Water" and Comp == "Snake":
                miss1()
            if y == "Water" and Comp == "Gun":
                win()
            if y == "Gun" and Comp == "Snake":
                win()
            if y == "Gun" and Comp == "Water":
                miss1()

    except Exception as e:
        time.sleep(0.5)
        print("Sorry, Something wrong happened.")
        s(0.5)
        print("[Error Type :- ")
        print(e)

    finally:
        if score == 10:
            print()
            print("Yay! You won the Game!")
            i = False
        else:
            if miss == 10:
                print()
                print("Oops! You lost the Game...")
                i = False

print("Thank You!")






